---
name: taste-notes
description: "King's visual taste and model choices — Luma originals, Codex beauty faces and elaborate focal subjects, Codex edits and preservation review"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b27232ca-5280-4208-9826-f1156f716aae
  modified: 2026-10-02T01:29:24.513Z
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
    screen where Claude ranked Grok and Muse above Luma, King said "it's just luma for me. settled."
    **Update 2026-10-02:** the approved general editing rules in §6 below supersede this older rule for edits.
    Original-generation preferences now include the beauty-portrait and elaborate focal-subject exceptions
    in `docs/playbook.md` §2b and §7 below;
    Codex is now the default generative editor. This is an explicit workflow choice, not a model-superiority finding.

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

**5. Faces: average, never scary (2026-09-30):** "i'm good with 'not pretty', most humans are not pretty, quite average
looking, perfectly normal, but i'm not ok with 'looking scary' like these deep creases, heavy spots and stuff (unless
it's intentional, like a man without one arm or something)."
- **Why:** Luma's first mother read about 70 instead of 58, and the son's edit sheets drifted into weathered, spotted,
  gaunt skin.
- **How to apply:** judge every face for "scary" and retake it. The prompt method is in docs/playbook.md §2b, "Faces".

**6. General image-editing rules (approved 2026-10-02):** King asked to establish general rules rather than
repair First Day, then approved the following policy with "yes, let's remember this".

1. **Choose original generation and editing separately.** Retain existing preferences for original images;
   use Codex's built-in image generation by default for generative edits, including corrections, reframing and
   derived poses/views. This is a workflow choice, not a claim that Codex always wins. Luma retries are not a
   prerequisite for using the default editor.
2. **Start from a clean, approved source best suited to the change.** Do not automatically pass the latest
   attempt into the next. The best source need not be the earliest when a later approved version contains a
   necessary pose, composition or intentional design change.
3. **Keep edit chains short.** Combine compatible changes when practical. A further edit of an edited image is
   acceptable when its existing improvements matter and its quality remains intact. No fixed edit count
   guarantees quality.
4. **Preserve authoritative references.** Retain approved character, costume and location references throughout;
   an edited shot must not silently replace them. Record intentional approved design changes.
5. **Check preservation as carefully as the requested change.** Compare the whole image at full size with its
   input and the clean approved source: faces, texture, sharpness, colour, lighting and geometry. Check neighboring
   shots for continuity, including after cross-model edits, so gradual deterioration is not missed.
6. **Reject degradation instead of repeatedly repairing it.** Harsh texture, identity drift or damaged geometry
   means returning to a clean source or regenerating, not building further work on the damaged result.
7. **Use ordinary editing tools for exact operations.** Cropping, resizing and typography generally do not need
   generative repainting. Preserve source pixels wherever practical, and retain originals and version history,
   including which images were the actual inputs to each edit.

Applies to future work generally; remembering the policy is not a request to regenerate existing episodes.
Operational guidance: `docs/playbook.md` §2b. Existing episode recipes remain historical records.

**7. Original generation: attention AND elaboration (approved 2026-10-02).** King finds Codex's added detail
undesirable when it competes with the intended subject. Use that detail deliberately through this general rule:

- For a non-face subject to qualify for Codex original generation under this exception, **both** conditions must
  hold: it **must command viewer attention** and its design **must be highly elaborate**, with close inspection
  of intricate detail part of the intended experience. Otherwise default to Luma.
- Small size, foreground position, prominence, beauty or intricacy alone does not qualify. A plain foreground cup
  remains Luma; an intricate background ornament remains Luma. A large elaborate focal sculpture can qualify.
- **Architecture defaults to Luma:** settings, skylines, cityscapes, buildings and interiors, including spectacular
  architecture whose appeal is scale, silhouette, proportion, space or light. An ornate background building stays
  with Luma. Codex applies to an architectural showpiece only when it meets both attention and elaboration
  conditions: the viewer is meant to inspect its mechanisms, carvings or layered construction. Grandeur alone
  does not qualify.
- **Beauty-focused base faces remain a separate Codex exception.** The two-condition non-face rule does not
  narrow that existing exception. The general Codex editing default and all seven editing rules in §6 are unchanged.
- This is an approved division of work based on King's taste, not a universal model-quality ranking. These
  original-generation exceptions do not require failed Luma attempts first. Ordinary objects and surrounding
  environments retain the Luma default.

Related: [[director-owns-creative-calls]], [[episode-defaults]].
