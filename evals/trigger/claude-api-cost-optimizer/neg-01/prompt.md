---
name: trig-claude-api-cost-optimizer-neg-01
description: 'Should NOT trigger skill claude-api-cost-optimizer'
tags: [trigger, trigger-skill, claude-api-cost-optimizer, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

How much does an m7g.large EC2 instance cost per month in Sydney?
