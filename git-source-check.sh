#!/bin/bash

echo "🔍 Git Source Health Check"
echo "=========================="

# 1. Check if we're inside a git repo
if ! git rev-parse --is-inside-work-tree &> /dev/null; then
  echo "❌ Not inside a Git repository"
  exit 1
fi

# 2. Show remote origin
echo ""
echo "📡 Remote Origin:"
git remote -v

# 3. Show Git user config for this repo
echo ""
echo "👤 Git User (Local Repo Config):"
git config user.name || echo "Not set"
git config user.email || echo "Not set"

# 4. Show global git user
echo ""
echo "🌍 Git User (Global Config):"
git config --global user.name || echo "Not set"
git config --global user.email || echo "Not set"

# 5. Show all config sources
echo ""
echo "⚙️ All Git Config Sources:"
git config --list --show-origin | grep user

# 6. Detect HTTPS or SSH
echo ""
echo "🔑 Authentication Method:"
remote_url=$(git remote get-url origin)

if [[ $remote_url == https* ]]; then
    echo "Using HTTPS → credentials stored in credential manager or ~/.git-credentials"
else
    echo "Using SSH → checking key..."
    ssh -T git@github.com 2>&1
fi

