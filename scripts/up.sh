#!/usr/bin/env zsh
set -euo pipefail

cd "$(dirname "$0")/.."
docker compose -f docker/compose.yml up -d

echo "Services started."
