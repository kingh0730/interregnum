---
name: reasoning-effort
description: "While King is at the keyboard, everything runs at default effort; only when he says he is away do checking jobs (critics, reviews, bug and flaw hunts, small pure improvements) run at max"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f848a25b-314d-4f2a-ad2f-d5f9d8a62ded
  modified: 2026-09-30T14:25:35.141Z
---

King's rule (2026-09-30), for this session and for every headless session I launch (`claude -p`):
- **King is present** (always assume so unless he says otherwise) → **default effort for everything**, checking
  included. Pass no `--effort` flag.
- **King is away** (only when he says so: "going to sleep", "going out for a couple of hours") →
  - **checking → `--effort max`**: critic passes, reviews, hunting for bugs, flaws and mistakes, and small pure
    improvements (see [[pure-improvement]]);
  - **everything else → default**, until the evidence clearly shows higher effort adds a lot.
- **Correction (2026-09-30):** I read the checking rule as applying even while he was present, and launched a
  max-effort critic before he had confirmed. He objected ("i'm here, why you started a max effort session?"). Never
  act on an unconfirmed reading of a rule. Presence always wins.

**Why:** King found max "really really slow". The only evidence so far is one blind pair:
- A concept pitch at xhigh (about 56 min) beat its medium-effort twin (about 11 min) by a clear gap, mostly on
  research accuracy (the medium pitch had a wrong statistic and an outdated fact).
- The xhigh pitch was also ahead on originality, detail and pacing plan; the medium pitch had the sharper hook.
- King: one experiment could be a fluke. It doesn't compare default with max, and a single judge may favour the longer
  document.
- Checking is where extra thinking plausibly pays: it catches errors. So King agreed to max there only.

**How to apply:** before every launch, ask whether King said he is away. If not, pass no effort flag. If he is away, give critics and reviewers `--effort max` and everything else no flag. Revisit
only when clear new evidence arrives, not after a single comparison.

Related: [[headless-session-tools]], [[dont-over-test]], [[pure-improvement]].
