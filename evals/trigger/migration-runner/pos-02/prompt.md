---
name: trig-migration-runner-pos-02
description: 'Should trigger agent migration-runner'
tags: [trigger, trigger-agent, migration-runner, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Move every service in this monorepo to the new logging library, module by module.
