---
name: reasoning-effort
description: "Use default reasoning effort whenever King is at the keyboard; max only when he's away AND higher effort proved to add real quality"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f848a25b-314d-4f2a-ad2f-d5f9d8a62ded
  modified: 2026-09-30T13:23:06.429Z
---

King's rule (2026-09-30), for this session and for every headless session I launch (`claude -p`):
- **King is present** (the default assumption) → default reasoning effort. Pass no `--effort` flag.
- **King is away** → only when he says so ("going to sleep", "going out for a couple of hours" and so on).
  - Then use `--effort max` only if the evidence shows higher effort really adds a lot of quality.
  - Otherwise use the default.
- **The evidence:** the 2026-09-30 blind test in a private episode's concept round. Pitcher D ran at medium (about 11 min) as a
  twin of A at xhigh (about 56 min). **Verdict: xhigh was better by a clear gap**, mainly in research accuracy. D had a wrong headline stat (81% where the source says 47%) and a stale fact, fewer details, and a flatter tempo map; D had the sharper hook. This was one pair, and medium isn't necessarily the CLI default. Conclusion: higher effort helps most on research-heavy concept work, so when King is away, max is justified there. The judge ran at default in 9 min and did well.

**Why:** King found max "really really slow" and doubted that higher effort was needed at all. Waiting only costs him
when he's at the keyboard.

**How to apply:** check whether he said he's leaving before every long launch. Once he's back, return to the default.

Related: [[headless-session-tools]], [[dont-over-test]].
