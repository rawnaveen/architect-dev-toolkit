---
name: trig-k8s-debugger-neg-02
description: 'Should NOT trigger agent k8s-debugger'
tags: [trigger, trigger-agent, k8s-debugger, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write a Helm chart for a simple nginx app.
