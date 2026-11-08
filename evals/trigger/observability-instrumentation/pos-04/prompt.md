---
name: trig-observability-instrumentation-pos-04
description: 'Should trigger skill observability-instrumentation'
tags: [trigger, trigger-skill, observability-instrumentation, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Instrument our outbound HTTP client calls to the payments provider with OpenTelemetry.
