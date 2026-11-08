---
description: 'aws-review-terraform'
tags: [output, skill, aws-solution-review]
plugins: ['../../..']
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---
Review main.tf before we apply it to production.
