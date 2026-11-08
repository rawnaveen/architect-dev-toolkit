---
name: trig-claude-api-cost-optimizer-pos-05
description: 'Should trigger skill claude-api-cost-optimizer'
tags: [trigger, trigger-skill, claude-api-cost-optimizer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Make this Claude API call cheaper: client.messages.create(model='claude-opus-5-5', max_tokens=64000, system=BIG_PROMPT, messages=msgs)
