# Episode playbook: blank page to finished reel

This is the evolving production playbook, informed by the pilot *CONTINUITY* and later work. Each stage lists
its tools, required inputs, QA checks, and observed failure modes. Where this document and memory disagree,
this document wins; update it when you learn something.

**Older episodes are historical examples, not gold standards.** Their results reflect the models, pipeline,
and constraints of their production dates. Preserve useful lessons and source material, but do not treat their
quality as a ceiling or copy their model choices, prompts, and workarounds by default. Judge a new episode
against its own goals and the current series taste and quality requirements.

**Re-evaluate technical defaults when planning a new production.** Model recommendations and failure reports
below record the evidence available when written; they are not permanent rankings. Check current primary
documentation for relevant capabilities and availability, and use a small representative comparison when
uncertainty would change the production choice. A newer model is not automatically better. Retain established
methods where the evidence still supports them, and record the reason and date when replacing a default.
This does not override budget approvals, paused services, privacy rules, or other explicit user constraints.
When restoring an old episode, preserve its original assets and setup for reproducibility; choose methods
for a new episode separately.

**Roles.** Claude is the director: every creative and technical call is Claude's to make and state. King is asked
only for what Claude can't do: **watch motion, listen to sound, spend money or provide keys and accounts**, and make
showrunner decisions about his own life or the release (privacy, platform). Never hand King a menu of artistic options.

**Default scope: stop before motion.** A run makes everything through stage 6 (a story reel with its final sound).
Stage 7 (motion) and 7b (the final finishing pass) start only when King gives the go-ahead after a cost estimate.

**Private projects:** anything made for King's family or that he marks private lives in `private/<project>/`. The
public repo ignores it, and it has its own local git repo that is never pushed. The shared tools are used from
`../../tools`.

---

## 0. Before starting
- **Read** `CLAUDE.md`, `README.md`, `docs/strategy.md`, `docs/history.md`, `bible/taste.md`, the series rules
  `bible/visual.md` and `bible/sound.md`, and this file. Other episodes' bibles (`episodes/pilot/bible/`) are
  worked examples, not rules: their choices belong to their films.
- **Budget:**
  - **fal:** images (Luma, about 0.3¢ each), music and SFX (about $4 per episode) and motion (MiniMax H3 Max, about
    $0.025/s, and its lip-sync, $0.05/s: roughly $5–15 per episode). The balance is shared by parallel sessions.
  - **Codex:** the default generative image editor, plus original-image uses in §2b; it draws on King's quota.
  - **ElevenLabs:** the Starter account (about 40,000 characters a month), which covers an episode's dialogue several
    times over.
  - Estimate before any batch, test one item first, and tell King the cost when it crosses about $10.
- **Keys** live only in `~/.zshenv`, which the home dotfiles repo ignores: `FAL_KEY`, `ELEVENLABS_API_KEY_STARTER`
  (everything that ships), and `ELEVENLABS_API_KEY` (an old free account for tests only; it has no commercial
  licence). Never put a key in a repo file.
- **Privacy:** the repo is public. King's candid views stay in the gitignored `bible/private/`, and every episode is
  fiction with no real people or named countries in conflict. Real brands may appear as background texture (King,
  2026-10-01), but never as the target of the film's satire or joke; keep those institutions unbranded.

## 1. Script and shot list (a headless writer session; effort per CLAUDE.md)
- **How:** a separate headless session in auto mode, with a deny-list for paid and publishing actions:
  `claude -p --permission-mode auto --disallowedTools "Bash(git push:*)" "Bash(codex:*)" "Bash(*imagegen*)" "Bash(*i2v.py*)" "Bash(*run_jobs.py*)" "Bash(*eleven.py*)" "Bash(*fal_run.py*)" < brief.md`.
  This command uses default effort. When King explicitly says he is away, add `--effort max` for writing, design,
  and checking sessions, following CLAUDE.md; omit the override while he is present or unspecified.
  Auto mode lets the session run `uv run` and `python3` to validate its own output and search the web. The earlier
  acceptEdits-plus-allowlist launch silently refused every interpreter: sessions couldn't validate JSON or check sources.
  Test auto mode on one short headless session before relying on it.
  Run it in the background and log to `work/logs/`.
- **Brief:** the pilot's writer brief is the template (it produced `episodes/pilot/*`). It must cover:
  - runtime of 3–5 minutes, shots of 2–10 s, 3 recurring faces or fewer;
  - every keyframe must work as an image-to-video start frame;
  - dialogue for lip-sync, one speaker per shot;
  - stillness designed as a strength (the "PPT" note);
  - fiction only;
  - the deliverables: `episode.md`, `script.md`, `shots/NN/shot.md`, lookdev prompts and a cue sheet.
- **Concept stage: go broad, grounded in evidence.**
  - Run 3 parallel concept sessions, each forced into a different shape, while a research subagent gathers
    virality evidence for the platform and audience, plus credible, sourced forecasts for the subject.
  - Then a judge compares the concepts against the research, picks or merges them, and writes
    `episode.md`.
  - **Taste filter:** every concept answers the questions in `bible/taste.md` §5, and the judge scores it with that
    rubric. A banned take from §3 at the core fails outright.
  - Breadth beats depth at the concept stage; afterwards use draft-and-critique.
- **Split big documents by chapter.** A full bilingual script for about 40 shots overran max's output limit 4 times
  in one session. Write it as `script/partN.md` sessions chained in order, each reading the earlier parts, then join
  them.
- **Draft, then critique.** Write each deliverable in its own session. Use default effort for both drafting and
  critique while King is present or his presence is unspecified; use max for both when he explicitly says he is away
  (see CLAUDE.md). Then run a short critic session on the finished file: attack the hook, find the generic beats, test the ending, and rewrite the weak
  parts. The critic sees the whole piece, which a single long max draft never does, and it avoids the long silent
  generations that drop connections.
- **Write incrementally.** Tell every long writing session to write its deliverables one piece per response
  (`episode.md` as soon as the concept is set, then the script, then shots in batches of about 8). One giant final
  response can be lost to a single dropped connection: the mom episode's writer lost 65 minutes to `ECONNRESET`.
  If it happens, resume with `claude -p --resume <session-id>` (the transcript filename) rather than starting over.
- **Expect** 45–90 minutes with long silent stretches, which are normal for long writing sessions.
  - **Monitor** the files and the session transcript under `~/.claude/projects/...`, not only the finish.
  - **Stuck** means 30 minutes with no transcript change.
- **QA:** a single subagent extracts a machine-readable image manifest (id, out, prompt, refs, alpha, deps, shots) and
  checks that every prompt matches its `shot.md` word for word.

### Pacing (King, 2026-09-30: "our first two films have constant pacing")
Both films measured as varied cut lengths (pilot median 6 s, range 2–35 s; mom film median 4 s, mostly 3–5 s), but they
felt like one tempo. Movement inside shots, narration cadence, sound density and intensity all stayed level.
- **Tempo map in the script:** write a section-by-section tempo map before any images. Include at least one deliberate
  acceleration, one hard stop, and one stretch of held stillness or silence.
- **Four dials:** set all four per section, not just cutting: cut length, movement inside the shot, sound and voice
  density, emotional intensity.
- **Contrast makes speed:** a burst only reads fast after stillness, and silence only lands after noise.
- **No constant dial, in any art aspect** (King, 2026-09-30): camera movement, palette, shot size, sound and
  performance all balance familiarity (a home register the audience learns), variety (sections differ) and surprise
  (a rare break the film has not taught us to expect). Use departures and surprises sparingly: overusing them is
  worse than constancy. Series rules: `bible/visual.md` §1 and §5.
- **Time as form:** slow motion, freezes, repetition or reversal can be the episode's formal invention (see
  `bible/taste.md` §2).
- **QA:** measure cut lengths from the render (`ffmpeg` `select='gt(scene,0.3)'`) and check them against the tempo map.

## 2. Visual bible and art direction (a writer session, then tests)
- **Bible:** a session writes the episode's own bible in `<episode>/bible/`, under the series rules in
  `bible/visual.md`: production design (the world as objects,
  with every screen as physical hardware), three distinct art directions each with a short style block for the image model (Luma by default, §2b),
  cinematography (whose eye, lens and height, composition, the camera's home register and moves, and how the
  series acting rule applies) and test-frame prompts.
- **Tests:** 2 frames per direction, 6 in all, with **no refs** (old refs pull the old look back). Pick one direction
  and state why.
- **Rules learned the hard way:**
  - **Codex drifts to semi-photoreal 3D** (when a stylised look uses Codex) unless the style block says so
    explicitly: matte ink, no reflections, no gradients, "avoid 3D render".
  - **Medium rule:** a character may differ in *technique*, not *medium*. Change the medium only if the change is
    fully committed, motivated, and either set up early or saved for a single earned revelation. The half-smooth Father
    failed; the engraved Father works.
  - **Screens are hardware,** never web UI: CRT phosphor, bitmap or teletext letterforms, flaps, needles, paper. Modern
    UI fonts are banned.
  - **Faces:** calm and underplayed in the stills too; emotion comes from staging and cutting (Kuleshov).

### Choose the animation method for the episode (2026-10-02)

Code, image generation and video models are alternative or complementary production methods. Choose by the
episode's visual direction and each shot's needs; no episode is required to use all of them. Limited animation
can be the finished visual language, not merely a temporary story reel or a compromise before video generation.

- **Code and reusable artwork:** consider pixel-art walk cycles, sprite poses, cutout rigs, replacement drawings,
  layered foreground/background movement, particles, procedural effects, and controlled Blender animation.
- **Image sequences:** a few consistent poses or photographs can convey an action with deliberate holds and cuts.
  Prefer reusing approved assets where appropriate; independently generated frames can drift in identity,
  proportions, clothing and texture, even when there are few frames.
- **Video models:** remain useful for complex naturalistic movement and performance when explicitly constructing
  the assets and motion would be impractical. H3 Max remains the default when choosing video generation (§7).
- **Frame rate alone is not the boundary:** code can render smooth high-frame-rate motion; low-frame-rate sequences
  still need good posing, timing, weight and continuity. Choose the method by what must move and how it should look.
- Record the method in the episode's visual bible and shot plans. Hybrid sequences should preserve the intended
  medium and continuity. Review the actual motion; a method's suitability does not establish a finished shot's quality.

The earlier local character-animation failures in `docs/history.md` remain evidence about those experiments,
not a blanket prohibition on authored character animation. This is an available direction for suitable episodes,
not a replacement default for every production. Existing production-scope and budget approvals still apply.

## 2b. Image technique: elegant, not "AI"
**Choose original generation and editing separately.** Use Luma Uni-1 Max
(`luma/agent/uni-1/v1/max`) as the default for original images, with the beauty-portrait exception below.
**Use Codex's built-in image generation as the default for generative edits**, including corrections,
reframing and derived poses/views (King, approved 2026-10-02). This is an adopted workflow preference,
not a claim that Codex always preserves quality better. Apply the general editing rules below.
The supporting evidence from the 2026-09-30 tests is in `docs/history.md`. Credible new evidence of a better fit
for original generation can warrant a small representative comparison under the reassessment guidance above;
Luma need not fail first. Keep Luma as the original-generation default unless the comparison supports changing it,
and record why.

For troubleshooting an original-generation shot assigned to Luma, make two honest Luma attempts with a rewritten
brief. If it still fails at something the shot needs, test a few alternatives on that shot and use the winner for it.
This does not require Luma attempts before a Codex edit. A shot-specific exception does not by itself establish
a new default or a general per-style routing rule.

**Approved beauty exception (2026-10-02):** when striking or idealized beauty is central to a character,
use Codex's built-in image generation for the base portrait when available and suitable, using the subscription
workflow first. If it is unavailable or cannot meet the brief, choose an appropriate alternative; there is no
fixed fallback model. This exception does not require two further Luma attempts. Use the approved base as an
identity reference for scene generation or editing, checking identity, makeup, age and skin texture on each result. The initial
reference test was promising, but consistency across multiple angles and scenes is not yet established.

**Non-face beauty preference (King, 2026-10-02):** keep Luma as the default for beautiful environments,
cityscapes, objects and other non-face subjects. After the city and futuristic-city comparisons, King preferred
Luma for non-face beauty despite the assistant favoring Codex's more polished results. Follow King's preference
for original generation; generative edits follow the Codex default. The Codex-first beauty exception above is
for base faces, not a general original-generation rule for anything described as beautiful.

### General image-editing rules (King, approved 2026-10-02)

1. **Separate generation from editing.** Retain the original-generation preferences above; use Codex by default
   for generative corrections, reframing and derived poses/views. Using images as references for a fresh composition
   does not by itself make that composition an edit. Changing an existing image follows the editing policy.
2. **Start from a clean, approved source.** For each revision, select the clean source best suited to the change,
   rather than automatically using the latest attempt. It need not be the earliest image if a later approved
   version contains a necessary pose, composition or intentional design change.
3. **Keep edit chains short.** Combine compatible changes when practical. A further edit of an edited image is
   acceptable when its existing improvements matter and its quality remains intact. No fixed number of edits
   guarantees quality.
4. **Preserve authoritative references.** Retain approved character, costume and location references throughout.
   An edited shot must not silently replace them. Record intentional updates to the approved design.
5. **Review preservation as carefully as the requested change.** Inspect the whole output at full size against
   its input and the clean approved source: faces, texture, sharpness, colour, lighting and geometry. Compare
   neighboring shots for continuity, including after a cross-model edit. A corrected detail does not excuse
   degradation elsewhere.
6. **Reject degradation instead of repeatedly repairing it.** If an edit introduces harsh texture, identity drift
   or damaged geometry, return to a clean source or regenerate; do not build further work on the damaged result.
7. **Use ordinary editing tools for exact operations.** Cropping, resizing and typography generally do not need
   generative repainting. Preserve source pixels wherever practical. Retain originals, version history and the
   actual input/output relationships; distinguish a serial edit from an independent retry using the same source.

These rules govern future work generally; adopting them does not authorize regenerating existing episodes.

### Prompts, faces and references

- **Prompts are short photographer's briefs**, not prop lists:
  - where the camera stands and which lens;
  - the one thing the eye lands on first, set apart by position, scale and light (use blur only when the shot calls
    for it);
  - one named light source;
  - the setting and each person's ethnicity, stated explicitly.

  Complexity is fine when it has a hierarchy. Don't pile on texture words (grain, pores, worn), and avoid words a model
  can take literally as an object ("snapshot", "print").
- **Characters and faces: one method.**
  - **Look:** average, never scary (King, 2026-09-30). Ordinary, unglamorous faces are right, but no deep creases,
    heavy spots or blotches, weathered or gaunt skin, or faces that read older than written, unless a shot calls for
    it on purpose. Write each character as "looks her age, with a clear, even complexion". Never write texture or
    ageing details ("deep laugh lines", "age spots", "sunken temples").
  - **One scene-generation model per character within a sequence;** cutting between models can read as the face
    changing. A base portrait made with another model under the beauty exception is a reference, not a reason to
    alternate scene-generation models. The Codex editing default permits cross-model repairs, but each must pass
    the same sequence-level identity and texture review; it does not guarantee that the face survives unchanged.
  - **Base portrait:** a Luma t2i head-and-shoulders on a plain wall, 16:9, and judged at 100% before anything is
    built on it. For beauty-focused characters, use the Codex-first exception above and judge the base the same way.
  - **Sheets** (three-quarter, profile, one expression) use Codex edits of the approved base by default, used to
    check the character and as extra references for younger faces. Derive variants from the clean base rather
    than chaining the sheet views together.
  - **Why the base matters:** earlier Luma edit chains increased skin texture into crepey, spotted faces. This is
    observed failure evidence, not a claim that every edit does so or that Codex cannot drift.
  - **Keyframes:** use the selected original-generation model for a new composition and the default editor for
    changes derived from an existing image. Supply the approved base plus sheets for young faces, or **the base
    only as the face reference for older faces**. Add shared location and recurring-prop references separately (§3);
    describe the shot within that established space rather than asking for an independently invented setting.
    Every identity-preserving face edit ends with the skin lock: "Keep the exact age and clear, even skin from the
    reference: add no blemishes, spots, weathering or extra lines."
  - **An aged version** of a character (60 → 80) is a Luma **t2i** with the younger base in
    `reference_image_urls` and the ageing described plainly ("soft and even for her age"), never an ageing edit.
    Only a small ageing done by edit (28 → 48, Codex by default) uses the ageing lock, "Age her only as described
    here, and keep a clear, even complexion", instead of the skin lock.
  - **Name the skin inside the character description, not only in the lock** (2026-10-01): "Her skin is smooth and
    clear, with an even tone and no freckles, moles or dark spots." Luma magnifies faint freckles in a base into heavy
    spots at close-up scale; the trailing lock and softer light alone didn't stop it, but this sentence did. Soft light
    on close-ups still helps. Edit and t2i+ref tested equal.
  - **Retake any face that drifts.** `tools/imagegen/luma_batch.py` runs a manifest; a generator script like
    `private/mom-future/v2c/work/make_images_json.py` can add the locks automatically.
- **Recurring props:** list the prop's reference image in `refs` on every shot that shows it, including character
  edits. Both Luma endpoints take `reference_image_urls` (t2i up to 9, edit up to 8).
- **Luma's queue sometimes hangs** a request IN_PROGRESS for 20+ minutes while fresh ones finish in about 2.
  After a 7-minute client timeout, `luma_batch.py` resumes the same logged request; it does not submit a replacement.
  Keep the log even if polling or downloading fails: a client timeout does not establish that generation failed.
- **Recover existing requests without another generation:** rerun
  `uv run tools/imagegen/luma_batch.py <images.json> --only <id>` or
  `uv run tools/video/h3_batch.py <motion.json> --only <id>` with the original `--root`, if supplied.
  H3 starts a fresh polling window on that same request; `--timeout` controls that window.
  For a standalone fal request, use
  `uv run tools/fal_run.py <endpoint> <original-payload.json> <original-out-prefix> --resume`.
  Do not use `--redo` for recovery. An ambiguous submission or legacy fal log without polling URLs needs manual
  request recovery; do not delete the log to force another POST. Record the service-provided status/response URLs
  and request ID in the existing log when recovered, clear `submission_pending` only after that recovery, then
  resume. If no request ID was returned, reconcile the request with the service before authorizing a replacement.
- **Judge honestly:**
  - look at full frames, never centre-cropped grids;
  - look at faces at 100% and at 1080p;
  - judge identity shot-to-shot in sequence, not against the reference.

  Would a good photographer have taken this frame? If not, rewrite the brief.
- **Finish:** `tools/imagegen/film_finish.py` evens out sheen and ties stills together. It can't rescue a bad frame.

## 3. Lookdev and keyframes
Original generation defaults to Luma, while generative editing defaults to Codex's built-in image tool (§2b).
`tools/imagegen/luma_batch.py <images.json> --jobs 8` runs Luma manifests (t2i or explicitly selected Luma edits,
in dependency order, resuming logged requests without automatic replacement). Existing Codex CLI helpers are
`tools/imagegen/gen.sh` for one image and `tools/imagegen/batch.py <manifest> --jobs 5` for many; check their
availability in the current environment. The historical Codex observations below apply when a shot uses Codex.
- **Order:**
  1. The master style frame alone, then judge it.
  2. The other lookdev: character sheets and locations.
  3. Judge the character sheets. The same person must appear in every view, and no face may read as a real person.
  4. All keyframes.
- **Shared location references:** before building shots that share a setting, establish an approved location frame
  (with additional views where needed) and record its asset ID in each relevant shot's image manifest `refs` and
  `deps`. Character references alone do not establish the room. Describe the camera position, people and action
  relative to the shared layout: doors, windows, counters, furniture and light sources. Different angles may reveal
  different parts of the space; they must remain spatially compatible. Record intentional setting or lighting changes
  in `shot.md` so review can distinguish them from drift.
- **Speed and quality:** about 1 minute per image at 5 in parallel. Identity holds well from the character sheets plus
  refs.
- **Known failures:**
  - **Cutout layers don't register with their keyframe.** Build mattes from the plate itself (GrabCut plus inpaint)
    instead of requesting cutouts.
  - **Generative edits can change unrequested regions.** For an isolated repair, preserve the original outside
    the edited region when registration, perspective and lighting permit a clean composite. Inspect the boundary,
    shadows and reflections; a pose, camera or lighting change may require a complete new frame.
  - **One image keeps failing with "network errors"** while others succeed: the prompt is usually too long (for
    example 4,900 characters). Cut it to about 3,000 by attaching the approved test frame as a composition reference.
  - **Codex flatters age.** "100 years old" rendered as about 78. Describe ageing through hair, posture, a narrower
    face and hands, and reference the previous age sheet, without scary skin detail (§2b).
  - **"Print" styles grow cream paper margins.** Frame past them in comp.
  - **Stray details,** such as a second mole: patch them locally with texture from the same hatching direction, sized
    to the defect. Verify at 4× zoom, then re-propagate to every consumer.
- **QA:** contact sheets read with the Read tool: identity, style consistency, framing inside the 2.39 band.
  Before motion generation, compare each scene's full starting frames together in edit order against its location
  reference. Check faces, clothing, room layout, background landmarks, props, lighting and people's positions across
  cuts. Fix incompatible frames before animating them and record the comparison in the episode review notes.
  An individually plausible frame, including one inherited from an earlier cut, is not proof of scene continuity.
- **Dance and crossings (First Day, 2026-10-02):** test the actual full-body dance composition and a source-to-destination
  crossing before batching their variants. Several location references can collapse separate floors into one plausible
  set. Require both platform outlines, the bridge and visible water/gap in the approved geography plate; derive later
  dock states from that plate. Leave deliberate floor beneath complete shoes for movement and subtitles. A landing
  still from another camera position is a QA reference, not automatically valid end-frame conditioning for a locked
  crossing shot. Inspect the final motion for complete traversal, contact and release; a beautiful still proves none
  of those actions. When a targeted repair replaces an input, retain its original bytes and exact recipe/hash provenance.

## 4. Screens and graphics (JS)
- **Tool:** `tools/web/render.mjs <page> <out.mp4|.mov> <seconds> 24`. Each page exposes `window.renderFrame(t)` and
  is deterministic.
- **Kit:** use a shared kit per episode (glyph tables, CRT pass, emblem), as in `episodes/pilot/js_v3/kit.js`.
- **Outputs:** full-frame pictures, overlays (.mov with alpha), or screen textures for homography into keyframes.
- **QA:** stills at key beats, read with Read. The text must be exact.
- **Prepare object graphics before motion:** render or correct lettering, clock faces and hands, display states,
  symbols and other graphics attached to a prop or in-world surface, then
  composite it into the approved image-to-video start frame with the intended perspective, lighting and occlusion.
  Check spelling, readings, geometry and readability before submitting that frame. Keep the clean plate and editable graphics as source
  assets. Subtitles, titles and screen-space narrative captions stay separate for post-production. See §7 for motion QA.

## 5. Compositing the stills reel
- **Tools:**
  - `tools/comp/reel.py` renders a shot from a JSON spec: camera, parallax, particles, light and grade.
  - Masked or time-varying effects are baked by per-shot prep scripts.
  - `tools/comp/assemble.py` conforms the cut and burns in subtitles.
- **Split:** three compositor subagents with a shared brief (`episodes/pilot/build/v3/comp_v3_brief.md` is the
  template), each owning a shot range. Only one agent may edit a shared tool.
- **Rules:**
  - Use only the camera moves the bible permits.
  - Broadcast shots are 4:3 pillarboxed; the world is 2.39 letterbox.
  - Frame counts must match the timeline exactly.
- **QA:** a mid-frame contact sheet of every shot, checked for grade continuity across the compositors' ranges.
- **Conform overlays with ffmpeg,** never `reel.py`: it always re-applies its highlight roll-off and gamma, so
  finished shots passed through it again lose about 13 % of their highlights. Use `overlay` with `eof_action=pass`.
- **Chinese subtitles:** `assemble.py` takes `"font": [PingFang.ttc path, 7, 46]` (PingFang SC Medium lives under
  `/System/Library/AssetsV2/…/PingFang.ttc`). Chinese on line 1, English smaller on line 2.
- **Captions:** broadcast shots use in-world captions instead of burned subtitles, never both.

## 6. Sound (see `bible/sound.md`, `episodes/pilot/bible/sound.md` and `audio/pilot/*`)
**Sound plan:** a session writes the episode's sound bible (`<episode>/bible/sound.md`), `casting.md`, `dialogue.json`, `score.md` and
`score_cues.json`, `sfx.json` and `mix_plan.md`. Validate every JSON file with a real parser.

**Prompting principles (adopted by reasoning from the image work, 2026-09-30).** Genre and quality adjectives pull toward
the stock, polished result, the audio version of the AI look. So describe the real source instead:
- **Voice design:** describe a documentary subject, not a performance: age, hometown, body, habits, "an ordinary
  person, not a trained voice". Avoid "warm, expressive, emotional".
- **Accent:** always name it ("Mandarin with a light Sichuan accent, as spoken by someone from Chengdu"). An unnamed
  accent drifts between lines.
- **Dialogue text:** write for the mouth: short clauses, fillers (嗯, 那个), false starts, punctuation as timing.
  Literary, emotionally loaded lines get acted; plain lines get spoken.
- **Continuity:** pass the neighbouring lines as context (ElevenLabs request stitching, `previous_text`/`next_text`, if
  v4 supports it; check first) so a speech reads as one train of thought.
- **Music:** name the instruments, room and recording ("one upright piano with felt dampers in a small room, one close
  mic, the player hesitates between phrases"), not genre or mood ("cinematic, emotional, epic"). Fewer instruments
  is audio's negative space.
- **SFX:** name the source and where the mic is ("a steel wok on a gas flame, heard from across a small tiled
  kitchen"), not "realistic".
- **Judging:** King judges audio in the finished cut, not in isolated A/Bs. Fix what bothers him there.

**Voices** (ElevenLabs direct API, Starter key):
- **Design, don't pick stock:** `tools/audio/voice_design.py spec.json outdir --rounds 2 --save`. The descriptions come
  from `casting.md`.
- **Selection is by measurement,** because Claude can't listen:
  - the transcript must match;
  - then the flattest delivery wins (pitch spread, level spread);
  - for age, lower pitch and more jitter.
  - The stock voices had no genuinely old woman; the designed Nana sits at 155 Hz.
- **Perform:** `tools/audio/perform.py dialogue.json voices.json outdir --seeds 3` keeps the flattest correct take of
  each line.
  - **Anti over-acting:** behaviour tags only, such as `[pause]` and `[quietly]`, and higher stability for the living
    characters.
  - **Tags:** long descriptive tags make v4 loop or read the tag aloud, so use short standard ones.
- **Mandarin:** run the tools with `--lang zh`. The transcript check compares Han characters with digits and 幺
  normalised, and converts Whisper's traditional characters to simplified first (otherwise correct takes score as
  mismatches). A mumbled register can fail every seed on one misheard word; the selector then takes the best match
  first, and the subtitle carries the line.
- **Voice slots:** with a full account, run designed roles through one slot in turn: design and save, perform every
  take, delete the voice, move on. Record the design description and generated id in `voices.json` in case a retake
  is needed.
- **Child voices:** ElevenLabs refuses Voice Design for children (a safety policy; don't work around it). Cast a young
  adult woman with a small, light, high voice, described honestly as an adult.
- **Free-tier limits:** it can't design voices, use library voices or output 192 kbps. Everything that ships comes from
  the Starter account.

**Score** (fal):
- **Contenders:** ElevenLabs Music, which takes a `composition_plan` of timed sections and is the only model that
  follows written structure and length; Lyria 3.5 and 3 Pro, which ignore length; Sonilo video-to-music (upload with
  `tools/fal_upload.py`).
- **ElevenLabs Music gotcha:** don't send `force_instrumental` together with a `composition_plan` (the request fails
  with 422).
- **Screening:** by length, pitch-set fit and chroma key. Music models **won't hit exact notes**, so any motif the story
  depends on is played by a **sampler**: one clean note cut from the take's own instrument, resampled, with ±1.5 dB and
  ±15 ms humanising.

**SFX:**
- **Generate:** `tools/audio/eleven.py sfx`, which writes a float WAV (mp3 overshoot must never clip).
- **Screen:** flat-top runs at full scale for true clipping; near-silent files; stray speech. Whisper's "Thank you" on
  noise is a hallucination.
- **Better options:** real royalty-free libraries for physical ambience; video-to-audio foley such as Mirelo once motion
  exists.

**Mix:**
- **Build and render:** `tools/audio/build_pilot_mix.py` → `mix2.py` → `qa_mix.py`, with rooms built by `rooms.py`.
- **Dynamics over loudness:** the master lands around −18 LUFS, whatever keeps the limiter at or under 2 dB outside
  the plan's allowed moments, with LRA ≤ 16. Fix loud consonants with clip-gain edits, not limiting.
- **Subtitles:** time them from voiced onsets (voice-band energy plus periodicity), never from Whisper's start times,
  which run early. Match subtitles to lines by ID and time, never by text (lines repeat).

## 7. Motion (default MiniMax H3 Max; fal; needs King's go)
**Models** (tested 2026-10-01; evidence in `docs/history.md`):
- **Default for video-generated motion and lip-sync: MiniMax H3 Max** (King's call). Choose whether to use video
  generation under §2's animation-method guidance. One family keeps motion, skin and light consistent from
  shot to shot, and mixing models reads as drift.
  - **Motion:** `minimax/h3-max/image-to-video`, about $0.025/s. Start frame, optional end frame, 5–15 s, 480P, 768P
    or 1080P; `prompt_expansion_mode: "disabled"` keeps prompts literal.
  - **Speech:** `minimax/h3-max/lip-sync/image-to-video`, $0.05/s. Image plus our audio, no prompt.
  - **Camera moves:** `minimax/h3-max/camera-controls` (keyframed camera paths, scene frozen).
  - **Restaging a still that's wrong:** `minimax/h3-max/reference-to-video` (images, videos and audio as refs).
- **Fallback per shot only,** when H3 Max truly can't: Luma Ray 3.2 (`luma/agent/ray/v3.2/image-to-video`,
  $0.03/s, no audio, keyframes pinned anywhere in the clip), then a quick comparison on that one shot.
- **Seedance 2.5 refuses photoreal human stills** ("likenesses of real people"), even though every face is
  generated. Don't work around it. It stays an option only for stylised looks without photoreal faces.
- **Tools:** `tools/fal_run.py <endpoint> <payload.json> <out>` for one clip; it never re-POSTs and it saves the
  request id. There's no H3 Max batch tool yet: write one on the first full run, following
  `tools/imagegen/luma_batch.py`. `tools/video/i2v.py` and `run_jobs.py` are Seedance-only.

**Speech only ever comes from our audio** (King: models "invent dialogue out of thin air").
- **Pure dialogue shots:** lip-sync with our voice take.
- **Motion prompts never mention speech** ("says a line", "shouts"): with no audio to follow, the model invents the
  words. Describe the action only, plus "mouth closed, not speaking".
- **Shots with both action and a line:** first test `target_audio_url` on the normal H3 Max model (it may give
  directable action plus lip-sync together). Otherwise split the line (lip-sync) from the action (H3 Max) in the edit.
- **Bound conditioning audio before padding:** trim to the intended line/shot with an explicit audio trim, reset
  timestamps, then pad with silence. Verify the padded tail; repeated ffmpeg output `-t` options do not perform two
  successive trims and can include the next shot's speech. Keep submitted input files for provenance.
- **Discard every audio track a video model returns;** the mix is always ours (§6, §7b).
- **Silent fake-talking:** a model can animate talking with no audio at all. QA every non-dialogue clip with a
  face-landmark mouth check (flag speech-like open and close rhythm), and retake or trim what's flagged.

**What to fix before motion, and what after.**
- **Before:** fix the visible face, setting and composition, and finish graphics that should already exist on objects
  in the start frame (§4), plus the edit (shot lengths and order). Flaws the shot's own action resolves (a hand that lifts, a
  book that opens) can be left to the motion, or trimmed off the clip's head.
- **After (§7b):** screen-space graphics, any necessary object-graphic repairs or deliberately timed display changes, the sound pass and
  every other polish. Do not automatically reapply graphics already present in the generated plate.

**Strategy.**
- **Triage shots by what the motion is for:**
  - **A, story beats carried by acting:** image-to-video with an end frame pinning the pose the beat must land on
    (make it using §2b's generation/editing defaults), a behaviour-only prompt, 2–3 takes, and a real performance clip from King as a
    reference where he can give one. Complex beats are split at the pose: start → the pose, then the pose → the end.
  - **B, dialogue:** lip-sync (above).
  - **C, action and places:** image-to-video with a plain behaviour prompt, 1–2 takes.
  - **D, stillness sections:** near-still takes (breathing, light, steam). Never frozen frames between moving shots,
    which read as a glitch or "PPT"; stillness comes from the content, not a freeze.
- **Image-to-video from the approved still is the default;** reference mode only to restage a still that's wrong.
- **Group short shots:** consecutive shots of one scene go in one continuous take (5–15 s) and are cut in the edit.
  Chain takes for continuity: the last frame of one clip starts the next.
- **Acting:** prompts describe behaviour, never emotion (see the series visual rules); faces underplay.
- **Story-critical actions must survive generation and the edit:** model output varies; a clear submitted prompt is
  direction, not evidence that the action happened. For each essential beat, record in `shot.md` the visible action,
  any required repetition, and its relation to dialogue or another event. Give that action priority in the prompt;
  remove conflicting restraint instructions when the beat requires an emphatic gesture.
  - **Check the full take:** inspect the actual submitted request, then locate the action's onset and completion in
    the output. Record take timestamps and whether the required action, count and order are present. Sample brief
    gestures densely enough to see their phases; sparse contact sheets and mouth-sync metrics alone cannot verify
    them. Mark uncertain motion for King's playback review rather than claiming a pass.
  - **Choose from the observed performance:** if the action is usable but late, adjust the cut or shot length while
    preserving dialogue sync, continuity and pacing. If it is missing, wrong, or cannot fit the scene, revise the
    direction or regenerate within the approved budget. Do not keep an incomplete beat just to match the planned
    duration, and do not assume a longer or more detailed prompt alone will fix it.
  - **Check the final cut separately:** verify the action remains visible after trimming, retiming and assembly,
    with enough time for the audience to read it and with the intended relation to the dialogue. A good source take
    does not establish that the edited shot works.
- **Graphics attached to objects — default adopted 2026-10-01:** supply correct lettering, clock faces and hands,
  display states, symbols and other object details in the approved start frame, then let the video model animate
  the complete object. Where the endpoint accepts a prompt, describe these details as already present and ask to
  preserve them through motion, lighting and occlusion. Specify any required change separately.
  - King's playback review preferred supplied lettering to the tested post-generation tracked overlay, whose text
    jiggled. Later clock overlays also looked bad: this failure is not specific to text. Generalizing the start-frame
    approach to other graphics is the production policy; it is not yet a demonstrated clock-generation result.
  - A blank surface plus a prompt to add lettering made text appear during the shot; do not use that approach for
    lettering that must exist from the beginning. Text-only scene generation also gives up the supplied faces,
    setting and composition, so it is not a substitute for image-to-video when continuity matters.
  - Check exact characters, clock/display readings, attachment, occlusion and legibility throughout the intended cut;
    review playback for jiggle, slipping edges, pop-in and changes in appearance. One successful shot does not
    guarantee reliable spelling or preservation on every surface, duration or model.
  - If preservation fails, repair the start frame and retake, or reframe/re-edit when the story permits. Tracking is
    an exceptional repair, never the default finishing pass; accept it only after playback review confirms attachment.
    Tracking confidence, smooth coordinates and still frames cannot establish that it looks natural.
  - Exact clock movement and changing displays need explicit state/timing checks. If the model cannot preserve a
    story-critical reading or transition, use a controlled insert or separately designed shot. Do not hide an incorrect
    reading under another unverified moving patch. Keep subtitles and narrative captions in screen space.
- **A stills-reel clip is a poor video reference:** it carries framing, which the still already gives, and stillness.
  Video references are for real performance or camera motion.
- **Test first on every new episode or model:** the key beat, one dialogue shot and one action shot, at a low
  resolution, and settle open questions (for H3 Max: `target_audio_url`, prompt expansion on or off, 768P against
  1080P) before the full batch.
- **Measure returned footage, not just requested seconds.** In the 2026-10-02 First Day test, H3 Max returned
  175 frames for a 7-second request and 243 frames for a 10-second request, both at 24 fps. Use actual decoded
  frame counts when assembling previews and selecting action; these two observations are not a fixed padding rule.
- **Review:** Claude screens every clip's frames (identity, hands, ageing, props, mouths) and retakes; King watches one
  assembled motion cut.
  For each new or regenerated take, compare the intended cut with its supplied frame, the scene's location reference
  and neighboring shots. Inspect background landmarks through the cut, including areas revealed by camera movement;
  a "locked camera" or preservation prompt is not evidence of compliance. Record mismatches and resolve them before
  accepting the replacement. Preserving an inconsistent input faithfully still fails scene continuity.
- **Money safety:** `fal_run.py` saves the request id at submit and never re-submits. Stranded results can be
  recovered through `GET https://api.fal.ai/v1/models/requests/by-endpoint?endpoint_id=…` and then
  `https://queue.fal.run/<app>/requests/<id>`.

## 7b. Final finishing pass (after motion; every episode)
Every stage can introduce flaws (stills, graphics, voices, video models), so the last stage fixes anything from any of
them, on the assembled film, in this order:
1. **Re-edit to the real motion:** re-set cut points from what actually happens in each clip, not from the stills
   plan. Use the recorded story-action timestamps (§7) to preserve each essential beat from setup through completion;
   recheck dialogue sync and pacing when extending or retiming a shot.
2. **Repair or replace:** trim around artefacts, paint out small glitches, retake what can't be hidden. Run the face
   check and the landmark mouth check on every clip.
3. **Unify the look:** film finish and grade over all the video, so takes and models sit together.
4. **Finish the graphics:** audit all graphics attached to objects, including inherited overlays from earlier cuts.
   Check their appearance, readings, timing and attachment. Apply §7's repair/retake policy to failures; do not
   automatically track remaining graphics onto generated footage. Add screen-space graphics separately.
5. **Sync:** dialogue to the lip-synced mouths, and hits to the stamps and actions.
6. **Final mix:** fix cut-off and clipped lines; balance voice, music, SFX and any usable model motion sound.
7. **Re-time the subtitles** from the final voice onsets.
8. **QA the whole film:** cut lengths against the tempo map, loudness, the silence, faces, text, mouths, and every
   story-critical action in the final rendered cut. Confirm action, required repetition, order and relation to dialogue;
   compare neighboring shots for compatible setting, background layout, lighting, faces, clothing and prop placement
   after all crops, trims and replacements. Check against the intentional changes recorded in `shot.md`;
   unresolved playback checks remain explicit for King's review.
9. **King's review, then one fix loop** on what he flags.

## 8. Operating rules (learned on the pilot)
- **Watch long jobs yourself.** Check output timestamps and running processes; King shouldn't have to ask "is anything
  stuck?".
- **Waiting on jobs:**
  - Never `pgrep -f <name>` when `<name>` appears in the waiting loop itself; wait on a PID or an output file. To find
    a session's PID, anchor on the binary's path: `pgrep -f '^/Users/kingh0730/.local/bin/claude -p'`
    (a monitor's own `bash -c ...` line can't match `^`). This bit three times on the mom episode.
  - Success is "the deliverable exists", never "the output log is non-empty" (a crash writes its error there).
  - Session transcripts are filed by working directory: a `claude -p` started in `private/<p>/` writes to
    `~/.claude/projects/-Users-kingh0730-repos-interregnum-private-<p>/`, not the repo's folder. Watch the right one.
  - Long writing sessions can loop on "Output token limit hit" and drop on proxy idle timeouts
    (`ECONNRESET`). Prefer one deliverable per session; if a session hits the output limit repeatedly with
    no file written, stop it and split the work.
  - Monitor scripts run under `bash -c` with `shopt -s nullglob` (zsh aborts on empty globs).
  - `find` here is `bfs` and rejects relative `-newermt`; use `stat -f %m`.
  - Under `nullglob`, never pass a glob to `ls`: an empty match makes it list the current directory. Count matches
    with a bash array instead: `d=(shots/*/); ${#d[@]}`.
- **Tool gotchas:**
  - Never give a payload file the same name as the runner's log (`<prefix>.json`); `tools/fal_run.py` now refuses it.
    Pass long payloads as files, not inline arguments.
  - Never POST to a paid API just to "check" an error; read the error via the status or response URL.
- **Scope and cleanup:**
  - Subagents own disjoint files. If one overwrites another's, tell the owner at once.
  - Delete intermediates when a shot is final; keep recipes (JSON and py) in `episodes/<ep>/build/` and commit them.
    Never commit media.
- **Honesty:** Claude judges stills and metrics only. Always tell King what needs his eyes or ears, and never claim a
  clip "works" from metrics alone.
