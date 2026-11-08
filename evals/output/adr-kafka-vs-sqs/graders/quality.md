---
type: llm
weight: 2
---
PASS if the record compares at least MSK/Kafka and SQS FIFO against the stated drivers (per-account ordering,
7-day replay, ~3k events/sec, small team), notes that SQS has no native replay of consumed messages (so replay
needs extra design such as an archive) while Kafka supports retention-based replay with more operational cost,
makes a clear decision with a one-line reason, and lists consequences or revisit triggers.
FAIL if it lacks a decision, ignores replay or ordering, or presents options without trade-offs.
