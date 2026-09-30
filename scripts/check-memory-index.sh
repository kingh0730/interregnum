#!/bin/bash

# Verify that the memory index and the memory files are in one-to-one
# correspondence. Ported from knf's scripts/check-memory-index.sh; its
# header explains the check. Briefly:
#   - an ORPHAN FILE is a memory with no index line (Claude never sees it
#     advertised at session start);
#   - a DANGLING LINK is an index line whose file doesn't exist.
#
# WHAT DIFFERS HERE (see scripts/sync-memory.sh): memory is split.
#   1. Public: memory/*.md against memory/MEMORY.md, which is exactly what
#      is committed. It must also contain no link to a private-* file.
#   2. Private: bible/private/memory/private-*.md against the private-*
#      lines of the full index in auto-memory, the only index that lists
#      them. This check is skipped, with a note, when Claude hasn't run in
#      this repo from this HOME.
#
# Run scripts/sync-memory.sh first to check the latest auto-memory state.
# Exit 0 when both are in correspondence, 1 otherwise.
#
# Usage: run from anywhere; the script resolves its own paths.
#
#   $ ./scripts/check-memory-index.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PUB="$REPO_ROOT/memory"
PRIV="$REPO_ROOT/bible/private/memory"
ENCODED_REPO_PATH="$(printf '%s' "$REPO_ROOT" | tr -c 'a-zA-Z0-9' '-')"
AUTO_INDEX="$HOME/.claude/projects/${ENCODED_REPO_PATH}/memory/MEMORY.md"

# Memory files in a directory (basenames), the index excluded.
files_in() {
  [ -d "$1" ] || return 0
  find "$1" -maxdepth 1 -name '*.md' ! -name 'MEMORY.md' -exec basename {} \; | sort
}

# Link targets ending in .md from an index, e.g. `- [Title](slug.md) — hook`.
links_in() {
  { grep -oE '\]\([^)]+\.md\)' "$1" || true; } | sed -E 's/^\]\(//; s/\)$//' | sort -u
}

STATUS=0
report() { # $1 heading, $2 newline-separated names
  [ -n "$2" ] || return 0
  echo "$1" >&2
  printf '%s\n' "$2" | sed 's/^/  /' >&2
  STATUS=1
}

# 1. Public.
if [ ! -f "$PUB/MEMORY.md" ]; then
  echo "Memory index not found: $PUB/MEMORY.md" >&2
  exit 1
fi
PUB_FILES="$(files_in "$PUB")"
PUB_LINKS="$(links_in "$PUB/MEMORY.md")"
report "Public orphan files (in memory/ but NOT listed in memory/MEMORY.md):" \
  "$(comm -23 <(printf '%s\n' "$PUB_FILES") <(printf '%s\n' "$PUB_LINKS"))"
report "Public dangling links (listed in memory/MEMORY.md but file missing):" \
  "$(comm -13 <(printf '%s\n' "$PUB_FILES") <(printf '%s\n' "$PUB_LINKS") | grep -v '^private-' || true)"
report "Private links in the PUBLIC index (must never be published):" \
  "$(printf '%s\n' "$PUB_LINKS" | grep '^private-' || true)"
report "Private files in the PUBLIC mirror (must never be published):" \
  "$(printf '%s\n' "$PUB_FILES" | grep '^private-' || true)"

# 2. Private.
if [ -f "$AUTO_INDEX" ]; then
  PRIV_FILES="$(files_in "$PRIV")"
  PRIV_LINKS="$(links_in "$AUTO_INDEX" | grep '^private-' || true)"
  report "Private orphan files (in bible/private/memory/ but NOT in the auto-memory index):" \
    "$(comm -23 <(printf '%s\n' "$PRIV_FILES") <(printf '%s\n' "$PRIV_LINKS"))"
  report "Private dangling links (in the auto-memory index but not in bible/private/memory/):" \
    "$(comm -13 <(printf '%s\n' "$PRIV_FILES") <(printf '%s\n' "$PRIV_LINKS"))"
else
  echo "Note: no auto-memory index at $AUTO_INDEX; private check skipped." >&2
  PRIV_FILES=""
fi

if [ "$STATUS" -eq 0 ]; then
  n_pub="$(printf '%s\n' "$PUB_FILES" | grep -c . || true)"
  n_priv="$(printf '%s\n' "$PRIV_FILES" | grep -c . || true)"
  echo "In sync: $n_pub public and $n_priv private memory files, all indexed and all present."
fi
exit "$STATUS"
