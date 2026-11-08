---
name: tool-schema-designer
description: >
  This skill should be used when the user wants to "expose an API to Claude", "turn this endpoint /
  controller / OpenAPI spec into a tool", "write a tool definition", "design function calling schema",
  "Claude keeps calling the wrong tool", or is defining tools for the Claude API, Agent SDK or an MCP
  server. Apply proactively whenever a new tool definition or MCP tool is being written.
metadata:
  version: "0.1.0"
---

# Tool schema designer

Produce Claude tool definitions that are easy to select correctly and hard to misuse.

## Procedure
1. Read the source (Spring `@RestController`, OpenAPI, service interface, function).
2. Group operations. Consolidate related ones into one tool with an `action` enum when they share a
   resource (e.g. `jira_issue` with `action: create|update|get|transition`). Keep the toolset small.
3. Name with a service namespace, using 1 to 128 letters, digits, underscores or hyphens, e.g. `payments_get_refund_status`.
4. Write the description (3-6 sentences): what it does, when to use it, when NOT to use it (name the
   sibling tool to use instead), what each parameter means, side effects, and what it does not return.
5. Write `input_schema`: `type: object`, explicit `required`, `additionalProperties: false`, enums for
   closed sets, formats for dates/emails, descriptions on every property. Prefer flat structures.
   Use IDs Claude can see (slugs, UUIDs), not internal opaque refs.
6. Add `strict: true` when inputs must validate (max 20 strict tools/request, 24 optional params total,
   16 union-typed params).
7. Add 1-3 `input_examples` that validate against the schema (not allowed on server tools).
8. Define the result contract: concise JSON with only fields needed for the next step; pagination
   (`next_cursor`); errors returned as `is_error: true` text that tells Claude how to recover.
9. Flag risky tools (writes, deletes, payments, sends) for approval gating.
10. If there are more than ~30 tools, recommend `defer_loading: true` plus the tool search tool.

## Avoid
- Parameters that ask for "reasoning" (can trigger `reasoning_extraction` refusals) - ask for a short
  `justification` only if needed.
- Aggressive wording ("MUST ALWAYS use this tool") - causes over-triggering on current models.
- Returning whole entities or logs; truncate and summarise.

## Output
Return the JSON tool definitions, a short table (tool | purpose | risk | strict), and the Java (Anthropic
Java SDK) or Python registration snippet the user's project uses.
