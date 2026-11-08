#!/usr/bin/env python3
"""Safety guards for the architect-dev-toolkit plugin.

Modes:
  bash     PreToolUse on Bash: blocks destructive commands, prod mutations, secret reads,
           and any mutation attempted by the plugin's read-only agents.
  files    PreToolUse on Read/Edit/Write/MultiEdit/NotebookEdit: blocks access to secret files.
  progress SessionStart: shows PROGRESS.md from the project root as context, if present.

Blocking uses exit code 2 with the reason on stderr (Claude sees the reason).
Any internal error exits 0 so the guard never breaks a session.
"""
import json
import os
import re
import shlex
import subprocess
import sys

READ_ONLY_AGENTS = {
    "k8s-debugger",
    "incident-triage",
    "security-reviewer",
    "performance-reviewer",
    "spring-conventions-reviewer",
    "doc-explorer",
}

SECRET_NAME_PATTERNS = [
    r"^\.env$",
    r"^\.env\.(?!example$|sample$|template$|dist$).+",
    r".*\.pem$",
    r".*\.key$",
    r".*\.p12$",
    r".*\.pfx$",
    r".*\.jks$",
    r".*\.keystore$",
    r"^id_(rsa|dsa|ecdsa|ed25519)(\.pub)?$",
    r"^\.git-credentials$",
    r"^\.npmrc$",
    r"^\.pypirc$",
    r"^\.netrc$",
    r".*-service-account\.json$",
    r"^application_default_credentials\.json$",
]
SECRET_PATH_PATTERNS = [
    r"(^|/)\.aws/credentials$",
    r"(^|/)\.kube/config$",
    r"(^|/)\.docker/config\.json$",
    r"(^|/)\.ssh/",
    r"(^|/)\.azure/",
    r"(^|/)\.config/gcloud/",
]

PROD_RE = re.compile(r"prod|prd|live", re.IGNORECASE)


def block(reason: str) -> None:
    print(f"[architect-dev-toolkit guard] {reason}", file=sys.stderr)
    sys.exit(2)


def is_secret_path(path: str) -> bool:
    if not path:
        return False
    p = path.replace("\\", "/")
    name = os.path.basename(p)
    if any(re.match(rx, name) for rx in SECRET_NAME_PATTERNS):
        return True
    return any(re.search(rx, p) for rx in SECRET_PATH_PATTERNS)


def base_agent(agent_type: str) -> str:
    return (agent_type or "").split(":")[-1]


def split_segments(command: str):
    """Split a shell command line into simple command segments."""
    parts = re.split(r"\|\||&&|;|\||\n", command)
    out = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        try:
            tokens = shlex.split(part)
        except ValueError:
            tokens = part.split()
        # drop leading env assignments and sudo/time wrappers
        while tokens and (re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", tokens[0]) or tokens[0] in {"sudo", "time", "nohup", "exec"}):
            tokens = tokens[1:]
        if tokens:
            out.append(tokens)
    return out


def flag_value(tokens, *names):
    for i, t in enumerate(tokens):
        for n in names:
            if t == n and i + 1 < len(tokens):
                return tokens[i + 1]
            if t.startswith(n + "="):
                return t.split("=", 1)[1]
    return None


VALUE_FLAGS = {
    "--context", "--kube-context", "-n", "--namespace", "--kubeconfig", "--cluster", "--user",
    "-f", "--filename", "-l", "--selector", "-o", "--output", "-c", "--container",
    "--profile", "--region", "--endpoint-url", "--output", "--query",
}


def positional(args):
    """Positional args, skipping the values of flags that take a separate value."""
    out, skip = [], False
    for a in args:
        if skip:
            skip = False
            continue
        if a.startswith("-"):
            if "=" not in a and a in VALUE_FLAGS:
                skip = True
            continue
        out.append(a)
    return out


def current_kube_context() -> str:
    try:
        r = subprocess.run(
            ["kubectl", "config", "current-context"],
            capture_output=True, text=True, timeout=3,
        )
        return r.stdout.strip()
    except Exception:
        return ""


KUBECTL_MUTATING = {
    "apply", "create", "delete", "edit", "patch", "replace", "scale", "set", "label",
    "annotate", "taint", "cordon", "uncordon", "drain", "autoscale", "expose", "run",
    "exec", "cp", "port-forward",
}
HELM_MUTATING = {"install", "upgrade", "uninstall", "delete", "rollback"}
TF_MUTATING = {"apply", "destroy", "import", "taint", "untaint", "state"}
AWS_MUTATING_RE = re.compile(
    r"^(delete|terminate|remove|put|create|update|modify|stop|start|reboot|attach|detach|"
    r"associate|disassociate|run|deregister|register|revoke|authorize|reset|restore|cancel|rm$|rb$|mv$|sync$|cp$)"
)


def check_bash(data: dict) -> None:
    command = (data.get("tool_input") or {}).get("command", "") or ""
    agent = base_agent(data.get("agent_type", ""))
    read_only = agent in READ_ONLY_AGENTS
    lowered = command.lower()

    # SQL destruction anywhere in the line
    if re.search(r"\b(drop\s+(database|schema|table)|truncate\s+table)\b", lowered):
        block("Destructive SQL (DROP/TRUNCATE) is blocked. Run it yourself if it is really intended.")

    for tokens in split_segments(command):
        prog = os.path.basename(tokens[0])
        args = tokens[1:]

        # secret reads via shell
        if prog in {"cat", "less", "more", "head", "tail", "bat", "cp", "scp", "base64", "xxd", "strings", "grep", "rg"}:
            for a in args:
                if not a.startswith("-") and is_secret_path(a):
                    block(f"Reading secret file '{a}' is blocked. Reference the variable name instead of its value.")

        if prog == "rm":
            flags = "".join(a for a in args if a.startswith("-"))
            recursive = "r" in flags.lower() or "--recursive" in args
            targets = [a for a in args if not a.startswith("-")]
            dangerous = {"/", "/*", "~", "~/", "$HOME", "${HOME}", ".", "./", "..", "*", "/home", "/Users"}
            if recursive and any(t.rstrip("/") in {d.rstrip("/") for d in dangerous} or t in dangerous for t in targets):
                block(f"'{' '.join(tokens)}' would delete a root, home or whole working directory.")
            if read_only:
                block(f"The {agent} agent is read-only; file deletion is not allowed.")

        if prog == "git" and args:
            sub = args[0]
            if sub == "push" and any(a in {"--force", "-f"} or (a.startswith("+") and len(a) > 1) for a in args[1:]):
                block("Force push is blocked. Use --force-with-lease after checking, or push yourself.")
            if sub == "push" and any(a in {"main", "master", "origin/main", "origin/master"} for a in args[1:]) and read_only:
                block(f"The {agent} agent is read-only; git push is not allowed.")
            if read_only and sub in {"push", "commit", "reset", "rebase", "merge", "checkout", "switch", "clean", "stash", "tag", "cherry-pick", "revert", "am", "apply"}:
                block(f"The {agent} agent is read-only; 'git {sub}' is not allowed.")
            if sub == "clean" and any("f" in a for a in args[1:] if a.startswith("-")) and any("d" in a or "x" in a for a in args[1:] if a.startswith("-")):
                block("'git clean -fdx' style cleanup is blocked; it deletes untracked work irreversibly.")

        if prog == "kubectl":
            verbs = positional(args)
            verb = verbs[0] if verbs else ""
            mutating = verb in KUBECTL_MUTATING or (verb == "rollout" and len(verbs) > 1 and verbs[1] in {"restart", "undo", "pause", "resume"})
            if mutating:
                if read_only:
                    block(f"The {agent} agent is read-only; 'kubectl {verb}' is not allowed. Propose the command for a human instead.")
                if verb == "delete":
                    block("'kubectl delete' is blocked by policy. Propose the exact command for a human to run.")
                ctx = flag_value(args, "--context") or current_kube_context()
                ns = flag_value(args, "-n", "--namespace") or ""
                if PROD_RE.search(ctx) or PROD_RE.search(ns):
                    block(f"Mutating production Kubernetes (context '{ctx}', namespace '{ns or 'default'}') is blocked. Propose the command for a human to run.")

        if prog == "helm":
            verbs = positional(args)
            verb = verbs[0] if verbs else ""
            if verb in HELM_MUTATING:
                if read_only:
                    block(f"The {agent} agent is read-only; 'helm {verb}' is not allowed.")
                ctx = flag_value(args, "--kube-context") or current_kube_context()
                ns = flag_value(args, "-n", "--namespace") or ""
                if PROD_RE.search(ctx) or PROD_RE.search(ns):
                    block(f"Helm {verb} against production (context '{ctx}') is blocked. Propose the command for a human to run.")

        if prog in {"terraform", "tofu", "terragrunt"}:
            verbs = positional(args)
            verb = verbs[0] if verbs else ""
            if verb == "destroy" or (verb == "apply" and "-destroy" in args):
                block("terraform destroy is blocked. Run it yourself after review.")
            if verb in TF_MUTATING and ("-auto-approve" in args or read_only):
                block(f"'terraform {verb}' with auto-approve (or from a read-only agent) is blocked. Run plan, then apply yourself.")

        if prog == "aws" and len(args) >= 2:
            op = positional(args)
            action = op[1] if len(op) > 1 else ""
            if AWS_MUTATING_RE.match(action):
                profile = flag_value(args, "--profile") or os.environ.get("AWS_PROFILE", "")
                if read_only:
                    block(f"The {agent} agent is read-only; 'aws {op[0]} {action}' is not allowed.")
                if PROD_RE.search(profile):
                    block(f"Mutating AWS call '{op[0]} {action}' with production profile '{profile}' is blocked. Run it yourself.")

        if read_only and prog in {"mv", "chmod", "chown", "dd", "mkfs", "truncate", "sed"} and (prog != "sed" or any(a.startswith("-i") for a in args)):
            block(f"The {agent} agent is read-only; '{prog}' that modifies files is not allowed.")


GENERATED_DIR_RE = re.compile(
    r"(^|/)(node_modules|target|build|dist|out|\.gradle|\.mvn/wrapper|\.next|coverage|__pycache__|\.venv|venv|\.terraform)/"
)
NOISE_FILE_RE = re.compile(r"(\.min\.(js|css)|\.map|package-lock\.json|yarn\.lock|pnpm-lock\.yaml|\.jar|\.class)$")
LARGE_FILE_BYTES = 512 * 1024


def check_cost(data: dict) -> None:
    """Block token-expensive reads; Claude sees the reason and adapts (limit, grep, doc-explorer)."""
    if os.environ.get("ADT_COST_GUARD", "on").lower() == "off":
        return
    if data.get("tool_name") != "Read":
        return
    ti = data.get("tool_input") or {}
    path = (ti.get("file_path") or "").replace("\\", "/")
    if not path:
        return
    if GENERATED_DIR_RE.search(path) or NOISE_FILE_RE.search(path):
        block(
            f"Cost guard: '{path}' is generated, vendored or a lockfile and is expensive to read. "
            "Read the source instead, grep for the specific symbol, or ask the doc-explorer agent. "
            "If you really need it, read a small range with offset/limit after the user agrees."
        )
    has_range = ti.get("limit") is not None or ti.get("offset") is not None
    try:
        size = os.path.getsize(path)
    except OSError:
        return
    if size > LARGE_FILE_BYTES and not has_range:
        block(
            f"Cost guard: '{path}' is {size // 1024} KB. Do not read it whole. Grep for what you need, "
            "read a targeted range with offset/limit, or delegate the scan to the doc-explorer agent "
            "(cheap model, returns a summary)."
        )


def check_bash_cost(data: dict) -> None:
    if os.environ.get("ADT_COST_GUARD", "on").lower() == "off":
        return
    command = (data.get("tool_input") or {}).get("command", "") or ""
    for tokens in split_segments(command):
        prog = os.path.basename(tokens[0])
        if prog in {"cat", "less", "more", "bat"}:
            for a in tokens[1:]:
                if a.startswith("-"):
                    continue
                try:
                    size = os.path.getsize(a)
                except OSError:
                    continue
                if size > LARGE_FILE_BYTES:
                    block(
                        f"Cost guard: '{a}' is {size // 1024} KB; dumping it costs many tokens. Use grep, "
                        "head/tail with a line count, or the doc-explorer agent."
                    )


def check_files(data: dict) -> None:
    ti = data.get("tool_input") or {}
    path = ti.get("file_path") or ti.get("notebook_path") or ti.get("path") or ""
    check_cost(data)
    if is_secret_path(path):
        block(f"Access to secret file '{path}' is blocked. Use environment variable names or a secrets manager reference instead.")
    agent = base_agent(data.get("agent_type", ""))
    if agent in READ_ONLY_AGENTS and data.get("tool_name") in {"Edit", "Write", "MultiEdit", "NotebookEdit"}:
        block(f"The {agent} agent is read-only; file edits are not allowed.")


def show_progress(data: dict) -> None:
    root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    for name in ("PROGRESS.md", ".claude/PROGRESS.md"):
        p = os.path.join(root, name)
        if os.path.isfile(p):
            with open(p, encoding="utf-8", errors="replace") as fh:
                lines = fh.readlines()[:150]
            text = "".join(lines)
            ctx = (
                f"This repository has a long-running task progress file at {name}. "
                f"Its current contents (first {len(lines)} lines) are below; continue from the "
                f"'In progress' and next unchecked items when the user resumes that work.\n\n{text}"
            )
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": ctx}}))
            return


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        sys.exit(0)
    try:
        if mode == "bash":
            check_bash(data)
            check_bash_cost(data)
        elif mode == "files":
            check_files(data)
        elif mode == "progress":
            show_progress(data)
    except SystemExit:
        raise
    except Exception:
        sys.exit(0)
    sys.exit(0)


if __name__ == "__main__":
    main()
