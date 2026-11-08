# Privacy policy

_Last updated: 8 November 2026_

Architect Dev Toolkit is an open-source plugin for Claude Code and Claude. This policy explains what
data the plugin handles. It applies to the plugin's own components (skills, agents and hooks) in this
repository.

## Summary

- The plugin has **no backend service**. It collects nothing, and it sends nothing to the author or
  any third party.
- It **stores no personal data** of its own.
- Some components **read content you give Claude or open through your own connectors**, and that content
  may contain personal data such as names or email addresses.

## What the plugin reads

Skills and agents run inside your Claude session and act only on content that you provide or that Claude
accesses with your tools and connectors. For example:

- `incident-postmortem` works from incident notes, chat threads or logs you share, which may name people.
- `runbook-operator` reads tickets and wiki pages through connectors you have set up (such as Jira or
  Confluence), which may contain names and email addresses.
- Review and debugging agents read code, configuration and logs in your workspace.

This content is processed by Claude under your agreement with Anthropic (or your cloud provider). The
plugin does not copy, export or retain it.

## What the hook script does

`hooks/scripts/guard.py` runs locally on your machine. It:

- makes no network connections
- never opens secret files; it only checks the file paths in Claude's tool calls so it can block them
- opens one file, `PROGRESS.md` in your project, if present
- runs one local command, `kubectl config current-context`, to detect production contexts
- reads the environment variables `AWS_PROFILE`, `ADT_COST_GUARD` and `CLAUDE_PROJECT_DIR`

See [SECURITY.md](SECURITY.md) for details.

## What the plugin writes

Only files you ask for, in your own workspace, for example ADRs, settings files, tests, or `PROGRESS.md`
for long-running tasks. These stay under your control. Content you include in them, such as names in an
ADR's "Deciders" line, is stored only where you save it.

## Data sent to other services

None by the plugin. Two agents (`doc-explorer`, `dependency-upgrader`) may use Claude Code's built-in web
fetch to read public pages such as library release notes. This requests a public URL and does not send
your data.

## Retention

The plugin retains nothing. There is no service to retain data in.

## Children

The plugin is intended for professional software engineers and is not directed at anyone under 18.

## Changes and contact

Changes to this policy are recorded in this file's history and in [CHANGELOG.md](CHANGELOG.md). For
questions, open an issue at https://github.com/rawnaveen/architect-dev-toolkit/issues. For security
concerns, see [SECURITY.md](SECURITY.md).
