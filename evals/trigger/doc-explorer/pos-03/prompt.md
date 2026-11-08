---
name: trig-doc-explorer-pos-03
description: 'Should trigger agent doc-explorer'
tags: [trigger, trigger-agent, doc-explorer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Scan the logs folder and tell me what's causing the 500 errors.
