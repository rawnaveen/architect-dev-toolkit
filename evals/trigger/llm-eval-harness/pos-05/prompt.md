---
name: trig-llm-eval-harness-pos-05
description: 'Should trigger skill llm-eval-harness'
tags: [trigger, trigger-skill, llm-eval-harness, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

I changed the system prompt of our support bot. How can I be sure it didn't get worse?
