---
name: trig-security-reviewer-pos-03
description: 'Should trigger agent security-reviewer'
tags: [trigger, trigger-agent, security-reviewer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Threat check our new file upload endpoint for vulnerabilities.
