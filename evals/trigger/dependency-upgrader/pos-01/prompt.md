---
name: trig-dependency-upgrader-pos-01
description: 'Should trigger agent dependency-upgrader'
tags: [trigger, trigger-agent, dependency-upgrader, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Upgrade this project from Spring Boot 3.3 to 3.5 and fix anything that breaks.
