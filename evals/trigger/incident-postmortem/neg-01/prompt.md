---
name: trig-incident-postmortem-neg-01
description: 'Should NOT trigger skill incident-postmortem'
tags: [trigger, trigger-skill, incident-postmortem, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Prod is down right now, checkout returns 503s! Help me find out why.
