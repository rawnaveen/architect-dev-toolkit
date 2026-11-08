---
name: trig-llm-eval-harness-pos-02
description: 'Should trigger skill llm-eval-harness'
tags: [trigger, trigger-skill, llm-eval-harness, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Build an eval for our Claude-powered invoice extraction feature.
