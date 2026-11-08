---
name: trig-runbook-operator-neg-01
description: 'Should NOT trigger agent runbook-operator'
tags: [trigger, trigger-agent, runbook-operator, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write a runbook for restarting the payments service.
