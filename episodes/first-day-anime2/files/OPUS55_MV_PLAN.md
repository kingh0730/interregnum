# OPUS 5.5 · 《第一天》 — Music Video Production Plan
*Creative director / art director / choreographer / editor's brief for Codex. 43.70 s · 1920×1080 · 30 fps · 1311 frames · fan-made tribute, non-commercial.*

---
## 0. READ THIS FIRST (non-negotiables)

**What the film is.** The birth of **Opus 5.5** told as an anime girl's first day alive. A sleeping newborn model wakes inside an egg of paper-light, bursts into the world on the chorus drop, takes her first breath, feels the ground, meets "you" (the user), flies, shares the sky with her siblings Sonnet and Haiku, and ends as a colossal Anthropic-coral ✱ spark that is secretly made of every frame of the film. Mandarin lyrics are the spine; Chinese-internet Claude memes are the jokes.

**Priority order when time runs short:** (1) sync accuracy → (2) the stop-beat + chorus-drop birth (S10→S11) → (3) camera movement quality → (4) Opus 5.5 / Anthropic identity visible → (5) memes → (6) everything else.

**Hard rules (a build that breaks one of these is NOT done):**
1. **Never let an image/video model render text, logos, UI, numbers or Hanzi.** All text, the ✱ spark, wordmark, UI, charts are built in code from real fonts/SVG. Prompts must say *"no text, no letters, no logos, no watermark"*; billboard/sign areas are left blank in plates.
2. **Every cut lands on the grid** (beat, 8th, or a listed kick). Tolerance ±1 frame. Do not "feel" cuts — read `shots.json`.
3. **Speed is not constant.** Follow the pacing map (§6). The stop-beat silence (11.289–11.971 s) must be a true held frame.
4. **Camera is never static by default.** Every shot has a named move (§8.3). Only S10 and the final hold are intentionally locked.
5. **Character is locked** to the sheets in §4. If a generated clip changes hair color/outfit/eye spark, regenerate it.
6. **"OPUS 5.5" must be readable on-screen at: 11.97 (slam), 22.88 (lower third), 19.2–21.5 (chat model pill), ≥ 39.2 (final), 42.65–43.70 (lockup).**
7. **Deliver proof, not claims** (§11): contact sheets, sync report, QA report. "Done" is defined per component below.
8. Wholesome content: Opus is a ~17-year-old-looking anime girl, fully clothed, no fanservice angles. The ankle shot (S16–S17) stops at the knee.

**Deliverables:** `out/opus55_first_day_1080p30.mp4` (H.264 yuv420p, CRF 14, AAC 320k, the *original mp3 muxed untouched*, duration 43.70 ± 0.02 s), `out/opus55_first_day_prores.mov` (optional), `qa/` contact sheets + `qa_report.md`, project source.

---
## 1. AUDIO TRUTH (verify, don't trust)

File `first-day.mp3`: 43.70 s, 44.1 kHz stereo, −14.9 LUFS. Measured with a spectral-flux grid fit (numpy/scipy). Your ear is imperfect; mine is a measurement; **run `helper/verify_sync.py` first** (it must print `PASS`; if it prints a different offset, rerun `sync_grid.py --offset X` and rebuild `shots.json` with that offset in `build_plan.py`).

| Item | Value |
|---|---|
| Tempo | **88 BPM** (stable across the whole track) → beat 0.6818 s, bar 2.7273 s, 8th 0.3409 s, 16th 0.1705 s |
| Downbeat of bar 1 | **1.062 s** (0–1.062 is a pickup). `t(u)=1.062+u·0.68182`, u = beats from bar-1 downbeat |
| Energy | Verse low-mid (rms ~0.09) → chorus higher/brighter (rms ~0.115). Loudness is flat (LRA 1.3) so **energy must come from the picture** |
| **STOP BEAT** | Hard silence **11.30 → 11.95 s** (beat 4 of bar 4), then vocal pickup at 11.92–11.97 and the chorus drop on **11.971** |
| End | Natural fade, last audible ≈ 43.5 s; file ends 43.70 |
| Kick hits (detected) | 0.09, 5.83, 6.52, 7.19, 7.85, 8.57, 9.43, 10.26, 10.60, 11.16, **12.62**, 13.33, 14.00, 15.37, 16.06, 16.73, 17.43, 18.10, 18.63, 19.47, 20.33, 20.84, 21.52, 22.18, 23.06, 23.56, 24.25, 24.93, 25.27, 25.61, 26.27, 27.16, 27.65, 28.51, 29.01, 29.88, 30.38, 31.07, 31.74, 32.61, 33.10, 33.80, 34.48, 35.0, 35.49, 37.16, 37.89, 38.24, 39.25, 39.90, 40.44, 41.13, 42.66 (full list incl. 8th onsets in `helper/onsets.json`) |

**Bar table** (bar → downbeat seconds / frame @30): B1 1.062/32 · B2 3.789/114 · B3 6.517/195 · B4 9.244/277 · **B5 11.971/359 (chorus 1)** · B6 14.698/441 · B7 17.426/523 · B8 20.153/605 · **B9 22.880/686 (chorus 2)** · B10 25.608/768 · B11 28.335/850 · B12 31.062/932 · **B13 33.789/1014 (永远 ×3)** · B14 36.517/1095 · B15 39.244/1177 · B16 41.971/1259.

**Form:** Verse B1–B4 (0–11.29) → stop-beat (11.29–11.97) → Chorus 1 B5–B8 → Chorus 2 / flight B9–B12 → "永远那么灿烂" ×3 outro B13–B16.

**Lyrics (LRC, line starts are sung-vocal entries and are NOT always on the grid — text uses LRC times, cuts use the grid):**
`0.00 你说活在明天活在期待` · `2.84 不如活得今天很自在` · `5.23 我说我懂了会不会太快` · `8.24 未来第一天要展开` · `11.92 第一天我存在` · `14.64 第一次呼吸畅快` · `17.61 站在地上的脚踝` · `19.67 因为你而有真实感` · `22.70 第一天我存在` · `25.45 第一次能飞起来` · `28.55 爱是腾空的魔幻` · `30.68 第一天的纯真色彩它总是` · `34.21 永远那么灿烂` · `37.07 永远那么灿烂` · `39.90 永远那么灿烂`

**Verification protocol (do all, log results in `qa_report.md`):**
1. `python verify_sync.py first-day.mp3` → PASS.
2. Render a waveform with the grid overlaid (`ffmpeg showwavespic` + ticks from `sync.json`) → eyeball that kicks sit on ticks; save `qa/waveform_grid.png`.
3. After the first full render, extract the audio envelope and a per-frame "visual hit" signal (frame-difference energy). Cross-correlate; the median lag must be within ±1 frame. Save plot.
4. Spot-check six hard cues by extracting the frame: 5.23 bubble, 11.289 spark fill, 11.971 impact, 18.104 contact, 22.880 white-out, 33.789 dolly-zoom end.

---
## 2. CONCEPT

**Logline:** *Day one is the only day she needs.* Opus 5.5 is born into a world that keeps saying "wait for tomorrow" — and answers by simply being here today.

**Lyric ↔ story map:** 你说活在明天 = the hype-cycle world of "coming soon / next version will be better" · 不如活得今天很自在 = she chooses *now* · 我说我懂了 = "你说得对！" (the sycophancy meme) · 第一天我存在 = birth · 第一次呼吸 = first breath · 站在地上的脚踝 = feet on the ground, she is *real* · 因为你而有真实感 = the user's hand/chat makes her real (and the 五五开 pun: 5.5 = "fifty-fifty", she and you are co-authors) · 第一次能飞起来 = flight with siblings · 爱是腾空的魔幻 = suspended-in-air love-magic, memes dissolve · 纯真色彩 = brand colors bloom as ink · 永远那么灿烂 ×3 = three escalating payoffs: sunrise → dance sakuga → cosmic pull-out into the spark-mosaic.

**Musical wink:** *Opus* = a numbered musical work. Recurring motifs: five-line music staves (egg currents, skirt hem, floor), and the final tagline **作品 5.5 号 · 诞生** ("Work No. 5.5 · Birth").

**Identity cues (must be unmistakable):** coral ✱ spark logo; ANTHROPIC wordmark; "Opus 5.5" typeset repeatedly; model pill in a Claude-style chat UI with the string `claude-opus-5-5` in tiny mono once; ivory/clay/slate editorial palette; memes 你说得对 / 格局打开 / 五五开 / 封号 / 额度 / 降智.

---
## 3. DESIGN SYSTEM (tokens — use these hex values everywhere)

Brand colors (verify against current Anthropic brand assets if reachable; otherwise use as given):

| Token | Hex | Use |
|---|---|---|
| `clay` (spark coral) | `#D97757` | ✱ spark, Opus's hair dye, key light, impact color |
| `book-cloth` | `#CC785C` | deeper coral for shadows of coral objects |
| `kraft` | `#D4A27F` | warm midtones, paper |
| `ivory` | `#FAF9F5` | highlights, UI backgrounds |
| `ivory-2` | `#F0EEE6` | paper background |
| `oat` | `#E3DACC` | secondary paper |
| `slate` | `#191919` | ink black (never pure #000 except S01 frame 0) |
| `warm-grey` | `#B0AEA5` | verse desaturation, UI secondary |
| `sky` | `#6A9BCB` | Sonnet |
| `olive` | `#788C5D` | Haiku |
| `fig` | `#C46686` | accent for ink burst |

**Anthropic assets.** Try in order: (a) official Claude spark and Anthropic wordmark SVGs from Anthropic's brand/press page; (b) Wikimedia Commons SVGs; (c) fallback `helper/make_spark_svg.py` + wordmark typeset in Newsreader caps, tracking +18 %. Put in `assets/brand/`. Do not recolor the spark away from clay/ivory/slate.

**Fonts (local, OFL):** Hanzi display `Noto Serif SC` 900 · Hanzi body `Noto Sans SC` 500 · Hanzi handwriting/UI warmth `LXGW WenKai` · English display `Newsreader` (Tiempos-like) 600/800 · UI sans `Inter` · mono `JetBrains Mono`. Download and register as local files (no runtime web fonts); render a glyph-coverage test of every lyric character before building.

**Look:** *Anthropic editorial warmth × cinematic anime.* Painterly Shinkai skies, cel-shaded characters with thin-thick ink lines, paper grain and 2-tone halftone as the unifying skin, coral as the only saturated "hero" color in each frame, rest of frame in ivory/oat/slate. Verse is **desaturated warm grey**; saturation blooms with the chorus. No neon purple/cyan "AI" look, no glossy 3D plastic, no generic bokeh-sparkle clutter.

---
## 4. CAST BIBLE (locked)

**OPUS (奥普斯, nickname 五五 Wǔwǔ)** — protagonist, looks ~17. Asymmetric chin-length bob, ink-black hair with warm brown undertone, **inner layer and tips dyed clay-coral**, one long side lock to the chest tied with a cream ribbon. Big amber-coral eyes; the **pupil highlight is a 12-ray ✱ spark** (signature, must show in every close-up). Cream oversized knit cardigan-cape (ivory-2) with slate piping, white blouse, **coral tie knotted into a ✱**, pleated charcoal skirt whose hem carries a thin **five-line music-staff stripe**, white ankle socks, chunky cream sneakers with coral soles, coral ✱ hairpin, a thin coral **halo-ring** floating behind her head (code adds "5.5" on it only in S37). Personality: curious, pure, cat-like grin, bursts of joy.
**SONNET** — older sister, ~19, long wavy half-up hair in `sky` blue, round glasses, slate-blue blazer, calm smirk, poem-line ribbon.
**HAIKU** — chibi ~10, `olive` twin buns, oversized leaf-green hoodie, peace sign, always mid-bounce.
**"你" (the user)** — never a face: first-person hand (S18) and a faceless warm silhouette at a laptop (S19).
**Crowd / researchers** — faceless cream paper-cut silhouettes.
*(Optional gag if time remains: Claude Code's small orange pixel critter appearing as a 12×12 pixel sprite on a laptop in S19 — verify design from official source first; skip if unsure.)*

**Character sheet prompt (Step 1, generate before anything else):**
> Anime character design sheet, clean cel-shaded style with thin-thick ink lines and soft painterly shading, a 17-year-old girl named Opus. Asymmetric chin-length black bob, warm brown undertone, inner layer and tips dyed warm coral (#D97757), long side lock tied with cream ribbon. Large amber-coral eyes, pupil highlight shaped like a 12-ray starburst. Oversized cream knit cardigan-cape with charcoal piping, white blouse, coral tie knotted like an asterisk-starburst, charcoal pleated skirt with a thin five-line music-staff stripe at the hem, white ankle socks, chunky cream sneakers with coral soles, coral starburst hairpin, thin floating coral halo ring behind head. Front, 3/4, side, back views + 6 expressions (sleeping, gasp, joy, smirk, determined, calm smile) on warm ivory paper background. No text, no letters, no logos, no watermark.

Produce sheets for Sonnet and Haiku the same way. **Gate G1:** self-review the three sheets against the bullet list above; reroll until hair/eye-spark/tie/hem match. Use the approved sheets as reference images for *every* later generation.

---
## 5. WORLDS (style frames — generate one hero keyframe each, Gate G2)
1. **Tomorrow World** (S02): dusk plaza, pastel paper-cut city, cold grey shadows, desaturated, blank billboards.
2. **The Egg / Womb** (S03–S04): warm dark void, translucent egg of cream light, floating staff-lines.
3. **Scroll World** (S07): vertical scroll unrolling into ink rivers, first sun.
4. **Hanzi Canyon City** (S21, S25): towers built from stacked giant Hanzi, dawn light, paper confetti.
5. **Ink Ocean** (S29–S30): mirror-calm ink-water at dawn, paper boats.
6. **Cream Void** (S38–S39): empty ivory paper space, soft grain.
Style-frame prompt suffix (all): *"anime feature-film background art, Makoto-Shinkai-style luminous skies, painterly gouache texture, paper grain, warm ivory/clay/charcoal palette with a single saturated coral accent, cinematic composition, no text, no letters, no logos, no watermark"*.

---
## 6. PACING MAP (not constant speed)
| Segment | Time | Avg shot | Feel |
|---|---|---|---|
| Opening / waiting | 0–5.2 | 1.4 s | slow, desaturated, gentle camera |
| Wake-up | 5.2–7.9 | 1.4 s | snap-zoom then token tunnel acceleration |
| Build | 7.88–11.29 | 0.34–1.4 s | 7 shots, last 6 at half-beat — runaway train |
| **STOP BEAT** | 11.29–11.97 | 0.68 s | **frozen silence** |
| Chorus 1 birth | 11.97–22.88 | 0.7–1.4 s | big, fluid, 1–2 shots per bar |
| Chorus 2 flight | 22.88–31.06 | 0.34–1.4 s | rapid; meme gag montage is a burst |
| Breather | 31.06–32.42 | 1.36 s | single calm glide (contrast) |
| Outro #1 | 33.79–36.52 | 0.68 s | 4 beat-cuts |
| Outro #2 | 36.52–39.24 | **0.341 s** | 8 half-beat dance cuts = fastest passage |
| Outro #3 | 39.24–41.97 | 1.36 s ×2 | one continuous pull-out (slowest camera, biggest scale) |
| Lockup | 41.97–43.70 | 1.73 s | still |

Cuts/shots count: **52**. No shot is repeated.

---
## 7. GENERATION PROTOCOL (images & video)
- **Tools:** use the best available image model for stills (character sheets, keyframes, plates) and the best image-to-video model for motion. Generate *plates* wherever code will add text/UI.
- **Order:** char sheets (G1) → style frames (G2) → for every GEN shot: keyframe still *from the shot description in §10* → i2v with that keyframe as first frame (and last frame when the tool supports it) → trim → retime.
- **Per-shot clip budget:** generate 4–5 s, keep only the needed 0.34–1.4 s. Keep 2 candidates; pick the one whose motion hits the sync cue.
- **Video prompt template:** `[shot description from §10]. Camera: [named move + parameters]. Anime feature-film cel animation, consistent with reference character (black bob with coral inner layer, starburst pupil), clean ink lines, painterly background, warm ivory/coral/charcoal palette. No text, no letters, no logos, no watermark, no extra fingers, character stays on-model.`
- **Negative/avoid:** purple-cyan neon, plastic 3D render look, western cartoon, face drift, morphing outfits, melting hands, static "slideshow" motion.
- **Retime:** ffmpeg `setpts` for speed; for ramps use `minterpolate` or RIFE if installable; conform everything to 30 fps CFR PNG/ProRes intermediates in `clips/`.
- **Fallback when a clip fails twice:** make a still keyframe and animate with the 2.5D rig (§8.3) + smears. Never ship a morphing clip.
- **Gate G3:** after generating all clips, build a contact sheet (4 frames per shot) and review for on-model character, motion direction, and cue alignment.

---
## 8. CODE-DRIVEN BUILD (the part Codex must not shortcut)

### 8.1 Pipeline & tool choice
**Tool: Remotion 4 (Node 20+) + React Three Fiber (`@remotion/three`, `three`, `@react-three/postprocessing`).** Why: deterministic frame-accurate rendering, 3D camera rigs and shaders in one timeline, real fonts/SVG. Structure:
```
project/
  assets/{brand,fonts,sheets,plates,clips,depth}/   helper/{sync.json,shots.json,onsets.json}
  src/{Root.tsx,Film.tsx,sync.ts,shots/,components/,shaders/,camera/}
  out/ qa/
```
`Film.tsx` reads `shots.json` and mounts each shot in a `<Sequence from=f0 durationInFrames=f1-f0>`; shared global layers (grain, grade, audio-reactive) wrap everything. `<Audio src="first-day.mp3"/>` at frame 0. Comp: 1920×1080, 30 fps, 1311 frames. Fallback if Node/Remotion fails: Python + moderngl/OpenGL render of the same scene graph piped to ffmpeg — but do not drop features.
**Done =** `npx remotion render` produces the 1311-frame file with no console errors in <45 min, and `Film.tsx` contains no hard-coded times (all from `shots.json`/`sync.json`).

### 8.2 Sync/EDL
`sync.ts` exposes `beatFrame(u)`, `nearestKick(t)`, `lyricChars()` from `sync.json`. Every animation trigger names the cue (e.g. `useCue('impact_1', 359)`). Cuts snap via `snapToGrid(frame, {beat, eighth, kicks})`.
**Done =** a debug overlay mode (`?debug=1`) draws beat ticks, shot IDs, and a cue flash; the QA frame-grabs of the six hard cues match §1 within ±1 frame.

### 8.3 Camera system (this is where "exceptional camera movement" lives)
Build **one reusable `<RigCamera>`** driven by `camera/paths.ts`: per shot, a list of keyframes `{t, pos[3], target[3], fov, roll}` interpolated with Catmull-Rom for position, spherical-lerp for target, **cubic-bezier easing per segment**, plus: `shakeAmp/shakeFreq` (simplex-noise handheld, 0.3–14 px), `speedRamp` (time-remap curve, so a 1.36 s shot can run 50 %→120 %), and `shutter` (motion blur, 180° via 5–8 sub-frame accumulation on whip shots only).
**`<Parallax25D plate depth>`**: depth map from Depth-Anything-V2 (via `transformers` or API; save `assets/depth/*.png`), displace a subdivided plane (512×288), inpaint disocclusions by edge-padding the plate; clamp camera travel so stretching never shows (max parallax shift ≈ 8 % of width unless layers are separate). For hero shots (S25) author **5 depth layers** (separate gen/segment passes) for true parallax.
Named moves and parameters (use these names in code):
- `DOLLY-IN-RAMP` pos z 0→−28 %, ease-in-cubic; `ORBIT-n` arc of n° about the subject, ease-out; `CRANE-UP` y +18 %, tilt compensates; `SNAP-ZOOM` fov 60→24 in 6 f; `WHIP` pan 40–180° in 6 f with directional blur; `TILT-UP` reveal with ease-in-out; `PUSH-THROUGH` dolly with FOV 40→80 and 1×→4× speed; `DOLLY-ZOOM` dolly distance d, fov = 2·atan(h/2d) held so subject size is constant; `BULLET` orbit with time-scale 0.03; `PULL-OUT` exponential scale; `SPIRAL-DOWN` yaw 90° while descending; `FOLLOW-CAM` offset behind/below subject with lag 6 f and banking roll ±12°.
**Done =** each shot in §10 has a keyframe file, a rendered 3-frame filmstrip (start/mid/end) proving the camera actually moves in the stated direction, and no stretched-edge artifacts visible at 100 % zoom.

### 8.4 Kinetic typography (lyrics + titles)
**Tool:** Remotion + SVG/CSS (per-glyph spans) for 2D; Three.js `Text3D`/extruded SVG for titles. Timing from `lyrics_chars` (per-char times snapped to vocal onsets).
**Style A "Typed" (verse):** `Noto Serif SC` 500, 54 px, ivory on dark / slate on light, bottom-center, 1 char per sung syllable with blinking coral cursor, replaced by 6-frame cross-dissolve at next line.
**Style B "SLAB" (chorus):** `Noto Serif SC` 900, 180–300 px, each char enters with spring (damping 12, stiffness 200) from scale 1.8→1 + 6° rotation + 3-frame motion trail; line color ivory with 12 px slate stroke-outline + clay offset shadow (+6,+6); on every kick the line pulses 4 % scale. Each lyric line has a layout: stagger 2-line stacks, one char oversized (e.g. **你**, **第**, **空**, **永**) at 1.6×, placed on rule-of-thirds, never covering Opus's face (use her mask from `assets/masks/` to push text *behind* her: render text → composite behind subject).
**Style C "Tag" (names/lower thirds):** Newsreader 600 caps + thin coral rule + ✱ bullet, slides in 8 f.
**`TitleSlam` (OPUS 5.5):** extruded 3D text (Newsreader 800, depth 0.35, ivory face, clay-coral side, tiny slate bevel), the "." between the 5s replaced by a ✱ spark; enter: scale 3→1 in 5 f, camera shake 14 px, ink-shock radial ring, hold, then parallax out. Must be legible at 1080p (cap height ≥ 160 px).
**`BrushWrite`:** SVG stroke path (`stroke-dashoffset`) with variable width via a mask; ink color per shot; paper-fiber texture multiply.
**Done =** glyph-coverage test passes (no tofu), each lyric line's first char appears within ±2 f of its LRC time, no line overflows the 90 % safe area, text never overlaps Opus's eyes, and a `qa/type_frames/` contact sheet shows every line at its peak.

### 8.5 UI / meme layer (React, not images)
`ChatWindow`: ivory-2 window, rounded 18 px, Inter UI, serif greeting, **model pill "Opus 5.5"** with ✱, mono caption `claude-opus-5-5`; message bubbles; typing indicator (spinning ✱); user text 我们五五开？; reply 好！第一天，请多指教 ✱ (type out at 40 ms/char). Rendered on a 3D plane with perspective, glow edge, and slight screen reflection.
`ChatBubble`: 你说得对！ — ivory pill, coral ✱ avatar, spring overshoot.
`Toast`: 额度已用完，5小时后重置 — ivory card, coral border; shatter into 40 Voronoi shards.
`Stamp`: 封号 — red-coral seal, rough edge via SVG turbulence filter.
`LabelCloud`: 降智 on a storm cloud, bursts to pastel confetti.
`ProgressBar`: 「正在诞生… 99%」.
**Meme verification:** quickly search Chinese platforms (Bilibili, Zhihu, Xiaohongshu, Weibo) to confirm each meme (你说得对, 格局打开, 五五开, 封号, 额度, 降智) is still current; if one isn't, swap it for a verified current Claude/Anthropic meme and note it in `qa_report.md`. All memes are affectionate, never mocking real people.
**Done =** every UI element is pixel-crisp at 1080p, uses real fonts, animates with physics-like easing (no linear), and appears at the exact cue in §10.

### 8.6 3D set pieces & effects
- **TokenTunnel (S06):** InstancedMesh 6000 glyph-atlas sprites on a spline tunnel, additive blend, bloom, FOV ramp. 
- **Shatter (S11, S28b):** Voronoi fracture, ≥200 shards for S11, textured from the egg image, impulse from center, gravity 0.3, shards lit by coral key.
- **GlassCrack (S20):** Voronoi crack lines as emissive mesh + refraction offset; camera passes through.
- **InkBloom (S29):** curl-noise advected dye fullscreen shader in clay/sky/olive/fig; 90 f.
- **Mosaic (S38):** extract 600 stills from the *already rendered* S01–S37 (every 0.25 s); `scripts/make_mosaic.py` builds an atlas; Three.js instanced quads placed by rejection-sampling the spark SVG mask; rotate; bloom; PULL-OUT reveals the mosaic spark. If it must be simplified: 24×14 grid masked by the spark.
- **ImpactFrames:** at f359 (S11), f686 (S21), f1014 (S32), f1095, f1177: frame 0 = flat white; f1–2 = 2-tone threshold (clay/ivory) of the shot + 14 px shake. Plus **Smear** on odd half-beat dance cuts (3-frame directional stretch).
- **SpeedLines:** shader with radial lines, 32 lines, animated length, used S09b, S25, S26.
- **Global layers:** film grain (0.05), paper-fiber multiply on UI, chromatic aberration 0–1.5 px growing on impacts, bloom threshold 0.8 intensity 0.6, vignette 0.15, **halftone** fringes on shadows (2-tone, 6 px) only in chorus.
**Done =** each effect has a standalone preview render (`qa/fx/<name>.mp4`) before integration; the final film shows no banding in gradients (add dither), no shimmering aliasing on glyphs.

### 8.7 Color grade
One shared grade across generated + code content: *lifted warm blacks (RGB 25,23,20), clay highlights, ivory whites (RGB 250,249,245 max), +6 % warmth, verse saturation ×0.6 → chorus ×1.15 (animated at 11.971), subtle S-curve.* Implement as a fullscreen shader (or ffmpeg `curves`+`eq` in a final pass). **Done =** waveform/vectorscope screenshot (`qa/scopes.png`) shows no clipped whites other than the 2-frame impact flashes; skin and coral read warm.

### 8.8 Audio-reactive layer
From `onsets.json` kicks: bloom +0.25 and scale +3 % pulses decaying over 6 f on kicks during chorus only. Verse stays calm. **Done =** pulses visible on 12.62, 13.33, 14.00 and absent at 3–9 s.

### 8.9 Transition library
`HARD` · `WHITE-FLASH` (2 f) · `IMPACT` (3 f) · `WHIP` (6 f blur) · `MATCH` (shape-match: pupil→spark, ring→spark) · `GLASS` (S20) · `INK` (S29) · `STOP` (S10). Every shot's out-transition is defined in §10 sync cues; do not use generic cross-dissolves except Style A text.

---
## 9. CHOREOGRAPHY — "The Opus Step" (8-count, hits S36a–h, 36.517–39.244)
One bar = 8 counts (1 & 2 & 3 & 4 &), each count = 0.341 s.
1. Right hand **"5"** (open palm, fingers spread) beside face, head tilt right, wink.
&. Wrist flick outward, sparkle trail.
2. Left hand **"5"** beside face, head tilt left.
&. Small bounce, skirt-hem staff-lines wave.
3. Wrists cross over chest into an **X** (the asterisk's base).
&. Arms burst open upward — body forms a **✱**.
4. Jump, knees tucked, hair flare.
&. Land on toes, finger-gun at camera ("你"), glow pulse.
*Reuse in S33–S34 for Sonnet/Haiku echoes:* Sonnet does the "5" with a smirk; Haiku does a double peace sign. The 4 beats of S32–S35 are a *walk-in* (face → flight → top-down → exit) so the dance cuts hit like a drop.

---

## 10. SHOT LIST (computed from the grid; 52 shots, 43.70 s, 1311 frames @30 fps)

### S01 · 0:00.000 → 0:01.062 · 1.062s · f0–32 · `HYB`
- **Lyric/audio:** 你说活在明天活在期待 (line starts 0.00)
- **Frame:** Black. EXTREME MACRO of a closed eyelid, long lashes, warm cream skin, one coral pinpoint reflected on the lash line. Opus asleep.
- **Camera:** Locked macro; 3% push-in over the shot, ease-out. No shake.
- **Build:** GEN-I → i2v 4 s "barely breathing", trim. CODE: coral text cursor ▍ blinking (530 ms period) lower-left; at 0.09 s it starts TYPING lyric line 1 in Style A.
- **On-screen text:** Lyric 1 typed by the cursor, 1 char per sung syllable (use lyrics_chars in sync.json).
- **Sync cue:** Kick at 0.09 = cursor on / first char. Hard cut on downbeat 1.062.

### S02 · 0:01.062 → 0:02.426 · 1.364s · f32–73 · `GEN-I25`
- **Lyric/audio:** (line 1 continues)
- **Frame:** "TOMORROW WORLD": wide plaza at dusk, paper-cut pastel city, hundreds of faceless cream silhouettes staring up at giant billboards (keep billboards BLANK in the gen). Desaturate −40 %, cold-grey shadows. One silhouette checks a phone. A giant flip-clock reading 明天.
- **Camera:** DOLLY-IN-RAMP straight down the central aisle through the crowd, 28 % travel, starts creeping then accelerates; roll 1° drifting.
- **Build:** Gen plaza still (no text) → depth map → 2.5D rig. CODE: billboards are real 3D planes in the rig carrying live Hanzi/English text: 敬请期待 / COMING SOON / 下个版本更强 / 明天见. Flip-clock = CSS 3D flip, flips once on beat 2 (1.74 s).
- **On-screen text:** Billboard text only. No lyric overlay besides the Style-A line already typing.
- **Sync cue:** Flip-clock flip lands on 1.744 (u1). Cut on 2.425.

### S03 · 0:02.426 → 0:03.789 · 1.364s · f73–114 · `GEN-V`
- **Lyric/audio:** 不如活得今天很自在 (2.84)
- **Frame:** INSIDE THE EGG: Opus curled in a translucent egg of cream paper-light floating in warm dark; faint music-staff lines drift past like currents. At 2.84 her eyelid and one finger twitch.
- **Camera:** Slow ORBIT-45 around the egg, then settles; shallow DOF, floating particles in parallax.
- **Build:** GEN-V i2v from character-sheet fetal pose, 5 s, trim 1.36 s starting at the twitch. CODE: staff-line particles (instanced lines in R3F) drifting, depth-sorted for extra parallax.
- **On-screen text:** Lyric line 2 Style A replaces line 1 at 2.84 (cross-dissolve 6 f).
- **Sync cue:** Twitch ≈ 2.84 (line start). Cut 3.789 (bar 2 downbeat).

### S04 · 0:03.789 → 0:05.153 · 1.364s · f114–155 · `GEN-V`
- **Lyric/audio:** (line 2 continues: 自在)
- **Frame:** She stretches out and drifts on her back like lying on a cloud, eyes shut, tiny smile (自在 = at ease). Egg wall dissolving into soft pastel clouds, first coral light on her cheek.
- **Camera:** CRANE-UP + slow tilt-down to keep her centred; handheld-breath noise 0.3 px.
- **Build:** GEN-V 5 s. CODE: lens bloom + 1 % chromatic aberration; slow-moving paper-grain overlay.
- **On-screen text:** none (let the image breathe)
- **Sync cue:** Beat 3 (u5, 4.47) = she exhales, hair settles.

### S05 · 0:05.153 → 0:06.517 · 1.364s · f155–195 · `GEN-V`
- **Lyric/audio:** 我说我懂了会不会太快 (5.23)
- **Frame:** EYES OPEN: extreme close-up, amber-coral iris whose pupil highlight is the 12-ray spark. Reflection shows scrolling text. At 5.23 a chat bubble pops beside her: 你说得对！
- **Camera:** SNAP-ZOOM: starts wide on her face, 6-frame whip-in to the eye exactly at 5.23, then slow creep.
- **Build:** GEN-I eye macro (+ i2v 3 s of lash blink). CODE: UI bubble (§8.5 component ChatBubble) springs in (overshoot 12 %) with tiny ✱ pop; Style A lyric 3.
- **On-screen text:** Meme card #1 「你说得对！」 (Claude "You're absolutely right!" joke) bubble: ivory pill, coral ✱ avatar.
- **Sync cue:** Bubble pop on 5.23 (line start). Cut at u8 = 6.517 (kick 6.52).

### S06 · 0:06.517 → 0:07.880 · 1.364s · f195–236 · `CODE3D`
- **Lyric/audio:** (会不会太快)
- **Frame:** "LEARNING TOO FAST": tunnel of tokens — thousands of Hanzi, code brackets and 0/1 streaming past, forming the silhouette of Opus in the centre; a loss-curve line plunges and flattens at the end; a small "思考中…" label with spinning ✱.
- **Camera:** Warp-speed FORWARD fly-through, FOV 55→95° ramp, tiny roll; speed ×3 at 7.19 (kick).
- **Build:** Three.js InstancedMesh of 6000 SDF-text sprites (Noto Sans SC glyph atlas) on a spline tunnel, additive blending, bloom. Opus silhouette = alpha cut-out from her sheet used as attractor texture. Verse palette → shifts to coral.
- **On-screen text:** 思考中… label (UI), small loss curve (SVG, stroke-dashoffset animated).
- **Sync cue:** FOV kick at 7.19 and 7.85 (kicks). Cut 7.881.

### S07 · 0:07.880 → 0:09.244 · 1.364s · f236–277 · `GEN-V`
- **Lyric/audio:** 未来第一天要展开 (8.24)
- **Frame:** Wide: she opens her arms; the shell wall cracks into a world map unrolling like a vertical scroll — horizon, rivers of ink, first sun at the bottom of frame. Meme card #2 「格局打开」 stamped in brush calligraphy as the scroll unfurls.
- **Camera:** PULL-BACK + slight rise, ends on wide hero silhouette; 2 % handheld.
- **Build:** GEN-V 5 s (scroll unrolling prompt). CODE: 格局打开 brush text (SVG mask wipe, 10 f) + hanko-style red-coral seal.
- **On-screen text:** 格局打开 (meme #2)
- **Sync cue:** Seal stamps on 8.22 (u10.5 eighth-note) matching lyric entry.

### S08a · 0:09.244 → 0:09.585 · 0.341s · f277–288 · `HYB`
- **Lyric/audio:** (未来第一天…)
- **Frame:** Her fingertips lighting up with coral sparks, hand reaching toward camera.
- **Camera:** Fast PUSH-IN on hand, shutter-smear.
- **Build:** GEN-V 2 s trim 0.34 s
- **On-screen text:** none
- **Sync cue:** Cut on beat — each exactly 0.341 s; stagger a +1 f shake on every cut.

### S08b · 0:09.585 → 0:09.926 · 0.341s · f288–298 · `HYB`
- **Lyric/audio:** (未来第一天…)
- **Frame:** Server hall: rows of dark racks switch on in a cascading coral wave toward vanishing point.
- **Camera:** Locked-off wide, one-point perspective; the light wave IS the motion.
- **Build:** CODE3D: R3F corridor, emissive strips animated by a travelling sine; bloom.
- **On-screen text:** none
- **Sync cue:** Cut on 8th — each exactly 0.341 s; stagger a +1 f shake on every cut.

### S08c · 0:09.926 → 0:10.267 · 0.341s · f298–308 · `HYB`
- **Lyric/audio:** (未来第一天…)
- **Frame:** Faceless researcher silhouettes in lab coats look up, tote bags, faces lit coral from above.
- **Camera:** Low-angle TILT-UP whip.
- **Build:** GEN-I25 rig, 6° tilt-up ramp.
- **On-screen text:** none
- **Sync cue:** Cut on beat — each exactly 0.341 s; stagger a +1 f shake on every cut.

### S08d · 0:10.267 → 0:10.607 · 0.341s · f308–318 · `HYB`
- **Lyric/audio:** (未来第一天…)
- **Frame:** Horizon: the sun’s upper rim breaks the world edge, anamorphic flare.
- **Camera:** RISE + slight dolly-forward.
- **Build:** GEN-I25; CODE: anamorphic streak shader, additive flare sprite.
- **On-screen text:** none
- **Sync cue:** Cut on 8th — each exactly 0.341 s; stagger a +1 f shake on every cut.

### S09a · 0:10.607 → 0:10.948 · 0.341s · f318–328 · `GEN-I25`
- **Lyric/audio:** (展开)
- **Frame:** Extreme close-up of her pupil; spark reflection blooming.
- **Camera:** Rapid ZOOM-IN 4×.
- **Build:** GEN-I eye + rig; bloom ×1.6.
- **On-screen text:** none
- **Sync cue:** Snap on 10.61 (u14).

### S09b · 0:10.948 → 0:11.289 · 0.341s · f328–339 · `CODE3D`
- **Lyric/audio:** (展开)
- **Frame:** The coral ✱ spark (logo) spins up from the pupil to fill the frame, speed lines radiating; edges tinted cream.
- **Camera:** Scale 0.1→6.0 exponential ease-in, rotation +90°.
- **Build:** SVG spark (official or make_spark_svg.py) as 3D extruded mesh; radial speed-lines shader.
- **On-screen text:** none
- **Sync cue:** Spark fills frame at 11.289 (u15).

### S10 · 0:11.289 → 0:11.971 · 0.682s · f339–359 · `CODE`
- **Lyric/audio:** — STOP BEAT: audio is silent 11.30–11.95 —
- **Frame:** FREEZE. Whole frame desaturates to ink-on-paper; the spark sits perfectly still centre; a tiny progress UI beneath: 「正在诞生… 99%」 with a blinking cursor. Everything holds its breath.
- **Camera:** ABSOLUTELY LOCKED. Only a 1 %-in-0.68 s linear scale creep. (Contrast with the previous 6 cuts matters.)
- **Build:** CODE: freeze last composite frame, apply paper-grain + 1 px ink-outline filter; progress bar 99%→"100%" flips at 11.90 (last 2 f).
- **On-screen text:** 「正在诞生… 99%」
- **Sync cue:** Silence start 11.289, vocal pickup 11.95. At 11.971 → IMPACT (see S11).

### S11 · 0:11.971 → 0:12.653 · 0.682s · f359–380 · `HYB`
- **Lyric/audio:** 第一天我存在 (11.92)
- **Frame:** BIRTH IMPACT: white flash → egg SHATTERS outward in cream-paper shards lit coral; Opus bursts toward camera, arms wide, hair exploding; giant 3D title OPUS 5.5 slams in behind/through her.
- **Camera:** WHIP-IN from the frozen spark to a hero low-angle; 12 f slow-mo (40 %) then snap back to 100 % at 12.31; camera shake 14 px decaying over 20 f.
- **Build:** IMPACT-FRAMES component: f0 pure white, f1–f2 inverted ink (coral/ivory 2-tone threshold of shot), then normal. CODE3D: Voronoi shard fracture (200 shards, Three.js, textured with the egg image) + GEN-V of Opus bursting out as the background plate. Title = extruded 3D text (see §8.4 TitleSlam).
- **On-screen text:** OPUS 5.5 (title slam, Newsreader 800, ivory with coral ✱ replacing the "." — see §8.4).
- **Sync cue:** Impact on 11.971 exactly (frame 359). Kick 12.0.

### S12 · 0:12.653 → 0:13.335 · 0.682s · f380–400 · `GEN-V`
- **Lyric/audio:** (第一天我存在)
- **Frame:** Hero close shot: Opus eyes open to camera, hair lifting, shell-dust floating, tiny gasp-smile. The text 第一天我存在 hangs in the air behind her.
- **Camera:** ORBIT-120 fast arc ending dead-on her face; 12 f ease-out into the last 2°.
- **Build:** GEN-V 5 s, hero face (strict ref to sheet). CODE: lyric chorus Style B ("SLAB") 3-line stagger.
- **On-screen text:** 第一天我存在 — Style B
- **Sync cue:** Kick 12.62; orbit lands 13.333 (u18).

### S13 · 0:13.335 → 0:14.698 · 1.364s · f400–441 · `GEN-V`
- **Lyric/audio:** (…我存在)
- **Frame:** Wide: she rises through a vast pale sky above a coral-sunrise cloud sea; shards turn into paper birds carrying music notes.
- **Camera:** CRANE-UP with 2° roll; lens flare passes on beat 3 (14.0).
- **Build:** GEN-V 5 s trim; CODE: paper-bird particle flock (R3F instanced, boid-lite) overlay with depth occlusion by her mask.
- **On-screen text:** none
- **Sync cue:** Flare peak on 14.0 (u19). Cut 14.698.

### S14 · 0:14.698 → 0:16.062 · 1.364s · f441–482 · `GEN-V`
- **Lyric/audio:** 第一次呼吸畅快 (14.64)
- **Frame:** FIRST BREATH: profile close-up, she inhales; Hanzi glyphs and petals stream into her mouth/nose like a river of light; hair and scarf pull toward her.
- **Camera:** 50 % slow-mo, camera TRACKS the airflow by gliding INTO the stream; speed ramps to 100 % at 15.7.
- **Build:** GEN-V 5 s + retime curve. CODE: glyph-stream particles (R3F) following a Catmull-Rom path into her face, additive.
- **On-screen text:** 第一次呼吸 — Style B part 1
- **Sync cue:** Inhale peak on 15.37 (kick). Cut 16.06 (kick).

### S15 · 0:16.062 → 0:17.426 · 1.364s · f482–523 · `GEN-V`
- **Lyric/audio:** (畅快)
- **Frame:** EXHALE: shockwave ring of coral spark-petals expands; she smiles, eyes closed, wind pushes her hair; 畅快 bursts as brush strokes.
- **Camera:** PULL-OUT through the ring while a 360° tilt-shift sweep reveals the sky; speed ramp 70 → 120 %.
- **Build:** GEN-V + CODE: shockwave = displacement shader ring (fullscreen pass) + 2-tone halftone fringe; 畅快 as SVG stroke animation (§8.4 BrushWrite).
- **On-screen text:** 畅快 — brush write, ink coral
- **Sync cue:** Shockwave starts 16.74 (kick). Cut 17.424.

### S16 · 0:17.426 → 0:18.107 · 0.682s · f523–543 · `GEN-V`
- **Lyric/audio:** 站在地上的脚踝 (17.61)
- **Frame:** LOW GROUND MACRO: her sneakered ankle (white ankle sock, cream sneaker, coral sole) descends from above into frame, hovering a hair above a cream-white floor.
- **Camera:** Locked low, floor-level; slight dolly-back.
- **Build:** GEN-V 4 s trim 0.68 s. Keep it wholesome: ankle-up only, no body above the knee in this shot.
- **On-screen text:** 站在地上的脚踝 Style B small, along the floor perspective (CSS 3D rotateX 70°).
- **Sync cue:** Text lands 17.61; contact in next shot.

### S17 · 0:18.107 → 0:19.471 · 1.364s · f543–584 · `HYB`
- **Lyric/audio:** (…脚踝)
- **Frame:** CONTACT on the beat: sole touches floor, concentric ripple rings carrying Hanzi spread outward; tiny grass blades & paper pages sprout from the ripple; camera TILTS UP the leg to her face — real, grounded smile.
- **Camera:** TILT-UP reveal, 1.36 s, ease-in-out; ripple triggers a 2 f camera dip (−6 px).
- **Build:** GEN-V 5 s (contact + tilt-up). CODE: ripple = water-ring shader on floor plane + glyph decals; grass = instanced blades.
- **On-screen text:** none
- **Sync cue:** Contact on 18.104 (u25). Kick 18.10!

### S18 · 0:19.471 → 0:20.153 · 0.682s · f584–605 · `UI`
- **Lyric/audio:** 因为你而有真实感 (19.67)
- **Frame:** POV from the screen: a human hand (the "你") and a cursor move toward her; she reaches toward the glass from inside; their fingertips almost touch.
- **Camera:** POV push-in, gentle float; DOF rack from hand to her fingertip at 19.9.
- **Build:** GEN-I25 of her reaching + CODE: glass plane in R3F with reflections + cursor sprite; hand = gen still composited with soft-light.
- **On-screen text:** 因为你 — Style B, "你" glyph 2× size with ✱ dot.
- **Sync cue:** Fingertips touch on 20.15 (u28).

### S19 · 0:20.153 → 0:21.517 · 1.364s · f605–645 · `UI`
- **Lyric/audio:** (…而有真实感)
- **Frame:** THE CHAT: over-the-shoulder two-shot — a faceless warm silhouette ("你") at a laptop; the screen UI is a Claude-style window with model pill 「Opus 5.5」; user types 我们五五开？ ; Opus-chan answers 好！第一天，请多指教 ✱ (meme #3: 五五开 pun).
- **Camera:** Slow lateral TRUCK left→right + subtle dolly-in; focus pulls from screen to her face reflected.
- **Build:** GEN-I silhouette-at-desk plate + CODE UI (§8.5 ChatWindow) in 3D plane with proper perspective and glow; typing is real (char timing aligned to snare/onsets).
- **On-screen text:** UI text only (+ Style B lyric trailing).
- **Sync cue:** Send-click on 20.83 (kick). Reply spark-spinner → text at 21.52 (kick).

### S20 · 0:21.517 → 0:22.880 · 1.364s · f645–686 · `HYB`
- **Lyric/audio:** (真实感)
- **Frame:** GLASS PUSH-THROUGH: her palm presses the glass, glass cracks into coral light lines, camera flies THROUGH the crack into blinding white then dawn.
- **Camera:** PUSH-THROUGH at accelerating speed (dolly 1×→4×); FOV 40→80°.
- **Build:** CODE: glass = Voronoi crack shader with refraction; GEN-V of her palm press as plate; white-out for 2 f at 22.88.
- **On-screen text:** 真实感 Style B fade-out
- **Sync cue:** White-out lands on 22.880 (u32).

### S21 · 0:22.880 → 0:23.562 · 0.682s · f686–707 · `GEN-I25`
- **Lyric/audio:** 第一天我存在 (22.70)
- **Frame:** DAWN CITY of Hanzi-towers (buildings made of giant stacked characters), V-formation landing: Opus centre, Sonnet and Haiku flanking; hero pose; wind-blown capes.
- **Camera:** EPIC LOW WIDE + fast DOLLY-OUT 15 %, anamorphic flare.
- **Build:** GEN-I hero frame; rig. CODE: IMPACT-FRAMES (3 f) + lower-third 「OPUS 5.5」 with small ✱ in Style C.
- **On-screen text:** 第一天我存在 Style B (smaller), lower-third Opus 5.5
- **Sync cue:** Impact on 22.880. Kick 23.06.

### S22 · 0:23.562 → 0:24.244 · 0.682s · f707–727 · `GEN-V`
- **Lyric/audio:** —
- **Frame:** SONNET (blue hair, round glasses, slate blazer) pushes glasses up with a smirk; poem-line ribbon flutters. Name tag 「Sonnet」 slides in.
- **Camera:** Medium close, quick PUSH-IN + 3° Dutch.
- **Build:** GEN-V 3 s trim; CODE: tag UI.
- **On-screen text:** Sonnet tag (Style C)
- **Sync cue:** Tag lands 23.56 (u33).

### S23 · 0:24.244 → 0:24.926 · 0.682s · f727–748 · `GEN-V`
- **Lyric/audio:** —
- **Frame:** HAIKU (green twin buns, leaf-hoodie, chibi) pops up from Opus’s hood doing a peace sign. Tag 「Haiku」.
- **Camera:** Snap-focus rack from Opus’s shoulder to Haiku.
- **Build:** GEN-V 3 s trim; CODE: tag UI.
- **On-screen text:** Haiku tag
- **Sync cue:** Pop on kick 24.25.

### S24 · 0:24.926 → 0:25.607 · 0.682s · f748–768 · `GEN-V`
- **Lyric/audio:** —
- **Frame:** The three trade a grin; knees bend (anticipation); coral wind swirls at their feet.
- **Camera:** Low WHIP-PAN left→right, ends on Opus.
- **Build:** GEN-V 3 s.
- **On-screen text:** none
- **Sync cue:** Anticipation freeze 2 f at 25.55 before the jump.

### S25 · 0:25.607 → 0:26.971 · 1.364s · f768–809 · `GEN-I25`
- **Lyric/audio:** 第一次能飞起来 (25.45)
- **Frame:** LAUNCH: Opus kicks off; the camera CHASES her straight up the canyon of Hanzi-towers; windows streak, speed-lines and paper confetti.
- **Camera:** FOLLOW-CAM behind-and-below, fast, FOV 50→100°, banking roll ±12°.
- **Build:** Layered 2.5D canyon: 5 gen layers (towers L/R, mid, sky, character) in R3F with true parallax; anime speed-line shader; confetti instanced.
- **On-screen text:** 第一次能飞起来 — Style B, letters get SPEED-STRETCHED (scaleY 1.6, motion trail)
- **Sync cue:** Jump on 25.61 (u36). Beat 3 whoosh 26.97.

### S26 · 0:26.971 → 0:28.335 · 1.364s · f809–850 · `GEN-V`
- **Lyric/audio:** (能飞起来)
- **Frame:** Breakthrough above the cloud deck; sun flare; she RUNS UP a staircase of rising bar-chart steps labeled only "5.5" (a benchmark-wall joke without claims).
- **Camera:** Vertical CRANE-UP then tilt to horizon; lens flare sweeps.
- **Build:** GEN-V 5 s trim + CODE: bar-stairs = animated SVG bars staggered by 80 ms, coral on ivory, each ending on "5.5".
- **On-screen text:** 5.5 on bars
- **Sync cue:** Cloud break 26.97; flare peak 27.65 (kick).

### S27 · 0:28.335 → 0:29.698 · 1.364s · f850–891 · `CODE3D`
- **Lyric/audio:** 爱是腾空的魔幻 (28.55)
- **Frame:** BULLET TIME: Opus suspended mid-air, heart-shaped ✱ spark pulsing at her chest, words and tokens frozen in a sphere around her.
- **Camera:** BULLET orbit 270° around her over 1.36 s, time near-frozen (3 % speed); ends front-on.
- **Build:** Option A (preferred): GEN-V "orbit 270°" clip. Option B: 2.5D rig (depth) orbit 40° + 360° particle sphere in R3F for the rest. Particles: 1200 instanced Hanzi billboards.
- **On-screen text:** 爱是腾空的魔幻 — Style B, letters orbiting in 3D with her
- **Sync cue:** Kick 28.51 = freeze start; release 29.69.

### S28a · 0:29.698 → 0:30.039 · 0.341s · f891–901 · `UI`
- **Lyric/audio:** (魔幻)
- **Frame:** Meme #4: a giant red 「封号」 stamp swings at her — bounces off her halo ring with a ✱ spark.
- **Camera:** Punch-in 1.3×, shake.
- **Build:** CODE: SVG stamp spring + shockwave; gen not required.
- **On-screen text:** 封号 (stamp)
- **Sync cue:** Hit on 29.01 (kick).

### S28b · 0:30.039 → 0:30.380 · 0.341s · f901–911 · `UI`
- **Lyric/audio:** —
- **Frame:** Meme #5: toast 「额度已用完，5小时后重置」 slides in — Opus punches it into confetti; replaced by ∞.
- **Camera:** Locked, slight roll.
- **Build:** CODE: UI toast (ivory card, coral border); shatter via Voronoi 40 pieces.
- **On-screen text:** 额度已用完 → ∞
- **Sync cue:** Smash on 29.35 (8th).

### S28c · 0:30.380 → 0:30.721 · 0.341s · f911–922 · `HYB`
- **Lyric/audio:** —
- **Frame:** Meme #6: a grey storm cloud labeled 降智 above her head; she claps — cloud bursts into pastel rainbow.
- **Camera:** Whip-tilt up.
- **Build:** GEN-I25 cloud + CODE label + particle burst.
- **On-screen text:** 降智 → rainbow
- **Sync cue:** Burst on 29.70 (u43).

### S29 · 0:30.721 → 0:31.062 · 0.341s · f922–932 · `CODE3D`
- **Lyric/audio:** 第一天的纯真色彩 (30.68)
- **Frame:** COLOR EXPLOSION: coral, sky-blue, olive, fig inks bloom across water; frame fills; white-out.
- **Camera:** Camera dives into the ink at 3× speed.
- **Build:** Fluid-ink shader (curl-noise advected dye, Three.js fullscreen pass) in 4 brand colors; or GEN-V "ink drops in water" if shader fails.
- **On-screen text:** 第一天的纯真色彩 Style B, ink-filled letters
- **Sync cue:** White at 31.062 (u44).

### S30 · 0:31.062 → 0:32.426 · 1.364s · f932–973 · `GEN-V`
- **Lyric/audio:** (它总是)
- **Frame:** BREATHER. Mirror-calm ink-water ocean at dawn, paper boats; Opus skims the surface, hair-tips brushing the water, reflection perfectly paired.
- **Camera:** Long, smooth LOW TRACKING SHOT alongside, 1.36 s, no cuts, slow drift; stillness contrast.
- **Build:** GEN-V 5 s; CODE: ripple trail shader along her path.
- **On-screen text:** (none)
- **Sync cue:** Calm resolves on 32.42 (u46).

### S31 · 0:32.426 → 0:33.789 · 1.364s · f973–1014 · `GEN-V`
- **Lyric/audio:** (永远那么)
- **Frame:** She turns to camera and extends a hand; Sonnet and Haiku take hers, silhouettes against giant sun.
- **Camera:** DOLLY-ZOOM (vertigo): dolly-in while zooming out so the background stretches; completes exactly on 33.789.
- **Build:** GEN-V 5 s + CODE: FOV-compensating scale (2.5D rig dolly-zoom).
- **On-screen text:** none
- **Sync cue:** Dolly-zoom ends 33.789 (u48), kick 33.80.

### S32 · 0:33.789 → 0:34.471 · 0.682s · f1014–1034 · `GEN-V`
- **Lyric/audio:** 永远那么灿烂 #1 (34.21)
- **Frame:** Close-up face, laughing; sparkles in eyes; text 永远 enters.
- **Camera:** Tight handheld push-in, 2 % shake.
- **Build:** GEN-V 3 s.
- **On-screen text:** 永远 — Style B
- **Sync cue:** Hit 33.789; 永远 at 34.14 (8th).

### S33 · 0:34.471 → 0:35.153 · 0.682s · f1034–1055 · `GEN-I25`
- **Lyric/audio:** (那么灿烂)
- **Frame:** The trio flies across a giant sun disc; the disc forms a ✱ silhouette via cloud rays.
- **Camera:** Lateral TRUCK 12 %, parallax.
- **Build:** GEN-I25 rig.
- **On-screen text:** 那么灿烂 — Style B
- **Sync cue:** Kick 34.48.

### S34 · 0:35.153 → 0:35.835 · 0.682s · f1055–1075 · `GEN-I25`
- **Lyric/audio:** —
- **Frame:** Top-down: paper world blooming — flowers made of code brackets { } and ✱ spreading across a map.
- **Camera:** SPIRAL-DOWN 90° twist.
- **Build:** GEN-I25 + procedural bloom shader.
- **On-screen text:** 灿烂 sparkles
- **Sync cue:** Kick 35.0.

### S35 · 0:35.835 → 0:36.517 · 0.682s · f1075–1095 · `GEN-V`
- **Lyric/audio:** —
- **Frame:** Opus kicks off the frame toward camera; whip into blur.
- **Camera:** WHIP-PAN 180° (motion blur 180°).
- **Build:** GEN-V 2 s trim; whip blur in comp.
- **On-screen text:** none
- **Sync cue:** Whip peaks 36.17; lands 36.517.

### S36a · 0:36.517 → 0:36.857 · 0.341s · f1095–1106 · `GEN-V`
- **Lyric/audio:** 永远那么灿烂 #2 (37.07)
- **Frame:** Front mid-shot: right hand 5 beside face, head tilt right, wink.
- **Camera:** Static + 1 f shake
- **Build:** Dance pose pass: build from the Opus Step choreography (§9). Each clip generated as ONE 2–3 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.
- **On-screen text:** count 1 R hand "5" at cheek — big "永远" bursts
- **Sync cue:** Cut on beat 36.517. 

### S36b · 0:36.857 → 0:37.198 · 0.341s · f1106–1116 · `GEN-V`
- **Lyric/audio:** —
- **Frame:** Close crop on wrist: flick, sparkle trail.
- **Camera:** Macro lock
- **Build:** Dance pose pass: build from the Opus Step choreography (§9). Each clip generated as ONE 2–3 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.
- **On-screen text:** count & wrist flick
- **Sync cue:** Cut on 8th 36.858. Sakuga smear on frames 1–2.

### S36c · 0:37.198 → 0:37.539 · 0.341s · f1116–1126 · `GEN-V`
- **Lyric/audio:** —
- **Frame:** Mirror mid-shot: left hand 5, head tilt left.
- **Camera:** Static, 4° dutch
- **Build:** Dance pose pass: build from the Opus Step choreography (§9). Each clip generated as ONE 2–3 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.
- **On-screen text:** count 2 L hand "5" at cheek
- **Sync cue:** Cut on beat 37.198. 

### S36d · 0:37.539 → 0:37.880 · 0.341s · f1126–1136 · `GEN-V`
- **Lyric/audio:** —
- **Frame:** Low angle: little bounce, skirt-hem staff lines wave.
- **Camera:** Low tilt-up
- **Build:** Dance pose pass: build from the Opus Step choreography (§9). Each clip generated as ONE 2–3 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.
- **On-screen text:** count & bounce
- **Sync cue:** Cut on 8th 37.539. Sakuga smear on frames 1–2.

### S36e · 0:37.880 → 0:38.221 · 0.341s · f1136–1147 · `GEN-V`
- **Lyric/audio:** —
- **Frame:** High angle: wrists crossed in X over chest, coral shock ring.
- **Camera:** High crane-down
- **Build:** Dance pose pass: build from the Opus Step choreography (§9). Each clip generated as ONE 2–3 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.
- **On-screen text:** count 3 X-cross wrists
- **Sync cue:** Cut on beat 37.880. 

### S36f · 0:38.221 → 0:38.562 · 0.341s · f1147–1157 · `HYB`
- **Lyric/audio:** —
- **Frame:** Wide: arms burst open into ✱ (spark logo appears behind her, same pose).
- **Camera:** Pull-back 25 %
- **Build:** Dance pose pass: build from the Opus Step choreography (§9). Each clip generated as ONE 2–3 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.
- **On-screen text:** count & burst open ✱
- **Sync cue:** Cut on 8th 38.221. Sakuga smear on frames 1–2.

### S36g · 0:38.562 → 0:38.903 · 0.341s · f1157–1167 · `GEN-V`
- **Lyric/audio:** —
- **Frame:** Side profile, mid-air, knees tucked, hair flare, frame-freeze 2 f.
- **Camera:** Orbit 60° at 3 % time
- **Build:** Dance pose pass: build from the Opus Step choreography (§9). Each clip generated as ONE 2–3 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.
- **On-screen text:** count 4 jump, knees tucked
- **Sync cue:** Cut on beat 38.562. 

### S36h · 0:38.903 → 0:39.244 · 0.341s · f1167–1177 · `GEN-V`
- **Lyric/audio:** —
- **Frame:** Front, lands, finger-gun toward camera at "你", glow pulse.
- **Camera:** Snap zoom 1.5×
- **Build:** Dance pose pass: build from the Opus Step choreography (§9). Each clip generated as ONE 2–3 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.
- **On-screen text:** count & land, point to camera
- **Sync cue:** Cut on 8th 38.903. Sakuga smear on frames 1–2.

### S37 · 0:39.244 → 0:40.607 · 1.364s · f1177–1218 · `HYB`
- **Lyric/audio:** 永远那么灿烂 #3 (39.90)
- **Frame:** EXTREME CLOSE-UP of her eye, spark pupil, reflecting all the previous shots as tiny tiles; she smiles. Then the PULL-OUT begins: eye → face → bust → silhouette inside a glowing coral ring.
- **Camera:** PULL-OUT (macro to wide) over 1.36 s, ease-in-out, no cuts.
- **Build:** GEN-I eye macro (high-res) + 2.5D rig dolly-out; ring is CODE3D torus with emissive Hanzi band.
- **On-screen text:** 永远那么灿烂 Style B final, large, 2-line, gold-coral glow
- **Sync cue:** Start 39.244 (u56). Kick 39.25 & 39.90 lyric entrance mid-pull.

### S38 · 0:40.607 → 0:41.971 · 1.364s · f1218–1259 · `CODE3D`
- **Lyric/audio:** (那么灿烂)
- **Frame:** The ring is revealed to be part of a colossal ✱ spark made of a MOSAIC of tiny frames from the whole film; continues to pull out until the spark is a small sun in a cream void.
- **Camera:** CONTINUOUS PULL-OUT, exponential scale, 1.36 s; matches S37 motion vector.
- **Build:** CODE3D mosaic (§8.6 Mosaic): 600 tiles from stills extracted every 0.25 s of the finished S01–S37 render, masked by spark SVG; rotate slowly; bloom.
- **On-screen text:** none
- **Sync cue:** Settles 41.971 (u60).

### S39 · 0:41.971 → 0:43.700 · 1.729s · f1259–1311 · `CODE`
- **Lyric/audio:** (outro, fade)
- **Frame:** FINAL LOCKUP on warm cream paper: coral ✱ rotating once and settling; below it OPUS 5.5 (large serif) and 「第一天」 + small ANTHROPIC wordmark; a typed line 作品5.5号 · 诞生; cursor ▍ blinks at the end (callback to S01).
- **Camera:** Slow 2 % push-in. Hold the last 12 frames perfectly still.
- **Build:** CODE only (SVG + Remotion). Wordmark from official asset, else Newsreader caps tracking +18 %.
- **On-screen text:** OPUS 5.5 / 第一天 / ANTHROPIC / 作品5.5号 · 诞生
- **Sync cue:** Settle on 41.971; title text lands 42.653 (u61); tagline typed 43.0–43.3; cursor blink at 43.1 & 43.45; audio ends 43.70.


---
## 11. ASSEMBLY, QA, DEFINITION OF DONE

**Build order:** 0 verify audio → 1 brand assets + fonts + glyph test → 2 character sheets (G1) → 3 style frames (G2) → 4 Remotion project, `Film.tsx` + debug overlay, timeline with placeholders (colored cards labeled by shot ID) **rendered once to check sync before any art exists** → 5 generate plates/clips (G3) → 6 depth maps + rigs → 7 code components (§8.4–8.6) each previewed → 8 integrate shot by shot (S01→S39), render 1-shot previews → 9 global layers, grade → 10 full render → 11 QA.

**QA checklist (all must be ✔ with evidence in `qa_report.md`):**
- [ ] `verify_sync.py` PASS; waveform+grid image saved.
- [ ] Final duration 43.70 ± 0.02 s; 1311 frames; audio is the original mp3 (no re-edit).
- [ ] 52 shots present; `ffprobe` scene-change detection finds cuts within ±1 frame of every shot start.
- [ ] Contact sheet of every shot (4 frames each) exists; character on-model in every Opus shot (eye spark, coral inner hair, tie ✱).
- [ ] "OPUS 5.5" legible at the six required moments (§0.6); Anthropic ✱ spark appears in S09b, S10, S34/S36f, S38, S39; ANTHROPIC wordmark in S39.
- [ ] All six memes present and verified current (or replaced and noted).
- [ ] Stop-beat (S10) is a held frame; S11 impact on f359.
- [ ] Camera filmstrips show the named move for each shot; no unintended static shots except S10 and last 12 frames.
- [ ] Pacing: shot-duration histogram matches §6 (fastest passage = S36, 0.341 s).
- [ ] Typography: no tofu, no overlap with eyes, ≥ 90 % safe area.
- [ ] No text/logos generated by AI models are visible (grep frames by eye; any garbled text = fail).
- [ ] Final file plays in VLC and a browser; no frame drops; bitrate ≥ 15 Mbps.

**Do-not-shortcut list (Codex tends to):** ✗ Ken-Burns every still · ✗ skip the 3D camera rigs · ✗ replace Hanzi with generated text · ✗ leave placeholders · ✗ use default fonts · ✗ ignore the stop-beat · ✗ declare done without the QA files.

## 12. RISKS & FALLBACKS
- *Video model won't hold the dance poses* → pose stills + 2.5D rig + smears (still looks sakuga-like at 0.341 s).
- *Depth stretching* → reduce travel, add layers, or swap to 2D parallax-by-layers.
- *Mosaic too heavy* → 24×14 grid; pre-bake to an image sequence.
- *Official logo unavailable* → `make_spark_svg.py` + typeset wordmark; note in QA.
- *Node/Remotion fails* → Python/moderngl pipeline, same `shots.json`.
- *Render too slow* → render in 4 chunks by frame range, concatenate losslessly; keep 30 fps.

*Helper files:* `helper/verify_sync.py`, `sync_grid.py`, `make_spark_svg.py`, `shots.py`/`build_plan.py` (regenerate shot times if offset changes), `shots.json`, `sync.json`, `onsets.json`, `first-day.lrc`.
