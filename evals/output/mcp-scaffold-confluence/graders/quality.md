---
type: llm
weight: 2
---
PASS if the answer provides tool definitions with descriptive docstrings for search and page read, keeps the
server read-only, reads credentials from environment variables, logs to stderr (not stdout) for stdio, and shows
registration with `claude mcp add` or a .mcp.json entry.
FAIL if credentials are hard-coded or registration is missing.
