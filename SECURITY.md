# Security

## What this edition contains

This is the Claude directory edition of Architect Dev Toolkit. It contains only Markdown, JSON and
two PNG images (the icon and the social preview). It ships no hooks, scripts, programs or MCP
servers, so installing it runs no code of its own.

Skills and agents are instructions for Claude. When they use tools (for example `Bash` in the
Kubernetes and review agents), those calls go through Claude Code's normal permission prompts and
your settings.

Some skills discuss credentials, environment variables and download commands as subject matter, for
example how an MCP server should receive an API key or which files a guardrail should protect. These
are documentation for the code you write; the plugin itself reads no credentials and sends no data.

## Reporting a vulnerability

Please report privately through GitHub's private vulnerability reporting:
https://github.com/rawnaveen/architect-dev-toolkit/security/advisories/new

Include what you found, how to reproduce it and the edition and version. You should get a response
within 7 days.
