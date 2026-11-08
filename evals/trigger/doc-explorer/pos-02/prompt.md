---
name: trig-doc-explorer-pos-02
description: 'Should trigger agent doc-explorer'
tags: [trigger, trigger-agent, doc-explorer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Find every place we read the 'feature.flags' config and summarise how it's used.
