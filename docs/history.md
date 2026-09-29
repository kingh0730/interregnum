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
