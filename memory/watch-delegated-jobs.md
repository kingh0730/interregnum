---
name: watch-delegated-jobs
description: "Proactively check long-running subagents and background jobs for stalls; don't wait for King to ask \"is anything stuck?\""
metadata:
  node_type: memory
  type: feedback
  originSessionId: b27232ca-5280-4208-9826-f1156f716aae
  modified: 2026-09-30T09:04:29.679Z
---

When a subagent or background job runs long, check it proactively for stalls. Look at real signals: output file timestamps, running render and ffmpeg processes, log tails. Don't just wait for the completion notification.

**Why:** On 2026-09-29 King had to ask "is anything stuck?" twice. The second time, a subagent was deadlocked for about 20 min: its wait loops ran `until ! pgrep -f render.mjs`, and pgrep matched the loops' own command lines, so they could never exit. Earlier, another compositor was killed by the 600 s stall watchdog. King then asked whether the job would ever have finished on its own.

**How to apply:**
- When delegating a long job, set a fallback check: ScheduleWakeup, or a check after my next piece of work.
- If outputs haven't changed in 10+ minutes, inspect the job.
- Tell agents to wait on a PID or an output file, never on `pgrep -f <name>` when `<name>` appears in the waiting command itself.
- Stall checks must watch the delegated session's own transcript file (find it by its brief text), never "the
  newest .jsonl in the project dir". My own session lives in the same dir and keeps it fresh, so a stall would never
  show (caught 2026-09-30).
- When a stage completes, stop its monitors at once (TaskStop). A leftover watcher keeps running and raises false
  "no activity" alarms; King found one still running after a film finished (2026-09-30).
