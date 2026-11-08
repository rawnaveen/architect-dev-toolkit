---
name: trig-claude-integration-reviewer-pos-03
description: 'Should trigger skill claude-integration-reviewer'
tags: [trigger, trigger-skill, claude-integration-reviewer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Review how our Python worker handles Claude tool_use responses and tool_result messages.
