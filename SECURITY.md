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

## Reporting a vulnerability

Please do **not** open a public issue. Use GitHub's
[private vulnerability reporting](https://github.com/rawnaveen/architect-dev-toolkit/security/advisories/new)
for this repository, with steps to reproduce and the Claude Code version.

You should get an acknowledgement within 7 days. Fixes are released as a new version with a note
in `CHANGELOG.md`.
