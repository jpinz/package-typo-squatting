#!/bin/bash
set -e

echo "📦 Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh

echo "🐍 Setting up Python environment..."
uv sync --link-mode=copy

echo "✅ Dev container setup complete!"
