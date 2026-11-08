---
description: 'api-cost-optimizer-nightly-job'
tags: [output, skill, claude-api-cost-optimizer]
plugins: ['../../..']
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---
This nightly job in nightly_classify.py is costing us a fortune on the Claude API and nobody needs the results before 8am. How do we make it much cheaper without hurting quality?
