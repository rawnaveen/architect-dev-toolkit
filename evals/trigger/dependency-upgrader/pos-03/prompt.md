---
name: trig-dependency-upgrader-pos-03
description: 'Should trigger agent dependency-upgrader'
tags: [trigger, trigger-agent, dependency-upgrader, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Bump all our outdated dependencies in this Maven project.
