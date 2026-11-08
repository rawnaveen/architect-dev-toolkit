---
type: llm
weight: 2
---
The job sends 50,000 tickets one by one to claude-opus-5-5 with max_tokens=32000 and the same ~8k-token
SYSTEM_PROMPT each time, then reads a single category label.
PASS if the answer recommends ALL of: (a) the Message Batches API (about 50% cheaper, results matched by custom_id),
(b) prompt caching on the static system prompt, (c) a smaller model such as Haiku and/or lower effort
together with a much smaller max_tokens or structured output for the label, and (d) validating the change with an eval.
FAIL if two or more of (a)-(d) are missing or if it recommends fast mode or a bigger model.
