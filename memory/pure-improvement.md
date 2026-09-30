---
name: pure-improvement
description: "King's rule for code, tools, docs, memory and reviews (not creative drafts; from hanair via knf, 2026-09-30): every change must be a pure improvement with no input where it's worse than what it replaces; think before writing; verify at primary source; no unscoped absolutes; drop speculative findings silently"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f848a25b-314d-4f2a-ad2f-d5f9d8a62ded
  modified: 2026-09-30T14:25:14.722Z
---

King's rule, first stated in hanair on 2026-08-19 as "super super super important", carried to knf on 2026-09-25, and
copied here on 2026-09-30 at his request.
- **Scope (King agreed, 2026-09-30):** code, tools, pipeline prompts and manifests, docs, memory, and reviews of them.
- **Not creative drafts:** concepts, scripts, shot design and art direction. A rewrite there can't dominate on every
  input because taste has trade-offs. Judge those by `bible/taste.md` and the critic pass instead.
- **Never change things hastily, especially small "improvements".**
- **Every change must be a pure improvement.** No input may exist on which it behaves worse than what it replaces,
  however narrow the edge case.
- **The loop he hates:** he asks "is it good?", I change something, he asks "so it's good now?", and I change it again.

**Why:**
- **An after-the-fact fix is proof** that the previous version shipped before the thinking was done. Each one erodes
  trust in every "yes, it's correct".
- **Hypotheticals caused the worst loops.** A reviewer's scenario that was never observed or documented justifies no
  change. Defending against speculation isn't free: it forces regressions and churn.

**How to apply:**
1. **Analyse adversarially before writing.** List the inputs where the change could be worse than the status quo:
   empty, oldest, newest, the edge a threshold creates, every variant of a union, every role.
   - If any regression case exists, don't write it. Either design the version that dominates, or leave things alone
     and present the trade-off for King to decide.
   - Prefer no change over a 90% improvement.
2. **Verify before he asks.** When he asks "is it good?", the checking must already be done. Answer from it; never
   discover flaws live and patch mid-answer.
3. **A fix is itself a change and must clear the same bar** (sharpened 2026-08-31, after a review where half the
   findings were regressions introduced by the previous fix). Before writing a fix:
   - Verify at the primary source: the code, the library's source, the raw doc. Not a summary, not a memory, not my own
     earlier turn.
   - Never write an absolute ("the only X", "always", "never", "first") unless the whole scope was actually enumerated.
   - After the edit, re-read the surrounding context and every consumer of the claim.
   - Treat "I established that earlier" as unverified.
4. **Only suggest what moves the needle.** "Is this OK?" asks one question: is there a hard, totally broken thing,
   observed or certainly triggerable? It doesn't ask whether every corner is guarded.
   - Triage review findings the same way.
   - Drop the speculative class silently: a dependency might change, our own invariant might change, cosmetics on
     unreachable inputs. Don't present these as accept/decline decisions, because that restarts the back-and-forth.

Related: [[reasoning-effort]] (checking runs at max when King is away), [[dont-over-test]].
