---
name: full-file-paths
description: "Give King every file as a complete path relative to the working dir (repo root), one clickable path per file, in backticks"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b27232ca-5280-4208-9826-f1156f716aae
  modified: 2026-09-30T06:37:15.401Z
---

When pointing King to a file, write its complete path relative to the working directory (the repo root), e.g.
`work/imgtest2/B_talkshow_lumaedit.png`. Never give a bare filename, write "same folder", or use a glob like `B_*.png`.
Use an absolute path only for files outside the repo (e.g. the scratchpad).

**Why:** King (2026-09-30): "always give me complete paths to files so i can click", then clarified: "i meant complete
relative paths to working dir", so not absolute paths. He opens files by clicking them in the terminal.

**How to apply:** every file mention in a reply to King, one complete relative path per file, always wrapped in
backticks (King wants them coloured: "i want color there").
