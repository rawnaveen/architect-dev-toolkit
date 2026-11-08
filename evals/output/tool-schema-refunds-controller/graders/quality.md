---
type: llm
weight: 3
---
PASS if the tool definitions use namespaced names (for example refunds_get or a consolidated refunds tool with an
action parameter), give each tool a multi-sentence description that says when to use it and when not to, mark
required fields, and flag the cancel/create operations as state-changing actions that need confirmation or approval.
FAIL if names are generic (like "get" or "create"), descriptions are one-liners, or risk is not mentioned.
