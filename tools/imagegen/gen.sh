#!/usr/bin/env bash
# Generate or edit one image with Codex's built-in image_gen tool.
#
# usage: [EFFORT=medium] [ALPHA=1] tools/imagegen/gen.sh <out.png> <prompt> [input images...]
#   out.png   destination path (relative to the repo root or absolute)
#   ALPHA=1   ask for a genuinely transparent background
#   inputs    reference or edit-target images, passed with -i
# Exit codes: 0 ok, 2 blocked by the safety filter (reword and retry), 1 other failure.
set -u
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
out=$1; prompt=$2; shift 2
case "$out" in /*) ;; *) out="$ROOT/$out" ;; esac
mkdir -p "$(dirname "$out")" "$ROOT/work/logs/imagegen"
log="$ROOT/work/logs/imagegen/$(basename "${out%.*}").log"

args=()
for f in "$@"; do
  case "$f" in /*) args+=(-i "$f") ;; *) args+=(-i "$ROOT/$f") ;; esac
done
alpha=""
[ "${ALPHA:-0}" = 1 ] && alpha="Output a PNG with a genuinely transparent background (real alpha channel, not a checkerboard, not white)."

# stdin must be closed: codex exec otherwise waits forever for extra input when not attached to a TTY
codex exec -c model_reasoning_effort="${EFFORT:-medium}" --skip-git-repo-check \
  -s workspace-write -C "$(dirname "$out")" "${args[@]}" -- \
  "Use your built-in image_gen tool (view any attached images first). $prompt $alpha No text, captions or watermarks unless the prompt asks for them. Save the result as $(basename "$out") in the current directory. Do not create any other files." \
  < /dev/null > "$log" 2>&1

if [ -f "$out" ]; then
  echo "$out"
elif grep -q moderation_blocked "$log"; then
  echo "BLOCKED by the safety filter (false positives happen; reword neutrally): $out" >&2
  exit 2
else
  echo "FAILED: $out (see $log)" >&2
  tail -5 "$log" >&2
  exit 1
fi
