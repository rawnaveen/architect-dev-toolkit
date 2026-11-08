#!/usr/bin/env python3
"""Generate trigger eval cases from triggers.yaml.

Writes evals/trigger/<component>/<pos|neg>-NN/{prompt.md,graders/*.md}.
Positive cases assert the component fired; negative (near-miss) cases assert it did not.
Only free, deterministic graders are used (tool_used), so the suite costs only the agent runs.

Usage: python3 evals/_spec/generate_triggers.py
"""
import pathlib
import shutil
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("pip install pyyaml")

HERE = pathlib.Path(__file__).resolve().parent
EVALS = HERE.parent
OUT = EVALS / "trigger"


def q(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def write_case(path: pathlib.Path, kind: str, name: str, prompt: str, positive: bool) -> None:
    (path / "graders").mkdir(parents=True, exist_ok=True)
    case_name = f"trig-{name}-{path.name}"
    tags = ["trigger", f"trigger-{kind}", name, "positive" if positive else "negative"]
    tools = ["Read", "Glob", "Grep", "Skill", "Agent"]
    (path / "prompt.md").write_text(
        "---\n"
        f"name: {case_name}\n"
        f"description: {q(('Should' if positive else 'Should NOT') + f' trigger {kind} {name}')}\n"
        f"tags: [{', '.join(tags)}]\n"
        "plugins: ['../../../..']\n"
        "max_turns: 6\n"
        "timeout_seconds: 240\n"
        f"allowed_tools: [{', '.join(tools)}]\n"
        "---\n\n"
        f"{prompt}\n"
    )
    if kind == "skill":
        tool, match = "Skill", rf'"skill"\s*:\s*"(?:[\w-]+:)?{name}"'
    else:
        tool, match = "Agent", rf'"subagent_type"\s*:\s*"(?:[\w-]+:)?{name}"'
    if positive:
        body = f"---\ntype: tool_used\ntool: {tool}\ninput_match: {q(match)}\n---\n"
        fname = "fired.md"
    else:
        body = (
            f"---\ntype: tool_used\ntool: {tool}\ninput_match: {q(match)}\n"
            "min: 0\nmax: 0\narm: both\n---\n"
        )
        fname = "did-not-fire.md"
    (path / "graders" / fname).write_text(body)


def main() -> None:
    spec = yaml.safe_load((HERE / "triggers.yaml").read_text())
    if OUT.exists():
        shutil.rmtree(OUT)
    count = 0
    for kind_key, kind in (("skills", "skill"), ("agents", "agent")):
        for name, sets in spec[kind_key].items():
            for i, p in enumerate(sets.get("positive", []), 1):
                write_case(OUT / name / f"pos-{i:02d}", kind, name, p, True)
                count += 1
            for i, p in enumerate(sets.get("negative", []), 1):
                write_case(OUT / name / f"neg-{i:02d}", kind, name, p, False)
                count += 1
    print(f"wrote {count} trigger cases to {OUT}")


if __name__ == "__main__":
    main()
