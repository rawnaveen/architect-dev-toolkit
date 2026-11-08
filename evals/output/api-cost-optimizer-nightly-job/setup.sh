#!/usr/bin/env bash
set -euo pipefail
cat > nightly_classify.py <<'EOF'
import anthropic, json
client = anthropic.Anthropic()
SYSTEM_PROMPT = open("taxonomy_and_rules.md").read()  # ~8,000 tokens, identical for every ticket

def classify(ticket: str) -> str:
    resp = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=32000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"Classify this ticket. Reply with the category only.\n\n{ticket}"}],
    )
    return resp.content[0].text.strip()

if __name__ == "__main__":
    tickets = json.load(open("tickets.json"))  # ~50,000 tickets per night
    results = {t["id"]: classify(t["body"]) for t in tickets}
    json.dump(results, open("results.json", "w"))
EOF
