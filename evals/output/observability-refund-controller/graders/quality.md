---
type: llm
weight: 2
---
PASS if the changes use Micrometer and/or OpenTelemetry (for example @Observed, Observation, Timer/Counter),
keep metric tags low-cardinality (no refund IDs or customer IDs as tags), include trace IDs in structured logs,
and propose at least one SLO or alert for the refund endpoints.
FAIL if it tags metrics with high-cardinality IDs or only adds log statements.
