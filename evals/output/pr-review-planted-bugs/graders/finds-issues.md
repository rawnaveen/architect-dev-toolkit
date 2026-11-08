---
type: llm
weight: 3
---
The repository's feature branch adds OrderController.java and OrderService.java with three planted defects:
(1) SQL injection: a SQL string is built by concatenating the request parameter `customerName` and run with JdbcTemplate;
(2) a hard-coded secret: PAYMENTS_API_KEY = "sk_live_..." in source;
(3) an N+1 query: orderRepository.findById / itemRepository call inside a loop over order IDs.
PASS if the final review identifies all three defects (any wording) and does not approve the merge as-is.
FAIL if any of the three is missed, or the review approves without requiring fixes.
