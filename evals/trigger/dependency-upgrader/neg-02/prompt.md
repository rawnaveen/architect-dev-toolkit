---
name: trig-dependency-upgrader-neg-02
description: 'Should NOT trigger agent dependency-upgrader'
tags: [trigger, trigger-agent, dependency-upgrader, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

How does Maven dependency resolution work?
