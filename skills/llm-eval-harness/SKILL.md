---
name: llm-eval-harness
description: >
  This skill should be used when the user asks to "evaluate a prompt", "build an eval", "test my LLM
  feature", "compare models", "will switching to Haiku/Sonnet break quality", "regression test prompts",
  or before changing a model ID, effort level or prompt in production code. Apply proactively when a
  prompt or model change is proposed without an eval.
metadata:
  version: "0.1.0"
---

# LLM eval harness

Build a small, repeatable eval that runs in CI and answers "is the change safe?".

## Procedure
1. **Success criteria**: specific and measurable (accuracy %, schema-valid %, refusal rate, p95 latency,
   $ per 1k requests). Write them down first.
2. **Dataset** (`evals/<feature>/cases.jsonl`): 30-200 cases with `id`, `input`, `expected` or
   `rubric`, `tags` (typical / edge / adversarial / regression). Seed from real production samples
   (redact PII) and every past failure.
3. **Graders**, cheapest first:
   - Code: exact match, regex, JSON schema validation, numeric tolerance, unit tests.
   - LLM-as-judge: separate prompt with an explicit rubric, structured output
     `{"pass": bool, "score": 1-5, "reason": str}`, a different or stronger model than the one under test.
   - Human spot-check 10% to calibrate the judge.
4. **Runner** (Python or Java): loads cases, calls the system under test with the exact production
   config (model, effort, tools, system prompt), grades, writes `results/<run>.json`, prints a summary.
   For large sets, submit through the Message Batches API (50% cheaper) and map results by `custom_id`.
   Record `usage` per case for cost.
5. **Compare**: baseline vs candidate table - pass rate per tag, cost, latency, and the list of cases
   that flipped from pass to fail.
6. **CI**: run on any change to prompts, model IDs or tool definitions; fail the build below threshold.

## Rules
- Change one variable at a time (model, effort, prompt, tools).
- Check `stop_reason` in results (`refusal`, `max_tokens`) and count them separately.
- Keep the judge prompt versioned alongside the dataset.
