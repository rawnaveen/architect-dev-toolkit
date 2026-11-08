---
name: observability-instrumentation
description: >
  This skill should be used when creating or modifying a Java/Spring Boot service, REST endpoint,
  Kafka/SQS consumer, scheduled job or outbound client, or when the user asks to "add metrics",
  "add tracing", "add logging", "instrument this", "define SLOs", "create alerts", or "make this
  observable". Apply proactively to new services and endpoints.
metadata:
  version: "0.1.0"
---

# Observability instrumentation (Spring Boot)

## Standards
- **Traces**: OpenTelemetry (Micrometer Tracing bridge or OTel Java agent). Propagate W3C `traceparent`
  across HTTP, messaging and async executors. Span per inbound request, outbound call and message.
- **Metrics**: Micrometer with low-cardinality tags (no user IDs, no raw URLs). For each endpoint and
  consumer: request rate, error rate, latency histogram (RED); for resources: utilisation, saturation,
  errors (USE). Name `domain.component.action` with units.
- **Logs**: structured JSON (logstash encoder / ECS), include `traceId`, `spanId`, request ID; levels
  used consistently; no PII, secrets or tokens; log once at the boundary, not at every layer.
- **Health**: Actuator liveness and readiness separated; readiness reflects downstream dependencies.
- **SLOs**: per user journey, e.g. 99.9% of requests under 300 ms over 28 days; multi-window burn-rate
  alerts (fast 2%/1h, slow 5%/6h); alert on symptoms, page only on SLO burn.
- **LLM calls (Claude/Bedrock)**: record model, effort, input/output/cache tokens, stop_reason,
  latency, cost estimate and request-id as span attributes and metrics; never log prompt text with PII.

## Procedure
1. Detect the current stack (pom.xml/build.gradle, logback config, existing exporters).
2. Add missing dependencies and config; reuse existing conventions.
3. Instrument code: `@Observed` or `Observation` API, `Timer`/`Counter`, context propagation for
   `@Async`/reactive.
4. Produce dashboards-as-code suggestions (Grafana/CloudWatch) and alert rules (PrometheusRule or
   CloudWatch alarms).
5. Add a test that asserts key metrics are registered.
