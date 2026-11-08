# Contributing

Thanks for helping improve Architect Dev Toolkit.

## Ground rules

- Keep components focused. One skill or agent should do one job well.
- Write skill and agent bodies as instructions for Claude (imperative), not as documentation for people.
- Prefer deterministic hooks for anything that must always happen, and skills or agents for judgement.
- Don't add anything that sends data to third-party services by default.

## Development setup

```bash
git clone https://github.com/rawnaveen/architect-dev-toolkit.git
cd architect-dev-toolkit
claude --plugin-dir .            # try your changes in a session
```

## Before opening a pull request

```bash
claude plugin validate .         # structure and frontmatter
python3 tests/test_guard.py      # hook regression tests (must stay green)
python3 scripts/build_directory_edition.py /tmp/edition   # directory edition still builds
```

If you change a skill or agent `description`, run its trigger evals:

```bash
claude plugin eval . --tag <name> --runs 3 --ablation none --max-cost-usd 5
```

If you add a component:

1. Add trigger prompts (positive and near-miss) to `evals/_spec/triggers.yaml` and run
   `python3 evals/_spec/generate_triggers.py`.
2. Add an output case under `evals/output/` when the component produces something checkable.
3. Document it in `README.md` and `docs/components.md`.
4. Add a line to `CHANGELOG.md` under "Unreleased".

Don't edit the `directory` branch by hand: CI rebuilds it from `main` on every push. If an agent or
skill mentions the plugin's hooks, add a patch for it in `scripts/build_directory_edition.py`, because
the directory edition has none.

If you change `hooks/scripts/guard.py`, add test cases to `tests/test_guard.py` for both the newly
blocked and the still-allowed behaviour.

## Commit messages

Use short imperative subjects, for example `skills: tighten ADR trigger description` or
`hooks: allow helm template`.

## Reporting bugs

Open an issue with your Claude Code version (`claude --version`), OS, what you asked, what happened,
and what you expected. For hook issues, include the exact command that was blocked or allowed.
