---
name: trig-agent-guardrails-config-pos-01
description: 'Should trigger skill agent-guardrails-config'
tags: [trigger, trigger-skill, agent-guardrails-config, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Set up Claude Code for this Spring Boot repo so it can run Maven without asking but can never touch .env or push to main.
