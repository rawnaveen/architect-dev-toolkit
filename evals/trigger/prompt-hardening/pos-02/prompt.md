---
name: trig-prompt-hardening-pos-02
description: 'Should trigger skill prompt-hardening'
tags: [trigger, trigger-skill, prompt-hardening, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

The model keeps ignoring the formatting instructions in my prompt. Can you make the prompt better?
