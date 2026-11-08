---
name: trig-performance-reviewer-pos-02
description: 'Should trigger agent performance-reviewer'
tags: [trigger, trigger-agent, performance-reviewer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Is there anything in this repository's data-access layer that won't scale?
