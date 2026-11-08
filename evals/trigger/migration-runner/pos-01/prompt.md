---
name: trig-migration-runner-pos-01
description: 'Should trigger agent migration-runner'
tags: [trigger, trigger-agent, migration-runner, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Migrate all 12 modules in this repo from javax to jakarta.
