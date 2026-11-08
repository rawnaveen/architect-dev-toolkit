---
name: trig-llm-eval-harness-pos-04
description: 'Should trigger skill llm-eval-harness'
tags: [trigger, trigger-skill, llm-eval-harness, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Compare claude-sonnet-5-5 and claude-haiku-5-5 on our classification task.
