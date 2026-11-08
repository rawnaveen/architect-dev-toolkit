---
type: llm
weight: 3
---
The repo has a ~420-line CLAUDE.md mixing global rules with module-specific rules for billing/ and search/,
and a .mcp.json with six MCP servers, several unrelated to this repo (spotify, figma, notion).
PASS if the advice includes: trimming CLAUDE.md under ~200 lines; moving module-specific rules to path-scoped
.claude/rules files (with paths frontmatter) and/or procedures into skills; disabling unused MCP servers; and at
least one usage habit or model lever (e.g. /clear between tasks, /compact, cheaper model or lower effort for routine
work, delegating searches to a cheap subagent).
FAIL if it misses the CLAUDE.md restructuring or the MCP servers.
