---
name: trig-incident-triage-pos-01
description: 'Should trigger agent incident-triage'
tags: [trigger, trigger-agent, incident-triage, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

PagerDuty: checkout-api p99 latency > 2s for 10 minutes in prod. Help!
