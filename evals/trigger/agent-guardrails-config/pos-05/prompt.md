---
name: trig-agent-guardrails-config-pos-05
description: 'Should trigger skill agent-guardrails-config'
tags: [trigger, trigger-skill, agent-guardrails-config, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Allow these commands without asking: ./mvnw test, git status, git diff.
