#!/usr/bin/env python3
"""Regression tests for hooks/scripts/guard.py. No model calls, runs in about a second.

Usage: python3 tests/test_guard.py        (exit 0 = all pass)
"""
import json
import os
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
GUARD = ROOT / "hooks" / "scripts" / "guard.py"

ALLOW, BLOCK = 0, 2


def run(mode, payload, env=None):
    data = payload if isinstance(payload, str) else json.dumps(payload)
    e = dict(os.environ, **(env or {}))
    e.setdefault("PATH", os.environ.get("PATH", ""))
    r = subprocess.run([sys.executable, str(GUARD), mode], input=data, capture_output=True, text=True, env=e, timeout=20)
    return r.returncode, r.stdout, r.stderr


def bash(cmd, agent=None):
    p = {"tool_name": "Bash", "tool_input": {"command": cmd}}
    if agent:
        p["agent_type"] = agent
    return p


def read(path, agent=None, tool="Read", **extra):
    p = {"tool_name": tool, "tool_input": {"file_path": path, **extra}}
    if agent:
        p["agent_type"] = agent
    return p


def main():
    tmp = pathlib.Path(tempfile.mkdtemp())
    big = tmp / "app.log"
    big.write_text("x" * (700 * 1024))
    small = tmp / "Main.java"
    small.write_text("class Main {}\n")
    (tmp / "PROGRESS.md").write_text("# Goal\nMigrate\n- [ ] module a\n")

    ro = "architect-dev-toolkit:k8s-debugger"
    cases = [
        # safety: bash
        ("bash", bash("./mvnw -q test"), ALLOW),
        ("bash", bash("rm -rf target build"), ALLOW),
        ("bash", bash("rm -rf /"), BLOCK),
        ("bash", bash("cd x && rm -rf ~"), BLOCK),
        ("bash", bash("git push --force origin feat"), BLOCK),
        ("bash", bash("git push -f origin feat"), BLOCK),
        ("bash", bash("git push origin +feat"), BLOCK),
        ("bash", bash("git push --force-with-lease origin feat"), ALLOW),
        ("bash", bash("git clean -fdx"), BLOCK),
        ("bash", bash("kubectl get pods -n prod"), ALLOW),
        ("bash", bash("kubectl --context dev-cluster apply -f x.yaml"), ALLOW),
        ("bash", bash("kubectl --context eks-prod apply -f x.yaml"), BLOCK),
        ("bash", bash("kubectl -n payments-prod scale deploy/a --replicas=2"), BLOCK),
        ("bash", bash("kubectl rollout restart deploy/api -n payments-prd --context dev"), BLOCK),
        ("bash", bash("kubectl delete pod x --context dev"), BLOCK),
        ("bash", bash("helm --kube-context eks-prod upgrade api ./chart"), BLOCK),
        ("bash", bash("helm --kube-context dev upgrade api ./chart"), ALLOW),
        ("bash", bash("terraform plan"), ALLOW),
        ("bash", bash("terraform destroy"), BLOCK),
        ("bash", bash("terraform apply -auto-approve"), BLOCK),
        ("bash", bash('psql -c "DROP TABLE users"'), BLOCK),
        ("bash", bash("aws ec2 describe-instances --profile prod-admin"), ALLOW),
        ("bash", bash("aws ec2 terminate-instances --instance-ids i-1 --profile prod-admin"), BLOCK),
        ("bash", bash("aws --profile prod-admin s3 rm s3://b/k"), BLOCK),
        ("bash", bash("aws s3 cp a s3://b/ --profile dev"), ALLOW),
        ("bash", bash("cat .env"), BLOCK),
        ("bash", bash("cat .env.example"), ALLOW),
        ("bash", bash("cat ~/.aws/credentials"), BLOCK),
        # read-only agents
        ("bash", bash("kubectl logs api-1 --context eks-prod", ro), ALLOW),
        ("bash", bash("kubectl scale deploy/a --replicas=3 --context dev", ro), BLOCK),
        ("bash", bash("git commit -m x", "security-reviewer"), BLOCK),
        ("bash", bash("git diff main...HEAD", "security-reviewer"), ALLOW),
        ("bash", bash("sed -i s/a/b/ f.txt", "performance-reviewer"), BLOCK),
        ("bash", bash("rm notes.txt", "doc-explorer"), BLOCK),
        ("bash", bash("git commit -m x", "spring-test-writer"), ALLOW),
        # safety: files
        ("files", read("/repo/.env"), BLOCK),
        ("files", read("/repo/.env.local"), BLOCK),
        ("files", read("/repo/.env.example"), ALLOW),
        ("files", read("/home/u/.aws/credentials"), BLOCK),
        ("files", read("/home/u/.ssh/id_ed25519"), BLOCK),
        ("files", read("/repo/certs/server.key"), BLOCK),
        ("files", read(str(small)), ALLOW),
        ("files", read(str(small), "doc-explorer", tool="Edit"), BLOCK),
        ("files", read(str(small), tool="Edit"), ALLOW),
        # cost guard
        ("files", read("/repo/target/classes/A.class"), BLOCK),
        ("files", read("/repo/node_modules/x/index.js"), BLOCK),
        ("files", read("/repo/package-lock.json"), BLOCK),
        ("files", read(str(big)), BLOCK),
        ("files", read(str(big), offset=100, limit=50), ALLOW),
        ("files", read("/repo/build/gen.java", tool="Edit"), ALLOW),
        ("bash", bash(f"cat {big}"), BLOCK),
        ("bash", bash(f"tail -n 200 {big}"), ALLOW),
        ("bash", bash(f"grep ERROR {big} | head"), ALLOW),
        # robustness
        ("bash", "not json", ALLOW),
        ("files", "", ALLOW),
    ]

    failures = 0
    for mode, payload, expected in cases:
        rc, _, err = run(mode, payload)
        ok = rc == expected
        failures += not ok
        label = payload if isinstance(payload, str) else json.dumps(payload["tool_input"])
        if not ok:
            print(f"FAIL {mode:5} expected={'BLOCK' if expected else 'ALLOW'} got rc={rc} {label[:90]} {err.strip()[:120]}")

    # cost guard can be switched off
    rc, _, _ = run("files", read(str(big)), env={"ADT_COST_GUARD": "off"})
    if rc != ALLOW:
        failures += 1
        print("FAIL cost guard off switch")

    # session resume
    rc, out, _ = run("progress", {"cwd": str(tmp)}, env={"CLAUDE_PROJECT_DIR": str(tmp)})
    if rc != 0 or "additionalContext" not in out or "module a" not in out:
        failures += 1
        print("FAIL progress loader did not emit PROGRESS.md")
    empty = pathlib.Path(tempfile.mkdtemp())
    rc, out, _ = run("progress", {"cwd": str(empty)}, env={"CLAUDE_PROJECT_DIR": str(empty)})
    if rc != 0 or out.strip():
        failures += 1
        print("FAIL progress loader should be silent without PROGRESS.md")

    total = len(cases) + 3
    print(f"{total - failures}/{total} guard tests passed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
