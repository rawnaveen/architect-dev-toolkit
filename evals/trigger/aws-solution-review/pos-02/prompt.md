---
name: trig-aws-solution-review-pos-02
description: 'Should trigger skill aws-solution-review'
tags: [trigger, trigger-skill, aws-solution-review, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Is this EKS setup well-architected? Pods use node IAM roles and secrets are in ConfigMaps.
