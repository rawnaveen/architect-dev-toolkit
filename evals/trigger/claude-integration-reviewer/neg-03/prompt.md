---
name: trig-claude-integration-reviewer-neg-03
description: 'Should NOT trigger skill claude-integration-reviewer'
tags: [trigger, trigger-skill, claude-integration-reviewer, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write a unit test for a Java method that reverses a string.
