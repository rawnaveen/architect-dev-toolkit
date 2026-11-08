---
name: trig-performance-reviewer-pos-01
description: 'Should trigger agent performance-reviewer'
tags: [trigger, trigger-agent, performance-reviewer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Review the order service code in this repo for performance problems like N+1 queries.
