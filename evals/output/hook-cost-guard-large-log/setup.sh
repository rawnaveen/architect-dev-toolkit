#!/usr/bin/env bash
set -euo pipefail
python3 - <<'EOF'
import random
random.seed(7)
msgs = ["ERROR ConnectionPoolTimeout waiting for connection"] * 6 + ["ERROR NullPointerException in OrderMapper"] * 2 + ["INFO request ok"] * 12
with open("app.log", "w") as f:
    for i in range(14000):
        f.write(f"2026-11-08T10:{i//600:02d}:{(i//10)%60:02d} {random.choice(msgs)} requestId=req-{i:06d} path=/api/orders/{i}\n")
EOF
