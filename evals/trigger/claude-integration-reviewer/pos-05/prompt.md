---
name: trig-claude-integration-reviewer-pos-05
description: 'Should trigger skill claude-integration-reviewer'
tags: [trigger, trigger-skill, claude-integration-reviewer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

We prefill the assistant turn with '{' to force JSON and since upgrading the model we get a 400. Why?
