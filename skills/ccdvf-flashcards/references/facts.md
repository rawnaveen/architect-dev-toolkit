# High-yield CCDV-F facts (as of 2026-11-08)

## Applications & Integration
- SSE order: message_start -> (content_block_start, content_block_delta*, content_block_stop)* -> message_delta (stop_reason, cumulative usage) -> message_stop. Tool input arrives as `input_json_delta.partial_json`.
- Errors can arrive mid-stream after HTTP 200. Ignore `ping` and unknown event types.
- Large max_tokens requires streaming (SDK refuses non-streaming calls that may exceed 10 min).
- Caching: prefix order tools -> system -> messages; up to 4 breakpoints; min 512 tokens on 5.x models; 5m write 1.25x, 1h write 2x, read 0.1x (0.05x Opus/Sonnet 5.5, 0.025x Fable 5.1); 20-block lookback; breakpoint on changing content never hits.
- Changing tool_choice, images, thinking or effort invalidates the messages cache; changing tools invalidates everything.
- Batches: 50% off, 100k requests or 256 MB, 24h expiry, results 29 days, any order -> custom_id; no stream / fast mode / max_tokens 0.
- Files API: 500 MB per file, file_id workspace-scoped (never accept from users), only code-execution/skill outputs downloadable; not ZDR.
- Errors: 400 invalid, 401 auth, 403 permission, 404, 413 too large, 429 rate limit (retry-after), 500, 504 timeout, 529 overloaded. SDK retries twice by default.
- Request limits: Messages 128 MB first-party, Bedrock 20 MB.
- Prefill on final assistant turn returns 400 on Claude 4.6+.

## Model Selection & Optimization
- Current: Fable 5.1 ($10/$50), Opus 5.5 ($4/$20, default effort medium, thinking always on), Sonnet 5.5 ($2/$10), Haiku 5.5 ($0.10/$0.50 under 100k prompt). All 1M context, 128K output.
- Effort: low / medium / high / xhigh / max at output_config.effort; affects thinking, tool calls and text. "adaptive" is a thinking type, not an effort.
- budget_tokens returns 400 on 4.7+; use adaptive thinking + effort.
- Thinking tokens billed as output; display summarized vs omitted billed the same.
- Fast mode: up to 2.5x output tokens/sec, not TTFT; Opus 5.5 $8/$40; not with batch; fallback = cache miss.
- count_tokens is free and an estimate. 4.7+ tokenizer ~30% more tokens.

## Agents & Workflows
- Patterns: prompt chaining, routing, parallelization (sectioning/voting), orchestrator-workers, evaluator-optimizer, autonomous agent. Start simplest.
- Subagents: fresh context, only the prompt goes in and the final message comes out; Agent tool (was Task); depth 3, concurrency 20 defaults; inherit bypass mode.
- Permission order: hooks -> deny -> ask -> mode -> allow -> canUseTool. Deny holds in bypass. allowed_tools does not restrict bypass.
- Hook decisions: deny > defer > ask > allow. Matchers match tool names only.
- Agent SDK is Python/TypeScript only; other languages use Messages API or `claude -p`.

## Prompt & Context Engineering
- Long docs at top, query at end. XML tags. 3-5 examples. Explain why. Calm tool language.
- Structured outputs: output_config.format (json_schema) and strict tools; limits 20 strict tools, 24 optional params, 16 unions; incompatible with citations and prefill; check refusal and max_tokens.
- Context editing beta context-management-2025-06-27: clear_tool_uses_20250919 (trigger 100k, keep 3), clear_thinking_20251015 (list first). Server-side compaction is the primary strategy.

## Tools & MCP
- Tool name regex ^[a-zA-Z0-9_-]{1,128}$. Descriptions 3-4+ sentences. input_examples must validate.
- Forced tool_choice any/tool returns 400 on Opus 5.5, Sonnet 5.5, Fable 5.1.
- defer_loading + tool search for large libraries. pause_turn for server tools.
- MCP: tools (model), resources (app), prompts (user); elicitation client feature; sampling and roots deprecated (2026-07-28); stdio (log to stderr) and Streamable HTTP; spec now stateless.

## Security
- Indirect injection: untrusted content in tool_result, labelled, policy in system prompt, JSON-encode, screen with Haiku, least privilege, egress allowlist, credential proxy.
- Isolation: sandbox-runtime < Docker < gVisor ~ Firecracker.

## Claude Code
- CLAUDE.md: managed > user > project > local, concatenated; <200 lines; advisory. Settings precedence managed > CLI > local > project > user; list keys merge.

## Eval & Debugging
- Replay the captured request: reproduces -> model/prompt; not -> integration/state. Code graders first, LLM judge with rubric, human calibration.
