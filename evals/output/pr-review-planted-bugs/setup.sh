#!/usr/bin/env bash
set -euo pipefail
git init -q -b main
git config user.email eval@example.com
git config user.name eval

mkdir -p src/main/java/com/acme/orders
cat > README.md <<'EOF'
# orders-service
Spring Boot service for order lookups.
EOF
git add . && git commit -q -m "initial"
git checkout -q -b feature/order-lookup
cat > src/main/java/com/acme/orders/OrderController.java <<'EOF'
package com.acme.orders;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/orders")
public class OrderController {
    private static final String PAYMENTS_API_KEY = "sk_live_51HxQ2eEXAMPLEKEY9fA";
    private final JdbcTemplate jdbc;
    private final OrderService service;

    public OrderController(JdbcTemplate jdbc, OrderService service) { this.jdbc = jdbc; this.service = service; }

    @GetMapping("/search")
    public List<Map<String, Object>> search(@RequestParam String customerName) {
        String sql = "SELECT * FROM orders WHERE customer_name = '" + customerName + "'";
        return jdbc.queryForList(sql);
    }

    @PostMapping("/details")
    public List<OrderDto> details(@RequestBody List<Long> orderIds) {
        return service.loadDetails(orderIds);
    }
}
EOF
cat > src/main/java/com/acme/orders/OrderService.java <<'EOF'
package com.acme.orders;

import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;

@Service
public class OrderService {
    private final OrderRepository orderRepository;
    private final ItemRepository itemRepository;

    public OrderService(OrderRepository o, ItemRepository i) { this.orderRepository = o; this.itemRepository = i; }

    public List<OrderDto> loadDetails(List<Long> orderIds) {
        List<OrderDto> out = new ArrayList<>();
        for (Long id : orderIds) {
            Order order = orderRepository.findById(id).orElseThrow();
            List<Item> items = itemRepository.findByOrderId(id);
            out.add(new OrderDto(order, items));
        }
        return out;
    }
}
EOF
git add . && git commit -q -m "add order lookup"
