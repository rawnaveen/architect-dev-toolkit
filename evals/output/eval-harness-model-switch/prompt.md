---
description: 'eval-harness-model-switch'
tags: [output, skill, llm-eval-harness]
plugins: ['../../..']
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---
We want to switch our ticket summariser from claude-opus-5-5 to claude-haiku-5-5 to save money. How do we know quality won't drop? Give me the plan.
