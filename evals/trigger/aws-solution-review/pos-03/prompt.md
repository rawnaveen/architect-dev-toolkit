---
name: trig-aws-solution-review-pos-03
description: 'Should trigger skill aws-solution-review'
tags: [trigger, trigger-skill, aws-solution-review, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Check this Terraform: an S3 bucket with acl = public-read and an IAM policy with Action = '*' and Resource = '*'.
