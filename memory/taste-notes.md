---
name: taste-notes
description: "King's taste notes after two episodes — images looked oily/crowded/AI; the art was cliché"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b27232ca-5280-4208-9826-f1156f716aae
  modified: 2026-09-30T10:14:58.804Z
---

**1. Images (2026-09-30):** "suboptimal… 'oily' and 'crowded' and just looking very ai-generated, not elegant."
- My prompts caused much of it: 3,000–5,000-character prompts listing every prop give crowded frames, and texture
  words (grain, pores, lived-in, worn) give an oily surface. The image model's own look adds to it.
- **How to apply:**
  - Spare prompts: one subject, negative space, and no over-described texture.
  - A/B test prompts and image models before a batch.
  - Judge frames for elegance, not just "photoreal". My eye was too lenient.
  - The tested technique (photographer's brief, model routing, film_finish.py) is in docs/playbook.md §2b.
  - King loves Luma Uni-1. Mixing models for one character's face "makes the drift way way more", even when each
    frame matches the reference, so judge faces shot-to-shot in sequence. But multiple models per film are fine for
    different styles or sequences (King: "it's not true that we should never use multiple models for one film").
    General rule (King): "use Luma Uni-1 Max unless there's truly something it just can't do right". Don't turn
    single-image test results into routing rules; that's overfitting (2026-09-30). Settled for good: even after a blind
    screen where Claude ranked Grok and Muse above Luma, King said "it's just luma for me. settled." Don't reopen the
    default model; only switch per shot when Luma really can't do it.

**2. Cliché:** "your art has been quite cliche so far… the artworks that I loved are all not cliche when they came out.
There's always something niche, unique, creative… it's not that we can't use repeated elements, it's just the core
can't be something so common that people are tired and sick of seeing."
- **Why:** my defaults drift to the most expected answer, and trend summaries are cliché too.
- **How to apply:**
  - Before pitching, list the 20 most predictable takes and ban them.
  - Every concept needs a formal invention: the way it's told is part of the idea (*Tenet*'s palindrome, *Arrival*'s
    language).
  - Draw on specific, odd human material rather than trends.
  - Judge against the taste bible, `bible/taste.md` (written 2026-09-30 from the "Loved works" in `bible/brief.md`):
    §3 is the ban list with IDs, and §5 is the concept test and rubric that every concept must pass. Read it before
    any concept work.

**3. Pacing (2026-09-30):** "pacing can also be altered. i feel like our first two films have constant pacing."
- **Why:** cut lengths varied, but movement inside shots, narration cadence, sound density and intensity stayed level,
  so each film felt like one tempo.
- **How to apply:** every script gets a tempo map with contrast across all four dials, including at least one
  acceleration, one hard stop and one stillness or silence (playbook §1, Pacing).

**4. No constant dial (2026-09-30):** "as with pacing, and other art aspects, i think constant is not necessarily good.
balancing surprise, varieties, familiarity is key." Said about the pilot's locked-off camera default.
- **How to apply:** in every art aspect (camera, palette, shot size, sound, performance), give each episode a home
  register, vary it between sections, and include at least one break we haven't taught the audience to expect.
  Don't turn one film's choice into a law (bible/visual/cinematography.md §6).
- **But sparingly** (King, same day): "it's also super super bad to overuse something, like over using surprises, big
  camera movements and stuff." The home register dominates; one or two surprises per film; when in doubt, cut a move.

Related: [[director-owns-creative-calls]], [[episode-defaults]].
