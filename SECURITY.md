# Security policy

## Scope

This plugin runs hook scripts on your machine and gives Claude instructions that can lead to commands
being run. Relevant issues include:

- A way to bypass a guard in `hooks/scripts/guard.py`, for example a destructive or production command
  it should block but doesn't
- A skill or agent instruction that leads Claude to leak secrets or take destructive action
- Anything that sends data off the machine unexpectedly

The hooks are a safety net based on pattern matching, not a security boundary. Use least-privilege
credentials and Claude Code's sandbox for real isolation.

## What the plugin runs, and what it doesn't

For users and reviewers: the plugin runs exactly one program, `hooks/scripts/guard.py` (Python standard
library only), from the three hooks in `hooks/hooks.json`. It:

- **Makes no network connections.** It imports no networking modules and sends nothing off the machine.
- **Reads no credentials.** It never opens secret files; it only matches the *paths* in Claude's tool calls
  against a list of secret-file patterns, so it can block them.
- **Opens one file:** `PROGRESS.md` in the project root, if present, to show it as session context.
- **Runs one subprocess:** `kubectl config current-context`, with a 3-second timeout, to tell whether the
  active Kubernetes context is production. Its output is used only for that check.
- **Reads environment variables** `AWS_PROFILE` (production detection), `ADT_COST_GUARD` (on/off switch) and
  `CLAUDE_PROJECT_DIR` (where to look for `PROGRESS.md`).
- **Checks file sizes** (not contents) for the cost guard.

Credential paths, regular expressions and command examples in the skills and docs are rules and
documentation: the deny lists Claude writes into settings files, and the patterns the guard blocks. They are
not code that reads or transmits anything. The Python files under `tests/`, `examples/` and `evals/` are
developer tooling that Claude Code never runs as part of the plugin.

## Reporting a vulnerability

Please do **not** open a public issue. Use GitHub's
[private vulnerability reporting](https://github.com/rawnaveen/architect-dev-toolkit/security/advisories/new)
for this repository, with steps to reproduce and the Claude Code version.

You should get an acknowledgement within 7 days. Fixes are released as a new version with a note
in `CHANGELOG.md`.
