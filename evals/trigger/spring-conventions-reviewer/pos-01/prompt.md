---
name: trig-spring-conventions-reviewer-pos-01
description: 'Should trigger agent spring-conventions-reviewer'
tags: [trigger, trigger-agent, spring-conventions-reviewer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Does the code in this Spring Boot repo follow good Spring conventions? Review the design.
