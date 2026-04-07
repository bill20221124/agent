#!/usr/bin/env zsh
set -euo pipefail

cd "$(dirname "$0")/.."
docker compose -f docker/compose.yml down

echo "Services stopped."
