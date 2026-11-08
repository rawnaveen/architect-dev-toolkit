---
name: trig-tool-schema-designer-pos-03
description: 'Should trigger skill tool-schema-designer'
tags: [trigger, trigger-skill, tool-schema-designer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Claude keeps calling get_order when it should call get_order_history. How should I redesign these two tools?
