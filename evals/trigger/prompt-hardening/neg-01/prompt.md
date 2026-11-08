---
name: trig-prompt-hardening-neg-01
description: 'Should NOT trigger skill prompt-hardening'
tags: [trigger, trigger-skill, prompt-hardening, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write a haiku about Sydney Harbour.
