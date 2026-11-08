---
name: trig-claude-api-cost-optimizer-pos-01
description: 'Should trigger skill claude-api-cost-optimizer'
tags: [trigger, trigger-skill, claude-api-cost-optimizer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Our nightly job sends 40k support tickets to claude-sonnet-5-5 with the same 6k-token system prompt each time and the bill is huge. How do we cut the cost?
