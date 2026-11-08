---
name: trig-migration-runner-pos-03
description: 'Should trigger agent migration-runner'
tags: [trigger, trigger-agent, migration-runner, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Refactor every controller in this project to use the new error response model.
