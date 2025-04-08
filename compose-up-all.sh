#!/bin/bash

VULHUB_DIR="vulhub"

find "$VULHUB_DIR" -type f -name "docker-compose.yml" | while read compose_file; do
  dir=$(dirname "$compose_file")
  echo "🚀 Starting services in $dir"
  (cd "$dir" && docker compose up -d)
done
