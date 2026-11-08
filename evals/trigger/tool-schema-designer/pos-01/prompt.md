---
name: trig-tool-schema-designer-pos-01
description: 'Should trigger skill tool-schema-designer'
tags: [trigger, trigger-skill, tool-schema-designer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

I want Claude to be able to call our refunds REST API: GET /refunds/{id}, POST /refunds, POST /refunds/{id}/cancel. Write the tool definitions.
