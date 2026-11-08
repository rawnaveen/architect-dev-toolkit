---
name: trig-incident-postmortem-pos-04
description: 'Should trigger skill incident-postmortem'
tags: [trigger, trigger-skill, incident-postmortem, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Summarise this outage for the incident report: DNS change at 09:10 broke service discovery until 09:55.
