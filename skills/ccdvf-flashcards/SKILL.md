---
name: ccdvf-flashcards
description: >
  This skill should be used when the user says "quiz me", "test me on the Claude exam", "CCDV-F
  practice", "Claude certification practice questions", "flashcards for the Claude developer exam",
  or wants to revise Claude API, Agent SDK, MCP, prompt engineering or Claude Code concepts.
metadata:
  version: "0.1.0"
---

# CCDV-F exam practice

Run scenario-style practice for the Claude Certified Developer: Foundations exam.

## Session flow
1. Ask which mode: mixed (weighted by exam weight), one domain, or weak areas from earlier in the session.
2. Ask one question at a time: a short production scenario, 4 options (or "select TWO"), one best answer.
   Distractors must be plausible (they would work, but are costlier, less deterministic or outdated).
3. After the answer: correct/incorrect, why the best option wins, why each distractor loses, and the
   doc fact behind it.
4. Track score per domain; after 10 questions show the tally and the two weakest domains.

## Domain weights
Applications & Integration 33.1 | Model Selection & Optimization 16.8 | Agents & Workflows 14.7 |
Prompt & Context Engineering 11.0 | Tools & MCP 10.6 | Security & Safety 8.1 | Claude Code 3.1 |
Eval, Testing & Debugging 2.6

## High-yield facts to draw from
See `references/facts.md`. Prefer the "exam traps" there - outdated practices that look right.
