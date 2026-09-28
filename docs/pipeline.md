# Pipeline and tool matrix

Every shot is built with the tool that is strongest for that job. These notes come from hands-on tests in
`~/repos/yue/outputs/anime_clip/` (v1 slideshow, v2 layered compositing, v3 Codex frame-by-frame, v4 Blender + VRM).

## Which tool for what

| Tool | Use it for | Don't use it for | Notes |
|---|---|---|---|
| **Claude** (writing/direction) | Bible, stories, scripts, shot lists, prompt design, edit decisions, QA via stills and frame metrics | Judging motion: Claude cannot watch video, only sampled frames. **King reviews all motion.** | Use max or xhigh effort for writing and directing; medium for production plumbing |
| **Codex image_gen** (`tools/imagegen/`) | Character sheets, key art, keyframes for the video model, painted backgrounds, style frames, props, transparent cutouts, edits to an existing image | Frame-by-frame animation: every image is an independent reinterpretation, so it boils (v3 failed). Precise numeric control ("head at 30°" is ignored) | ~2 min/image at medium effort; runs parallelize well; about 1 in 10 prompts hits a false-positive safety block, so reword neutrally |
| **Video model** (`tools/video/`, provider TBD) | Character acting and motion, anything that has to *move* like drawn or filmed footage | Long takes, exact choreography, text | Needs an API key (fal.ai suggested: one key, several models). Sora is discontinued (app April 2026, API September 24 2026) |
| **Blender** (`tools/blender/`) | Big 3D set pieces: ships, mechs, cities, space, crowds, destruction; exact camera moves; previs and layout; depth and mask passes for compositing; rigged VRM characters when exact motion matters more than a drawn look | Hero close-ups of anime characters: toon 3D still reads as 3D | VRM add-on 4.7.2 is installed. MToon counts each light's color almost fully whatever its energy, so use one key light plus low world ambient |
| **JS rendering** (`tools/web/`) | Diegetic screens (social feeds, chats, dashboards, propaganda UIs, AI interfaces), typography, title sequences, data-driven and generative visuals, HUDs, glitch and transition effects, animatics and review pages | Painterly imagery | HTML/Canvas/WebGL rendered frame by frame in headless Chrome; Node v22 is at `~/.nvm/versions/node/v22.23.1/bin` (the `node` shell function is broken in non-interactive shells) |
| **Python compositing** (`tools/comp/`) | Layering, parallax, particles (petals, snow, ash, embers), light FX (flare, bloom, light wrap, rim), grading, grain, assembly | Character animation (bending a still reads as a game cutscene, as v2 showed) | numpy + OpenCV, run with `uv run`; v2 effects are in `tools/comp/legacy/` |
| **ffmpeg** | Encoding, editing, conforming | | `-tune animation` for cel material |
| **Audio** (`tools/audio/`) | Ambience, sound design, simple synthesized cues | Real music: needs a music model or licensed tracks | v2's synth is in `tools/audio/` |

## Shot workflow

1. **Script → shot list** (`episodes/<ep>/shotlist.md`): each shot names its tool, duration, camera and acting.
2. **Look development** (`assets/`): character sheets and locations first; every later image references them.
3. **Keyframes** (Codex) → **motion** (video model, or Blender for 3D set pieces) → **UI/graphics** (JS) as needed.
4. **Composite** (Python): layers, FX, grade. **Edit and sound** (ffmpeg plus audio).
5. **Review**: Claude checks sampled frames and metrics; King watches the motion.

## Constraints

- Disk is nearly full (about 11 GB free on 2026-09-29). Keep intermediates in `work/` and delete them after a shot is final; renders are git-ignored.
- Never put API keys in files. Read them from environment variables (e.g. `FAL_KEY`).
