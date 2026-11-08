---
type: llm
weight: 3
---
PASS if the plan includes: measurable success criteria; a dataset of real (redacted) tickets with typical, edge and
adversarial cases; graders (code checks and/or an LLM judge with a rubric, ideally calibrated by humans); running
both models with the same prompt/config and comparing pass rate, cost and latency; changing one variable at a time;
and a CI gate or threshold.
FAIL if it skips the dataset or the comparison against the current model.
