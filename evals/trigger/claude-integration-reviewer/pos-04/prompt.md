---
name: trig-claude-integration-reviewer-pos-04
description: 'Should trigger skill claude-integration-reviewer'
tags: [trigger, trigger-skill, claude-integration-reviewer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

The Anthropic SDK call in our service hangs for minutes on long reports. What's wrong with how we call it?
