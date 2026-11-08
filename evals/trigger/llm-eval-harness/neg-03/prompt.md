---
name: trig-llm-eval-harness-neg-03
description: 'Should NOT trigger skill llm-eval-harness'
tags: [trigger, trigger-skill, llm-eval-harness, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Set up load testing for our REST API with Gatling.
