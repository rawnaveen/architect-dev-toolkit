---
name: trig-agent-guardrails-config-pos-03
description: 'Should trigger skill agent-guardrails-config'
tags: [trigger, trigger-skill, agent-guardrails-config, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Create a .claude/settings.json and a CLAUDE.md for our payments service.
