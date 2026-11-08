---
name: claude-code-cost-coach
description: >
  This skill should be used when the user asks to "reduce my Claude Code usage", "save tokens", "why is
  Claude Code using so many tokens", "I keep hitting limits", "optimise my Claude setup", "audit my
  CLAUDE.md", or when a session's context is large (many files read, long history, many MCP servers).
  Apply proactively when starting work in a repo whose CLAUDE.md is over 200 lines or that has no
  path-scoped rules.
metadata:
  version: "0.1.0"
---

# Claude Code cost coach

Audit the current repo and user setup, then propose a leaner configuration with estimated savings.

## Audit
1. Run `/context` mentally: list CLAUDE.md files (user, project, local, nested), their line counts,
   `.claude/rules/` files with and without `paths:`, enabled MCP servers and their tool counts,
   skills, and auto memory size.
2. Read `~/.claude/settings.json` and `.claude/settings.json`: default `model`, `effortLevel`,
   permission allow list (frequent prompts waste turns), enabled plugins.
3. Spot waste: generated folders being read (target/, build/, node_modules/, logs), very large files
   read whole, repeated re-explanations that belong in CLAUDE.md.

## Recommendations to produce
- CLAUDE.md under 200 lines; move module-specific rules to `.claude/rules/*.md` with `paths:`; move
  procedures to skills (load on demand).
- Disable MCP servers not used in this repo.
- Deny reads of generated dirs: `Read(./target/**)`, `Read(./build/**)`, `Read(**/node_modules/**)`.
- Allow frequent safe commands to avoid approval round trips.
- Default model/effort per task type: Sonnet or Haiku at low/medium for routine edits, tests and
  lookups; Opus/high for design and hard debugging. Avoid mid-session model switches (each model has
  its own prompt cache).
- Delegate searches and log reading to the `doc-explorer` (Haiku) subagent from this plugin.
- Habits: `/clear` between unrelated tasks, `/compact` early on long sessions, plan mode before large
  changes, `--max-turns` in headless runs, check `/cost` and `/status` after a typical day.
- Tell Claude not to spawn subagents for simple sequential work.

## Output
A prioritised list with the exact file edits (diffs) and an estimate of context tokens saved per turn.
Apply only after the user confirms.
