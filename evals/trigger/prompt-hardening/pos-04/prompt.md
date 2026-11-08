---
name: trig-prompt-hardening-pos-04
description: 'Should trigger skill prompt-hardening'
tags: [trigger, trigger-skill, prompt-hardening, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

We're migrating our prompts from Claude Sonnet 4.5 to Sonnet 5.5. Rewrite this prompt for the new model: 'Think step by step inside <thinking> tags, then answer.'
