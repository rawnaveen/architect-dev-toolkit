---
name: trig-runbook-operator-pos-01
description: 'Should trigger agent runbook-operator'
tags: [trigger, trigger-agent, runbook-operator, positive]
plugins: ['../../../..']
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Follow the runbook for rotating the TLS certificate on the ingress, steps are in the file docs/runbooks/cert-rotation.md.
