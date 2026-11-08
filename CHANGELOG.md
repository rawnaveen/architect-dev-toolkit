# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.3.0] - 2026-11-08

### Added
- 58 hook regression tests (`tests/test_guard.py`).
- 160 trigger evals and 19 output-quality evals for `claude plugin eval` (`evals/`).
- Public documentation, MIT licence, contributing and security policies, and CI.

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

[Unreleased]: https://github.com/rawnaveen/architect-dev-toolkit/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/rawnaveen/architect-dev-toolkit/releases/tag/v0.3.0
