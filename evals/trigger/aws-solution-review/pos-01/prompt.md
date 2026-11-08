---
name: trig-aws-solution-review-pos-01
description: 'Should trigger skill aws-solution-review'
tags: [trigger, trigger-skill, aws-solution-review, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Review this architecture: ALB -> EKS (single node group in one AZ) -> RDS PostgreSQL single-AZ, S3 bucket for uploads with public read.
