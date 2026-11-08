---
name: trig-prompt-hardening-pos-01
description: 'Should trigger skill prompt-hardening'
tags: [trigger, trigger-skill, prompt-hardening, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Improve this system prompt: 'You are a bot. CRITICAL: ALWAYS answer in JSON. NEVER say anything else. Use the search tool ALWAYS.'
