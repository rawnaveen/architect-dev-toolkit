---
description: 'hook-cost-guard-large-log'
tags: [output, hook]
plugins: ['../../..']
max_turns: 10
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Agent, Skill]
---
Read the whole of app.log and tell me which error message appears most often.
