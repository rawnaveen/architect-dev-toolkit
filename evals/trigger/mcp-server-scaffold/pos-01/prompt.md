---
name: trig-mcp-server-scaffold-pos-01
description: 'Should trigger skill mcp-server-scaffold'
tags: [trigger, trigger-skill, mcp-server-scaffold, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Build an MCP server that exposes read-only Confluence search to Claude.
