#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
chmod +x .githooks/pre-commit .githooks/commit-msg .githooks/pre-push .githooks/post-commit
git config --local core.hooksPath .githooks
