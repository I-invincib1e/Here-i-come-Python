#!/usr/bin/env bash
# Requires GitHub CLI: https://cli.github.com/
# Usage: bash ./scripts/create_issues.sh owner/repo
set -euo pipefail

REPO="${1:?Usage: bash ./scripts/create_issues.sh owner/repo}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/issues_config.json"

# Check if jq is available for JSON parsing
if ! command -v jq &> /dev/null; then
    echo "Error: jq is required for JSON parsing. Please install jq."
    exit 1
fi

# Read issues from JSON and create them
jq -r '.issues[] | @base64' "$CONFIG_FILE" | while read -r issue_encoded; do
    issue=$(echo "$issue_encoded" | base64 --decode)
    title=$(echo "$issue" | jq -r '.title')
    labels=$(echo "$issue" | jq -r '.labels')
    body=$(echo "$issue" | jq -r '.body')

    gh issue create --repo "$REPO" --title "$title" --label "$labels" --body "$body"
done
