---
name: trig-performance-reviewer-neg-02
description: 'Should NOT trigger agent performance-reviewer'
tags: [trigger, trigger-agent, performance-reviewer, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

How do I measure CPU usage on Linux?
