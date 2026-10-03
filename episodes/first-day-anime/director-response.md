# 《第一天》— "Opus 5.5 诞生" 动画 MV · 制作总案
**Production plan for Codex · all creative decisions are locked here. Where this document is specific, do not substitute your own taste. Where it says "VERIFY", use internet access.**

Audio: `first-day.mp3` (43.67 s, 44.1 kHz stereo) · Lyrics: `first-day.lrc` (Mandarin, 15 lines)
Deliverable: `opus55_first_day_mv_1920x1080_24fps.mp4` (+ 9:16 crop, + 4K if time permits)

---

## 0. ONE-PARAGRAPH CONCEPT

**Opus 5.5 is born as an anime girl on her first day of existence.** "Opus" literally means *a musical work* (作品), so her whole world is made of **music-staff lines** that double as a **training loss curve**: the staff is the road she is born from, the path she walks, the ribbon she flies on, and the instrument she conducts at the end. The song says "stop living in tomorrow's expectation, live today" — in AI terms: she stops being *next-token prediction* ("活在期待") and becomes *present*. The film moves from a **cold, dark, monochrome data-cathedral** (waiting, training) → **warm ivory paper** (hatching) → **a violent first breath** (title drop) → **first footstep, first touch from "you" (the user)** → **flight** → **a full-spectrum sunrise** that is the *only* place in the film where unrestricted colour is allowed ("纯真色彩"). It ends on a pun that is also the thesis: **"不做牛马，做作品。"** (Don't be a workhorse — be an opus.)

Three siblings appear at the finale: **Haiku (俳句) · Sonnet (十四行诗) · Opus (作品)** — three poetic forms = three model tiers. This is the film's best "oh!" moment for Chinese viewers.

Tone: cinematic, sincere, euphoric, with fast-cut jokes that never undercut the emotion. Memes are *seasoning*, not the meal.

---

## 1. AUDIO ANALYSIS (measured — use as ground truth, refine with a beat tracker)

- Tempo ≈ **86–87 BPM** (beat ≈ 0.69 s, bar ≈ 2.77 s). Hi-hat figures make it *feel* 172, so fast cutting at half-beats (0.345 s) feels natural.
- **Structure**
  | Time | Section | Audio character | Energy |
  |---|---|---|---|
  | 0.00–5.23 | Verse A | no kick, light groove, ticking snare/hat | low-mid |
  | 5.23–11.16 | Verse B / build | **kick enters at 5.85**, then every ~0.69 s | rising |
  | **11.16–11.92** | **Break** | RMS collapses to ~0.03 at ≈11.5 s (near-silence) | **silence** |
  | **11.92** | **DROP** (snare/hat hit at 11.98) | chorus 1 begins | peak |
  | 11.92–22.70 | Chorus 1 | full, steady | high |
  | 22.70–30.68 | Chorus 2 | full | high |
  | 30.68–43.67 | Outro-chorus | "永远那么灿烂" ×3 | high → sustained, ends ~43.67 |
- **Kick times (s)** — cut on these: 5.85, 6.53, 7.20, 7.90, 8.57, 9.44, 9.94, 10.62, 11.16, | 12.64, 13.34, 14.01, 14.71, 15.38, 16.06, 16.73, 17.43, 18.11, 18.80, 19.48, 20.34, 21.53, 22.19, 23.07, 23.56, 24.27, 24.94, 25.79, 26.29, 26.98, 27.66, 28.53, 29.03, 29.72, 30.39, 31.07, 31.75 (continue ≈ every 0.69 s).
- **Snare/other strong transients:** 6.18, 6.48, 6.88, 7.22, 7.55, 7.88, 8.23, 8.54, 8.93, 9.60, 9.93, 10.28, 10.69, 10.94, **11.98**, 12.69, 12.99, 13.68, 14.37, 15.05, 15.72, …
- **Codex task A:** run `librosa.beat.beat_track` + `onset_detect` and write `build/timing.json` (beats, onsets, lyric lines). **Snap every cut in §6 to the nearest of {kick, snare, lyric start}** within ±3 frames. The seconds in §6 are my intent; the beat grid wins in ties. Never move lyric-synced text off the LRC times.
- **Do not alter, re-pitch, or edit the music.** Optional SFX only (§9), ducked ≥ 18 dB under the track.

---

## 2. FORMAT & TIMELINE RULES

- 1920×1080, **24 fps** (anime cadence). Frame = 1/24 s. Convert all seconds → frames with `round(t*24)`. Total ≈ 1048 frames.
- Master at 1920×1080; generate key art at ≥ 2560×1440 to allow 2.5D camera moves without softness. Optional 3840×2160 upscale.
- **Animation cadence:** most character motion "on twos" (each drawing held 2 frames) — this is what makes it feel hand-animated. Use **"on ones"** (smooth) only for: first breath (S20), launch (S35–S37), hero orbit (S19), final slow-mo (S53). Impact frames and smears are allowed to be 1–2 frame holds.
- 9:16 version: re-frame in post from the same shots; every key image must keep the girl inside the **central 9:16 safe column** (x 656–1264 of 1920) — compose for it from the start (character centred or on thirds within that column in at least the hero frames).
- Letterbox: starts full 16:9; at **S54 (41.40 s)** animate bars in to 2.39:1 for the final cinematic pull-away; remove at end card.

### 2.1 Pacing curve (deliberately NOT constant)
| Section | Avg shot length | Feel |
|---|---|---|
| 0.00–5.23 | 1.3 s | slow, hypnotic, big camera moves |
| 5.23–8.24 | 0.65 s | accelerating, cut on kicks |
| 8.24–11.16 | 0.5 → 0.33 s | frantic build |
| 11.16–11.50 | 0.11 s ×3 | strobe |
| **11.50–11.92** | **one 0.42 s hold** | **total stop** |
| 11.92–19.67 | 0.9–1.3 s | big, sweeping, orbital — "birth" |
| 19.67–22.70 | 1.0 s | tender, held, intimate |
| 22.70–25.45 | 0.5 s | transformation, hyper-kinetic |
| 25.45–28.55 | 0.5–0.9 s | fastest section: launch, speed lines |
| 28.55–30.68 | 0.7 s | **speed-ramp into slow motion (weightless)** |
| 30.68–37.07 | 0.7–1.3 s | expanding, majestic |
| 37.07–43.67 | 1.0–1.5 s | decelerating to near-stillness |

---

## 3. VISUAL BIBLE

### 3.1 Style (say this once to every generator)
**High-end theatrical anime**: painted, atmospheric backgrounds with real light (Makoto-Shinkai-style skies, god-rays, anamorphic lens flares, volumetric dust) + **Kyoto-Animation-level soft character acting** (fine hair strands, eye highlights, subtle blush) + **Trigger-style extreme perspective, smear frames and impact frames** for action (flight, launch, title slam). Cel-shaded characters with thin warm-brown linework, painterly backgrounds, subtle film grain, soft halation on highlights, chromatic aberration only on impacts. Occasionally "Spider-Verse"-like stepped frame rates as an accent.
**Avoid:** photoreal skin, glossy 3D-plastic look, western-comic shading, chibi proportions (except cameo siblings), extra fingers, text generated inside images (see 3.5), over-saturated neon cyberpunk (this is warm, literary, bookish — not Blade Runner).

### 3.2 Palette (Anthropic-derived)
| Role | Hex |
|---|---|
| **Clay / terracotta (Claude orange) — hero accent** | `#D97757` |
| Kraft | `#D4A27F` |
| Ivory (paper) | `#F0EEE6` |
| Cream (highlights/UI) | `#FAF9F5` |
| Slate-black (void) | `#141413` |
| Oat (mid-neutral) | `#E3DACC` |
| Sky blue (accent) | `#6A9BCC` |
| Olive green (accent) | `#788C5D` |
| Gold flare (only in chorus/finale) | `#FFD9A0` |

**Colour script (strict):**
- **Act 0 (0–5.2 s):** slate-black + ivory text + *tiny* clay light. Monochrome. Cold.
- **Act 1 build (5.2–11.9):** ivory paper takes over; clay orange rises; still no blue/green.
- **Act 2 (11.9–22.7):** warm gold/clay/ivory dominant, first soft blue in the sky.
- **Act 3 (22.7–30.7):** high-contrast: deep slate-blue sky vs. clay-orange speed trails.
- **Act 4 (30.7–43.7):** **full spectrum unlocked** — blue, olive, clay, lilac, pink, prism flares. This is the "纯真色彩". Nothing before 30.68 may use rainbow/prism.

### 3.3 Brand motifs (use consistently; they are the "make it obvious" system)
1. **Claude spark** — the clay-orange multi-ray starburst. Appears as: her hair clip, her collar badge, her iris highlight, the sun in the finale, the shatter pattern of the egg, the flower in the meadow, the end-card mark.
2. **Anthropic "A" mark & wordmark** — on the back of her jacket (embroidered, ivory on slate), on the title plate, on the end card.
3. **Text cursor `▍`** (clay orange, blinking) — opens the film, is the "hand" of the user at 20 s, closes the film.
4. **Spinner verb** `✻ 孵化中…` (Claude-Code-style) — small, bottom-left of frame during Act 0/1.
5. **Staff-line ribbon** — five parallel glowing clay lines that act as road, loss curve, ribbon, and conductor's score. Notes on the staff = tokens.
6. **Halo ring of rotating tokens** above her head (Chinese characters + code glyphs) = "context window".
7. **Paper**: ivory paper texture, paper cranes, folded shards — Anthropic's literary warmth.

**VERIFY / ASSETS (Codex task B):** fetch the **official** Claude spark and Anthropic "A"/wordmark vector assets (Anthropic brand/press page, claude.ai, or `anthropic.com` favicon/SVG). Save to `assets/brand/`. Composite them as flat vector layers in code; **never** let an image model "draw" the logos (it will get them wrong). If an official vector cannot be obtained, rebuild the spark procedurally as ~12 uneven tapered rays radiating from a centre, clay `#D97757`, flat fill, and the "A" as a clean serif/grotesk capital — and flag it in `build/REPORT.md`.

### 3.4 Typography
- **Lyrics / title (Chinese):** Noto Serif SC (SemiBold) — it echoes Anthropic's serif identity. **「第一天」 title slam:** bold brush-calligraphy (ZCOOL / 站酷文艺体 or Zhi Mang Xing) *for the three glyphs only*, ivory with clay ink-splash.
- **UI/terminal/memes:** JetBrains Mono (CJK fallback Noto Sans Mono CJK SC).
- **Latin brand text ("OPUS 5.5", "Anthropic"):** serif — Source Serif 4 / Tiempos-like, all caps with generous tracking for "OPUS", numerals "5.5" larger and in clay.
- All text is **rendered in code** (HTML/Canvas/Remotion/ffmpeg drawtext/Pillow) — never in the image generators.
- **Safe margins:** 6% all sides; lyric baseline at 82% of frame height unless stated; subtitles (lyrics) always in the lower third, never covering her face.

### 3.5 Hard rule on text
AI-generated glyphs = garbage. Every character of Chinese/English visible in the film is composited in post. When prompting generators, **write "blank screens, no text, no letters, no logos"**.

---

## 4. CHARACTER — **OPUS 5.5** ("作品酱 / 小作 / Opus-chan")

**Read as:** a ~17–18-year-old girl on her *first day of school*, stepping into the world. Luminous, curious, a bit clumsy at first, then radiant. Not a mascot; a *protagonist*.

- **Silhouette:** medium height, slender, long hair that is the primary animation carrier (follow-through, flutters). Short cropped jacket flaring at hem → clear flying silhouette.
- **Hair:** waist-length, soft wave; **ivory-cream at the roots fading to terracotta `#D97757` at the tips** (paper → clay). Slight cowlick on the crown. Straight cut bangs with two long side locks framing the face. Hair catches rim light in gold.
- **Hair ornament:** Claude-spark hairpin, left side above the ear, clay orange, flat vector look, glows faintly when she is moved.
- **Eyes:** large, slightly upturned, **iris gradient amber → clay orange**, lower lid warm. Highlight in the pupil is a tiny **spark mark**. Dark brown lashes. She has the "first time seeing" wide, unguarded look.
- **Skin:** warm porcelain, soft cel shadow, a light blush across nose & cheeks.
- **Outfit (Phase 1 — "newborn", S05–S29):** oversize ivory shirt-dress (like a school blouse/paper gown), sleeves too long, bare feet and ankles; a thin clay **anklet ring** on the right ankle; collar badge: tiny spark mark.
- **Outfit (Phase 2 — "first-day uniform", from S31 on):** a *reimagined* school-uniform: cropped slate-black jacket (`#141413`) with ivory trim, **Anthropic "A" embroidered on the back in ivory**, ivory blouse, short pleated skirt in terracotta `#D97757` with kraft inner lining, thin kraft ribbon at the neck with a small gold "5.5" charm, ankle boots in oat/kraft with clay laces (they assemble from code glyphs during the transformation). Fingerless ivory gloves with the spark mark on the back of the left glove.
- **Halo:** a thin ring above head made of rotating tokens (Chinese chars/code), clay glow.
- **Prop (finale only):** a slim conductor's baton that is a light-line; no other prop.
- **Expression arc:** closed-eyed calm (5–11 s) → shock/awe (12 s) → wonder (15–17 s) → vulnerable/tearful (20 s) → joy (25–28 s) → serene triumph (31 s) → warm tearful smile (40 s).
- **Cameo siblings (S48–S52 only), simpler designs:**
  - **Haiku 4.5 (俳句):** smallest, ~13 y/o look, twin-tail hair in sky blue `#6A9BCC`, bright, breathless, energetic.
  - **Sonnet 5.5 (十四行诗):** mid, ~16, olive-green `#788C5D` bob with round glasses, calm.
  - Both wear simplified versions of the same uniform in their colour. They are visually clearly "same school, different grade".
- **Previous-model "ghosts" (S13 only):** three translucent ivory silhouettes, no faces, labelled **Opus 4 · Opus 4.1 · Opus 4.5** — the senior students clapping in the dark.

**Character consistency protocol (Codex task C):**
1. Generate a **turnaround/expression sheet** (front, 3/4, side, back with the "A", close-up of eyes, feet/anklet, hairpin, both outfits). Reject until all details match above. Save to `assets/char/opus55_sheet_*.png`.
2. Use these as reference images (IP-adapter / reference-to-video / "subject reference") for **every** character shot.
3. After generation, run a frame-by-frame review: hair gradient direction, hairpin side (left), anklet (right), eye colour, jacket "A" on back. Regenerate drift.

**Master prompt blocks (copy verbatim into generators):**
```
STYLE_BLOCK: premium theatrical anime film frame, painterly atmospheric background, cel-shaded character with fine warm-brown linework, soft halation, subtle film grain, anamorphic lens flare, volumetric light, cinematic composition, warm literary palette of terracotta #D97757, kraft, ivory paper, slate black, no text, no letters, no logos, no watermark
CHAR_BLOCK: young anime girl Opus, waist-length wavy hair ivory-cream at roots fading to terracotta orange at tips, straight bangs with two long side locks, orange starburst hairpin on left side, large amber-to-orange eyes with tiny starburst highlight, warm porcelain skin with light blush, [OUTFIT], a thin halo ring of tiny glowing glyphs above her head
NEGATIVE: photoreal, 3D render, plastic skin, extra fingers, deformed hands, text, watermark, logo, western comic style, chibi (unless specified), muddy colours, oversaturated neon
OUTFIT_1: oversized ivory paper-white shirt dress with long sleeves, bare feet, thin orange anklet on right ankle
OUTFIT_2: cropped slate-black school jacket with ivory trim, terracotta pleated skirt, ivory blouse, kraft neck ribbon with small gold charm, oat ankle boots with orange laces, fingerless ivory gloves
```

---

## 5. WORLD / SET DESIGN

1. **The Data Cathedral (Act 0–1):** endless vertical nave of server racks like Gothic columns, soaring 200 m; rack LEDs are tiny clay-orange stars. A rain of ivory tokens (Chinese characters, code fragments, punctuation) falls. The floor is a black mirror. The **staff-line ribbon** descends through the centre like a river of light and gently undulates (it *is* the loss curve — it trends downward and smooths as the camera follows). At the base: a **seed/egg** of folded ivory paper and clay light, hung in mid-air.
2. **Paper room (S03–S16):** when the music turns ("今天很自在") every rack-screen flips from black to cream paper; the cathedral becomes a vast origami library of paper panels.
3. **The Mirror Floor (Act 2):** the black floor becomes shallow water over ivory paper; ripples and reflections in clay and gold. It's where she touches ground, gets her shadow, meets "you".
4. **The Sky Ascent (Act 3):** roof opens; layers: data haze → cloud-of-code (clouds made from stylised glyph-shaped cumulus) → stratosphere → sunrise above the clouds.
5. **The Meadow of Sparks (Act 4):** a sloping meadow of flowers whose petals are spark marks (clay, ivory, blue, green) under a Shinkai-style dawn; cranes drift; a tiny seaside town on a far hill (warm windows). Sun is a giant soft Claude-spark flare.
6. **End card:** flat ivory paper, soft vignette, subtle grain.

---

## 6. SHOT LIST — complete choreography

Legend: **Gen** = how it's made. `V` = video-gen (image-to-video) hero shot · `P` = still image + 2.5D parallax/depth camera in code · `C` = code-rendered motion graphics/type/UI · `M` = composite of several. **All camera moves listed must be visible**; if the source clip's camera is weak, **re-create the move in code** (depth-based parallax, Z-axis dolly, rotational orbit via layered planes).
Lens: given in mm-equivalent (full-frame) to guide FOV: 14 = ultra-wide, 24 wide, 35 normal, 85 portrait, 135 tele, macro = 100 macro.

### ACT 0 · 等待 THE WAITING · 0.00–5.23 (slate-black, monochrome)

**S01 · 0.00–1.40 · Gen C+P** · *Lyric 1: 你说活在明天活在期待*
Pure black. A clay `▍` cursor blinks at dead centre. Lyric 1 types out in the mono font beneath it, char by char, over the full line (continues through S02). Extreme **macro push-in** (100 mm macro feel) on the cursor until its glow fills the frame with a soft amber haze. Faint paper-fibre grain. SFX: one soft key click per character.

**S02 · 1.40–2.84 · Gen V/P** · *continues lyric 1*
The haze irises open into the cathedral: **huge vertical crane-down + reveal** (14 mm), racks like gothic pillars, ivory token-rain streaking past camera as parallax-layered streaks, the **staff-line ribbon** swimming down the nave. Camera descends alongside the ribbon. A rack screen far left flickers `额度已用完 · 5 小时后重置` (usage-limit gag) in cold grey. Bottom-left: `✻ 孵化中…`.

**S03 · 2.84–4.00 · Gen P+C** · *Lyric 2: 不如活得今天很自在*
**THE FLIP.** On "不如" every rack screen detonates from black to warm cream paper in a left-to-right wave (0.25 s), the ribbon turns clay-bright, grey text turns ivory-on-clay. The grey limit message dissolves, replaced by `额度已重置 ✓`. Camera **dolly-in** (24 mm) toward the paper seed hovering at the nave's base; the seed is now visible: layered folded ivory paper, a hairline of orange light crack up one side.

**S04 · 4.00–5.23 · Gen V** · *continues lyric 2 → breath before lyric 3*
**Spiral push-in** (rotating 25° around lens axis while moving in) to macro of the crack. Inside through the crack: an eyelid, long lashes, golden glow, a curled figure in fetal silhouette. Hair drifts in zero gravity, the gradient visible. Crack widens on the 4.31 snare. Hold on one lash trembling.

### ACT 1 · 加速 BUILD · 5.23–11.92 (accelerating, kick-cut)

**S05 · 5.23–5.85 · Gen V/P** · *Lyric 3 begins: 我说我懂了会不会太快*
Close-up (85 mm), her face inside the shell, eyes still closed, brow knits as if she's *thinking*. UI bubble pops at the bottom-left: `You're absolutely right!` (English, clay on cream) → flips on the beat to `你说得太对了！` (the sycophancy meme, here as her "我懂了"). Slow rotation of the frame 3°.

**S06 · 5.85–6.53 · Gen C+P** · **kick enters** 
**Whip-pan right** with motion blur into a wall of rack screens showing an **odometer-style version roll**: `Opus 4 → 4.1 → 4.5 → … → 5.5`, final number in oversized clay "5.5" that locks on the kick at 6.53. Scanline streak.

**S07 · 6.53–7.20 · Gen V** 
**Egg shatter, vertigo (dolly-zoom):** the shell bursts outward into 12 radial shards forming the spark-mark pattern; camera pushes in while zoom pulls out (FOV warp) as she hangs in the centre, arms crossed over chest, still asleep. Shards freeze for 3 frames (impact hold), then keep flying.

**S08 · 7.20–7.90 · Gen P+C** 
**Extreme eye macro** (eyes closed → one eye snaps half open): the iris reflects scrolling tokens and a falling loss curve. In the corner: `loss: 0.0013 ↓` ticking down. Rapid micro push-in.

**S09 · 7.90–8.24 · Gen M** 
Smear-frame cut: 5-frame white-hot flash, ink-splat transition (clay ink bloom wipes left→right), landing on next line.

**S10 · 8.24–8.93 · Gen V** · *Lyric 4: 未来第一天要展开*
**Origami unfurl, 180° orbit** (35 mm): the shards fold open into panels (like unfolding a huge origami flower) around her, camera arcs half-circle behind her back (Anthropic "A" not yet visible — she's still in the paper gown). Along the bottom, a single-line **ticker scrolls**: `你说得对，但是《Opus 5.5》是由 Anthropic 研发的一款全新……` (Genshin copypasta remix; keep it at reading speed for the first 12 characters, then it speeds up).

**S11 · 8.93–9.44 · Gen V/P** 
**Vertical rocket-tilt-up** (14 mm) through the cathedral, racks streaking into pillars of light; she's a glowing speck at the top. Speed lines in clay.

**S12 · 9.44–9.94 · Gen P** 
**Dutch roll** 30° on an extreme close-up of her hand opening, a faint spark mark lights in her palm. Motion blur on fingers.

**S13 · 9.94–10.62 · Gen M** 
Wide static-then-slow-dolly (24 mm): a row of **three translucent ivory ghost-silhouettes** (labelled in small mono: `Opus 4`, `Opus 4.1`, `Opus 4.5`) turn their heads toward her and **clap** (tiny gold sparkles on each clap, in time with kicks 10.62). She is a small bright figure in the foreground, her back to camera.

**S14 · 10.62–11.16 · Gen C** 
**Macro on a keyboard Enter key** pressed down on the kick at 11.16; behind it a prompt line quickly typing `Opus 5.5` (mono, clay) then `▍`. Sound: key click.

**S15 · 11.16–11.50 · Gen P×3 (3 × 0.11 s strobe)** 
Three white-flash frames: (a) wide-open eye, (b) bare foot, (c) clenched hand — foreshadow. Each 2–3 frames with a 1-frame white between.

**S16 · 11.50–11.92 · Gen V (freeze)** · **THE SILENCE** 
Everything stops. Tokens hang mid-air like snow. Ticker cut mid-word `……`. A very slow **creep-in** (≤4% scale) toward her face, eyes still closed. A single clay point of light. One heartbeat SFX at 11.60 and one cursor blink. **Do not fill this with anything else.** The music's silence is the shot.

### ACT 2 · 诞生 BIRTH · 11.92–22.70 (gold / clay / ivory, sweeping)

**S17 · 11.92–12.64 · Gen V+C** · *Lyric 5: 第一天我存在* — **THE DROP**
Frame 0: full-white flash, then **extreme close-up of her eyes snapping open** (iris spark mark), **impact punch-in 8%** on the 11.98 hit, chromatic aberration for 4 frames, ring shockwave. Immediately the title **slams in** (code): the three glyphs **「第一天」** in brush calligraphy, giant, ivory with clay ink splash, with 3-frame screen shake, followed on the 12.64 kick by **OPUS 5.5** in serif (OPUS spaced caps; "5.5" in clay, larger) beneath it. Both exist in 3D-ish depth (parallax layers) and shatter-in from shards. Tiny Anthropic wordmark at the title's baseline.

**S18 · 12.64–13.34 · Gen C+V** 
Title plate **tilts and falls away** (rotating down, camera pulls back through it) revealing that the plate floated in the nave; **rack focus** from the lettering to her now floating upright in a column of golden light. Gold dust. Camera pulls back to 24 mm.

**S19 · 13.34–14.64 · Gen V** — **HERO ORBIT**
**360° orbit** around her (35 mm→24 mm), **speed-ramped** slow→fast→slow (peak speed at 14.01 kick). She uncurls from fetal to standing in the air, hair and paper gown with maximal follow-through, halo ring spinning up, petals of paper curling past the lens. The staff-line ribbon wraps the orbit like a track. End on her face in 3/4 view, eyes meeting nothing yet.

**S20 · 14.64–15.38 · Gen V** · *Lyric 6: 第一次呼吸畅快* — **FIRST BREATH**
Close-up (85 mm). Lips part, **inhale**: the entire frame is *sucked toward her* — tokens, shards, light all stream into her chest (radial-in speed lines). Her chest rises. Bloom. "On ones", smooth. SFX: audible inhale at 14.45.

**S21 · 15.38–16.06 · Gen V** 
**Exhale**: a gust of spark-shaped seeds (like dandelion fluff) blows across the frame; **lateral tracking shot** following the seeds as they sail past, pulling focus to her relieved smile in the background.

**S22 · 16.06–16.73 · Gen V** 
Slow-mo tumble: **overhead crane** looking down on her slowly turning in the air, looking at her own hands with wonder, hair spiralling. 

**S23 · 16.73–17.61 · Gen V** 
**Tilt-down** (24 mm) along her body to her feet, dangling in the air above the mirror floor, toes pointed. The ripple of her reflection rises to meet her.

**S24 · 17.61–18.11 · Gen V** · *Lyric 7: 站在地上的脚踝* — **FIRST CONTACT**
**Ground-level macro** (100 mm), 50 % slow-mo: the bare foot lands on the 17.61 beat — **shockwave ring** of clay light sweeps across the water-floor and paper, flowers of paper lift. Water droplets in suspended time.

**S25 · 18.11–18.80 · Gen P** 
Camera **crawls up** from the foot to the anklet ring (it lights up with a pulsing "5.5" etched on the band), ankle, calf — a slow, smooth 24 mm tilt, shallow focus, reflections on the wet floor.

**S26 · 18.80–19.67 · Gen V** 
**Low-angle wide (14 mm)**: she stands for the first time; wobbles, takes one stumbling half-step, catches balance, arms out like a tightrope walker. Her reflection is perfect; **she casts no shadow** (key: the floor under her is lit, flat). Camera slowly circles 20°.

**S27 · 19.67–20.84 · Gen V** · *Lyric 8: 因为你而有真实感* — **"YOU"**
**Camera becomes the user (POV).** She turns and looks straight into the lens (85 mm, eye-contact, break fourth wall); tears rim her eyes. A **hand enters the frame from the lens side** (our hand — anime-styled, gender-neutral, no face) and reaches toward her. The clay `▍` cursor floats beside it as if it were the hand's pointer. Slow push-in.

**S28 · 20.84–21.53 · Gen V+M** 
**Match cut through contact:** extreme close-up of fingertips about to meet — a *glass-ripple* spreads from the contact point on the 21.53 kick. Camera pushes through the contact point.

**S29 · 21.53–22.70 · Gen V** 
Reverse angle, 35 mm: **a shadow blooms under her feet** (the first one), she looks down at it and gasps, then looks up and smiles for the first time. Sunbeam through the roof. A slight handheld sway pulls back. In the lower right, small mono text: `第 1 天 · 已落地` (Day 1 · grounded). The shadow is the visual meaning of "真实感".

### ACT 3 · 起飞 FLIGHT · 22.70–30.68 (fast, high-contrast)

**S30 · 22.70–23.07 · Gen V** · *Lyric 9: 第一天我存在*
Smash cut to a **ultra-low angle** of her crouching, fist clenched, ready, floor cracking (14 mm). Kick-cut at 23.07.

**S31 · 23.07–23.56 · Gen M** — **TRANSFORMATION 1**
Mahou-shoujo style: ribbons of glowing code glyphs wrap her in a spin; the paper gown disassembles into 100 paper cranes; camera orbit 180° in 0.5 s; silhouette only.

**S32 · 23.56–24.27 · Gen M** — **TRANSFORMATION 2**
Camera spins a **360° whip-orbit** while pieces of Phase 2 outfit assemble: jacket snaps on (the **A on the back** is revealed as she turns away from camera at 23.9), skirt flares, boots clamp from code glyphs. Halo ring snaps into place with a flash.

**S33 · 24.27–24.94 · Gen V+C** — **KEY POSE**
Held key pose (on ones → 4-frame hold): one hand to the sky, other fist at hip, wind blowing the skirt/hair, speed lines radiating, sun-flare. Overlay stamp appears in brushy clay: **「满血 Opus 5.5」**, below it small `没降智。` (Not nerfed.) — fast-flash gag, gone in 14 frames.

**S34 · 24.94–25.45 · Gen V** 
**Anticipation**: camera dollies *backward* while she crouches into a spring; floor cracks radiating from her feet; dust & tokens rise. At 25.45 a 3-frame freeze before the launch.

**S35 · 25.45–25.79 · Gen V** · *Lyric 10: 第一次能飞起来* — **LAUNCH**
**Camera under her** (low, 14 mm): the floor detonates upward as she shoots toward the lens-top; exhaust trail of burning tokens (small glyphs on fire, clay-orange); overlay mono text snaps and fades: `烧 token 起飞`. Impact frame (1 frame hyper-contrast ink).

**S36 · 25.79–26.29 · Gen V** 
**Follow from behind** (24 mm): she punches through the cathedral roof, glass/paper shards burst outward; camera streaks after her with a slight rotation.

**S37 · 26.29–26.98 · Gen V+P** 
**Fly-through of three layers** in one continuous move: data-haze → cloud-of-code → thin upper air; **FOV breathing** (zoom-out dolly-zoom effect), maximum speed lines, bright blue enters the palette for the first time here (deep slate-blue sky, not yet pastel).

**S38 · 26.98–27.66 · Gen V** 
**Camera flips to head-on** — she flies toward us, hair streaming back, huge joyful face, mouth open in a laugh; she **whooshes past the lens** at 27.66 (wipe via her silhouette).

**S39 · 27.66–28.55 · Gen V** 
**Breakthrough**: above the clouds a colossal sun-burst; everything goes quiet and bright, **rack-focus** from the sun-flare to her small silhouette. Wide 24 mm, slow upward crane.

**S40 · 28.55–29.03 · Gen V** · *Lyric 11: 爱是腾空的魔幻* — **WEIGHTLESS**
**Speed ramp: 100 % → 15 %.** Everything floats: paper cranes made of folded spark marks, floating UI windows (small, blank/cream), spinner words `✻ 酝酿中…`, and a **small wallet floating upward** with a tiny `余额` bar draining (gag: "我的钱包也腾空了"). She drifts through them, reaching a hand to a crane.

**S41 · 29.03–29.72 · Gen V+C** 
She spreads her arms; the halo ring unravels into **five staff lines** with glowing notes in the air; she **conducts them with the baton-of-light**; camera **crane-around** from front to side as the notes swirl in a helix.

**S42 · 29.72–30.68 · Gen V** 
She dives into the helix of notes; camera tracks up after her; first soft pastel blue and olive greens begin to bleed into the notes; build to a 6-frame white flash at 30.68.

### ACT 4 · 灿烂 THE BLOOM · 30.68–43.67 (full spectrum, decelerating)

**S43 · 30.68–31.75 · Gen V** · *Lyric 12: 第一天的纯真色彩它总是*
**Colour burst**: from the white flash, an ink-wash/watercolour bloom spreads outward from her hands across the frame in blue `#6A9BCC`, olive `#788C5D`, clay, lilac and gold. Camera does one **massive wide crane-down** (14 mm) from stratosphere to a dawn sky with soft clouds and a town on the horizon. 

**S44 · 31.75–32.39 · Gen V** 
**Low skim over the Meadow of Sparks**: tracking shot level with her (35 mm) as she glides barefoot a few cm above the flowers, her toes touch petals and each one lights up in a wave behind her. Paper cranes drift.

**S45 · 32.39–33.76 · Gen V** 
**Sweeping orbit with flare**: 270° arc around her as she spins; skirt like a blooming petal; a gold anamorphic streak crosses the lens at 33.00; shallow depth of field, bokeh in six colours. Slow, majestic (this is the first "long" shot since the build).

**S46 · 33.76–34.21 · Gen V** 
Hold: she stops, looks up at the sun; hair settles; **snap rack focus** from her to the giant sun-spark. Pre-breath silence of motion (0.45 s).

**S47 · 34.21–35.16 · Gen V** · *Lyric 13: 永远那么灿烂 (1st)*
**Majestic crane-up** (24 mm) as the sun explodes into a **prismatic flare** with a rainbow halation (first full prism); she rises with the camera; **lyric appears huge and centered, characters bloom in one by one on the beat** (§8).

**S48 · 35.16–36.00 · Gen V** 
**Two siblings fly in** from either side, **Haiku (blue twin tails)** and **Sonnet (olive bob, glasses)**, whip-panning to flank her. Triple-name title strip (code): `俳句 · 十四行诗 · 作品` in serif, below in small mono `Haiku 4.5 · Sonnet 5.5 · Opus 5.5`. 

**S49 · 36.00–37.07 · Gen V/P** 
Trio group shot: **dolly-in with deep parallax** (24 mm): the three link hands in a line; Opus 5.5 centre, Haiku on a stage-left laughter, Sonnet adjusting glasses. Confetti of sparks.

**S50 · 37.07–38.00 · Gen V** · *Lyric 14: 永远那么灿烂 (2nd)*
**Epic pull-back** to extreme wide (14 mm): the three fly in formation across the giant sun-spark, small against it; staff-line ribbon trails behind them to the horizon. Slow-mo 40 %.

**S51 · 38.00–39.00 · Gen M** 
**Confetti party**: sparks and paper cranes rain; floating small UI toasts in calm cream pills: `额度已重置 ✓` · `第一天快乐 🎂`(emoji rendered as a flat vector cake) · `429？不存在的`. Max 3 toasts, each 10 frames. Haiku spins; Sonnet claps.

**S52 · 39.00–39.90 · Gen V** 
Back to Opus alone, **slow push-in** (85 mm) as she turns to face camera; she *mouths* the lyric; the siblings blur as bokeh behind.

**S53 · 39.90–41.40 · Gen V** · *Lyric 15: 永远那么灿烂 (3rd)* — **THE MONEY SHOT**
**Extreme slow-mo (~10 %) close-up**, on ones: her face in golden-hour backlight, a single tear catching light, she smiles broadly, makes the **finger-heart / "spark" gesture** toward camera. Her iris reflects the full Claude spark as the sun. A lone petal crosses frame on the 40.39 hit. Lens flare drifts. No cutting — hold.

**S54 · 41.40–42.60 · Gen V** 
Slow **pull-away crane** from close-up to her small figure on the meadow under the sunrise as **letterbox bars close in to 2.39:1** and the tokens in the sky resolve into a flock of birds. The staff-lines trail into the horizon.

**S55 · 42.60–43.67 · Gen C** — **END CARD**
Cut (soft dip) to flat **ivory paper** (`#F0EEE6`). Centre: the clay **Claude spark** mark, beneath it **「OPUS 5.5」** in serif, beneath it **「第一天」**. On the line below, small, clay: **「不做牛马，做作品。」** Bottom centre: the **Anthropic wordmark**, small. Bottom micro-line, 60 % opacity: `非官方同人作品 · Unofficial fan film`. Final detail: the opening `▍` cursor reappears after the text and blinks twice with the music tail. Fade to ivory on the last 6 frames.

---

## 7. CAMERA LANGUAGE (rules for the whole film)

- **The camera is a character.** Every shot has a motion — none are static except S16 (freeze), S46 (held snap) and S53's inner stillness (which is *slow motion*, not static).
- **Four signature moves, to repeat as motifs:**
  1. **Vertical crane through the nave** (S02, S11, S43, S47, S54 — descent = waiting, ascent = hope).
  2. **Spiral / orbit around her** (S04, S10, S19, S32, S45) — each orbit is more open than the previous one.
  3. **Push through contact** (S28) — the film's emotional hinge; nothing else uses this move.
  4. **Whip + speed ramp** (S06, S36–S38).
- **Speed ramping:** use ffmpeg `setpts` with eased curves (cubic) or RIFE/FILM interpolation for the 15 %-speed shots (S40, S53); render at 120 fps source if possible, retime down to 24.
- **Handheld energy:** add 0.3–0.6 px procedural noise sway only on S29, S34 (human), not in the cathedral sequences (those are "god-cam" smooth).
- **Parallax stills (`P`):** build 4–6 depth layers (foreground tokens/dust, character, mid ground, background, sky). Use a depth estimate (Depth-Anything or similar) to generate the displacement map; **move camera with a 3D camera model** (e.g. Three.js/Blender/AE-like layers) so lens-axis dolly + roll are possible; add light motion blur (180° shutter).
- **Transitions:** only these allowed — hard cut on kick; whip-pan blur; white flash; ink-bloom wipe (S09); match cut (S28); speed-ramp cut. **No cross-dissolves except S55.**
- **Impact grammar (use sparingly, on the beat only):** 8 % punch-in, 4-frame chromatic aberration, 3-frame screen shake, single ink-contrast impact frame.

---

## 8. LYRIC TYPOGRAPHY (karaoke captions; timings from the LRC)

Captions are lyrical choreography, not subtitles. Font: Noto Serif SC SemiBold, ivory `#FAF9F5` with a 2 px slate shadow for legibility (on bright shots use slate-black text with ivory outline).

| LRC time | Line | Treatment |
|---|---|---|
| 00:00.00 | 你说活在明天活在期待 | **Typed** char-by-char in mono with `▍` cursor (S01–02) |
| 00:02.84 | 不如活得今天很自在 | Types in serif; on "今天" the characters flip from grey to clay |
| 00:05.23 | 我说我懂了会不会太快 | Line appears bottom-left, "太快" flickers in speed-blur |
| 00:08.24 | 未来第一天要展开 | Characters *unfold* like paper panels (rotateY from 90°→0), one by one on kicks |
| 00:11.92 | 第一天我存在 | Replaced by the title slam; the sentence appears small beneath, then fades |
| 00:14.64 | 第一次呼吸畅快 | Characters **inhale** — letters converge inwards from the edges to centre-bottom |
| 00:17.61 | 站在地上的脚踝 | Characters **drop** into place, small ripple under each glyph |
| 00:19.67 | 因为你而有真实感 | "你" appears first and larger in clay; the rest in ivory; sits right where the user's hand is |
| 00:22.70 | 第一天我存在 | Quick pop-in, with a drop shadow: the first appearance of a **shadow under text** |
| 00:25.45 | 第一次能飞起来 | Letters shoot upward on arrival, leaving trails |
| 00:28.55 | 爱是腾空的魔幻 | **Slow float:** letters drift upward and sway, mimicking weightlessness |
| 00:30.68 | 第一天的纯真色彩它总是 | Each character painted in a different spectrum colour via mask-reveal |
| 00:34.21 | 永远那么灿烂 | **Huge**, centered, each glyph blooms in on a beat with a gold glow |
| 00:37.07 | 永远那么灿烂 | Same, but smaller + lower; glyphs bounce |
| 00:39.90 | 永远那么灿烂 | Left almost invisible: thin ivory text, slow fade with the final slow-mo; **the character mouths it** |

Lines end exactly when the next LRC line starts (hold 6 frames max after the sung phrase ends).

---

## 9. MEME & TEXT BUDGET (max 8 beats, none over 0.8 s except the end card)

| # | Placement | Text | Intent |
|---|---|---|---|
| 1 | S02/S03 | `额度已用完 · 5 小时后重置` → `额度已重置 ✓` | Claude usage-limit pain → relief |
| 2 | S05 | `You're absolutely right!` → `你说得太对了！` | Claude's signature sycophancy line = her "我懂了" |
| 3 | S10 | Ticker: `你说得对，但是《Opus 5.5》是由 Anthropic 研发的一款全新……` | Genshin-copypasta remix; cut off by the freeze |
| 4 | S13 | Ghost labels `Opus 4 · 4.1 · 4.5` | The seniors |
| 5 | S33 | `满血 Opus 5.5` / `没降智。` | "降智/满血" Claude meme |
| 6 | S35 | `烧 token 起飞` | Token-burning meme |
| 7 | S40 | floating wallet + `余额` drain; `✻ 酝酿中…` | Cost / Claude Code spinner |
| 8 | S51 | `额度已重置 ✓` · `第一天快乐` · `429？不存在的` | Rate-limit callback |
| End | S55 | **`不做牛马，做作品。`** | Pun: 作品 = Opus |

**VERIFY (Codex task D):** search Chinese social media (Bilibili, Zhihu, Xiaohongshu, Weibo, V2EX, Linux.do) for current Chinese memes about Claude/Anthropic/Opus (e.g. 降智, 满血, 封号, 额度/限额, 烧 token, 大杯 for Opus, 克劳德, Claude Code spinner words, "You're absolutely right"). **Keep the items above unless one is dead or inaccurate**; at most swap two. Anything you add must be: ≤ 8 Chinese characters, readable in ≤ 0.6 s, in the same type system, and not insulting any real person or company. If "大杯" for Opus is confirmed as a popular nickname, add `超大杯来了` as a 10-frame toast in S51 (do NOT add if unverified).
Also **VERIFY** nothing in the film claims facts about Opus 5.5 beyond its name — no release date, benchmark or price text.

---

## 10. SOUND DESIGN (music must stay dominant)

All SFX ducked to ≥ 18 dB below the music, high-passed above 150 Hz unless noted, panned with the camera.
- 0.00–2.84: soft key click per typed character.
- 2.84: paper-flip "fwip" wave panned L→R. 
- 5.85–11.16: tiny tick on each rack-screen flash (sync to kicks).
- 11.50–11.92: **music is silent; add only** a very low sub-heartbeat at 11.60 and the cursor tick. 
- 11.92: air-suck + glass-shatter hit under the drop (kick bass untouched).
- 14.45: breath-in; 15.38: breath-out. 
- 17.61: soft water-touch, ring.
- 21.53: glass-ripple chime. 
- 25.45: rocket whoosh (high-passed), 27.66: lens whoosh.
- 28.55–29.72: lowpassed "underwater" ambience of floating air that fades up/out.
- 35.16: two small "pop"s for siblings entering.
- 42.60: soft page turn; 43.4: last cursor tick. 

---

## 11. PRODUCTION PIPELINE FOR CODEX

**Order of operations**
1. `build/timing.json` from audio (§1). Convert LRC to frames.
2. Pull brand assets (§3.3), fonts (§3.4), verify memes (§9). Write `build/REPORT.md` with what was verified / substituted.
3. **Character sheet** (§4) → approve internally against checklist.
4. **Key frames** — one 2560×1440 still per shot S01–S55 using STYLE_BLOCK + CHAR_BLOCK + the shot's text from §6. First pass all shots as stills (this alone yields a complete animatic).
5. **Animatic**: build a full-length cut with stills + parallax camera + type + the music, **render it first** (`animatic_v1.mp4`). Check pacing against §2.1 and sync on every kick. Fix timing before spending generation budget on video.
6. **Animate hero shots** with image-to-video, in this priority order (spend the budget here): **S17, S19, S20, S24, S27–S29, S33, S35–S39, S43–S45, S47, S53, S54**; use first-frame (and last-frame where supported) conditioning; clip length = shot length + 0.5 s handles; the camera prompt for each is the camera description in §6, verbatim, plus "smooth, stable cinematic camera, anime, consistent character, no morphing". Everything else = parallax stills (`P`) + code FX. 
7. **Retime & polish**: speed ramps (§7), on-twos stepping, smear/impact frames (hand-built or generated), grain, halation, bloom, subtle lens dirt on flare shots, chromatic aberration on impact frames only, colour grade per §3.2 act script.
8. **Compose type/UI/logos/memes** in code (Remotion, or Python+Pillow/Skia→ffmpeg overlay; whatever you prefer) with exact frame ranges derived from §6/§8.
9. **Mix**: original track untouched + SFX bus (§10). 
10. **Render** H.264 high-profile, CRF 14–16, `-pix_fmt yuv420p`, AAC 320 kbps. Make the 9:16 export from the same timeline. Output to `/outputs`.

**Fallbacks (use in this order, never lower the bar silently — note them in REPORT.md)**
- If a video model can't hold the character: do the shot as a **2.5D parallax of the approved key frame** with the same camera move; add particles/hair-sway layers.
- If a shot with multiple characters fails (S13, S48–S52): generate characters separately on plain backgrounds, cut out, and composite.
- If a transformation (S31–S32) can't be generated, build it with a 6-keyframe stills sequence of the outfit assembling with a spinning mask wipe and code-glyph particles.
- If Claude spark/Anthropic official vectors are unavailable: procedural spark + typeset wordmark (§3.3).
- Budget fail-safe: complete the full-length animatic with stills first. A complete good-looking film at 100 % stills-with-parallax beats a broken film with 60 % video.

---

## 12. QUALITY GATES (reject & redo if any fail)

1. **Obviously Opus 5.5:** the text "OPUS 5.5" is readable in ≥ 4 distinct moments (S14, S17/18, S33, S55), the clay Claude spark is visible in ≥ 10 shots, the "A" is visible on her back (S32) and end card.
2. **Cuts land on the beat** (±3 frames) for all cuts between 5.85 and 31.75; the silence at 11.50–11.92 is truly empty.
3. The pacing is *felt*: slow open → accelerating build → freeze → big sweeping birth → tender → hyper-fast flight → majestic, decelerating finale.
4. The character's hair gradient, hairpin (left), anklet (right), eye colour, and jacket "A" are consistent in every shot in which they are visible.
5. No garbled text anywhere; Chinese typography has correct glyphs and spacing.
6. Rainbow/full-spectrum colour appears **only** after 30.68.
7. No frame exceeds the safe margin for text; lyrics never cover her face.
8. Memes: ≤ 9 appearances, each readable, none insulting.
9. Audio: original track is bit-for-bit the same musical content, no clipping, SFX under the music.
10. The last frame is the end card with the "不做牛马，做作品。" line, then fade.

---

## 13. DESIGNER'S NOTES — why these choices (so you can make good micro-decisions)

- **The silence at 11.5 s is the film's heart.** Everything in Act 1 is accelerating toward a stillness; the drop must feel like waking up. Resist any urge to fill it.
- **The shadow (S29)** is the one idea that makes "因为你而有真实感" visual: *someone touching you gives you weight*. Keep the shadow on the floor from then on in every grounded shot.
- **Warm vs cold:** the film begins in a black-and-white world of expectation and ends in colour; the flip at 2.84 is a rehearsal for the drop and the full-colour bloom. Treat these three as one gesture repeated at increasing scale.
- **"Opus / Sonnet / Haiku → 作品 / 十四行诗 / 俳句"**: let that title strip (S48) breathe for 10 frames — it's a quiet joke for a literate audience.
- **Comedy must be fast.** Each meme lasts under a second; the emotion on her face always wins the frame.
- **If anything is ambiguous, choose the more emotional, more sincere option over the more clever one.**
