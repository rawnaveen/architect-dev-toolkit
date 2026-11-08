---
name: trig-architecture-decision-record-pos-01
description: 'Should trigger skill architecture-decision-record'
tags: [trigger, trigger-skill, architecture-decision-record, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Should we use Kafka or SQS for payment events between our EKS services? We need ordering per account and replay.
