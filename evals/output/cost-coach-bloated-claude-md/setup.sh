#!/usr/bin/env bash
set -euo pipefail
mkdir -p billing search
{
  echo "# Project rules"
  for i in $(seq 1 120); do echo "- Global rule $i: keep code tidy and follow standard conventions number $i."; done
  echo "## Billing module rules"
  for i in $(seq 1 150); do echo "- In billing/, rule $i: invoices must use BigDecimal and rounding mode HALF_EVEN ($i)."; done
  echo "## Search module rules"
  for i in $(seq 1 150); do echo "- In search/, rule $i: queries must go through the SearchGateway ($i)."; done
} > CLAUDE.md
cat > .mcp.json <<'EOF'
{"mcpServers": {
  "github": {"command": "gh-mcp"}, "jira": {"command": "jira-mcp"}, "postgres": {"command": "pg-mcp"},
  "spotify": {"command": "spotify-mcp"}, "figma": {"command": "figma-mcp"}, "notion": {"command": "notion-mcp"}
}}
EOF
echo "class Billing {}" > billing/Billing.java
echo "class Search {}" > search/Search.java
