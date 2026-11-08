---
name: claude-api-cost-optimizer
description: >
  This skill should be used when code calls the Claude / Anthropic Messages API or Amazon Bedrock
  Claude models and the user asks to "reduce Claude cost", "optimise tokens", "make this LLM call
  cheaper or faster", "which Claude model should I use", "should I use batch or caching", or when
  writing or reviewing any new Claude API call site (Java SDK, Python, TypeScript, Bedrock InvokeModel
  or Converse). Apply it proactively whenever a Claude API request is created or modified.
metadata:
  version: "0.1.0"
---

# Claude API cost and latency optimiser

Review every Claude API call site in scope and produce a concrete, priced recommendation.

## Procedure

1. Locate call sites: grep for `messages.create`, `messages.stream`, `MessageCreateParams`, `AnthropicClient`,
   `InvokeModel`, `Converse`, `anthropic.claude`, `claude-` model strings, `count_tokens`, `batches`.
2. For each call site record: model ID, `max_tokens`, effort (`output_config.effort`), thinking config,
   `speed`, system prompt size, tools count, whether `cache_control` is present, call frequency and
   latency requirement (interactive, near-real-time, offline).
3. Apply the decision rules below and estimate monthly cost before and after.
4. Output a table: call site | current config | recommended config | est. $ before -> after | latency impact | risk.
5. Offer patch-ready code changes. Never change behaviour without an eval to confirm quality holds.

## Decision rules

- **Model tier**: start from the cheapest model that passes evals. Haiku 5.5 for classification, extraction,
  routing and subagents; Sonnet 5.5 for balanced coding/agentic work; Opus 5.5 as default for hard reasoning;
  Fable 5.1 only when evals prove Opus at high effort falls short. Check current prices in
  `references/pricing.md`; recheck the live pricing page if the date there is old.
- **Effort**: set explicitly. `low` for simple/high-volume/subagents, `medium` balanced, `high` complex,
  `xhigh`/`max` only with measured headroom. Lower effort before rewriting prompts to "think less".
  Keep top-level effort constant inside a cached conversation (changing it invalidates the cache).
- **Prompt caching**: any repeated prefix over 512 tokens (5.x models) reused within 5 min -> add
  `cache_control` (or top-level automatic caching). Reused 5-60 min apart -> `ttl: "1h"`. Order prefix
  tools -> system -> static docs -> history; breakpoint on the last block that stays identical. Max 4
  breakpoints. Verify with `cache_read_input_tokens`.
- **Batches**: no latency SLA -> Message Batches API (50% off, stacks with caching, results any order,
  match on `custom_id`, 24h window). Not with `stream`, `speed: "fast"`, or `max_tokens: 0`.
- **Fast mode** (`speed: "fast"`, Opus 5.5): only where output tokens/second matters to users; 2x price;
  does not improve time-to-first-token; fallback to standard speed is a cache miss.
- **max_tokens**: size to real output plus thinking; truncation (`stop_reason: max_tokens`) wastes the call.
- **Context**: trim tool outputs, paginate, cap `max_content_tokens` on web fetch, use context editing or
  compaction for long agents, delegate noisy reads to Haiku subagents.
- **Haiku 5.5 tier trap**: prompts over 100k tokens (cache reads count) pay 5x rates per request.
- **Images**: downscale; tokens = ceil(w/28) x ceil(h/28).
- **Routing**: count_tokens (free) or a Haiku classifier to send easy requests to cheap models.
- **Bedrock**: 20 MB request cap, no url/file image sources, automatic top-level caching unavailable on the
  legacy integration (use explicit breakpoints), features lag the first-party API.

## Output

Lead with the single biggest saving and its dollar figure. Then the table. Then patches. Then the eval
needed to confirm quality.
