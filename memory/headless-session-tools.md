---
name: headless-session-tools
description: "Launch headless `claude -p` sessions in auto mode with a deny-list for paid/publishing actions; my old --allowedTools allowlist is what blocked their interpreters"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b27232ca-5280-4208-9826-f1156f716aae
  modified: 2026-09-30T05:09:51.607Z
---

Headless writing sessions (`claude -p ... --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*)"`) can't run
`python3`, `uv`, `node`, `jq` and so on. That is **only because the launch command's allowlist leaves them out**. It is
not a property of this repo or of non-interactive runs in general. Subagents started with the Agent tool, and the main
session, run Python and uv fine.

**Why:** a redesign session (2026-09-29) found its interpreters refused and generalised that into "every interpreter
is refused in non-interactive runs"; the belief was wrong and was corrected on 2026-09-30.

**How to apply:**
- Launch headless sessions with `--permission-mode auto` plus `--disallowedTools` for paid and publishing actions
  (git push, codex, imagegen, i2v.py, run_jobs.py, eleven.py, fal_run.py). See docs/playbook.md stage 1. King
  asked why they weren't in auto mode (2026-09-30); the allowlist was my over-restriction.
- Test that on one short session first.
- Grep line-shape counting is a fallback only for a session that truly has no interpreter.

Related: [[watch-delegated-jobs]].
