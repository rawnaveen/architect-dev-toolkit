---
name: trig-dependency-upgrader-pos-02
description: 'Should trigger agent dependency-upgrader'
tags: [trigger, trigger-agent, dependency-upgrader, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Dependabot flagged jackson-databind as vulnerable, fix it.
