# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- `PRIVACY.md` privacy policy, linked from the README and `plugin.json` (`privacyPolicyUrl`).

## [0.3.1] - 2026-11-08

### Changed
- Hooks now use exec form (`command` + `args`) instead of a one-line shell command, as the Claude directory requests. Paths with spaces need no quoting.
- README describes the secret-file guard without quoting credential file paths. The full list is in `docs/hooks.md`.
- `tool-schema-designer` states the tool-name rule in words instead of a regex (clears a directory scanner false positive).
- `SECURITY.md` now states exactly what the hook script does and doesn't do: no network access, no credential reads, one file opened, one local `kubectl` lookup.

### Fixed
- `agent-guardrails-config` referred to the plugin by an old name.

## [0.3.0] - 2026-11-08

### Added
- 58 hook regression tests (`tests/test_guard.py`).
- 160 trigger evals and 19 output-quality evals for `claude plugin eval` (`evals/`).
- Public documentation, MIT licence, contributing and security policies, and CI.
- Plugin icon, social preview image and a demo GIF generated from real guard output (`examples/guard_demo.py`).

### Changed
- Marketplace renamed to `rawnaveen`. Install with `/plugin install architect-dev-toolkit@rawnaveen`.

## [0.2.0] - 2026-11-08

### Added
- Cost guard hook: blocks reads of generated or vendored folders, lockfiles, minified or compiled
  files, and whole-file reads over 512 KB. Disable with `ADT_COST_GUARD=off`.

## [0.1.0] - 2026-11-08

### Added
- 14 skills, 10 subagents, a Bash safety guard, a secret-file guard, read-only agent enforcement and
  `PROGRESS.md` session resume.

[Unreleased]: https://github.com/rawnaveen/architect-dev-toolkit/compare/v0.3.1...HEAD
[0.3.1]: https://github.com/rawnaveen/architect-dev-toolkit/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/rawnaveen/architect-dev-toolkit/releases/tag/v0.3.0
