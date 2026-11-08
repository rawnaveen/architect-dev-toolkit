---
name: trig-runbook-operator-pos-02
description: 'Should trigger agent runbook-operator'
tags: [trigger, trigger-agent, runbook-operator, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Work through OPS-482, the Kafka consumer lag runbook.
