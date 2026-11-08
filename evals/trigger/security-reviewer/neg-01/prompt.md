---
name: trig-security-reviewer-neg-01
description: 'Should NOT trigger agent security-reviewer'
tags: [trigger, trigger-agent, security-reviewer, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

What is OAuth 2.0?
