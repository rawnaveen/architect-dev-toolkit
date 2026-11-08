---
name: trig-mcp-server-scaffold-neg-02
description: 'Should NOT trigger skill mcp-server-scaffold'
tags: [trigger, trigger-skill, mcp-server-scaffold, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Set up a Spring Boot REST endpoint that returns inventory levels.
