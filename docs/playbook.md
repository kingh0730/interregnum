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
- **Read** `CLAUDE.md`, `README.md`, `docs/strategy.md`, `docs/history.md`, `bible/visual/*`, `bible/sound/*` and this
  file.
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

## 1. Script and shot list (a max-effort writer session)
- **How:** a separate headless session in auto mode, with a deny-list for paid and publishing actions:
  `claude -p --effort max --permission-mode auto --disallowedTools "Bash(git push:*)" "Bash(codex:*)" "Bash(*imagegen*)" "Bash(*i2v.py*)" "Bash(*run_jobs.py*)" "Bash(*eleven.py*)" "Bash(*fal_run.py*)" < brief.md`.
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
  - Run 3 parallel concept sessions (xhigh), each forced into a different shape, while a research subagent gathers
    virality evidence for the platform and audience, plus credible, sourced forecasts for the subject.
  - Then a max-effort judge compares the concepts against the research, picks or merges them, and writes
    `episode.md`.
  - Breadth beats depth at the concept stage; afterwards use draft-and-critique.
- **Split big documents by chapter.** A full bilingual script for about 40 shots overran max's output limit 4 times
  in one session. Write it as `script/partN.md` sessions chained in order, each reading the earlier parts, then join
  them.
- **Draft at xhigh, critique at max.** Write each deliverable in its own xhigh session. Then run a short max-effort
  critic session on the finished file: attack the hook, find the generic beats, test the ending, and rewrite the weak
  parts. The critic sees the whole piece, which a single long max draft never does, and it avoids the long silent
  generations that drop connections.
- **Write incrementally.** Tell every long max-effort session to write its deliverables one piece per response
  (`episode.md` as soon as the concept is set, then the script, then shots in batches of about 8). One giant final
  response can be lost to a single dropped connection: the mom episode's writer lost 65 minutes to `ECONNRESET`.
  If it happens, resume with `claude -p --resume <session-id>` (the transcript filename) rather than starting over.
- **Expect** 45–90 minutes with long silent stretches, which are normal for max effort.
  - **Monitor** the files and the session transcript under `~/.claude/projects/...`, not only the finish.
  - **Stuck** means 30 minutes with no transcript change.
- **QA:** a single subagent extracts a machine-readable image manifest (id, out, prompt, refs, alpha, deps, shots) and
  checks that every prompt matches its `shot.md` word for word.

## 2. Visual bible and art direction (max effort, then tests)
- **Bible:** a max-effort session writes `bible/visual/` for the episode: production design (the world as objects,
  with every screen as physical hardware), three distinct art directions each with a 130–170-word Codex style block,
  cinematography (lens and height, composition, the permitted camera moves, and the acting rule) and test-frame
  prompts.
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

## 2b. Image technique: elegant, not "AI" (tests of 2026-09-30, `work/imgtest*`)
King's note on episodes 1–2: frames looked "oily", "crowded" and "very AI-generated, not elegant". A/B tests over 3 scenes
× 3 prompt styles × 6 models, plus identity and finishing tests, found:
- **The prompt matters most.** A prop list ("twelve tables, a clock, a vending machine, towels...") gives a crowded
  stock-photo frame on every model. Write a **photographer's brief** instead:
  - where the camera stands (height, lens);
  - one sharp subject that the eye lands on first;
  - everything else soft, partial or small: backs, shoulders, hands at the edge;
  - one named light source, with areas left to fall into dark;
  - empty space ("plenty of calm floor");
  - "colour film photograph, candid, unposed".

  Complexity is fine when it has a hierarchy ("the table is full but the frame is not busy").
- **Keep the brief short and don't pile on texture words.** Grain, pores, worn and lived-in make the surface oily. A
  one-line guard helps a little: "ordinary people with matte skin and uneven features; nothing glossy, polished or
  symmetrical; no HDR, no over-sharpening". Never write a paragraph of them.
- **State each person's ethnicity and setting.** Seedream made a Chinese metro passenger Western; FLUX.2 edit moved a
  Chengdu woman to an American suburb in a denim jacket.
- **Model routing for photoreal work (fal):**

  | Job | Model | Why |
  |---|---|---|
  | Settings, hero and establishing frames | Luma Uni-1 max; FLUX.2 Pro | Most film-like and elegant |
  | Second choice for those | Seedream 5 Pro; Krea 2 | Good, slightly more digital |
  | Recurring characters (identity from a ref) | Seedream 5 Pro edit (first); Nano Banana Pro edit | Hold the face and stay natural |
  | Avoid for photoreal | GPT Image 2.5 (clean stock); Codex (glossy even with good prompts); Luma edit (broken crops: an arm, the top of a head); Luma t2i with refs (loses identity) | |

  Codex stays right for stylised looks (woodcut, ink) where its style block controls the surface.
- **Finish every still with `tools/imagegen/film_finish.py`.** It tames specular highlights, lifts the blacks, applies
  a gentle curve, halation and real grain. It removes the wet sheen from skin and makes frames from different models
  sit together. It will not rescue a stock-photo composition or Codex gloss; fix those in the prompt or the model.
  Default strength is 1.0.
- **Judge for elegance, not just photorealism.** Look at a 100% crop of the face: is the skin wet or plastic? Are there
  more than about 3 things competing for the eye? Would a good photographer have taken this frame? If not, rewrite
  the brief. Don't reroll.

## 3. Lookdev and keyframes (Codex)
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

## 6. Sound (see `bible/sound/` and `audio/pilot/*`)
**Sound plan:** a max-effort session writes the sound bible, `casting.md`, `dialogue.json`, `score.md` and
`score_cues.json`, `sfx.json` and `mix_plan.md`. Validate every JSON file with a real parser.

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
    a session's PID, anchor on the binary's path: `pgrep -f '^/Users/kingh0730/.local/bin/claude -p --effort xhigh'`
    (a monitor's own `bash -c ...` line can't match `^`). This bit three times on the mom episode.
  - Success is "the deliverable exists", never "the output log is non-empty" (a crash writes its error there).
  - Session transcripts are filed by working directory: a `claude -p` started in `private/<p>/` writes to
    `~/.claude/projects/-Users-kingh0730-repos-interregnum-private-<p>/`, not the repo's folder. Watch the right one.
  - Long max-effort writing sessions can loop on "Output token limit hit" and drop on proxy idle timeouts
    (`ECONNRESET`). Prefer xhigh and one deliverable per session; if a session hits the output limit repeatedly with
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
