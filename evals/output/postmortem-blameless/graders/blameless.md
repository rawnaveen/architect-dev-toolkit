---
type: llm
weight: 3
---
PASS if the report is blameless (does not attribute the cause to Raj or any individual; frames causes as process or
tooling gaps such as missing index review or no load test), identifies the missing index on orders.customer_ref as
root cause, quantifies impact (about 6% of checkouts, roughly 21:46-22:40), and lists action items with an owner
role and type (prevent/detect/mitigate), including a guard such as migration/index review or query-plan checks in CI.
FAIL if it blames a person, omits root cause, or has no concrete action items.
