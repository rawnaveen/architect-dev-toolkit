---
name: trig-incident-postmortem-pos-01
description: 'Should trigger skill incident-postmortem'
tags: [trigger, trigger-skill, incident-postmortem, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write a postmortem for yesterday's outage: 14:02 deploy of checkout v2.3, 14:05 5xx alerts, 14:20 rollback, 14:31 recovered. Cause was a missing DB index.
