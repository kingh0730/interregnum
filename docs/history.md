# How we got here (experiments, 2026-09-29)

Before this repo existed, four tests in `~/repos/yue/outputs/anime_clip/` tried to make a short anime clip of a
silver-haired girl in a red scarf on a rooftop at sunset with a paper airplane. King's verdicts decided the pipeline.

| Version | Method | King's verdict | Why |
|---|---|---|---|
| v1 | 6 Codex keyframes + ffmpeg zoom/pan + crossfades | "More like PPT than anime" | No motion, only camera moves |
| v2 | Codex layer separation (sky/city/character cutouts, aligned with SIFT), parallax, hair/scarf mesh warp, blink cels, petals, flare, bloom, synth audio | "Interesting, but like an old anime game cutscene" | The character is a puppet: bending a still never changes the silhouette |
| v3 | Codex draws every in-between (key poses, breakdowns, follow-through), timed on twos | Round 1 "a bit weird"; round 2 (held body cel, more drawings) "even worse" | Each Codex image is an independent reinterpretation: no consistency from frame to frame. Head floated on the fixed body; more drawings meant more shimmer. Frame metrics *improved* while the motion got worse |
| v4 | Blender + VRM sample model (pixiv, permissive license), rigged head turn with overlap, blink, spring-bone hair, MToon toon look, composited over the Codex plate | "It does work", but then "this method may not work" | Motion correct and consistent, but it reads as 3D; drawn anime faces need per-character normal editing and more |

**Conclusion:** motion that is both drawn-looking and consistent needs a video model. Codex is excellent for stills,
and everything else stays in-house (see `strategy.md`).

**Other facts established:**
- Sora is gone (app April 2026, API September 24 2026).
- Codex (`gpt-6-astra`) defaults to `xhigh` in `~/.codex/config.toml`. For image jobs, reasoning effort doesn't
  change image quality, so `gen.sh` uses `medium` (about 2 min per image vs about 3 min at xhigh). King chose medium.
- The image model behind Codex's built-in `image_gen` isn't stated anywhere local; the API fallback defaults to `gpt-image-2`.
- `~/.claude/settings.json` allows `Bash(codex exec:*)`; auto mode blocks Claude from changing its own permissions.
- `~/.codex/config.toml` is now tracked in King's home dotfiles repo (only that file; auth and history stay ignored).

## Pilot v1 overnight build (2026-09-29)
- **Codex drifts to semi-photoreal 3D** even when the prompt asks for "hand-painted cel". A leading style block
  ("Flat 2D illustration, cel-shaded … matte surfaces only … absolutely no 3D rendering look") fixed it on the first retake,
  and every later prompt carries it (`episodes/pilot/build/style_prefix.txt`) plus the master style frame as a reference.
- **Character sheets plus refs hold identity well** across 27 keyframes (3 faces).
- **Codex cutout layers don't register with their source keyframe**: they get redrawn at a different scale or pose,
  and sometimes with a different arrangement. Build parallax mattes from the plate itself (GrabCut plus inpainting) instead.
- **Codex edits of a keyframe (e.g. eyes closed) change lines outside the edit.** Paste back only the edited region
  with a feathered mask.
- **Throughput:** about 1 min per image at medium effort, 5 in parallel. 39 images took roughly 15 min with no safety blocks.

## Pilot v2 with Seedance (2026-09-29)
- **Bake-off verdict (King):** the motion looks good, with small imperfections that are unavoidable. The voice was
  consistent across shots but the accent drifted, so every prompt now carries a fixed per-character voice line (the
  "voice bible" in `episodes/pilot/v2_jobs.json`).
- **Off-screen lines come from the same take as the character's on-screen lines.** The Father's whole final address is
  one 22 s take, cut across shots 29–34. Nana's two call-back lines are one take. This makes voice consistency hold by construction.
- **fal polling can drop on a flaky network after the job is billed.** `i2v.py` now saves the request id at submit
  and retries GETs; stranded results can be recovered through the request-history API
  (`GET https://api.fal.ai/v1/models/requests/by-endpoint?endpoint_id=…`, then fetch
  `https://queue.fal.run/bytedance/seedance-2.5/requests/<id>`).
- **Whisper start times run early,** by up to 1.6 s on a short line under a ringing bell. Time subtitles from voiced
  onsets (voice-band energy + periodicity) instead.
- **Don't add a sky grade on top of a Seedance dawn:** the model already does it, and a second one just hazes the image.

## Blender-guided rotoscoping tests (in `~/repos/yue/outputs/anime_clip/`, 2026-09-29)
King's verdicts after v4: v3's drawings were "actually pretty good"; they flicker too, but less visibly because the head moved less, and the weirdness was mostly
the head's unnatural motion path. v5 (camera projection of a painting) is not usable: the layers are hard to get
right and cut through objects. v6 (a drawn face on the 3D head) is "creepy". v7 (a Blender layout frame as a
reference for a Codex keyframe) "looks good".
- **v8 (v7 + v3):** Blender supplies the head-turn motion, and Codex draws every pose over its layout frame with two
  approved drawings as references. Variants: drawn on twos, drawn on ones, optical-flow in-betweens.
- **v9:** a full-body paper-airplane throw (IK arm in Blender), 21 Codex drawings on anime timing, and a composited
  plane after release.
- **Mechanics that worked:** draw the two hold poses first as style anchors; register drawings to a smoothed path of
  their own torso position (the layout's silhouette is unreliable); throws need the flight direction set by the
  camera's vanishing point, not the body's forward vector. Safety false positives: about 1 in 10, and usually pass on a plain retry.
- **King's verdict:** v8 flickers (every drawing reinterprets the character), and v9 "looks really bad, bad physics,
  and flickers" (hand-keyed IK motion has no weight).
- **v10–v13 (EbSynth):** Blender renders the motion, Codex paints 3–7 keyframes over it, and EbSynth (built locally,
  `~/.local/share/ebsynth`) propagates them. v11–v13 used a stand-in of our girl (procedural bob, navy uniform, scarf
  wrap). Flicker dropped from 4.6–7.0 (v8) to about 3.2–4.0, but frames between keyframes smear wherever the pose
  changes a lot, because patch synthesis cannot invent new views. Keyframes made as a chain of Codex edits agree
  better with each other, but that only cut flicker about 5%. Deflickering v8 with optical flow cut it only 7–12%.
- **Conclusion (agreed with King):** local character animation is at diminishing returns. The missing capability is
  inventing in-between views that stay consistent over time, which is what video models do. **Character motion goes to
  Seedance.** Standard inputs are Codex character sheets and Codex keyframes as start frames. Blender layouts are used
  only when a shot needs exact staging (a specific camera move, eyelines, a complex action), and Blender is also used
  for non-character 3D. No EbSynth, rotoscoping, deflickering or procedural character modelling in production.
- **Engineering notes:** OpenCV's DIS optical-flow object is not thread-safe (use one per thread; sharing it corrupted
  the heap), and parallel jobs must not rewrite shared input files that another process is reading.

## Image-model tests (2026-09-30, `work/imgtest*`)
King found the first two episodes' images "oily", "crowded" and "very AI-generated". Tests A–G compared prompt styles
and about 10 models. Each finding rests on one or a few images, so treat them as evidence, not rules. The general rule
that came out of them is "Luma unless it truly can't" (playbook §2b).

- **Prompts (A, D):** prop lists gave crowded stock frames on every model. Photographer's briefs fixed most of it. One
  razor-sharp subject with a blurred world is itself a tell; deep focus read more real. "Snapshot" produced a fake date
  stamp (Nano) and a printed border with gibberish text (Luma).
- **Models, photoreal (A, D):**
  - best: Luma ≈ FLUX.2 Pro;
  - then Seedream 5 Pro and Krea 2;
  - Nano Banana Pro: the most documentary-real, less elegant;
  - GPT Image 2.5 and Codex: glossy stock;
  - FLUX.1 Krea [dev]: centred grins and vignettes;
  - Z-Image Turbo: real but plain at about 1¢.

  Models without an explicit ethnicity and setting drifted Western.
- **Identity (B, E):**
  - My first verdict that Luma edit "crops badly" was wrong: my QA grid had centre-cropped its portrait outputs.
  - Luma-editing a Luma plate re-sharpened skin into crunch.
  - Nano face swaps matched the ref best frame by frame, but King saw that cutting between Luma and Nano frames made
    the drift "way way more".
- **Finish (C):** `film_finish.py` removed wet sheen and unified models; it didn't fix Codex gloss.
- **Styles (F):** Luma led painting, 2D animation, clay and signage; it failed one woodcut (FLUX.2 and Nano were good).
  All six models wrote 明天见面 correctly; for brush characters on paper, only Nano and Codex wrote real ones.
- **Genres (G):** Luma led or tied in nature, animal, space interior, SEM, underwater, night and fights. FLUX.2 and
  Krea 2 tangled limbs in a fight. Nano sometimes ignored instructions. Seedream refused an SEM bee (a false positive).
- **Cost:** about $6.50 of fal credit in all; Luma is about 0.3¢ an image, Nano 15¢.
- **Challenger screen (H, `work/imgtest7/`):** fal lists about 200 active text-to-image endpoints; Luma was a lucky
  wildcard among the ~10 families first tested. Four newer challengers, 2 prompts each, judged blind against Luma (Luma
  was only partly blind, since its frames had been seen before):
  - Dinner: Luma ≈ Recraft V4.1 Pro > Grok Imagine 2 > Meta Muse > Qwen-Image 3.
  - Gouache: Meta Muse > Luma ≈ Recraft > Grok > Qwen.
  - Nothing beat Luma overall. Recraft (21¢) is the closest all-rounder; Muse (1¢) made the most distinctive bold
    painting. First to try when Luma truly can't: Recraft, or Muse for bold painted looks. Re-screen new model families
    every couple of months by listing the fal catalogue by API, not from memory.
- **Challenger screen, round 2 (`work/imgtest7/blind2_*`, key in `.key2.json`):** 16 prompts (hall, metro, 6 styles,
  8 genres) × fresh Luma + 4 challengers, one image each, ranked fully blind by Claude.
  - Points (5 for 1st … 1 for 5th): Grok Imagine 2: 57 (5 firsts); Meta Muse: 54 (5); Qwen-Image 3: 51 (4); Luma: 43 (2);
    Recraft V4.1 Pro: 35 (0).
  - This reverses round 1 for Qwen and Recraft, so single samples are noisy.
  - Blind, Claude ranked Luma lower than when its outputs were labelled. Several fresh Luma frames looked like amateur
    flash snapshots.
  - Claude's blind taste favours clean cinematic frames; King's favours Luma's filmic restraint. Settle the default with
    King's own blind picks, not Claude's.
- **Decision:** King chose Luma as the default regardless of the round-2 scores: "it's just luma for me. settled."

## Video-model test (2026-10-01, v2c *The Exception*)
- Three test shots (key beat 47 with an end frame, action 27, dialogue 04): Seedance 2.5 (i2v and ref), Luma Ray 3.2,
  MiniMax H3 Max, and MiniMax H3 Max lip-sync.
- **Seedance 2.5 refused all four jobs:** "may contain likenesses of real people" (partner validation), on generated
  faces.
- Ray made 47 and refused 27 once (content checker). MiniMax made 47 and 27, and its lip-sync made 04 with our voice.
- **MiniMax invented dialogue on 27,** because the prompt said she "says one short line" and there was no audio to
  follow. Hence the rules that motion prompts never mention speech and that model audio is discarded.
- King chose MiniMax H3 Max as the single video family (motion plus lip-sync).

## Lettering through video generation (2026-10-01)
- A post-generation tracked surface-text overlay jiggled in playback. King judged lettering supplied in the start
  frame and animated by MiniMax H3 Max with the object clearly better.
- Supplying a blank surface and prompting the model to add lettering made the text appear during the shot. King
  rejected this for text that should already exist on the object.
- Text-only scene generation was also tried, but cannot preserve the supplied faces, setting and composition as
  required for these shots; it did not answer the intended test of an unlettered scene reference.
- **Adopted workflow:** finish exact surface lettering in the approved start frame, then animate the complete image.
  Keep screen-space captions in post. Check spelling, readability, attachment and appearance throughout the cut;
  use tracked repairs only where necessary. This is a production default based on one surface-text comparison,
  not a reliability claim for every model or shot.

## Story-action verification (2026-10-01)
- An audit found that an explicitly requested facial action appeared late and with different repetition in the
  generated take, while the selected edit ended before the action. Prompt adherence and editing both contributed
  to the missing story beat; checking lip-sync did not catch it.
- **Lesson:** retain the overall generation pipeline, but verify essential actions twice: in the full take, recording
  their timestamps, and in the final rendered cut. Adjust the edit for usable late action; revise or regenerate
  missing or unusable action. Clear prompts do not guarantee action, timing or repetition, and more prompt detail
  alone is not a demonstrated fix.

## Object graphics beyond lettering (2026-10-01)
- King reported that clock overlays moved to follow generated footage also looked bad. The earlier lesson had been
  applied too narrowly to text; the finishing instructions still called for tracking remaining surface graphics.
- **Revised policy:** prepare all attached graphics in the approved start frame, including clocks, display states
  and symbols. Audit inherited overlays as well as new work. Prefer corrected frames and retakes to another tracking
  adjustment; accept exceptional tracked repairs only after playback review. Exact changing readings may require
  controlled inserts. The lettering test supports this direction, but does not prove reliable clock animation.

## Applying the object-graphics policy (2026-10-01)
- Replaced inherited tracked object graphics with complete-frame animation or controlled fixed-camera inserts.
  Deliberate screen-space graphics remain separate. Review caught extra actors, newly revealed garbled signage
  and generated captions in otherwise plausible replacement takes; those outputs were rejected or reframed.
- Audio preparation also matters: repeated output duration flags allowed following-shot audio into padded
  conditioning tails. Use an explicit trim before silence padding, preserve submitted inputs, and check the actual
  selected dialogue interval. This is an implementation error, not evidence of model randomness.

## Beauty portraits and reference transfer (2026-10-02)
- Compared nine image workflows on three adult Chinese portrait briefs: natural beauty, glamour, and natural
  beauty with modern Chinese makeup. One sample per model per brief, with differing native resolutions;
  these are exploratory results, not a general model ranking.
- Luma's text-only portraits stayed more understated. Codex image generation and GPT Image 2.5 produced more
  idealized beauty; Seedream produced a more dramatic glamour interpretation.
- One Luma edit using the Codex makeup portrait as its face reference placed the character in a cafe while
  retaining much of her identity and beauty. Makeup softened and skin texture increased. This supports trying
  the workflow, not assuming multi-shot consistency.
- Adopted preference: Codex built-in image generation first for beauty-focused base portraits through the
  subscription workflow. Choose another suitable option only if Codex is unavailable or unsuitable. Use the
  approved original base as the reference for Luma scenes and check each result; avoid edits of edits.
- Local test artifacts: `work/beauty-natural-comparison/comparison.jpg`,
  `work/beauty-model-comparison/comparison.jpg`, `work/beauty-chinese-makeup-comparison/comparison.jpg`,
  and `work/luma-beauty-reference-test/cafe.png` (media is untracked).

## Non-face beauty preference (2026-10-02)
- Compared Luma and Codex on the same two briefs: a Singapore riverfront at blue hour and a beautiful futuristic
  tropical waterfront city. One image per model per brief; native resolutions differed.
- The assistant favored Codex's visual allure. King preferred Luma for beautiful non-face subjects. This is an
  explicit creative preference, not evidence of universal model superiority, and it governs the production default.
- Keep Luma for beautiful environments and other non-face subjects. Retain Codex-first only for beauty-focused
  base portraits, then use approved faces as references for Luma scenes.
- Local comparisons: `work/city-luma-codex-test/comparison.jpg` and
  `work/future-city-luma-codex-test/comparison.jpg` (media is untracked).
- **Later policy on the same date:** King separately adopted Codex for generative edits and for original non-face
  subjects that must both command attention and be highly elaborate. Architecture retains the Luma default unless
  it meets both conditions. The beauty-focused base-face exception remains separate. See `docs/playbook.md` §2b
  for the current rules; these preferences are not additional results from the two city comparisons above.

## First episode: COMMON ROOM / 一室两家 (2026-10-02)
- Developed and produced episode 01 of **AI SI - I** through the pre-motion story reel: 3:50, 40 shots,
  1920×1080 at 24 fps, with Chinese-first bilingual subtitles. Eda and Sen separate their households while
  retaining one shared kitchen. The ending preserves the practical inconvenience rather than reuniting them.
- Selected the photographic direction after three contrasting look tests. Luma Uni-1 Max supplied originals;
  Codex built-in edits supplied the final continuity states. The selected package has 27 photographic plates,
  six authored paper states and an exact code-rendered end card. Source selection, hashes, rejected alternatives
  and executed edit prompts are recorded in `episodes/ep01/build/` and the 40 per-shot documents.
- Completed 26 designed-voice lines, original score, recorded-effect sources, five stems and the 230-second mix.
  The master measures −18.0 LUFS and −1.8 dBTP. Static image/caption inspection, transcription, waveform checks
  and complete export decoding were performed. Perceptual audio playback was not performed and remains distinct
  from those technical checks.
- Prepared and dry-ran the 30-job H3 Max handoff at an $8.28 first-pass estimate, with a proposed $4 retake reserve.
  No video-generation requests were submitted. Actual generated motion and final finishing remain later stages.
- Several Luma requests ended with generic HTTP 422 results. Separate PNG/JPEG and contact-board tests did not
  establish a cause or a lower reference-count limit. Existing requests were polled rather than silently resubmitted;
  request outcomes and conservative estimates are retained in the incident and budget records.
- The reel and media remain local and ignored by Git. Open `episodes/ep01/README.md` for the delivery links,
  rebuild commands, review limits and next-stage manifest. Production recipes and small audits are committed.
