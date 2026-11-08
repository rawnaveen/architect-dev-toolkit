---
name: pr-architecture-review
description: >
  This skill should be used when the user asks to "review this PR", "review my changes", "review the
  diff", "is this ready to merge", "check before I push", "code review", or has finished a feature or
  bug fix in a git repository. Apply proactively before commits that change more than a few files or
  before pushing a branch.
metadata:
  version: "0.1.0"
---

# Parallel PR architecture review

Run three specialist reviews in parallel, then synthesise one verdict.

## Procedure
1. Determine scope: `git diff --stat <base>...HEAD` (base = `main` or `master`, or the PR target), plus
   uncommitted changes. If more than ~40 files, group by module.
2. In a single turn, launch these subagents in parallel via the Agent tool, each given the base ref,
   the changed file list and the purpose of the change:
   - `security-reviewer` - vulnerabilities, secrets, authz, injection, dependency risk.
   - `performance-reviewer` - complexity, N+1 queries, blocking calls, memory, concurrency, caching.
   - `spring-conventions-reviewer` - layering, Spring Boot idioms, transactions, config, tests, API design.
   If the diff touches Claude/LLM integration code, also apply the claude-integration-reviewer skill.
3. Synthesise: deduplicate, rank by severity, keep file:line references.

## Output
```
Verdict: Approve | Approve with fixes | Request changes
Critical (must fix): ...
Warnings (should fix): ...
Suggestions: ...
Tests: what is missing
```
Keep it under one screen; link to subagent detail only when needed. Do not edit code unless asked.
