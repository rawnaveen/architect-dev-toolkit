---
name: architecture-decision-record
description: >
  This skill should be used when the user is making or documenting a technical or architecture decision:
  "write an ADR", "document this decision", "should we use X or Y", "compare options for", "design
  decision", "trade-off analysis", "architecture options", or when a design discussion reaches a choice
  between technologies, patterns or vendors. Apply proactively when a decision is made in conversation
  so it gets recorded.
metadata:
  version: "0.1.0"
---

# Architecture Decision Record

Produce an ADR an enterprise architecture review board can approve.

## Gather
Ask only for what is missing: the problem, drivers (business, regulatory, NFRs), constraints (budget,
skills, existing platforms such as AWS/EKS, Java/Spring), options already considered, and the decision
deadline. Look for existing ADRs (`docs/adr/`, `adr/`) and match their numbering and format.

## Template
```
# ADR-<NNN>: <decision in one line>
Status: Proposed | Accepted | Superseded by ADR-<n>   Date: <YYYY-MM-DD>   Deciders: <names/roles>

## Context
Problem, scope, drivers, constraints. Link to requirements and incidents.

## Options considered
| Option | Fit to drivers | Cost (build/run) | Risk | Operability | Lock-in |
Describe each option in 2-4 lines.

## Decision
The choice and the one-sentence reason.

## Consequences
Positive, negative, follow-up work, what we will monitor (SLOs, cost).

## Architecture views (TOGAF)
Business / Data / Application / Technology impact in one line each. Principles applied.

## Compliance and risk
Security, privacy, regulatory (e.g. APRA CPS 234 / CPS 230 for Australian banking), resilience.

## Revisit when
Concrete triggers to reopen the decision.
```

## Rules
- Options must be genuine alternatives, including "do nothing" when relevant.
- Quantify where possible (latency, $ per month, effort in weeks).
- Keep it to 1-2 pages. Save as `docs/adr/NNNN-kebab-title.md` when working in a repo.
