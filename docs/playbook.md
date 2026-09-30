# Episode playbook: blank page to finished reel

This is how the pilot *CONTINUITY* was made. Follow it for every episode. Each stage lists its tool, the brief or
input it needs, the QA check that proves it worked, and its known failure modes. Where this document and memory
disagree, this document wins; update it when you learn something.

**Roles.** Claude is the director: every creative and technical call is Claude's to make and state. King is asked
only for what Claude can't do: **watch motion, listen to sound, spend money or provide keys and accounts**, and make
showrunner decisions about his own life or the release (privacy, platform). Never hand King a menu of artistic options.

**Default scope: stop before Seedance.** A run makes everything through stage 6 (a story reel with its final sound).
Stage 7 (Seedance) is the expensive step: start it only when King gives the go-ahead after a cost estimate.

**Private projects:** anything made for King's family or that he marks private lives in `private/<project>/`. The
public repo ignores it, and it has its own local git repo that is never pushed. The shared tools are used from
`../../tools`.

---

## 0. Before starting
- **Read** `CLAUDE.md`, `README.md`, `docs/strategy.md`, `docs/history.md`, `bible/taste.md`, the series rules
  `bible/visual.md` and `bible/sound.md`, and this file. Other episodes' bibles (`episodes/pilot/bible/`) are
  worked examples, not rules: their choices belong to their films.
- **Budget:**
  - **Codex:** about 45 images per episode; this draws on King's quota.
  - **fal:** Seedance is about $0.47 per second at 720p and is the expensive stage; the audio models together cost
    about $4 per episode.
  - **ElevenLabs:** the Starter account (about 40,000 characters a month), which covers an episode's dialogue several
    times over.
  - Estimate before any batch, test one item first, and tell King the cost when it crosses about $10.
- **Keys** live only in `~/.zshenv`, which the home dotfiles repo ignores: `FAL_KEY`, `ELEVENLABS_API_KEY_STARTER`
  (everything that ships), and `ELEVENLABS_API_KEY` (an old free account for tests only; it has no commercial
  licence). Never put a key in a repo file.
- **Privacy:** the repo is public. King's candid views stay in the gitignored `bible/private/`, and every episode is
  fiction with no real people, brands or countries.

## 1. Script and shot list (a headless writer session; effort per CLAUDE.md)
- **How:** a separate headless session in auto mode, with a deny-list for paid and publishing actions:
  `claude -p --permission-mode auto --disallowedTools "Bash(git push:*)" "Bash(codex:*)" "Bash(*imagegen*)" "Bash(*i2v.py*)" "Bash(*run_jobs.py*)" "Bash(*eleven.py*)" "Bash(*fal_run.py*)" < brief.md`.
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
- **Draft, then critique.** Write each deliverable in its own session (default effort). Then run a short
  critic session (max effort only when King is away; see CLAUDE.md) on the finished file: attack the hook, find the generic beats, test the ending, and rewrite the weak
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
  with every screen as physical hardware), three distinct art directions each with a 130–170-word Codex style block,
  cinematography (whose eye, lens and height, composition, the camera's home register and moves, and how the
  series acting rule applies) and test-frame prompts.
- **Tests:** 2 frames per direction, 6 in all, with **no refs** (old refs pull the old look back). Pick one direction
  and state why.
- **Rules learned the hard way:**
  - **Codex drifts to semi-photoreal 3D** unless the style block says so explicitly: matte ink, no reflections, no
    gradients, "avoid 3D render".
  - **Medium rule:** a character may differ in *technique*, not *medium*. Change the medium only if the change is
    fully committed, motivated, and either set up early or saved for a single earned revelation. The half-smooth Father
    failed; the engraved Father works.
  - **Screens are hardware,** never web UI: CRT phosphor, bitmap or teletext letterforms, flaps, needles, paper. Modern
    UI fonts are banned.
  - **Faces:** calm and underplayed in the stills too; emotion comes from staging and cutting (Kuleshov).

## 2b. Image technique: elegant, not "AI"
**Use Luma Uni-1 max (`luma/agent/uni-1/v1/max`, edit at `/max/edit`) for every image unless Luma truly can't do a
shot.** "Truly can't" means that after two honest attempts with a rewritten brief, it still fails at something the shot
needs. Only then test a few other models on that one shot and use the winner for it. Don't carry per-style routing rules
forward; the evidence from the 2026-09-30 tests is in `docs/history.md`.

- **Prompts are short photographer's briefs**, not prop lists:
  - where the camera stands and which lens;
  - the one thing the eye lands on first, set apart by position, scale and light (use blur only when the shot calls
    for it);
  - one named light source;
  - the setting and each person's ethnicity, stated explicitly.

  Complexity is fine when it has a hierarchy. Don't pile on texture words (grain, pores, worn), and avoid words a model
  can take literally as an object ("snapshot", "print").
- **Characters:** one model per character within a sequence; cutting between models reads as the face changing. With
  Luma:
  - give it a Luma-made reference sheet (front, three-quarter, profile, one expression) in `reference_image_urls`;
  - pad the base reference image to 16:9 as `image_url` (Luma edit's output follows the base image's shape);
  - put the scene in the prompt.
- **Recurring props:** list the prop's reference image in `refs` on every shot that shows it, including character
  edits. Both Luma endpoints take `reference_image_urls` (t2i up to 9, edit up to 8).
- **Faces: average, never scary** (King, 2026-09-30). Ordinary, unglamorous, average-looking faces are right; most
  people aren't pretty. But no deep creases, heavy spots or blotches, weathered or gaunt skin, or faces that read
  older than written, unless a shot calls for it on purpose. Luma drifts this way, especially in edit sheets. So state
  each character's age as "looking their age" with a clear, even complexion, add an age-and-skin lock to every edit
  ("keep the exact age and clear, even skin from the reference: add no blemishes, spots, weathering or extra lines"),
  and retake any face that drifts.
- **Luma edit ages faces (v2c, 2026-10-01).** Each edit adds skin texture, so edits of edits (sheets, then keyframes
  from sheets) compound into crepey, spotted faces. So:
  - keyframes reference the base portrait, not the sheets, when faces are older;
  - make an aged version of a character (60 → 80) with t2i plus the younger base in `reference_image_urls`, not an
    ageing edit;
  - an ageing edit needs its own lock ("age her only as described"), since "keep the exact age" contradicts it.
- **Luma's queue sometimes hangs** a request IN_PROGRESS for 20+ minutes while fresh ones finish in about 2;
  `luma_batch.py` resubmits after 7 minutes.
- **Judge honestly:**
  - look at full frames, never centre-cropped grids;
  - look at faces at 100% and at 1080p;
  - judge identity shot-to-shot in sequence, not against the reference.

  Would a good photographer have taken this frame? If not, rewrite the brief.
- **Finish:** `tools/imagegen/film_finish.py` evens out sheen and ties stills together. It can't rescue a bad frame.

## 3. Lookdev and keyframes
The default model is Luma (§2b). The Codex notes below apply when a shot uses Codex.
- **Tools:** `tools/imagegen/gen.sh` for one image; `tools/imagegen/batch.py <manifest> --jobs 5` for many (it
  respects dependencies and retries safety false positives neutrally).
- **Order:**
  1. The master style frame alone, then judge it.
  2. The other lookdev: character sheets and locations.
  3. Judge the character sheets. The same person must appear in every view, and no face may read as a real person.
  4. All keyframes.
- **Speed and quality:** about 1 minute per image at 5 in parallel. Identity holds well from the character sheets plus
  refs.
- **Known failures:**
  - **Cutout layers don't register with their keyframe.** Build mattes from the plate itself (GrabCut plus inpaint)
    instead of requesting cutouts.
  - **Edits of a keyframe re-render everything.** Paste back only the edited region, with a feathered mask.
  - **One image keeps failing with "network errors"** while others succeed: the prompt is usually too long (for
    example 4,900 characters). Cut it to about 3,000 by attaching the approved test frame as a composition reference.
  - **Codex flatters age.** "100 years old" rendered as about 78. Describe ageing physically (hair density and scalp,
    skin laxity and spots, sunken temples, hooded eyes, a narrower face, hands) and reference the previous age sheet.
  - **"Print" styles grow cream paper margins.** Frame past them in comp.
  - **Stray details,** such as a second mole: patch them locally with texture from the same hatching direction, sized
    to the defect. Verify at 4× zoom, then re-propagate to every consumer.
- **QA:** contact sheets read with the Read tool: identity, style consistency, framing inside the 2.39 band.

## 4. Screens and graphics (JS)
- **Tool:** `tools/web/render.mjs <page> <out.mp4|.mov> <seconds> 24`. Each page exposes `window.renderFrame(t)` and
  is deterministic.
- **Kit:** use a shared kit per episode (glyph tables, CRT pass, emblem), as in `episodes/pilot/js_v3/kit.js`.
- **Outputs:** full-frame pictures, overlays (.mov with alpha), or screen textures for homography into keyframes.
- **QA:** stills at key beats, read with Read. The text must be exact.

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

## 7. Motion: Seedance 2.5 (fal; needs budget)
**What to fix before Seedance, and what after** (King, 2026-10-01). Seedance animates the start frame and nothing else.
- **Before:** only what the viewer will see and Seedance won't change by itself (a wrong face, a wrong setting or
  composition), plus the edit (shot lengths and order; seconds are billed). Flaws the shot's own action resolves (a
  hand that lifts, a book that opens) can be left to Seedance. Three ways to use its freedom:
  - image-to-video locks frame 0 but changes things through motion;
  - reference-to-video treats images as references and can restage the shot (more drift from our framing; test it
    first);
  - trimming the clip's head hides a bad opening, at the cost of paid seconds.
- **After:**
  - **Graphics:** overlays must be re-tracked to the moving plates anyway; that pass is where alignment and motion
    design are brought up to film level.
  - **Sound:** the final pass (clipped onsets, cut-offs, timing), since motion and lip-sync shift the timing.
- **Default video model: MiniMax H3 Max, for everything** (King, 2026-10-01): `minimax/h3-max/image-to-video` for
  motion (start and end frame; about $0.025/s) and `minimax/h3-max/lip-sync/image-to-video` for every spoken line (our
  voice take; $0.05/s). One family keeps motion, skin and light consistent from shot to shot; mixing models reads as
  drift. Switch per shot (Luma Ray 3.2 first) only when H3 Max truly can't do it. Discard its audio track.
- **Video-model test (2026-10-01, v2c):**
  - **Seedance 2.5 refuses photoreal human stills** ("may contain likenesses of real people"; partner validation),
    even though every face is AI-generated. Don't work around it. Seedance is out for photoreal people.
  - Luma Ray 3.2 ($0.03/s, no audio, keyframe pinning) and MiniMax H3 Max ($0.025/s) accept them. MiniMax H3 Max
    lip-sync ($0.05/s) takes only an image and our audio, with no prompt.
  - **Speech only ever comes from our audio** (King: models "invent dialogue out of thin air"):
    - pure dialogue shots use MiniMax lip-sync;
    - action shots use Ray, with "mouth closed, not speaking" in the prompt. Having no audio doesn't stop a model
      from animating silent talking, so pin closed-mouth keyframes where possible, and QA every non-dialogue clip
      with a face-landmark mouth check (flag speech-like open/close rhythm); retake or trim what's flagged;
    - shots with both action and a line are split: lip-sync on the line, cut to Ray for the action.
    - **Motion prompts never mention speech** ("says a line", "shouts"): with no audio to follow, the model invents
      the words (MiniMax did on shot 27). Describe the action only, plus "mouth closed, not speaking".
    - **Discard any audio a video model returns** (MiniMax H3 Max adds its own track); the mix is always ours.
  - The tiered strategy below was written for Seedance; apply its tiers with these models.
- **Strategy (reasoned 2026-10-01):**
  - **Triage shots by what the motion is for:**
    - **A, story beats** carried by acting: i2v, plus a real performance clip where King can give one, plus a
      behaviour-only prompt; 2–3 takes.
    - **B, on-screen dialogue:** i2v with the voice take as ref audio for lip-sync.
    - **C, action and places:** i2v with a plain behaviour prompt; keep Seedance's motion sound as a stem.
    - **D, stillness sections:** cheap near-still takes (breathing, light, steam), never frozen frames between
      moving shots, which read as a glitch or "PPT". Stillness comes from the content, not a freeze.
  - **i2v is the default** (frame 0 is the approved still); reference mode only to restage a still that's wrong.
  - **Pin key beats with an end frame:** i2v takes `end_image_url`. Make the pose the beat must land on as a Luma still
    (the hand over the mouth), or match the next shot's start frame for continuity.
  - **Facts (fal schema, 2026-10-01):**
    - clip length 4–30 s, or auto;
    - 480p, 720p or 1080p (test motion at 480p);
    - generate_audio on or off;
    - ref mode takes up to 10 images, videos and audio, named `@Image1`, `@Video1`, `@Audio1` in the prompt (fix
      i2v.py's `[Image1]` wording before using it).
  - **A stills-reel clip is a poor video reference:** it carries framing, which the still already gives, and
    stillness. Video refs are for real performance or camera motion.
  - **Text and graphics never go into Seedance.** Composite them afterwards, tracked to the motion.
  - **Group short shots:** consecutive shots of one scene go in one continuous take, cut in the edit. Check
    Seedance's minimum clip length and multi-shot support first; paying for 5 s to use 1.5 s wastes most of it.
  - **Review:** Claude screens every clip's frames (identity, hands, ageing, props) and retakes; King watches one
    assembled motion cut.
  - **Test first:** the key beat, one lip-sync shot and one action shot, plus a control take of the key beat with
    the stills-reel reference. That measures real cost with refs and tests the assumptions. If the key beat fails,
    compare other fal video models on that one shot before more retakes (Seedance is the default, not dogma).
- **Seedance's job:** the action a still can't show, not polish. It also has two sound jobs:
  - **on-screen dialogue:** our ElevenLabs take goes in as `--ref-audio`, and Seedance lip-syncs the performance to it;
  - **motion sound** (splashes, steps, slams): keep its audio as a stem, and use it when it syncs better than the
    library sound.

  Music, ambience and the final mix stay ours.

- **Tools:** `tools/video/i2v.py` for one take; `tools/video/run_jobs.py jobs.json outdir` for many. Take the job list
  format and voice bible from `episodes/pilot/v2_jobs.json`.
- **Acting:** motion prompts describe behaviour, not emotion (see the cinematography bible). Performance-reference
  video (reference-to-video `video_urls`) is the strongest lever: ask King for short phone clips of underplayed beats.
- **Consistency:** voice consistency comes from generating each character's off-screen lines in the same take as their
  on-screen ones. Once the designed voices exist, prefer audio-driven lip-sync or the voice changer, so the cast voices
  stay.
- **Continuity:** generate a scene's consecutive broadcast or dialogue shots as **one continuous take** and cut it, to
  avoid pose jumps at the cuts.
- **Audio:** non-dialogue shots use `--no-audio`.
- **Money safety:** `i2v.py` saves the request id at submit, and polls retry without ever re-submitting. Stranded
  results can be recovered through `GET https://api.fal.ai/v1/models/requests/by-endpoint?endpoint_id=…` and then
  `https://queue.fal.run/<app>/requests/<id>`.

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
