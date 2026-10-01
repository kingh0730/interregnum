---
name: parallel-sessions-git
description: "When other Claude sessions share the repo, commit with `git commit -m … -- <paths>` only; never -a, never a bare commit after git add"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b27232ca-5280-4208-9826-f1156f716aae
  modified: 2026-09-30T13:29:42.853Z
---

King often runs several Claude sessions in the interregnum repo at once (e.g. 2026-09-30: an adviser session and a v3
episode builder alongside mine). Their edits sit uncommitted or **staged** in the same working tree.

**Why:** a plain `git commit` commits everything staged, including another session's `git mv` moves, and `commit -a`
also sweeps up their unstaged edits. Either one would publish someone else's half-finished work under my message.

**How to apply:**
- Always commit with explicit paths on the commit command: `git commit -m "…" -- path1 path2`. That commits only those
  paths, whatever else is staged.
- In a private project's own repo, commit only my own episode folder.
- Coordinate shared resources (fal credit, ElevenLabs voice slots and deletion, shared tool files) by SendMessage.
- Give each episode its own voice prefix, e.g. "v2c_".
- **Kill only by PID, never `pkill -f <pattern>`.** On 2026-09-30, `pkill -f "fal_run.py luma…"` also killed the v3
  episode's in-flight Luma requests. Record the PIDs of the jobs I start and kill those.

Related: [[watch-delegated-jobs]].

## Deferred production isolation (2026-10-01)

Concurrent agents edited shared generation runners during a production. No resulting damage was confirmed,
but the exact runner version was not pinned, leaving a reproducibility gap.

King wants this issue remembered, with no implementation today. Candidate approach for a future production:
a dedicated Git worktree at a recorded commit, deliberate imports of reviewed fixes, and separate media,
manifests, outputs and request logs. Nested private repos need separate handling; a parent worktree does not
copy them. This is a deferred idea, not authorization to create worktrees or reorganize existing productions.
