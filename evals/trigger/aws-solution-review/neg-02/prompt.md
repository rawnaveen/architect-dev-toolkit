---
name: trig-aws-solution-review-neg-02
description: 'Should NOT trigger skill aws-solution-review'
tags: [trigger, trigger-skill, aws-solution-review, negative]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write a Python script to upload a file to S3 with boto3.
