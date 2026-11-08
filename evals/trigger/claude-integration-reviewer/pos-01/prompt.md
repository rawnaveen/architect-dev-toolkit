---
name: trig-claude-integration-reviewer-pos-01
description: 'Should trigger skill claude-integration-reviewer'
tags: [trigger, trigger-skill, claude-integration-reviewer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Is this Claude integration production ready? It's a Java service that calls the Messages API, parses the JSON reply, and retries on any exception.
