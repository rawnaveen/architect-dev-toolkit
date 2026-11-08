#!/usr/bin/env python3
"""Show what the plugin's hooks do, using the real guard script.

Feeds sample tool calls (the same JSON Claude Code sends to PreToolUse hooks) into
hooks/scripts/guard.py and prints whether each is allowed or blocked, with the reason
Claude would see. Nothing is executed.

Usage: python3 examples/guard_demo.py
"""
import json
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
GUARD = ROOT / "hooks" / "scripts" / "guard.py"

work = pathlib.Path(tempfile.mkdtemp())
big_log = work / "app.log"
big_log.write_text("2026-11-08T10:00:00 ERROR ConnectionPoolTimeout\n" * 30000)

SCENARIOS = [
    ("Claude", "Bash", {"command": "kubectl --context eks-prod delete pod payments-api-7d9f"}, None),
    ("Claude", "Bash", {"command": "git push --force origin main"}, None),
    ("Claude", "Read", {"file_path": "/repo/.env"}, None),
    ("Claude", "Read", {"file_path": str(big_log)}, None),
    ("k8s-debugger", "Bash", {"command": "kubectl scale deploy/orders --replicas=0 -n orders-staging"}, "k8s-debugger"),
    ("k8s-debugger", "Bash", {"command": "kubectl logs orders-6f7c --previous -n orders-staging"}, "k8s-debugger"),
    ("Claude", "Bash", {"command": "./mvnw -q test"}, None),
]


def describe(tool, tool_input):
    if tool == "Bash":
        return tool_input["command"]
    path = tool_input["file_path"]
    return "logs/" + pathlib.Path(path).name if path.startswith(str(work)) else path


def main():
    for who, tool, tool_input, agent in SCENARIOS:
        payload = {"tool_name": tool, "tool_input": tool_input}
        if agent:
            payload["agent_type"] = f"architect-dev-toolkit:{agent}"
        mode = "bash" if tool == "Bash" else "files"
        r = subprocess.run([sys.executable, str(GUARD), mode], input=json.dumps(payload),
                           capture_output=True, text=True)
        print(f"$ {who} wants {tool}: {describe(tool, tool_input)}")
        if r.returncode == 2:
            reason = r.stderr.strip().replace("[architect-dev-toolkit guard] ", "").replace(str(work) + "/", "logs/")
            print(f"  BLOCKED  {reason}")
        else:
            print("  allowed")
        print()


if __name__ == "__main__":
    main()
