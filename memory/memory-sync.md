---
name: memory-sync
description: "Auto-memory is mirrored by scripts/sync-memory.sh at SessionStart and Stop; private-* memories go to gitignored bible/private/memory/, the rest to public memory/; always write auto-memory"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f848a25b-314d-4f2a-ad2f-d5f9d8a62ded
  modified: 2026-09-30T14:10:13.881Z
---

Since 2026-09-30, `scripts/sync-memory.sh` (ported from King's knf repo at his request) keeps auto-memory and the
repo's copies identical. It runs at `SessionStart` and `Stop` from the tracked `.claude/settings.json`.

**Why:** King wanted knf's memory sync here too. This repo is public, so he chose a public/private split.

**How to apply:**
- Always write auto-memory, never the repo copies.
- Anything private must go in a file named `private-*.md`. That covers the private film's content, his network and
  personal setup, and his candid views. Those files mirror only to gitignored `bible/private/memory/`. Every other
  file is published in `memory/` on GitHub, so keep it free of private detail, and never link a `private-*` name
  from a public file. Merely mentioning that a mom episode exists is fine in public (King: "mom episode is fine.
  everybody has moms").
- The public `memory/MEMORY.md` drops index lines that link `private-*` files. It merges line-union
  (`.gitattributes`).
- `scripts/check-memory-index.sh` (also from knf) flags orphan files and dangling index lines on both sides, and any
  private name in the public index. Run it after adding or deleting a memory.
- After editing memory through Bash, run `bash scripts/sync-memory.sh` by hand if the repo copy must be current that
  turn; otherwise the Stop hook does it.

Related: [[parallel-sessions-git]].
