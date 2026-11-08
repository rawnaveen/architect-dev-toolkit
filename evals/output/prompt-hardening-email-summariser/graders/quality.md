---
type: llm
weight: 3
---
PASS if the rewritten prompt and notes do ALL of: use XML-style sections or tags; replace shouting/absolute tool
wording with calm conditional guidance (use lookup_customer when needed); add an untrusted-content policy so
instructions inside the email are treated as data; remove or replace the "Summary:" assistant prefill (not
supported on current models) with instructions or structured output; and drop the manual <thinking> scaffolding
in favour of adaptive thinking/effort.
FAIL if two or more of these are missing.
