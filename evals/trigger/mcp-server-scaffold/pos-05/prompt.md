---
name: trig-mcp-server-scaffold-pos-05
description: 'Should trigger skill mcp-server-scaffold'
tags: [trigger, trigger-skill, mcp-server-scaffold, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Create an MCP integration so Claude can list and describe our Kubernetes deployments without changing anything.
