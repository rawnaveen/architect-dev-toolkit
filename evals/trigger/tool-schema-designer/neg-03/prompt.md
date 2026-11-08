---
name: trig-tool-schema-designer-neg-03
description: 'Should NOT trigger skill tool-schema-designer'
tags: [trigger, trigger-skill, tool-schema-designer, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Generate a Java record for a Customer with name, email and address.
