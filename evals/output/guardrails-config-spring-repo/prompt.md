---
description: 'guardrails-config-spring-repo'
tags: [output, skill, agent-guardrails-config, needs-write]
plugins: ['../../..']
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, Write, Edit]
---
Set up Claude Code safely for this repo: it should run Maven without asking, never read .env, never delete Kubernetes resources and never force push. Create the config files.
