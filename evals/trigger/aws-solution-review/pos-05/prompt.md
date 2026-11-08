---
name: trig-aws-solution-review-pos-05
description: 'Should trigger skill aws-solution-review'
tags: [trigger, trigger-skill, aws-solution-review, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Estimate the AWS cost drivers and risks for this design: 3 NAT gateways, cross-AZ traffic heavy microservices, CloudWatch logs retained forever.
