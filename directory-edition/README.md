# Architect Dev Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A Claude plugin for engineers and architects who work with
**Java/Spring Boot, AWS/EKS, SRE practices and the Claude API**.

It adds **14 skills and 10 subagents** that work without being called by name:

- **Skills** load when your request matches them ("should we use Kafka or SQS?" writes an ADR).
- **Subagents** are delegated to automatically in Claude Code ("our pod is in CrashLoopBackOff"
  starts a read-only Kubernetes investigation).

You can still call anything by name, for example `/architect-dev-toolkit:architecture-decision-record`
or "use the k8s-debugger agent".

> **Two editions.** This is the **directory edition**: skills and agents only, made entirely of
> Markdown and JSON. The **full edition** adds three hooks that block destructive or
> production-changing commands, secret-file reads and token-wasting reads, and that enforce read-only
> agents. Install it from GitHub:
> `/plugin marketplace add rawnaveen/architect-dev-toolkit` then
> `/plugin install architect-dev-toolkit@rawnaveen`. Source, tests and evals:
> https://github.com/rawnaveen/architect-dev-toolkit

## What's inside

### Skills (Claude Code and Claude apps)

<!-- SKILLS_TABLE -->

### Subagents (Claude Code)

<!-- AGENTS_TABLE -->

"Read-only" agents are read-only by instruction in this edition. Detailed descriptions:
[docs/components.md](docs/components.md).

## How the automatic behaviour works

| Mechanism | What makes it automatic | Reliability |
|---|---|---|
| Skills | Claude matches your request to each skill's `description` and loads its instructions on demand | Usually; depends on phrasing |
| Subagents | Claude delegates when a task matches the agent's description (several say "use PROACTIVELY") | Usually; Claude decides |

Only the short skill and agent descriptions sit in context each session; full instructions load
when used.

### Cost optimisation

- **Automatic:** Haiku `doc-explorer` for searches; Sonnet-pinned reviewers; on-demand skill loading;
  `claude-api-cost-optimizer` when you write Claude API code.
- **One-time per repo:** ask "optimise my Claude setup" to run `claude-code-cost-coach`. It proposes
  CLAUDE.md, rules, MCP and settings changes and applies them only after you confirm.

## Requirements and limitations

- Claude Code with plugin support for subagents. Skills also work in the Claude apps.
- Some content is opinionated towards Java/Spring Boot and AWS/EKS.
- Model IDs and prices in the Claude cost skills were checked on 2026-11-08; re-check against the
  [Anthropic docs](https://platform.claude.com/docs) as models change.

## Support, security and privacy

- Issues and contributions: https://github.com/rawnaveen/architect-dev-toolkit
- Security: [SECURITY.md](SECURITY.md)
- Privacy: [PRIVACY.md](PRIVACY.md). The plugin has no backend and collects nothing.

## License

[MIT](LICENSE) © 2026 Naveen Rawat
