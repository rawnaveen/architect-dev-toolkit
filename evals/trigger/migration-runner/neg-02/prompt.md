---
name: trig-migration-runner-neg-02
description: 'Should NOT trigger agent migration-runner'
tags: [trigger, trigger-agent, migration-runner, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

What changed between Spring Boot 2 and 3?
