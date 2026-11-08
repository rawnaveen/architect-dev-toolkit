---
name: trig-claude-integration-reviewer-pos-02
description: 'Should trigger skill claude-integration-reviewer'
tags: [trigger, trigger-skill, claude-integration-reviewer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

My Claude API call sometimes returns truncated JSON and my parser crashes. What am I doing wrong?
