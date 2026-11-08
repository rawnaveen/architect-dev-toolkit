---
description: 'prompt-hardening-email-summariser'
tags: [output, skill, prompt-hardening]
plugins: ['../../..']
max_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---
Improve this system prompt for our email summariser running on claude-sonnet-5-5. The user turn contains the raw
customer email, and we also prefill the assistant turn with "Summary:".

```
YOU ARE A SUMMARY BOT. CRITICAL: YOU MUST ALWAYS USE THE lookup_customer TOOL. NEVER EVER USE MARKDOWN.
Summarise the email. Think step by step inside <thinking> tags first.
```
