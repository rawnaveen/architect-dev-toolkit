---
description: 'incident-triage-after-deploy'
tags: [output, agent, incident-triage]
plugins: ['../../..']
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---
PagerDuty fired 6 minutes ago: orders-service 5xx rate 18% in prod (normal is <0.5%).
Deploy history: orders-service v4.12.0 rolled out at 15:02 AEDT, alert started 15:04.
Sample log lines since 15:03:
```
15:03:11 ERROR c.a.o.OrderMapper - NullPointerException: Cannot invoke "Address.getPostcode()" because "customer.address" is null
15:03:12 ERROR c.a.o.OrderMapper - NullPointerException: Cannot invoke "Address.getPostcode()" because "customer.address" is null
15:03:15 WARN  o.h.e.j.s.SqlExceptionHelper - none
```
What's going on and what do we do right now?
