---
name: trig-claude-integration-reviewer-neg-01
description: 'Should NOT trigger skill claude-integration-reviewer'
tags: [trigger, trigger-skill, claude-integration-reviewer, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Review this SQL query for performance: SELECT * FROM orders WHERE status = 'NEW' ORDER BY created_at.
