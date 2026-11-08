---
description: 'adr-kafka-vs-sqs'
tags: [output, skill, architecture-decision-record]
plugins: ['../../..']
max_turns: 10
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---
We need to pick between Amazon MSK (Kafka) and SQS FIFO for payment events between services on EKS. Requirements: ordering per account, ability to replay the last 7 days, about 3,000 events/sec peak, small platform team. Write this up as a decision record.
