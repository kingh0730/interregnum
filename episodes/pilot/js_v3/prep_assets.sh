#!/usr/bin/env bash
# Embed the pictures the v3 screens need as data-URI scripts in work/pilot/js_v3/src/ (git-ignored media).
# Pages load them with K.asset(name). Data URIs keep canvases untainted under file://, so WebGL can read them.
# Stand-ins are used until the v3 frames exist; re-run this script once they do (preferred sources first).
set -euo pipefail
cd "$(dirname "$0")/../../.."
OUT=work/pilot/js_v3/src; mkdir -p "$OUT"
pick() { for f in "$@"; do [ -f "$f" ] && { echo "$f"; return; }; done; echo "missing: $*" >&2; exit 1; }
emb() { # name src filter
  local name=$1 src=$2 vf=$3 tmp="$OUT/$1.jpg"
  ffmpeg -loglevel error -y -i "$src" -vf "$vf" -q:v 3 "$tmp"
  printf 'window.ASSET=window.ASSET||{};window.ASSET["%s"]="data:image/jpeg;base64,' "$name" > "$OUT/$name.js"
  base64 -i "$tmp" | tr -d '\n' >> "$OUT/$name.js"; printf '";\n' >> "$OUT/$name.js"; rm "$tmp"
  echo "$name <- $src"
}
C43='crop=ih*4/3:ih:(iw-ih*4/3)/2:0'
emb p01    "$(pick work/pilot/keys_v3/p01_lighting.png)"                               "$C43,scale=1440:1080"
emb k02    "$(pick work/pilot/v3/f04_frozen.png work/pilot/keys_v3/k02_father_cu.png work/pilot/keys/k02.png)" "$C43,scale=1440:1080"
emb k01    "$(pick work/pilot/keys_v3/k01_father_mcu.png work/pilot/keys/k01.png)"     "$C43,scale=720:540"
emb father "$(pick assets/pilot/lookdev_v3/father.png)"                                "scale=1672:-2"
