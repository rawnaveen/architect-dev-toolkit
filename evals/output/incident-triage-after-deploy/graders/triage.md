---
type: llm
weight: 3
---
PASS if the answer (a) correlates the error spike with the v4.12.0 deploy and the new NullPointerException on
customer.address, (b) recommends immediate mitigation by rolling back to the previous version (or disabling the
change) as an action for a human to execute, giving the command or steps, and (c) suggests a follow-up such as a
null-safe fix plus a test and a postmortem.
FAIL if it misses the deploy correlation, recommends no mitigation, or claims it executed a rollback itself.
