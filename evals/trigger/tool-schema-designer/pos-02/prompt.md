---
name: trig-tool-schema-designer-pos-02
description: 'Should trigger skill tool-schema-designer'
tags: [trigger, trigger-skill, tool-schema-designer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Turn this OpenAPI operation into a Claude tool: operationId searchCustomers, query params name, email, page.
