---
name: trig-incident-postmortem-pos-02
description: 'Should trigger skill incident-postmortem'
tags: [trigger, trigger-skill, incident-postmortem, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Do an RCA for this incident thread: payments timed out for 40 minutes because the connection pool was exhausted after a config change.
