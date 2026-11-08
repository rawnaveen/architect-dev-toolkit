---
name: trig-observability-instrumentation-pos-02
description: 'Should trigger skill observability-instrumentation'
tags: [trigger, trigger-skill, observability-instrumentation, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Make our Kafka consumer in Spring observable: we can't tell how far behind it is or how often it fails.
