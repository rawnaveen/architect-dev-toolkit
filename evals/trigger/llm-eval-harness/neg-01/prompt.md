---
name: trig-llm-eval-harness-neg-01
description: 'Should NOT trigger skill llm-eval-harness'
tags: [trigger, trigger-skill, llm-eval-harness, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write JUnit tests for this Calculator class.
