#!/usr/bin/env bash
set -euo pipefail
git init -q -b main
git config user.email eval@example.com
git config user.name eval

echo hi > a.txt && git add . && git commit -q -m init && git checkout -q -b feature/x
