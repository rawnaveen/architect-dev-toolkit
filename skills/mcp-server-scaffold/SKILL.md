---
name: mcp-server-scaffold
description: >
  This skill should be used when the user asks to "build an MCP server", "create an MCP integration",
  "expose our service/Jira/Confluence/database/kubectl to Claude via MCP", "wrap this API as MCP",
  or debug an MCP server that disconnects or returns errors. Applies to Java (MCP Java SDK / Spring AI)
  and Python (FastMCP) servers over stdio or Streamable HTTP.
metadata:
  version: "0.1.0"
---

# MCP server scaffold

## Decide the shape first
- **Tools** (model-controlled): actions and queries Claude calls. **Resources** (app-controlled):
  read-only data by URI. **Prompts** (user-controlled): reusable templates.
- Transport: **stdio** for local/dev tools launched by Claude Code or Desktop; **Streamable HTTP** for
  shared remote servers (OAuth 2.1). Do not use the deprecated HTTP+SSE transport.
- Spec 2026-07-28 is stateless: no initialize handshake or session id; servers implement
  `server/discover`; cross-call state goes in explicit handles passed as tool arguments. Do not build on
  Sampling or Roots (deprecated) - pass paths as parameters, call the LLM provider directly.

## Procedure
1. List capabilities from the source API; design tools with the tool-schema-designer rules
   (namespaced names, rich descriptions, strict schemas, concise outputs, `is_error` messages).
2. Add tool annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) - remember
   clients treat them as hints only.
3. Scaffold the project:
   - Python: `uv init`, `mcp[cli]`, `FastMCP("name")`, `@mcp.tool()` functions with type hints and
     docstrings, `mcp.run()`.
   - Java: MCP Java SDK (or Spring AI MCP server starter), `McpServer.sync(...)` with tool specs, Jackson
     schemas.
4. **Log to stderr only** for stdio servers - stdout carries JSON-RPC.
5. Credentials from env vars or a secrets manager; never return secrets in results. For remote servers
   put OAuth at the edge and scope tokens per user.
6. Return tools from `tools/list` in deterministic order (helps prompt caching).
7. Test with the MCP Inspector (`npx @modelcontextprotocol/inspector <command>`), then register:
   - Claude Code: `claude mcp add <name> -- <command>` or project `.mcp.json` (team-shared).
   - Claude Desktop: Settings > Connectors / developer config.
   - Messages API: MCP connector (`mcp_servers` in request; remote servers only).
8. Write a README: tools, required env vars, auth, example prompts.

## Safety
Read-only by default. Destructive tools require an explicit `confirm: true` parameter and should be
paired with an `ask` permission rule in Claude Code.
