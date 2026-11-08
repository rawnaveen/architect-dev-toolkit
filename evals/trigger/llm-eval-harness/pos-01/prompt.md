---
name: trig-llm-eval-harness-pos-01
description: 'Should trigger skill llm-eval-harness'
tags: [trigger, trigger-skill, llm-eval-harness, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

We want to switch our ticket summariser from Opus to Haiku to save money. Will quality drop? How do we check?
