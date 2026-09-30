#!/bin/bash

# Keep Claude Code's auto-memory directory and this repo's copies of it
# identical, so memory is tracked and follows the repo between machines.
# Ported from knf's scripts/sync-memory.sh (two-way, manifest, git-aware
# deletions); read that script's header for the full reasoning. What
# differs here is the split:
#
# WHY TWO MIRRORS:
#
# interregnum is a PUBLIC repo. Some memory is private (the film made
# for King's family, his network setup). So each memory file goes to
# exactly one mirror, chosen by its name:
#   private-*.md  -> bible/private/memory/  (gitignored, never public)
#   everything else -> memory/               (tracked, public)
# MEMORY.md is the one file both sides need: its public copy drops every
# index line that links a private-*.md file, so no private name or hook
# leaks. When git brings in a newer public index, the import keeps this
# machine's private lines and appends them to it.
#
# The private mirror has no git history, so git-recorded deletions apply
# to the public mirror only. Local deletions still propagate to both
# through the manifest.
#
# Usage: run from anywhere; the script resolves its own paths.
#
#   $ ./scripts/sync-memory.sh          # report every step
#   $ ./scripts/sync-memory.sh --quiet  # print only when something changed
#
# Exit 0 when the mirrors end up in sync, 1 otherwise. Never 2: as a
# Stop hook, exit 2 would keep Claude from stopping.

set -euo pipefail
trap '[ $? -eq 0 ] || exit 1' EXIT

QUIET=0
[ "${1:-}" = "--quiet" ] && QUIET=1
say() { [ "$QUIET" -eq 1 ] || echo "$*"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Claude encodes the project path by replacing every non-alphanumeric
# character with "-". `printf`, not `echo`: `tr -c` would turn the
# trailing newline into a stray "-".
ENCODED_REPO_PATH="$(printf '%s' "$REPO_ROOT" | tr -c 'a-zA-Z0-9' '-')"
PROJECT_DIR="$HOME/.claude/projects/${ENCODED_REPO_PATH}"
AUTO_MEMORY="$PROJECT_DIR/memory"
PUB="$REPO_ROOT/memory"
PRIV="$REPO_ROOT/bible/private/memory"
MANIFEST="$PROJECT_DIR/memory-sync-manifest"
INDEX=MEMORY.md
PRIVATE_LINE='](private-'

if [ ! -d "$PROJECT_DIR" ]; then
  echo "Claude Code has not run in this repo from HOME=$HOME: $PROJECT_DIR not found." >&2
  exit 1
fi
mkdir -p "$AUTO_MEMORY" "$PUB" "$PRIV"

TMP="$(mktemp -d)"
cleanup() { local rc=$?; rm -rf "$TMP"; [ "$rc" -eq 0 ] || exit 1; }
trap cleanup EXIT

# Flat listing of memory files (basenames), .DS_Store excluded.
list_files() {
  (cd "$1" && find . -maxdepth 1 -type f -name '*.md' | sed 's|^\./||' | sort)
}
is_private() { case "$1" in private-*) return 0 ;; *) return 1 ;; esac; }
mirror_of() { if is_private "$1"; then echo "$PRIV"; else echo "$PUB"; fi; }
in_manifest() { [ -f "$MANIFEST" ] && grep -qxF -- "$1" "$MANIFEST"; }
rel() { echo "${1#"$REPO_ROOT"/}"; }
mtime() { stat -f %m "$1" 2>/dev/null || stat -c %Y "$1"; }

# The public index: the auto-memory index minus private lines, carrying
# the source's mtime so `-nt` comparisons still work.
public_index() {
  grep -vF -- "$PRIVATE_LINE" "$AUTO_MEMORY/$INDEX" > "$1" || true
  touch -r "$AUTO_MEMORY/$INDEX" "$1"
}

# Print every difference between auto-memory and the two mirrors.
drift() {
  local name dst
  while IFS= read -r name; do
    [ -n "$name" ] || continue
    [ "$name" = "$INDEX" ] && continue
    dst="$(mirror_of "$name")/$name"
    cmp -s "$AUTO_MEMORY/$name" "$dst" 2>/dev/null || echo "differs or missing: $name"
  done < <(list_files "$AUTO_MEMORY")
  for dir in "$PUB" "$PRIV"; do
    while IFS= read -r name; do
      [ -n "$name" ] || continue
      [ "$name" = "$INDEX" ] && [ "$dir" = "$PUB" ] && continue
      [ "$dir" = "$PUB" ] && is_private "$name" && { echo "private file in public mirror: $name"; continue; }
      [ "$dir" = "$PRIV" ] && ! is_private "$name" && { echo "public file in private mirror: $name"; continue; }
      [ -e "$AUTO_MEMORY/$name" ] || echo "only in mirror: $name"
    done < <(list_files "$dir")
  done
  if [ -f "$AUTO_MEMORY/$INDEX" ]; then
    public_index "$TMP/index"
    cmp -s "$TMP/index" "$PUB/$INDEX" 2>/dev/null || echo "differs: public $INDEX"
  fi
}

# FAST PATH: already in sync, the common case at every Stop.
if [ -f "$AUTO_MEMORY/$INDEX" ] && [ -z "$(drift)" ]; then
  list_files "$AUTO_MEMORY" > "$MANIFEST"
  say "In sync (nothing to do)."
  exit 0
fi

# 1. IMPORT: mirror -> auto-memory, for files git (or another session)
#    brought in: absent here and not exported before, or newer and
#    different. Never deletes. The public index is merged, not copied.
IMPORTED=0
for dir in "$PUB" "$PRIV"; do
  while IFS= read -r name; do
    [ -n "$name" ] || continue
    [ "$name" = "$INDEX" ] && continue
    [ "$(mirror_of "$name")" = "$dir" ] || continue
    src="$dir/$name"; dst="$AUTO_MEMORY/$name"
    if [ ! -e "$dst" ]; then
      in_manifest "$name" && continue
    elif cmp -s "$src" "$dst" || [ ! "$src" -nt "$dst" ]; then
      continue
    fi
    cp -p "$src" "$dst"
    IMPORTED=$((IMPORTED + 1))
    echo "imported from $(rel "$dir")/: $name"
  done < <(list_files "$dir")
done
if [ -f "$PUB/$INDEX" ]; then
  if [ ! -f "$AUTO_MEMORY/$INDEX" ]; then
    cp -p "$PUB/$INDEX" "$AUTO_MEMORY/$INDEX"
    IMPORTED=$((IMPORTED + 1)); echo "imported from memory/: $INDEX"
  else
    public_index "$TMP/index"
    if ! cmp -s "$PUB/$INDEX" "$TMP/index" && [ "$PUB/$INDEX" -nt "$AUTO_MEMORY/$INDEX" ]; then
      { cat "$PUB/$INDEX"; grep -F -- "$PRIVATE_LINE" "$AUTO_MEMORY/$INDEX" || true; } > "$TMP/merged"
      cp "$TMP/merged" "$AUTO_MEMORY/$INDEX"
      touch -r "$PUB/$INDEX" "$AUTO_MEMORY/$INDEX"
      IMPORTED=$((IMPORTED + 1)); echo "merged from memory/: $INDEX (private lines kept)"
    fi
  fi
fi

# 2. DELETIONS (public only): a file only in auto-memory whose removal
#    git recorded after the file's mtime was pruned on another machine.
if git -C "$REPO_ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  while IFS= read -r name; do
    [ -n "$name" ] || continue
    is_private "$name" && continue
    [ -e "$PUB/$name" ] && continue
    deleted_at="$(git -C "$REPO_ROOT" log -1 --diff-filter=D --format=%ct -- "memory/$name" || true)"
    [ -n "$deleted_at" ] || continue
    if [ "$deleted_at" -gt "$(mtime "$AUTO_MEMORY/$name")" ]; then
      rm -f "$AUTO_MEMORY/$name"
      echo "removed (deleted in git): $name"
    fi
  done < <(list_files "$AUTO_MEMORY")
fi

if [ ! -f "$AUTO_MEMORY/$INDEX" ]; then
  echo "Auto-memory has no $INDEX: $AUTO_MEMORY" >&2
  echo "Refusing to mirror an empty auto-memory over the repo copies." >&2
  exit 1
fi

# 3. EXPORT: auto-memory -> mirrors, exact. Files absent from
#    auto-memory, or in the wrong mirror, are removed.
EXPORTED=0
for dir in "$PUB" "$PRIV"; do
  while IFS= read -r name; do
    [ -n "$name" ] || continue
    [ "$name" = "$INDEX" ] && [ "$dir" = "$PUB" ] && continue
    if [ ! -e "$AUTO_MEMORY/$name" ] || [ "$(mirror_of "$name")" != "$dir" ] || [ "$name" = "$INDEX" ]; then
      rm -f "$dir/$name"
      EXPORTED=$((EXPORTED + 1))
      echo "removed from $(rel "$dir")/: $name"
    fi
  done < <(list_files "$dir")
done
while IFS= read -r name; do
  [ -n "$name" ] || continue
  [ "$name" = "$INDEX" ] && continue
  src="$AUTO_MEMORY/$name"; dst="$(mirror_of "$name")/$name"
  if [ ! -e "$dst" ] || ! cmp -s "$src" "$dst"; then
    cp -p "$src" "$dst"
    EXPORTED=$((EXPORTED + 1))
    echo "exported to $(rel "$(mirror_of "$name")")/: $name"
  fi
done < <(list_files "$AUTO_MEMORY")
public_index "$TMP/index"
if ! cmp -s "$TMP/index" "$PUB/$INDEX" 2>/dev/null; then
  cp -p "$TMP/index" "$PUB/$INDEX"
  EXPORTED=$((EXPORTED + 1)); echo "exported to memory/: $INDEX (public lines only)"
fi
list_files "$AUTO_MEMORY" > "$MANIFEST"

# 4. VERIFY.
DIFF_OUTPUT="$(drift)"
if [ -n "$DIFF_OUTPUT" ]; then
  echo "Drift detected:" >&2
  echo "$DIFF_OUTPUT" >&2
  exit 1
fi
if [ "$QUIET" -eq 0 ] || [ "$IMPORTED" -gt 0 ] || [ "$EXPORTED" -gt 0 ]; then
  echo "In sync (imported $IMPORTED, exported $EXPORTED)."
fi
