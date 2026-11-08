---
name: trig-claude-api-cost-optimizer-pos-04
description: 'Should trigger skill claude-api-cost-optimizer'
tags: [trigger, trigger-skill, claude-api-cost-optimizer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

We call Bedrock Claude from a Spring Boot service for every page view and latency and cost are both too high. What should we change?
