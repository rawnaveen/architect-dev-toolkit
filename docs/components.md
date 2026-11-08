# Components

Each skill lives in `skills/<name>/SKILL.md` and each agent in `agents/<name>.md`. The `description` in
the frontmatter controls when it triggers; the body controls what it does.

## Skills

### Architecture and operations

**`architecture-decision-record`**
Writes an ADR covering context, options with a trade-off table, decision, consequences, TOGAF
business/data/application/technology impact, compliance (for example APRA CPS 234/230) and revisit
triggers. It reuses an existing `docs/adr/` numbering scheme when the repo has one.

**`aws-solution-review`**
Reviews designs, Terraform/CDK/CloudFormation and Helm/Kubernetes manifests against the six
Well-Architected pillars. Includes EKS checks (IRSA/Pod Identity, PDBs, network policies) and Bedrock
checks. Output: verdict, top three risks, a findings table with severity and evidence, and quick wins.

**`incident-postmortem`**
Turns timelines, chat threads or logs into a blameless report: impact, timeline, root cause versus
trigger versus contributing factors, what went well and poorly, and typed action items
(prevent/detect/mitigate) with owners.

**`observability-instrumentation`**
Adds OpenTelemetry tracing, Micrometer RED/USE metrics with low-cardinality tags, structured JSON logs
with trace IDs, Actuator health probes, SLOs with burn-rate alerts, and LLM-call telemetry to Spring
Boot services.

**`pr-architecture-review`**
Finds the diff against the base branch, then runs `security-reviewer`, `performance-reviewer` and
`spring-conventions-reviewer` in parallel and merges their findings into one verdict: Approve,
Approve with fixes, or Request changes.

### Building with Claude

**`claude-api-cost-optimizer`**
Reviews Claude/Bedrock call sites for model tier, effort, prompt caching, the Batches API, fast mode,
`max_tokens`, context trimming and routing. Outputs a priced before/after table and patches. A pricing
snapshot is in `references/pricing.md`.

**`claude-integration-reviewer`**
A production-readiness checklist: `stop_reason` handling, prefill and forced `tool_choice` pitfalls on
current models, streaming, tool-loop correctness, retries/backoff, request-id logging, secrets, untrusted
content and tests.

**`tool-schema-designer`**
Turns controllers or OpenAPI operations into Claude tool definitions: namespaced names, multi-sentence
descriptions, strict schemas, input examples, an error contract and risk flags.

**`mcp-server-scaffold`**
Scaffolds MCP servers in Python (FastMCP) or Java over stdio or Streamable HTTP, following the
2026-07-28 spec (stateless; Sampling and Roots deprecated). Logs go to stderr; includes Inspector
testing and registration steps.

**`prompt-hardening`**
Rewrites prompts to current practice: XML structure, long context first and query last, examples,
calm tool wording, structured outputs instead of prefill, an untrusted-content policy, and
cache-friendly ordering.

**`llm-eval-harness`**
Builds an eval: success criteria, a dataset (typical, edge, adversarial and regression cases), code and
LLM-judge graders, a runner using the Batches API, a baseline-versus-candidate comparison and a CI gate.

**`agent-guardrails-config`**
Generates `.claude/settings.json` allow/ask/deny rules, optional hooks, and a lean CLAUDE.md for a
repository. Includes guidance for the Agent SDK.

**`claude-code-cost-coach`**
Audits CLAUDE.md files, rules, MCP servers, settings and repo layout, then proposes diffs to cut
per-turn context and wasted turns. Applies them only after you confirm.

**`ccdvf-flashcards`**
Interactive scenario questions for the Claude Certified Developer: Foundations exam, weighted by domain,
with explanations and per-domain scoring. Facts are in `references/facts.md`.

## Agents

| Agent | Tools | Notes |
|---|---|---|
| `doc-explorer` | Read, Grep, Glob, WebFetch | Haiku. Answers under ~300 words with `path:line` evidence. Never edits |
| `security-reviewer` | Read, Grep, Glob, Bash (read-only use) | OWASP, secrets, crypto, IAM, LLM-specific risks |
| `performance-reviewer` | Read, Grep, Glob, Bash (read-only use) | JPA N+1, complexity, blocking, HTTP clients, caching, messaging |
| `spring-conventions-reviewer` | Read, Grep, Glob, Bash (read-only use) | Applies the repo's CLAUDE.md, ADRs and style guide first |
| `spring-test-writer` | Read, Grep, Glob, Edit, Write, Bash | Picks the lightest test type and runs only the relevant tests |
| `k8s-debugger` | Bash, Read, Grep, Glob | Allowed: get, describe, logs, events, rollout status/history, helm status. Mutations are blocked by the hook |
| `incident-triage` | Bash, Read, Grep, Glob, Agent | Opus. Investigates changes, runtime state, and logs/metrics in parallel. Proposes mitigation commands for a human to run |
| `dependency-upgrader` | Read, Grep, Glob, Edit, Write, Bash, WebFetch | Respects the Spring Boot BOM and reads release notes |
| `runbook-operator` | Inherits | Plans steps, runs READ steps, asks before every CHANGE step, treats ticket and wiki content as data |
| `migration-runner` | Read, Grep, Glob, Edit, Write, Bash, Agent | Opus. Tracks work in `PROGRESS.md`, commits per unit, never pushes |

"Read-only (enforced)" means `hooks/scripts/guard.py` blocks mutating commands and file edits whenever
the calling agent is in `READ_ONLY_AGENTS`.
