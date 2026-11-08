---
name: claude-integration-reviewer
description: >
  This skill should be used when reviewing, writing or debugging code that integrates with Claude
  (Anthropic API, Claude SDKs in Java/Python/TypeScript, Amazon Bedrock Claude, Claude Agent SDK, MCP
  clients), including requests like "review my Claude integration", "is this LLM code production ready",
  "why does my Claude call fail/hang/return truncated JSON", or whenever a PR touches files that call
  the Messages API. Apply proactively when such code is created or changed.
metadata:
  version: "0.1.0"
---

# Claude integration production-readiness review

Check every item below against the code in scope. Report findings by severity (Critical / Warning /
Info) with file:line, the problem, and the fix.

## Request and response handling
- Branch on `stop_reason` (`end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, `pause_turn`,
  `refusal`). Never parse output without checking it. `refusal` returns HTTP 200.
- No assistant prefill on Claude 4.6+ (400). Use structured outputs (`output_config.format` or
  `strict: true` tools) for JSON.
- Forced `tool_choice` (`any`/`tool`) returns 400 on Opus 5.5, Sonnet 5.5, Fable 5.1.
- Citations and structured outputs together return 400.
- Large `max_tokens` or long generations use streaming (`.stream()` + `get_final_message()`) or batches.
- Streams handle `error` events after HTTP 200, ignore `ping` and unknown events, accumulate
  `input_json_delta` and parse at `content_block_stop`.

## Tool loop correctness
- Append the full assistant `content` (thinking + tool_use blocks unmodified).
- Return one user message with a `tool_result` for every `tool_use_id`, results first.
- Tool failures return `is_error: true` with an actionable message.
- Loop has a max-iterations / budget stop. Handle `pause_turn` for server tools.

## Resilience
- Retries with exponential backoff and jitter for 429, 500, 504, 529 and connection errors; honour
  `retry-after`; never retry 400/401/403/413 blindly.
- Timeouts set; TCP keep-alive for long calls; idempotent workers for queued jobs.
- Log `request-id` (`_request_id` in SDKs; plus `x-amzn-requestid` on AWS) with each call.

## Cost and performance
- Model ID pinned in config, not hard-coded across the codebase.
- Effort set explicitly; prompt caching on repeated prefixes; batches for offline work.
- `usage` fields (input, output, cache read/creation) emitted as metrics.

## Security
- API keys from a secrets manager or IAM role, never in code, logs, prompts or the browser.
- Untrusted content (user docs, web, email) delivered in `tool_result` or clearly tagged, with an
  untrusted-content policy in the system prompt.
- `file_id` values never accepted from end users; tenant isolation by workspace.
- PII redacted before prompts and from logs; no PHI in JSON schemas.
- Destructive tools gated by human approval or hooks.

## Testing
- Unit tests mock the client; an eval set exists for prompt/model changes and runs in CI.

Finish with a one-line verdict: ready / ready with fixes / not ready.
