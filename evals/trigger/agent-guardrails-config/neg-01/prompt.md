---
name: trig-agent-guardrails-config-neg-01
description: 'Should NOT trigger skill agent-guardrails-config'
tags: [trigger, trigger-skill, agent-guardrails-config, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

What is Kubernetes RBAC?
