---
name: trig-spring-test-writer-pos-01
description: 'Should trigger agent spring-test-writer'
tags: [trigger, trigger-agent, spring-test-writer, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Write unit tests for the services in this Spring Boot repo and run them.
