---
description: 'postmortem-blameless'
tags: [output, skill, incident-postmortem]
plugins: ['../../..']
max_turns: 10
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---
Write the incident report for last night. Notes from the channel:
- 21:40 Raj deployed checkout v3.1 which added a query on orders.customer_ref
- 21:46 p99 latency alerts, DB CPU at 98%
- 21:58 on-call paged, Raj was blamed in the channel for not testing
- 22:25 identified full table scans, missing index on orders.customer_ref
- 22:31 index created, latency recovered by 22:40
- about 6% of checkouts failed during the window
