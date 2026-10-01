---
name: reasoning-effort
description: "King present or unspecified: default effort for everything. Explicitly away: max for creative work (concepts, writing, design, art direction) and checking; default for routine execution."
metadata:
  node_type: memory
  type: feedback
  originSessionId: f848a25b-314d-4f2a-ad2f-d5f9d8a62ded
  modified: 2026-09-30T14:25:35.141Z
---

King's current rule (updated 2026-10-01), for reasoning-effort choices and sessions I launch:
- **King is present** (always assume so unless he says otherwise) → **default effort for everything**, checking
  included. Pass no `--effort` flag.
- **King is away** (only when he says so: "going to sleep", "going out for a couple of hours") →
  - **checking → `--effort max`**: critic passes, reviews, hunting for bugs, flaws and mistakes, and small pure
    improvements (see [[pure-improvement]]);
  - **creative work → max**: concepts and pitches, stories and scripts, design, art direction, and other creative
    development. This applies beyond pitch writing. King explicitly authorized this expansion on 2026-10-01.
  - **routine execution / production plumbing → default**.
- When King indicates he is back, return to **default for everything**. Do not infer absence from silence.
- Apply the equivalent effort setting for the model/tool in use; default means no explicit reasoning-effort
  override, not a hardcoded medium setting. This rule governs reasoning work, not automatic changes to media
  generation parameters. The image-rendering helper `tools/imagegen/gen.sh` retains its existing medium preset
  for executing prepared prompts; creative design and prompt development follow the presence rule above.
- **Correction (2026-09-30):** I read the checking rule as applying even while he was present, and launched a
  max-effort critic before he had confirmed. He objected ("i'm here, why you started a max effort session?"). Never
  act on an unconfirmed reading of a rule. Presence always wins.

**Initial evidence:** King found max "really really slow". The first evidence was one blind pair:
- A concept pitch at xhigh (about 56 min) beat its medium-effort twin (about 11 min) by a clear gap, mostly on
  research accuracy (the medium pitch had a wrong statistic and an outdated fact).
- The xhigh pitch was also ahead on originality, detail and pacing plan; the medium pitch had the sharper hook.
- King: one experiment could be a fluke. It doesn't compare default with max, and a single judge may favour the longer
  document.
- Checking is where extra thinking plausibly pays: it catches errors. So King agreed to max there only.

**Historical testing plan (King, 2026-09-30; superseded by the current rule above):** does max help creative work (concepts, scripts)? It
stays at default until tested. Planned method: when King is away during a concept round, run one pitcher at max
next to a default-effort twin with the same angle, and let the judge score them blind as usual. Decide after several
rounds, never after one. Never run it while King is present. The next time he says he is away before a concept round, propose it in one line before he goes.

**Evidence 2 (2026-10-01, King away):** a blind judge (max) scored three pitches from one brief. Claude at max got
26 (pass, 1st, 63 min, no false claims); GPT-6 Astra got 24 (pass, 2nd, 22 min); Claude at default got 22 (revise,
3rd, 9 min, one real factual error), according to that judge. These uncontrolled comparisons cannot separate effort
from output length, concept luck, or judge preferences. At that point, the rule remained unchanged pending King's
decision; he later expanded away-time max to creative work, as recorded in the current rule above. The report is
in work/morning_report.md.

**Evidence 3 — equal-length Astra experiment (2026-10-01, explicitly requested by King):** King suspected that
max scored higher merely because it wrote more. Tested GPT-6 Astra at explicit medium versus max: three fictional
briefs, two independent pitches per setting per brief (12 pitches). Every pitch had exactly six 100-word sections
(600 words); no trimming, replacement, or retries were needed. Fresh Astra medium judges evaluated each of six
pairs twice, reversing presentation order and hiding the writing effort.
- Mean score: medium **24.6/30**, max **27.0/30**; mean paired advantage **+2.42 points** for max. Max had the
  higher order-averaged score in all six pairs. Five pairs preferred max in both orders; one switched preference.
- Mean writing time: medium **2.58 min**, max **13.66 min** (**5.3× slower**, including word-count checking).
- Largest gains: Form +0.83/5, Core and Originality each +0.50/5. Tempo tied. Production feasibility was slightly
  lower for max: **3.92/5 versus 4.08/5**, scored separately from the 30-point total.
- Interpretation: the score advantage survived identical output length, so extra written volume cannot explain
  this result. Evidence favors extra effort for these constrained creative pitches, at a substantial latency cost.
- Limits: only three briefs; repeated runs and reversed judgments are not independent briefs; Astra judged Astra,
  so style/taste bias remains. Shared fictional facts replaced open-web research, and the rubric was adapted.
  This does not establish what caused the earlier Claude results, general superiority, or statistical significance.
- King initially asked to remember this result without changing the policy. In a subsequent explicit instruction
  on 2026-10-01, he expanded away-time max to creative work, including design and writing, as recorded above.
  This is a user preference informed by the pilot, not evidence that the pilot tested every creative discipline.
- Results: `work/astra_effort_v2/results.txt`; preregistered design: `work/astra_effort_v2/protocol.md`;
  raw drafts, judgments, timing, usage, and audit are preserved in that directory.

## Deferred research-effort experiment (2026-10-02)

King wants to test the effect of reasoning effort on research later. Do not start the experiment now or change
our effort policy. The existing controlled creative experiment used supplied fictional facts, not open-web
research, so it does not establish a research benefit. A future test should distinguish information gathering
from evidence evaluation, synthesis and verification, and assess factual/source accuracy as well as time and cost.
Higher effort helping difficult synthesis more than routine lookup remains a hypothesis to test.

**How to apply:** before every launch, check whether King explicitly said he is away and has not indicated his
return. If present or unspecified, use default effort for everything. If away, use max for creative development
and checking, and default for routine execution. No repeated confirmation is needed after he announces absence.

Related: [[headless-session-tools]], [[dont-over-test]], [[pure-improvement]].
