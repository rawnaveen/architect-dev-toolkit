#!/usr/bin/env bash
set -euo pipefail
cat > RefundController.java <<'EOF'
package com.acme.refunds;
import org.springframework.web.bind.annotation.*;
@RestController
@RequestMapping("/refunds")
public class RefundController {
    private final RefundService service;
    public RefundController(RefundService s) { this.service = s; }
    @PostMapping public RefundDto create(@RequestBody CreateRefundRequest req) { return service.create(req); }
    @GetMapping("/{id}") public RefundDto get(@PathVariable String id) { return service.get(id); }
}
EOF
