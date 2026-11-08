---
name: trig-k8s-debugger-pos-02
description: 'Should trigger agent k8s-debugger'
tags: [trigger, trigger-agent, k8s-debugger, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

My pod keeps going into CrashLoopBackOff on EKS. Investigate.
