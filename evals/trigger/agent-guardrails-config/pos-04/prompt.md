---
name: trig-agent-guardrails-config-pos-04
description: 'Should trigger skill agent-guardrails-config'
tags: [trigger, trigger-skill, agent-guardrails-config, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Lock down a headless Claude Agent SDK agent so it can only read files and run our test command.
