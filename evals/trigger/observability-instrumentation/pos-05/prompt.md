---
name: trig-observability-instrumentation-pos-05
description: 'Should trigger skill observability-instrumentation'
tags: [trigger, trigger-skill, observability-instrumentation, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Set up structured JSON logging with trace IDs in our Spring Boot 3 service.
