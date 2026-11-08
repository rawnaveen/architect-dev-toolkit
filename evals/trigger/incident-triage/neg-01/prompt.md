---
name: trig-incident-triage-neg-01
description: 'Should NOT trigger agent incident-triage'
tags: [trigger, trigger-agent, incident-triage, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write a postmortem for last week's outage from these notes: deploy at 14:02, rollback at 14:20.
