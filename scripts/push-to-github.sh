#!/usr/bin/env bash
# Push this repo to GitHub. On the first run, create the private repo rpupo63/complex-analysis-guide.
set -euo pipefail
cd "$(dirname "$0")/.."

REPO=rpupo63/complex-analysis-guide

if ! git remote get-url origin >/dev/null 2>&1; then
    if gh repo view "$REPO" >/dev/null 2>&1; then
        git remote add origin "https://github.com/$REPO.git"
    else
        gh repo create "$REPO" --private --source . --remote origin \
            --description "Source and build for the Complex Analysis Companion study guide"
    fi
fi

git push -u origin "$(git branch --show-current)"
echo "GitHub: https://github.com/$REPO"
echo "Local page: file://$PWD/build/guide.html"
