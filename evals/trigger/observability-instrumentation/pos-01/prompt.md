---
name: trig-observability-instrumentation-pos-01
description: 'Should trigger skill observability-instrumentation'
tags: [trigger, trigger-skill, observability-instrumentation, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Add metrics and tracing to this Spring Boot controller that handles refunds.
