---
name: agent-guardrails-config
description: >
  This skill should be used when setting up Claude Code or the Claude Agent SDK in a repository, or when
  the user asks to "configure permissions", "make Claude Code safer", "stop Claude from running X",
  "set up hooks", "allow these commands without asking", "lock down the agent", "create settings.json"
  or "set up CLAUDE.md". Apply proactively when a repo has no .claude/settings.json or CLAUDE.md.
metadata:
  version: "0.1.0"
---

# Agent guardrails configuration

Produce `.claude/settings.json`, optional hook scripts and a lean CLAUDE.md for the repository.

## Procedure
1. Inspect the repo: build tool (Maven/Gradle/npm), test commands, infra dirs (helm, terraform, k8s),
   secret-bearing files (.env, *.pem, application-*.yml with credentials), generated dirs (target/, build/,
   node_modules/).
2. Write `permissions`:
   - `allow`: safe, frequent commands (`Bash(./mvnw *)`, `Bash(./gradlew *)`, `Bash(git status)`,
     `Bash(git diff *)`, `Bash(git log *)`, `Bash(kubectl get *)`, `Bash(kubectl describe *)`,
     `Bash(kubectl logs *)`).
   - `ask`: `Bash(git push *)`, `Bash(kubectl apply *)`, `Bash(terraform apply *)`, `Bash(helm upgrade *)`.
   - `deny`: `Read(./.env)`, `Read(./.env.*)`, `Read(**/*.pem)`, `Read(**/*.key)`,
     `Bash(git push --force *)`, `Bash(kubectl delete *)`, `Bash(terraform destroy *)`, `Bash(rm -rf *)`,
     `Edit(./src/main/resources/db/migration/**)` if migrations must not change.
   - `defaultMode`: `default` (never `bypassPermissions` outside a throwaway sandbox).
3. Remind: deny rules hold even in bypass mode; hooks run first and a hook deny wins; CLAUDE.md is
   advisory, settings and hooks are enforced; project allow rules wait for workspace trust.
4. Hooks: the claude-dev-toolkit plugin already ships global guards (dangerous Bash, secret files). Add
   repo-specific hooks only when needed, e.g. PostToolUse on `Write|Edit` running `./mvnw -q spotless:apply`.
5. CLAUDE.md under 200 lines: build/test commands, module map, conventions that differ from defaults,
   "never do" list. Move path-specific guidance to `.claude/rules/<topic>.md` with `paths:` frontmatter,
   multi-step procedures to skills. Put personal items in `CLAUDE.local.md` / `settings.local.json`.
6. For Agent SDK apps: `allowed_tools` + `permission_mode="dontAsk"` for locked-down headless agents,
   `max_turns`, `max_budget_usd`, `setting_sources=[]` and per-tenant `cwd` for multi-tenant hosting.

## Output
Show each file in full, then a short table of what is allowed / asked / denied and why.
