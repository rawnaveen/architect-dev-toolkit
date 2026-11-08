"""Build the Claude directory edition of this plugin from the full edition.

The Claude plugin directory accepts command hooks, scripts and files other than
Markdown, text, JSON, YAML and images only from Verified organisations. The
directory edition therefore ships the skills and agents only. The full edition
(hooks, guard script, tests, evals) stays on `main` and installs from GitHub.

Usage: python3 scripts/build_directory_edition.py OUT_DIR
Writes the edition into OUT_DIR (which must be empty or absent) and fails if
any file would break the directory policy.
"""

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OVERLAY = ROOT / "directory-edition"

# Copied from main as they are (then patched below).
INCLUDE = [
    ".claude-plugin",
    "agents",
    "skills",
    "assets/icon.png",
    "assets/social-preview.png",
    "docs/components.md",
    "CHANGELOG.md",
    "LICENSE",
]

ALLOWED_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico"}
ALLOWED_NAMES = {"LICENSE"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico"}

DESCRIPTION = (
    "Auto-triggering skills and subagents for Java/Spring, AWS/EKS, SRE, "
    "architecture work and building with Claude."
)
PRIVACY_URL = "https://github.com/rawnaveen/architect-dev-toolkit/blob/directory/PRIVACY.md"

# (file, old, new): every `old` must be present, so main can't drift silently.
PATCHES = [
    (
        "agents/migration-runner.md",
        " (a SessionStart hook in this plugin shows it automatically in new sessions)",
        " (read it first at the start of every session and after compaction)",
    ),
    (
        "skills/agent-guardrails-config/SKILL.md",
        "4. Hooks: the architect-dev-toolkit plugin already ships global guards (dangerous Bash, secret files). Add\n"
        "   repo-specific hooks only when needed,",
        "4. Hooks: this edition of the plugin ships no hooks, so cover dangerous Bash and secret files with\n"
        "   deny rules. Add repo-specific hooks only when needed,",
    ),
    (
        "agents/k8s-debugger.md",
        " A plugin hook enforces this.",
        " If a command could change state, do not run it; propose it for a human to run.",
    ),
    (
        "agents/incident-triage.md",
        " Plugin hooks block mutating commands.",
        " Propose any mutating command for a human to run instead of running it.",
    ),
    (
        "docs/components.md",
        "Mutations are blocked by the hook",
        "Instructed to run read-only commands only",
    ),
]

COMPONENTS_FOOTER_RE = re.compile(r'\n"Read-only \(enforced\)" means .*?READ_ONLY_AGENTS`\.\n', re.S)
COMPONENTS_FOOTER = (
    "\nIn this edition, read-only agents are read-only by instruction. The full edition on GitHub adds\n"
    "hooks that enforce it: https://github.com/rawnaveen/architect-dev-toolkit\n"
)


def section(readme: str, heading: str) -> str:
    """Return the table under `heading` in the main README."""
    match = re.search(rf"^{re.escape(heading)}\n\n(\|.*?)\n\n", readme, re.S | re.M)
    if not match:
        sys.exit(f"README section not found: {heading}")
    return match.group(1)


def build(out: Path) -> None:
    if out.exists() and any(out.iterdir()):
        sys.exit(f"{out} is not empty")
    out.mkdir(parents=True, exist_ok=True)

    for rel in INCLUDE:
        src, dst = ROOT / rel, out / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(src, dst)

    for name in ("README.md", "SECURITY.md", "PRIVACY.md"):
        shutil.copy2(OVERLAY / name, out / name)
    (out / ".gitignore").write_text("__pycache__/\n", encoding="utf-8")

    for rel, old, new in PATCHES:
        path = out / rel
        text = path.read_text(encoding="utf-8")
        if old not in text:
            sys.exit(f"Patch target not found in {rel}: {old[:60]!r}")
        path.write_text(text.replace(old, new), encoding="utf-8")

    components = out / "docs/components.md"
    text, count = COMPONENTS_FOOTER_RE.subn(COMPONENTS_FOOTER, components.read_text(encoding="utf-8"))
    if count != 1:
        sys.exit("Read-only footer not found in docs/components.md")
    components.write_text(text, encoding="utf-8")

    # Fill the README tables from main so the two editions list the same components.
    main_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    agents_table = section(main_readme, "### Subagents (Claude Code)").replace(
        "Read-only, enforced by hook", "Read-only"
    )
    readme = out / "README.md"
    readme.write_text(
        readme.read_text(encoding="utf-8")
        .replace("<!-- SKILLS_TABLE -->", section(main_readme, "### Skills (Claude Code and Claude Desktop)"))
        .replace("<!-- AGENTS_TABLE -->", agents_table),
        encoding="utf-8",
    )

    for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
        path = out / rel
        data = json.loads(path.read_text(encoding="utf-8"))
        if rel.endswith("plugin.json"):
            data["description"] = DESCRIPTION
            data["privacyPolicyUrl"] = PRIVACY_URL
            data.pop("hooks", None)
        else:
            for plugin in data["plugins"]:
                plugin["description"] = DESCRIPTION
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    check(out)


def check(out: Path) -> None:
    problems = []
    for path in sorted(p for p in out.rglob("*") if p.is_file()):
        rel = path.relative_to(out).as_posix()
        if rel.startswith(".git/"):
            continue
        if path.suffix.lower() not in ALLOWED_SUFFIXES and path.name not in ALLOWED_NAMES and rel != ".gitignore":
            problems.append(f"file type not allowed: {rel}")
            continue
        data = path.read_bytes()
        if path.suffix.lower() in IMAGE_SUFFIXES:
            continue
        if data.startswith(b"#!"):
            problems.append(f"starts with #!: {rel}")
        if b"\x00" in data:
            problems.append(f"contains NUL bytes: {rel}")
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            problems.append(f"not UTF-8: {rel}")
    if (out / "hooks").exists():
        problems.append("hooks/ directory present")
    manifest = json.loads((out / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    if "hooks" in manifest:
        problems.append("plugin.json declares hooks")
    for md in out.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for target in re.findall(r"\]\((?!https?://|#|mailto:)([^)#\s]+)", text):
            if not (md.parent / target).exists():
                problems.append(f"broken link in {md.relative_to(out)}: {target}")
    if problems:
        sys.exit("Directory edition would break policy:\n  " + "\n  ".join(problems))
    count = sum(1 for p in out.rglob("*") if p.is_file())
    print(f"Directory edition OK: {count} files in {out}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build(Path(sys.argv[1]).resolve())
