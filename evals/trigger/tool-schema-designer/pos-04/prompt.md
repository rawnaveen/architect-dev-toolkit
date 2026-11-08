---
name: trig-tool-schema-designer-pos-04
description: 'Should trigger skill tool-schema-designer'
tags: [trigger, trigger-skill, tool-schema-designer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Design the function-calling schema for a tool that books a meeting room with date, start time, duration and attendees.
