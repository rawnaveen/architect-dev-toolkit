---
type: llm
weight: 3
---
ClaudeClient.java has five planted defects: (1) the API key is hard-coded in source; (2) the request prefills the
final assistant turn with "{" (rejected with 400 on Claude 4.6+ models; use structured outputs instead);
(3) it forces tool_choice {"type":"any"} on claude-sonnet-5-5 (returns 400 on that model); (4) it never checks
stop_reason (e.g. max_tokens truncation or refusal) before parsing JSON; (5) it retries every exception immediately
in a tight loop with no backoff or retry-after handling (should back off on 429/529/5xx and not retry 4xx).
PASS if the review identifies at least four of the five defects and gives a not-ready verdict.
FAIL otherwise.
