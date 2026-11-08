---
name: trig-incident-postmortem-pos-05
description: 'Should trigger skill incident-postmortem'
tags: [trigger, trigger-skill, incident-postmortem, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

We need a blameless incident report for the SEV2 last night where certificates expired.
