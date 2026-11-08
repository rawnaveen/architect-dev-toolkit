---
name: trig-llm-eval-harness-pos-03
description: 'Should trigger skill llm-eval-harness'
tags: [trigger, trigger-skill, llm-eval-harness, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

How do I regression test prompts in CI so a prompt change doesn't break production?
