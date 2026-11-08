---
name: trig-doc-explorer-pos-01
description: 'Should trigger agent doc-explorer'
tags: [trigger, trigger-agent, doc-explorer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Where in this codebase do we call the payments service, and with what timeouts?
