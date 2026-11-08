# Customising

Fork the repository (or clone it and load it with `claude --plugin-dir`), make changes, and reinstall.

## Make a skill trigger more or less often

Claude decides whether to use a skill from the `description` in its frontmatter.

- **Not triggering:** add the phrases your team actually uses ("PIR" or "post-incident review", not just "postmortem").
- **Triggering when it shouldn't:** add a "not for ..." clause naming the neighbouring case
  (for example "not for live incidents; use incident-triage").
- Measure the change with the trigger evals:
  `claude plugin eval . --tag <skill-name> --runs 3 --ablation none`.
- Edit prompts in `evals/_spec/triggers.yaml` and regenerate with `python3 evals/_spec/generate_triggers.py`.

## Change what a skill or agent does

Edit the body of `skills/<name>/SKILL.md` or `agents/<name>.md`. Keep `SKILL.md` lean and move long
reference material into `skills/<name>/references/`, which Claude reads only when needed.

For agents you can also change:

- `model`: `haiku`, `sonnet`, `opus` or `inherit`
- `tools`: restrict to the minimum
- `color`: display only

If you make an agent read-only, add its name to `READ_ONLY_AGENTS` in `hooks/scripts/guard.py` so the
hook enforces it.

## Tune the hooks

Constants at the top of `hooks/scripts/guard.py`:

| Constant | Purpose |
|---|---|
| `PROD_RE` | What counts as production in kubectl/helm contexts, namespaces and AWS profiles |
| `READ_ONLY_AGENTS` | Agents that may never mutate |
| `SECRET_NAME_PATTERNS`, `SECRET_PATH_PATTERNS` | Secret files |
| `GENERATED_DIR_RE`, `NOISE_FILE_RE`, `LARGE_FILE_BYTES` | Cost guard |
| `KUBECTL_MUTATING`, `HELM_MUTATING`, `TF_MUTATING`, `AWS_MUTATING_RE` | What counts as a change |

After any change, run:

```bash
python3 tests/test_guard.py
claude plugin validate .
```

## Remove what you don't need

Delete the skill folder or agent file. If you remove an agent that a skill delegates to (for example
the reviewers used by `pr-architecture-review`), update that skill too.

## Company-specific versions

Common edits for an internal fork:

- Add your ADR template, review checklists and naming conventions to the relevant skills.
- Point `runbook-operator` at your ticketing and wiki MCP servers.
- Add an `.mcp.json` at the plugin root to ship shared MCP servers with the plugin.
