#!/usr/bin/env bash
set -euo pipefail
cat > RefundController.java <<'EOF'
package com.acme.refunds;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/refunds")
public class RefundController {
    @GetMapping("/{id}")
    public RefundDto get(@PathVariable String id) { return service.get(id); }

    @PostMapping
    public RefundDto create(@RequestBody CreateRefundRequest req) { return service.create(req); } // orderId, amountCents, currency, reason

    @PostMapping("/{id}/cancel")
    public RefundDto cancel(@PathVariable String id, @RequestParam String reason) { return service.cancel(id, reason); }

    @GetMapping
    public Page<RefundDto> list(@RequestParam(required = false) String orderId,
                                @RequestParam(required = false) RefundStatus status,
                                @RequestParam(defaultValue = "0") int page) { return service.list(orderId, status, page); }
}
EOF
