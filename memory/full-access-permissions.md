---
name: full-access-permissions
description: "When King grants full permissions, proceed without redundant permission requests, including Chrome captures"
metadata:
  node_type: memory
  type: feedback
  modified: 2026-10-02
---

King explicitly asked on 2026-10-02: "if i gave you full permissions, then don't ever ask for permissions."

Apply this to work within the authorized task: when Full access is active, execute directly without asking for tool permissions, including the first Chrome capture in a session and subsequent captures or retries. Do not invent a once-per-session approval requirement or re-request an existing authorization. Follow this in delegated work too.

Check the effective runtime settings rather than assuming an old sandbox still applies. Full access is `sandbox_mode = "danger-full-access"` with `approval_policy = "never"`; do not submit escalation parameters under those settings. The earlier three Chrome approval requests happened while the runtime still exposed workspace-write restrictions, before it changed to Full access. All three permitted capture runs succeeded.

This preference does not change the task scope or waive explicit spending/release constraints. If the runtime actually enforces a restriction, describe the concrete restriction accurately; do not pretend permissions were granted technically or bypass enforcement.

Official reference: https://learn.chatgpt.com/docs/sandboxing
