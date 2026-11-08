---
name: trig-prompt-hardening-pos-03
description: 'Should trigger skill prompt-hardening'
tags: [trigger, trigger-skill, prompt-hardening, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Our summariser prompt reads customer emails, and I'm worried an email could hijack it. Harden the prompt.
