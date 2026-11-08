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

| Skill | Triggers on |
|---|---|
| `architecture-decision-record` | Technology choices and trade-offs, "write an ADR" |
| `aws-solution-review` | AWS/EKS designs, Terraform/CDK/Helm changes (Well-Architected lens) |
| `incident-postmortem` | Postmortems, RCA, incident reports (blameless template) |
| `observability-instrumentation` | New Spring services, endpoints, consumers; metrics, tracing, SLOs |
| `pr-architecture-review` | "Review my changes / this PR", before merge or push; runs three reviewers in parallel |
| `claude-api-cost-optimizer` | Writing or changing Claude / Amazon Bedrock API calls; "make this cheaper" |
| `claude-integration-reviewer` | Code that calls the Claude API, Agent SDK or MCP; "is this production ready" |
| `tool-schema-designer` | Defining tools / function calling, exposing an API to Claude |
| `mcp-server-scaffold` | "Build an MCP server", wrapping Jira, Confluence, kubectl or a database |
| `prompt-hardening` | Writing or improving prompts and system prompts |
| `llm-eval-harness` | Prompt or model changes, "build an eval", "compare models" |
| `agent-guardrails-config` | Setting up Claude Code in a repo: permissions, hooks, CLAUDE.md |
| `claude-code-cost-coach` | Hitting usage limits, token-heavy sessions, bloated CLAUDE.md |
| `ccdvf-flashcards` | "Quiz me", practice for the Claude Certified Developer: Foundations exam |

### Subagents (Claude Code)

| Agent | Model | Access | Used for |
|---|---|---|---|
| `doc-explorer` | Haiku | Read-only | Wide searches and log reading; returns a summary so the main context stays small |
| `security-reviewer` | Sonnet | Read-only | Security review after sensitive changes and before merge |
| `performance-reviewer` | Sonnet | Read-only | N+1 queries, blocking calls, caching, concurrency |
| `spring-conventions-reviewer` | Sonnet | Read-only | Layering, Spring idioms, transactions, API design, tests |
| `spring-test-writer` | Sonnet | Edit and run tests | JUnit 5, Mockito, slice tests, Testcontainers |
| `k8s-debugger` | Sonnet | Read-only | Failing pods, rollouts, EKS issues |
| `incident-triage` | Opus | Read-only | Incidents and alerts; delegates to `k8s-debugger` and `doc-explorer` |
| `dependency-upgrader` | Sonnet | Edit and build | Dependency, CVE and Spring Boot upgrades |
| `runbook-operator` | Inherits | Approval before every change | Following runbooks and tickets |
| `migration-runner` | Opus | Edit and build | Long migrations with `PROGRESS.md` and per-unit commits |

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
