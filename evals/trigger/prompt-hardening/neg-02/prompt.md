---
name: trig-prompt-hardening-neg-02
description: 'Should NOT trigger skill prompt-hardening'
tags: [trigger, trigger-skill, prompt-hardening, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Summarise this paragraph: Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.
