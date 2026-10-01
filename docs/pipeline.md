# Pipeline and tool matrix

The overall plan is in `strategy.md`: v1 is everything in-house, v2 is polish with a video model. **The current tool choices are in `docs/playbook.md`** (Luma Uni-1 for images, MiniMax H3 Max for motion and lip-sync, ElevenLabs for voices, music and SFX); this table is the earlier survey. `history.md` covers the experiments behind these choices.

Every shot is built with the tool that is strongest for that job. These notes come from hands-on tests in
`~/repos/yue/outputs/anime_clip/`: v1 slideshow, v2 layered compositing, v3 Codex frame-by-frame, v4 Blender + VRM,
v5–v7 Blender and Codex hybrids, v8–v9 Codex rotoscoping over Blender, v10–v13 EbSynth (details in `history.md`).

## Which tool for what

| Tool | Use it for | Don't use it for | Notes |
|---|---|---|---|
| **Claude** (writing/direction) | Bible, stories, scripts, shot lists, prompt design, edit decisions, QA via stills and frame metrics | Judging motion: Claude cannot watch video, only sampled frames. **King reviews all motion.** | Follow CLAUDE.md: default while King is present or unspecified; max for creative work and checking when explicitly away; default for routine production plumbing |
| **Codex image_gen** (`tools/imagegen/`) | Character sheets, key art, keyframes for the video model, painted backgrounds, style frames, props, transparent cutouts, edits to an existing image | Frame-by-frame animation or keyframes for propagation: every image is an independent reinterpretation, so it flickers (v3, v8; less visible when the motion is small) or smears (v10–v13). Character motion is Seedance's job. Precise numeric control ("head at 30°" is ignored) | ~2 min/image at medium effort; runs parallelize well; about 1 in 10 prompts hits a false-positive safety block, so reword neutrally |
| **Video model: Seedance 2.5** (`tools/video/`; superseded by MiniMax H3 Max for photoreal, which Seedance refuses) | Character acting and motion; dialogue with lip-sync, sound effects and ambience in the same pass | Long takes, exact choreography, generating exact text from a prompt (for animating supplied lettering, see the current workflow below), background music (Suno does music) | Needs an API key (fal.ai is the candidate). Voice consistency across shots is a known weak spot. Sora is discontinued (app April 2026, API September 24 2026) |
| **Blender** (`tools/blender/`) | Big 3D set pieces: ships, mechs, cities, space, crowds, destruction; exact camera moves; layouts under a Codex keyframe when a shot needs exact staging (the v7 method); depth and mask passes for compositing | Character acting in the final picture: toon 3D reads as 3D, and hand-keyed motion lacks weight (v4, v9) | VRM add-on 4.7.2 is installed. MToon counts each light's color almost fully whatever its energy, so use one key light plus low world ambient |
| **JS rendering** (`tools/web/`) | Diegetic screens (social feeds, chats, dashboards, propaganda UIs, AI interfaces), typography, title sequences, data-driven and generative visuals, HUDs, glitch and transition effects, animatics and review pages | Painterly imagery | HTML/Canvas/WebGL rendered frame by frame in headless Chrome; Node v22 is at `~/.nvm/versions/node/v22.23.1/bin` (the `node` shell function is broken in non-interactive shells) |
| **Python compositing** (`tools/comp/`) | Layering, parallax, particles (petals, snow, ash, embers), light FX (flare, bloom, light wrap, rim), grading, grain, assembly | Character animation (bending a still reads as a game cutscene, as v2 showed) | numpy + OpenCV, run with `uv run`; v2 effects are in `tools/comp/legacy/` |
| **ffmpeg** | Encoding, editing, conforming | | `-tune animation` for cel material |
| **Audio** (`tools/audio/`) | Ambience, sound design, temp score, scratch dialogue (macOS `say`), mixing and loudness | Final music (**Suno**, run by King from Claude's cue sheets) and final voices (**Seedance**) | v2's synth is in `tools/audio/` |

## Shot workflow

1. **Script → shot list** (`episodes/<ep>/shotlist.md`): each shot names its tool, duration, camera and acting.
   Identify story-critical actions, required repetitions and their relation to dialogue or other events.
2. **Look development** (`assets/`): character sheets and locations first; every later image references them.
3. **Keyframes** (Luma; Codex for some stylised looks) → **finish object graphics in the start frame** (JS/compositing
   as needed; verify text, clock readings and display states) → **motion** (video model, or Blender for 3D set pieces).
   For image-to-video, let the model animate supplied graphics with their objects. Use the approved scene frame to preserve faces, setting and
   composition; do not replace it with text-only generation. Add screen-space UI/graphics afterward.
4. **Check takes → composite → edit and sound:** locate essential actions in the full generated takes and record their
   timestamps before selecting cut points. Composite layers, FX and grade (Python); edit and sound with ffmpeg plus
   audio. If an action is usable but late, adjust the edit while preserving sync and pacing; if missing or unusable,
   revise or regenerate within budget. A prompt requesting an action is not evidence that it happened.
5. **Review**: Claude checks sampled frames and metrics; King watches the motion. Check all object graphics for exact content,
   readings, readability, attachment, jiggle and pop-in over the intended cut, including inherited overlays. Prefer
   corrected start frames and retakes for failures; tracked repairs require playback acceptance. Exact clock/display
   transitions may need controlled inserts.
   Verify every essential action again in the final rendered cut, including repetition and timing relative to dialogue.
   Keep uncertain motion explicitly pending playback review.

## Constraints

- Disk is nearly full (about 11 GB free on 2026-09-29). Keep intermediates in `work/` and delete them after a shot is final; renders are git-ignored.
- Never put API keys in files. Read them from environment variables (e.g. `FAL_KEY`).
