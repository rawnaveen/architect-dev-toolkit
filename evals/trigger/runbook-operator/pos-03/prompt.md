---
name: trig-runbook-operator-pos-03
description: 'Should trigger agent runbook-operator'
tags: [trigger, trigger-agent, runbook-operator, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Run the DR checklist for the payments database step by step.
