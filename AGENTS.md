# INTERREGNUM: Codex startup instructions

## Load the existing project context

At the start of each session, before substantive project work:

1. Read `CLAUDE.md` for the shared project guidance and follow its project-document reading order.
2. Read `memory/MEMORY.md`, then read the linked memory files relevant to the task before acting.
   Resolve those links relative to `memory/`.
3. Read all Markdown memory files in `bible/private/memory/` when that directory is available.
   These notes are private: keep their contents and individual filenames out of public files and commits.
   If the directory is unavailable, do not assume its contents or recreate them from guesses.

Reuse these existing sources rather than maintaining a separate copy of the project knowledge.
Apply their working agreements to Codex where applicable; Claude-specific commands, capabilities,
hooks and settings describe the previous tool and must be checked against the current environment.
In particular, the Claude memory-sync hooks described in `memory/memory-sync.md` are not automatically
run by Codex.

## Tool transition

King switched from Claude Code to Codex on **2026-10-01 (Asia/Singapore)**.
The existing guidance and memories carry forward across that switch.

Claude's commits can be identified by their `Co-Authored-By: Claude ... <noreply@anthropic.com>`
trailers. At the handoff, the latest such commit in this branch's history was
`861f612f36490c1165f60c89c18ac8d30dd334a8` (2026-10-01 05:42:36 +08:00), adding the
MiniMax H3 Max / lip-sync / Ray motion manifest runner in `tools/video/h3_batch.py`.
This is an attribution marker, not a claim that every subsequent unsigned commit was made by Codex.
Do not add Claude's co-author trailer to Codex's work.
