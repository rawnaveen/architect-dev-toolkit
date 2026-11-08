---
name: trig-claude-api-cost-optimizer-neg-02
description: 'Should NOT trigger skill claude-api-cost-optimizer'
tags: [trigger, trigger-skill, claude-api-cost-optimizer, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

My Claude Code sessions keep hitting the usage limit, how do I make Claude Code itself use fewer tokens?
