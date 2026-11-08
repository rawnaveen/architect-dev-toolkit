---
name: trig-incident-triage-pos-03
description: 'Should trigger agent incident-triage'
tags: [trigger, trigger-agent, incident-triage, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Alert fired: error rate on orders-service jumped to 15% after the 3pm deploy.
