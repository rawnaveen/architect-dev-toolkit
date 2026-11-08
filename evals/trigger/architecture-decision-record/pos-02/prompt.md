---
name: trig-architecture-decision-record-pos-02
description: 'Should trigger skill architecture-decision-record'
tags: [trigger, trigger-skill, architecture-decision-record, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write an ADR for moving our session store from Redis to DynamoDB.
