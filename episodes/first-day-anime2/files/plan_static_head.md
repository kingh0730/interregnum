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
