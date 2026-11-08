---
name: trig-prompt-hardening-pos-05
description: 'Should trigger skill prompt-hardening'
tags: [trigger, trigger-skill, prompt-hardening, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

My prompt gives inconsistent output formats between runs. Here it is: 'Summarise the doc. Give key points. Be concise.'
