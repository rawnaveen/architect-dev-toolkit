---
name: trig-incident-triage-pos-02
description: 'Should trigger agent incident-triage'
tags: [trigger, trigger-agent, incident-triage, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Prod is down, we're getting 500s from the payments API since the last release.
