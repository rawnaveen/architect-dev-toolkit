---
name: trig-observability-instrumentation-neg-02
description: 'Should NOT trigger skill observability-instrumentation'
tags: [trigger, trigger-skill, observability-instrumentation, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Our pod is in CrashLoopBackOff, why?
