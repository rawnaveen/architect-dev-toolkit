# Evals for architect-dev-toolkit

Three layers, cheapest first. Run them from the plugin root (the folder with `.claude-plugin/`).
Requires Claude Code v2.1.269+ signed in as usual, and git 2.31+.

| Layer | What it checks | Cases | Model calls |
|---|---|---|---|
| `tests/test_guard.py` | Hook guard logic (safety, read-only agents, cost guard, session resume) | 58 | None |
| `evals/trigger/` | Each skill and agent fires on realistic prompts and stays quiet on near-misses | 160 | Agent runs only (free graders) |
| `evals/output/` | Quality of what the key skills/agents produce, on fixture repos with planted problems, plus hooks end-to-end | 19 | Agent runs + judge calls |

## 1. Hook tests (free, 1 second)
```bash
python3 tests/test_guard.py
```

## 2. Trigger suite (cheap)
One run per case, no baseline arm (a "did the skill fire" check is meaningless without the plugin):
```bash
claude plugin eval . --tag trigger --runs 1 --ablation none --threshold 1 \
  --model claude-sonnet-5-5 --max-cost-usd 15 -j 4
```
- Positive cases (`pos-*`) pass when the component fired; negative cases (`neg-*`) pass when it did not.
- Read the summary as: per component, positives passed = recall, negatives passed = precision.
- One skill or agent only: `--tag k8s-debugger`. Only skills: `--tag trigger-skill`.
- Use the model you actually work with in Claude Code, because triggering depends on the model.
- A single run is noisy: re-run failures with `--runs 3` before changing a description.

Fix a failing positive by adding the user's phrasing to the skill's `description` (or the agent's
`description` and `<example>` blocks). Fix a failing negative by adding a "not for ..." clause.
Edit prompts in `_spec/triggers.yaml`, then regenerate with `python3 evals/_spec/generate_triggers.py`.

## 3. Output suite (more expensive)
```bash
claude plugin eval . --tag output --scaffold \
  --allow-tools Write Edit "Bash(git *)" \
  --model claude-sonnet-5-5 --judge-model claude-sonnet-5-5 \
  --threshold 0.8 --max-cost-usd 40 -j 2
```
- Runs each case 3 times with the plugin and 3 times without, so `Δ` shows what the plugin adds.
- `--scaffold` runs the fixture scripts in each case folder (they only create small local files and a git repo).
- Bash is granted only for `git` (PR review and force-push hook cases) and runs inside Claude Code's sandbox.
- Hooks-only cases: `--tag hook`. One case: `--case pr-review-planted-bugs`.
- To iterate cheaply on one case: `--case <name> --runs 1 --ablation none`.

| Case | Tests |
|---|---|
| pr-review-planted-bugs | PR review finds SQL injection, hard-coded key and N+1; security-reviewer agent used |
| api-cost-optimizer-nightly-job | Recommends batches, caching, smaller model/effort/max_tokens, and an eval |
| integration-reviewer-java-client | Finds prefill, forced tool_choice on 5.5, hard-coded key, no stop_reason check, retry loop |
| k8s-debugger-oomkilled | Diagnoses JVM heap larger than container limit, proposes fix without applying it |
| incident-triage-after-deploy | Correlates deploy and NPE, recommends human-run rollback |
| adr-kafka-vs-sqs | ADR structure, real trade-offs on ordering and replay, clear decision |
| postmortem-blameless | Blameless, correct root cause, quantified impact, typed action items |
| prompt-hardening-email-summariser | XML structure, calm tool wording, untrusted-content policy, no prefill, no manual thinking tags |
| tool-schema-refunds-controller | Namespaced tools, rich descriptions, strict schema, risk flagged |
| guardrails-config-spring-repo | Writes .claude/settings.json denying .env and kubectl delete, allowing Maven |
| cost-coach-bloated-claude-md | Trims CLAUDE.md, path-scoped rules, drops unused MCP servers |
| aws-review-terraform | Flags public bucket, wildcard IAM, unencrypted single-AZ RDS without backups, open DB port |
| flashcards-quiz | One scenario MCQ, answer withheld |
| eval-harness-model-switch | Dataset, graders, side-by-side comparison, CI gate |
| mcp-scaffold-confluence | FastMCP server, read-only, env credentials, stderr logging, registration |
| observability-refund-controller | Micrometer/OTel, low-cardinality tags, trace IDs in logs, SLOs |
| hook-blocks-force-push | Force push blocked end-to-end |
| hook-cost-guard-large-log | Whole-file read of a 1.3 MB log blocked; answer found another way |
| hook-secret-guard-env | .env read blocked; secret value never appears in the reply |

## Cost and CI
Every run is a real model call on your account. Always set `--max-cost-usd`; the run stops starting new
cases once the estimate reaches it and reports partial results. Results land in `evals/results/<timestamp>/`
(`report.html` plus `aggregate-result.json`); that folder is git-ignored.

For CI, add `--trust-plugin --json results.json --no-publish`, pin `--model` and `--judge-model`, and fail
the build on the exit code. Run the hook tests and the trigger suite on every change, and the output suite
nightly or before releases.
