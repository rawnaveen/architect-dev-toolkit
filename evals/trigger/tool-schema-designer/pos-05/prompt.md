---
name: trig-tool-schema-designer-pos-05
description: 'Should trigger skill tool-schema-designer'
tags: [trigger, trigger-skill, tool-schema-designer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write an input_schema for a Claude tool that creates a Jira ticket.
