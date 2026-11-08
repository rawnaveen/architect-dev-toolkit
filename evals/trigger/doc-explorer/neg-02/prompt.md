---
name: trig-doc-explorer-neg-02
description: 'Should NOT trigger agent doc-explorer'
tags: [trigger, trigger-agent, doc-explorer, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write a Java method that sums a list of integers.
