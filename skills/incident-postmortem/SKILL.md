---
name: incident-postmortem
description: >
  This skill should be used when the user shares an incident timeline, Slack/Teams thread, alert history,
  logs from an outage, or asks to "write a postmortem", "write an incident report", "RCA", "root cause
  analysis", "post incident review", "PIR", or "summarise this outage". Apply proactively after an
  incident investigation concludes.
metadata:
  version: "0.1.0"
---

# Blameless postmortem

## Procedure
1. Build a timeline (timezone stated, Australia/Sydney by default) from the sources: detection, escalation,
   mitigation, resolution. Mark detection gap and time to mitigate.
2. Quantify impact: users/transactions affected, duration, SLO/error-budget burn, financial or regulatory
   exposure.
3. Root cause with "5 whys" down to systemic causes (process, tooling, design), never a person.
   Separate trigger, root cause and contributing factors.
4. What went well, what went poorly, where we got lucky.
5. Action items: each with owner role, priority, due date and type (prevent / detect / mitigate),
   and measurable done criteria. Prefer automated guards over "be more careful".

## Template
```
# Incident <ID>: <title>
Severity: <SEV>   Date: <date>   Duration: <hh:mm>   Status: Draft
## Summary (3 sentences)
## Impact
## Timeline
| Time | Event |
## Root cause and contributing factors
## Detection and response
## What went well / poorly / lucky
## Action items
| # | Action | Type | Owner | Priority | Due |
## Lessons learned
```
Use neutral language ("the deploy pipeline allowed", not "X forgot"). Flag missing data as open questions.
