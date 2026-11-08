---
name: trig-mcp-server-scaffold-pos-02
description: 'Should trigger skill mcp-server-scaffold'
tags: [trigger, trigger-skill, mcp-server-scaffold, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

I want Claude Code to query our Postgres read replica. Create an MCP server for it in Python.
