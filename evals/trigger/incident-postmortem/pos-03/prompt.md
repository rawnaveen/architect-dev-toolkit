---
name: trig-incident-postmortem-pos-03
description: 'Should trigger skill incident-postmortem'
tags: [trigger, trigger-skill, incident-postmortem, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Turn these Slack notes from the incident into a post incident review.
