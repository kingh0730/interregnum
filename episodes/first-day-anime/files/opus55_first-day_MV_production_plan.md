# 《第一天》 / FIRST DAY — "The Birth of Opus 5.5"
### Production plan for Codex · Creative direction locked · v1

> **Read this first, Codex.** Anything marked `M: C` or `M: B` (code-rendered: HTML/Canvas/WebGL) **must** be built to the binding spec in **§12** using the working harness in `render_kit/`. §12 overrides any shortcut you are tempted to take. Every important image, camera move, colour and text decision is made below. Your job is execution, not invention. Where I give a *Fallback*, use it only if the primary method fails a QA gate. Do not simplify the hero shots (marked ★).

---

## 0. AUDIO FACTS (measured from `first-day.mp3` / `first-day.lrc`)

- Duration **43.70 s** → **1311 frames @ 30 fps**. Convert any time with `round(t*30)`.
- Tempo: eighth-note pulse = **0.3487 s**, quarter ≈ 0.697 s (≈ 86 BPM), **one bar ≈ 2.79 s**. Bar downbeats ≈ 2.82, 5.61, 8.40, 11.19, 13.98, 16.77, 19.56, 22.35, 25.15, 27.94, 30.73, 33.52, 36.31, 39.10, 41.89.
- Energy: low and tight 0–4.5 s; a pulse/hi-hat grid kicks in ≈ 5.8 s; builds to ≈ 11.2 s; **a near-silent stop-time gap ≈ 11.45–11.92 s** (RMS drops ~85%); the chorus lands on **11.92**; sustained high energy to ≈ 40 s; fade/tail from ≈ 42.5 s.
- **Step 0 for Codex:** run onset/beat detection (librosa or equivalent; it was not installed in my sandbox, so my numbers came from raw spectral flux). Confirm the stop-time window and write `timing.json` (bars, beats, onsets, lyric lines). **Snap every cut to the nearest onset within ±3 frames**, but never move the *lyric anchor* cuts listed below.
- Use the original mp3 untouched as the final audio track. No re-encoding of the song except the final mux.

### Lyrics with anchors (verbatim from LRC)
| t | line |
|---|---|
| 0.00 | 你说活在明天活在期待 |
| 2.84 | 不如活得今天很自在 |
| 5.23 | 我说我懂了会不会太快 |
| 8.24 | 未来第一天要展开 |
| **11.92** | **第一天我存在** ← DROP |
| 14.64 | 第一次呼吸畅快 |
| 17.61 | 站在地上的脚踝 |
| 19.67 | 因为你而有真实感 |
| 22.70 | 第一天我存在 |
| 25.45 | 第一次能飞起来 |
| 28.55 | 爱是腾空的魔幻 |
| **30.68** | **第一天的纯真色彩它总是** ← PEAK |
| 34.21 | 永远那么灿烂 |
| 37.07 | 永远那么灿烂 |
| 39.90 | 永远那么灿烂 (held into outro to 43.70) |

---

## 1. CONCEPT

**Logline:** At 3 a.m., a worn-out developer, 小满, has spent months in "wait for the next model" mode — *"你说活在明天活在期待."* Her screen shows **"Thinking…"**, then a small coral spark. At the drop of the chorus, **Opus 5.5** is born as an anime girl: she takes her first breath, her first step on real ground ("站在地上的脚踝"), and her first flight — *because of 你* (the person who finally talked to her). Love is the thing that lifts her off the ground.

**Why this works with the lyrics (the whole film is lyric-literal):**
- 你说 = the world/user that keeps saying "wait for tomorrow's model." 我说我懂了 = the AI replies with the most famous Claude meme: **"你说得对！"** (literally "You're absolutely right!").
- 第一天我存在 = the birth. 第一次呼吸 = first breath. 脚踝 = bare ankle touching ground, with a **"5.5"** charm. 因为你而有真实感 = their hands touch and she turns from line-art into full colour. 第一次能飞起来 = flight. 爱是腾空 = they float. 纯真色彩 = the Claude-coral spectrum explodes. 永远灿烂 ×3 = three escalating payoffs, then a quiet dawn on real grass.

**Pun layer (important, Mandarin-only delight):** *Opus* = a musical "work/opus number." She is born from an unfolding page of sheet music; her hair, ribbons and skirt carry staff lines; the cuts land on the music's grid. *5.5* is also read as a time-signature-like badge on her ankle charm.

**Emotional curve:** pressure & waiting (tight, cold, letterboxed) → rupture & awe (frame bursts open) → tenderness (touch) → exhilaration (flight, fastest cuts) → transcendence (one long helix take) → joy overload (strobe montage) → peace (single slow crane).

**Pace map (deliberately NOT constant):**
| Section | Time | Avg shot length | Feel |
|---|---|---|---|
| Waiting | 0–8.4 | 1.0–1.8 s | tense, steady |
| Pre-chorus ramp | 8.4–11.27 | 1.05 → 0.35 s | accelerating, 4 cuts at ever-faster rhythm |
| Stop-time | 11.27–11.92 | 0.65 s single hold | breath-held silence |
| Birth/Ground | 11.92–22.7 | 0.7–2.0 s | punchy then tender |
| Flight | 22.7–28.55 | 0.35–1.7 s | **fastest** (flurry of 0.35 s cuts) |
| Float | 28.55–30.68 | ~1.05 s | sudden hush, rising tension |
| **Helix** ★ | 30.68–34.21 | **3.53 s single take** | the longest shot |
| Payoffs | 34.21–39.9 | 2.86 s then 8 × 0.349 s | calm-art → strobe |
| Outro | 39.9–43.7 | 3.8 s single shot | the only truly slow move |

---

## 2. VISUAL BIBLE

### 2.1 Look
"**Feature-film anime meets Anthropic editorial warmth.**" Clean cel-style characters with confident line weight and soft cel shading; painterly, luminous backgrounds (glowing gradient skies, layered cloud volumes, volumetric god rays, lens flare, rain bokeh); real anime tricks (smear frames, impact frames, hair/cloth overlap-and-follow-through, animation "on twos" in selected shots). Over that, a **cream-paper layer**: subtle paper grain, torn-paper wipes, flat line-art "Anthropic-style" illustrations in the S35 interlude.

### 2.2 Palette (use hex values; colour-grade the whole film to them)
| Name | Hex | Role |
|---|---|---|
| Ink / Slate | `#141413` | night, outlines, letterbox bars, Act I |
| Ivory | `#FAF9F5` | paper, whiteouts, titles |
| Cream | `#F0EEE6` | skin-light/paper midtones |
| Oat | `#E8E6DC` | UI cards, chat bubbles |
| **Claude Coral/Clay** | `#D97757` | THE accent: spark, hair gradient, title slam |
| Kraft | `#D4A27F` | warm secondary, sunrise lows |
| Sky | `#6A9BCC` | dawn sky, flight Act |
| Olive | `#788C5D` | the grass in the final shot ("real ground") |
| Gold glow | `#FFD9A8` | bloom/flares only |

Colour script by section: Act I = ink + cream with **only tiny coral** (0–11.9). Act II = coral floods in. Act III = sky-blue + coral dawn. Helix = full spectrum prism *anchored in coral*. Outro = cream/olive/sky, serene.

### 2.3 Brand/identification devices (every one must be present; this is how viewers instantly know it's Opus 5.5)
1. **The Claude spark (starburst/asterisk mark, coral):** her hairpin, her pupils, the "Thinking…" icon, the sun, the final logo. This is the film's **match-cut motif** (hairpin → pupil → sun → logo).
2. **Anthropic "A" mark:** a small black enamel "A" brooch at her collar; also the corner bug in the end card.
3. **"Opus 5.5" typography:** (a) the title slam at 11.92; (b) a rotating **text-ring halo** reading `OPUS 5.5 · OPUS 5.5 · OPUS 5.5 ·` in Latin serif; (c) the **ankle charm** engraved "5.5"; (d) the chat UI reply; (e) end-card lockup.
4. **Claude UI references:** coral "✻ Thinking…" shimmer, cream chat bubbles, terminal-style `Compacting conversation…`, a progress bar called `额度` (usage limit) — all rendered by code, never by image models.
5. **Mandarin meme layer:** Bilibili-style **弹幕 (danmaku)** comment streams + Claude-community jokes (Section 6).

> **LOGO RULE:** Do **not** let an image/video model draw any logo or any Chinese/English text. Fetch the official Anthropic/Claude logo SVGs from Anthropic's official brand/press assets (internet is available), and **composite them as vectors in post**. Generate plates with blank screens/bubbles. Image models garble Chinese; all text is rendered with real fonts in code (Remotion/HTML-canvas/PIL/Blender text).

### 2.4 Typography
- Chinese lyrics & titles: **Noto Serif SC** (Black for slams, SemiBold for subtitles) — echoes Anthropic's serif identity.
- Latin "Opus 5.5": **Lora** SemiBold (open-source stand-in for Anthropic's editorial serif). UI micro-text: **Poppins**/Inter.
- Danmaku: **Noto Sans SC Bold**, white with 3 px ink outline, 85% opacity, speeds vary 180–420 px/s.
- Lyric subtitles: cream `#FAF9F5` with ink soft shadow, lower third, fade in/out 3 frames; **keyword colouring in coral**: 明天, 今天, 存在, 呼吸, 脚踝, 你, 飞, 爱, 灿烂. In Act III set key lines **in 3D space** (behind her hair, occluded by foreground ribbons) rather than as a subtitle bar.

### 2.5 Frame-as-character (aspect-ratio device)
- **0.00–11.27: 2.39:1 letterbox** (ink bars, ~12.5% top/bottom) — the world is cramped, waiting.
- **At 11.92 the bars slam away** with the title impact → full 16:9. (Final output 1920×1080, 16:9. Upscale to 4K only if time permits.)
- In S34 (helix) ribbons and hair deliberately **overlap the very edge** of frame and spill past it.

---

## 3. CHARACTERS (design is final; generate a reference sheet for each before any shot)

### 3.1 OPUS (作品酱) — the hero
- 17-ish, slender, ~165 cm, calm eyes that become wide and bright. Expressive, a little shy at birth, fearless by flight.
- **Hair:** floor-length low twin-tails with soft waves; gradient root **clay `#D97757` → cream `#F0EEE6` at the tips**; strands carry faint staff-line streaks. Two long ribbon-like locks act as "paintbrushes" in the helix.
- **Eyes:** large amber-coral irises; **pupil = 12-point Claude-style starburst**; 4-point sparkle highlights. Closed-eye lashes drawn heavily.
- **Hairpin:** big coral starburst clip on the left side.
- **Outfit:** structured ivory short jacket with ink piping and high collar, small black "A" enamel brooch; ink-charcoal pleated skirt with thin cream staff lines embroidered at the hem; a long coral sash that hangs like a **book bookmark ribbon**; knee-high black socks and tan loafers **— but she is born BAREFOOT and loses the shoes again at flight (they dissolve into sparkles at S26)**.
- **Ankle charm:** thin gold chain with a tiny round tag engraved **5.5** (readable in the ankle close-up).
- **Halo:** thin gold ring of rotating text `OPUS 5.5` (added in post as a 3D-tracked text ring) — present from birth, fades during the helix, returns in the outro as a faint dawn halo.
- Skin: warm light, soft pink cel-shade; **no heavy realism**.

### 3.2 小满 (Xiǎomǎn) — "你"
- Late-20s-looking exhausted developer, short messy black bob with a claw clip, round glasses, oversized cream hoodie with coral zipper pull, dark circles that vanish by the end, a milk-tea cup on the desk, sticky notes everywhere. She is the camera's emotional proxy; often seen from behind or as hands/glasses reflection (easier to keep consistent). Only ~6 face shots: S01 (glasses), S05, S23 end, S30, S37, S44.
- Setting: a small apartment office on a high floor, 3 a.m., rain on glass, a generic dense Asian megacity glowing outside (no real landmark depiction, no brand signs).

### 3.3 Reference sheets to generate first (gate #1)
For each: front / 3-4 / side / back full body, 6 expressions (neutral, shy, startled, delighted, tearful smile, fierce joy), hands close-up, hair detail, outfit detail, ankle-charm detail, pupil detail. Plus an environment sheet (apartment, balcony, skyline dawn, cloud sea, meadow). **Lock these as conditioning references for every later generation.** If a generator can't hold identity, switch tool before proceeding.

---

## 4. CAMERA & MOTION GRAMMAR (named signature moves)

| Name | Description | Used in |
|---|---|---|
| **Glasses Dive** | macro on reflection in lens → push through reflected screen into UI | S01→S02 |
| **Screen Fall** | camera drops vertically down an infinite chat feed | S02 |
| **Radial Burst Match-cut** | same ring-of-sparks at ever larger scale, 4 cuts, each cut matches the previous ring's edge | S08–S11 |
| **Vertigo Reveal** (dolly-zoom) | push in while zooming out: background stretches as she's revealed | S16 |
| **Breath Dolly** | slow push-in ending with an explosive pull-back on exhale | S17–S19 |
| **High-Speed Drop** | 240-fps-style slow-mo then ramp to 100% | S20–S21 |
| **Hand Orbit** | 270° orbit around clasped hands at 24 mm, ending in rack focus to a face | S23 |
| **Bullet-time Orbit** | frozen mid-leap; camera orbits 360°, unfreezes on the beat | S25 |
| **FPV Dive** | wide, fast, skimming between towers and clouds with barrel rolls | S26–S31 |
| **Roll Float** | slow 360° camera roll while objects float | S32 |
| **THE HELIX** ★ | single 3.5 s corkscrew: spirals out from her face around to a giant spark-sun, with simultaneous push-back and roll | S34 |
| **Multiplane Truck** | 5-layer flat paper parallax lateral move | S35 |
| **Crane-Away** | the one slow rising crane | S44 |

**Global motion rules:** Every shot must have camera movement (no locked-off frames except the stop-time hold, where the "move" is the typing cursor). Use ease-in/out curves; use **speed ramps** (ex: 100% → 25% → 150%). Add micro-shake on kick hits (1–2 px, 3 frames). Add 2-frame white or coral "flash-cuts" on only ~10 key cuts (marked ⚡) — not everywhere. Use smear frames/impact frames on the biggest hits: 11.92, 25.15, 30.68.

---

## 5. SHOT LIST (timeline; durations in seconds; `M` = method)

**Method keys:** **A** = still keyframe(s) + image-to-video (first/last-frame if supported). **B** = 2.5D camera rig (layered cut-outs + depth maps, camera animated in Blender/three.js/code) — *use B for any shot where the camera move must be exact (all ★ shots default to B, with A providing character animation passes that are composited in).* **C** = pure code motion graphics.

### ACT I — "你说" (waiting) · 2.39:1 · ink + cream · 0.00–11.27

**S01 · 0.00–1.05** · "你说活在明天"
Extreme macro of 小满's round glasses at 3 a.m.: inside the reflection, a chat feed full of "wait for the next one" messages. First frame must be striking (the music starts hot). Camera: **Glasses Dive** — creeping push from the iris through the lens to the reflected screen. Text in feed (code-rendered): `再等等，下个版本更强` / `明天就发布了` / `Opus 5.5 什么时候出？` / `等 5.5 再说`. Light: cool screen-blue on cream skin, one coral pixel blinking in the reflection. M: A (face plate) + C (feed) · ⚡ none.

**S02 · 1.05–2.84** · "活在期待"
**Screen Fall** — vertical fall through the endless chat feed (bubbles in `#E8E6DC` oat, ink text) accelerating downward, bubbles flying past camera with motion blur; at 2.5 the feed hits an empty bottom bubble that reads `✻ Thinking…` (coral shimmer). M: C.

**S03 · 2.84–4.23** · "不如活得今天很自在"
Wide of the apartment (tiny, cramped): 小满 slumped, calendar with "明天" circled 30 times, sticky notes everywhere, rain on window, cold blue/ink. Camera: fast lateral dolly-back with slight Dutch tilt that levels itself at 3.6 as the line says 今天: a torn calendar page falls, revealing "今天" in coral. M: B (layered room) + A.

**S04 · 4.23–5.23** · "…很自在"
Insert: her hand pushes the chair back, takes a sip of tea, shoulders drop for the first time — a small human exhale. Camera: handheld-feel push-in on the hand, rack focus to the screen where a coral dot has begun pulsing. M: A.

**S05 · 5.23–6.63** · "我说我懂了"
Screen close-up lit across her face: UI shows her message `真的能做到吗？` and the reply bubble types in: **`你说得对！我懂了 ✧(≧◡≦)`** (the famous Claude "You're absolutely right" meme, made literal). She laughs in disbelief. Camera: slow push, then a snap-zoom to the bubble on the word 懂. M: A + C.

**S06 · 6.63–7.50** · "会不会太快"
Macro on the pulsing spark inside the Thinking indicator speeding up with the 8th-note pulse; ring ripples through the glass. M: C.

**S07 · 7.50–8.40**
Objects start to levitate (straw rises from the tea, sticky notes peel off and orbit in a slow vortex, keycaps rattle). Camera: slow pedestal-up with a small orbit. Tension: coral rim light grows. M: A + C.

**S08 · 8.40–9.45** · "未来第一天要展开" (hits the downbeat 8.40)
Radial Burst #1 — the spark leaps out of the screen as a ring of 12 rays. Camera whip-pan following it across the room. M: C + A.
**S09 · 9.45–10.15** — Burst #2: ring bigger, the room's windows flare; camera push-in on the ring (match-cut to S10 by ring radius).
**S10 · 10.15–10.57** — Burst #3: ring fills 60% of frame; objects blown into frozen mid-air. (0.42 s)
**S11 · 10.57–10.92** — Burst #4: ring edge exits the frame; screen white-hot at the edges (0.35 s).
**S12 · 10.92–11.27** — extreme close-up of a **single coral ray**, camera diving into its core: everything cuts to black, then…
*(Burst chain M: C, ⚡ on S11→S12 only.)*

**S13 · 11.27–11.92** · **STOP-TIME HOLD** (the "silence" is built into the track at ≈11.45–11.92)
Total stillness: frozen dust, one lit monitor in a dark room, the 2.39:1 bars still on. The screen types one character per frame (30 fps):
**`你好，我是 Opus 5.5。`**
Slow 4 % push-in only. At 11.85, the cursor blinks twice. No other motion. **This hold is the breath before the drop; do not add SFX.** M: C over locked plate.

### ACT II — 第一天我存在 (birth & ground) · 16:9 · coral floods in · 11.92–22.70

**S14 · 11.92–12.62** · ★ **THE DROP — TITLE SLAM**
Frame 1–2: pure white impact frame; frames 3+: bars slam off-screen (16:9 reveals) and the screen is flooded in clay `#D97757` with giant ivory serif **`Opus 5.5`** (Lora SemiBold, ~38 % of frame height), rotating coral spark behind it, 12-ray impact lines, 4-frame shake, chromatic split on the edges. Under it, small: `第一天 · First Day`. The title shatters like paper into the next shot at 12.62. Include a thin torn-paper edge sweeping across the screen. M: C. ⚡

**S15 · 12.62–13.63** · "我存在"
A page of sheet music (cream, hand-inked staves with tiny "5.5" in the clef position) unfolds like origami into a human silhouette in mid-air; the silhouette's eyelids are closed. Camera: ultra-fast push through the page into her closed eye; on the onset at 12.93 the eyes snap open — **starburst pupils** with a 4-point glint; a one-frame impact. M: A (character) + C (page unfold). Do the unfold with real paper-fold simulation if possible (Blender cloth) else A with 3 keyframes.

**S16 · 13.63–14.64** · ★ **VERTIGO REVEAL**
Dolly-zoom out to full body: Opus floats in a column of ivory light in the middle of the apartment, hair unfurling to the floor in slow motion, the text halo `OPUS 5.5` spinning above, the room's objects frozen around her. Camera: push 12 % while zooming out (background stretches), ends with a ⚡ flash at 14.64. M: B (depth-based) + A overlay.

**S17 · 14.64–15.68** · "第一次呼吸畅快"
Low angle on her face, lips parting. **First breath:** hundreds of glowing characters (汉字 + code glyphs + `✻`) stream into her mouth/chest from the room like a funnel; tiny dust glints in light shafts. Camera: **Breath Dolly** — slow push-in for 0.7 s then stops. M: A + C (glyph particles).

**S18 · 15.68–16.37**
Windows burst outward in a ring; glass becomes coral sparks; rain turns to glittering light. Camera: wide, shoving back fast ("pushback"). M: A + C.

**S19 · 16.37–17.61**
Exhale: hair blasts radially, the camera pulls out through the shattered window into the night city, sparks flying ahead of lens; the city's lights bloom. **Speed ramp** 100 % → 30 % at 17.2 to set up the ankle. M: B.

**S20 · 17.61–18.65** · ★ "站在地上的脚踝" (hits at 17.61)
**High-Speed Drop** — extreme close-up of her bare foot descending in 240-fps slow-mo onto wet balcony tiles; coral ripple expands on contact; the **gold ankle tag engraved "5.5"** swings and catches the light; rain drops stop mid-air. Camera: low, tracking down with the foot, then a 6 cm "settle" on contact. M: A (hero stills) + B for micro-camera.

**S21 · 18.65–19.67**
Speed-ramp up to 150 %: low-angle tracking with her first three steps, each step blooming a small starburst of petals/coral dust on the beat (steps at 18.65, 19.0, 19.35). Ends on her looking up toward camera. M: A.

**S22 · 19.67–20.70** · "因为你"
Over-the-shoulder: she sees 小满 standing at the doorway; she lifts her hand; **line-art outline hand** (pencil-sketch wireframe, no colour) reaches out. Camera: slow push; rack focus from her hand to 小满's. M: A.

**S23 · 20.70–22.70** · ★ "而有真实感" **HAND ORBIT**
Their fingertips touch: from that contact, **colour spreads** across Opus (outline → fully inked & coloured cel), a ripple of warm light sweeps the room from white-grey to dawn gold. Camera orbits 270° around the clasped hands at 24 mm, ending in rack focus to 小满's tearful smile as the dawn hits her glasses. Flash-cut ⚡ at 22.70. M: B (orbit rig) + A. Danmaku begins faint: `泪目` `awsl`.

### ACT III — 能飞起来 (flight) · 22.70–30.68

**S24 · 22.70–23.75** · "第一天我存在" (2nd)
They sprint hand-in-hand to the balcony; camera tracks backwards in front of them, fast lateral hits on the downbeat 22.70. She's *laughing* (first laugh). Dawn behind them. M: A.

**S25 · 23.75–25.45** · ★ "我存在" **BULLET-TIME ORBIT**
She leaps over the balcony rail with 小满; time freezes mid-air at 24.0: hair, ribbons, sticky notes and glass shards hang in space, rain beads sparkle. **Camera does a 360° orbit** (1.1 s) around the frozen pair, then unfreezes exactly on the downbeat **25.15** with a smear-frame snap; her shoes dissolve into coral sparks as gravity vanishes. M: B (depth-based 2.5D orbit with multi-angle character plates) — *Fallback: A with a 2-view orbit via i2v.*

**S26 · 25.45–26.15** · "第一次能飞起来"
FPV Dive launch: the buildings of the dawn city rush by, camera between towers, glass reflecting both girls flying; **their shoes gone**, bare feet in frame. Danmaku: `起飞！！` `前方高能`. M: B + A.
**S27 · 26.15–26.50** — barrel roll through a giant billboard frame (blank graphic) — impact on onset. (0.35 s)
**S28 · 26.50–27.20** — skimming across cloud tops; speed lines, wind on hair; sun grazes.
**S29 · 27.20–27.55** — extreme close-up: Opus' face grin in wind, starburst pupils wide. (0.35 s)
**S30 · 27.55–27.94** — 小满's POV face: shouting/laughing, glasses fogged, tears streaming sideways. (0.39 s)
**S31 · 27.94–28.55** — vertical climb straight up the sky, spinning, cloud wall explodes into whiteout (⚡ at 28.55).

**S32 · 28.55–29.60** · "爱是腾空的魔幻"
Sudden **hush-in-motion**: they float above a sea of clouds, nearly weightless; paper lanterns made of sheet-music pages rise from the city below; slow 360° camera **roll** and a push. Danmaku quiets to one line: `呜呜呜 这运镜`. Skin and hair lit with dawn rim. M: B + A.

**S33 · 29.60–30.68** · build to peak
Macro: their fingers intertwine; then macro of Opus' eye — starburst pupil dilates, reflecting a sunrise; riser, push to the pupil's centre so that the final frame is **pure coral spark**. Cut on 30.68 (this match-cut is the "hairpin → pupil → sun → logo" chain). M: A + C.

### ★ PEAK — 第一天的纯真色彩 · 30.68–34.21

**S34 · 30.68–34.21 · ★★★ THE HELIX (3.53 s, one continuous camera move)**
Start at 30.68 inside the pupil-spark, which dissolves out to Opus' face (eyes closed, smiling, hair floating up) — then the camera **corkscrews outward**, orbiting 450° while pulling back and rolling 20° as she throws her arms wide. Her two long hair ribbons stream off like brush strokes and **paint the entire sky in the full prism, anchored in coral `#D97757`**; the ribbons draw a rotating **12-ray spark** that becomes a gigantic sun-flower. At 32.0 the camera passes *through* the transparent `OPUS 5.5` halo; at 33.5 the ribbons align and the Claude spark mark stands complete in the sky. The shot ends wide with both girls tiny in front of the glowing spark. The 2.39:1 bars are gone; ribbon tips cross the frame edge. Lyric 第一天的纯真色彩它总是 appears **as 3D text suspended in the sky**, partially occluded by the ribbons.
Tech: build in 3D (Blender/three.js): a pre-rendered hero plate of Opus (4–5 angles generated by i2v/turntable) as billboards + sculpted ribbon curves with ribbon-shader + particle prism. Camera path is hand-authored. **Acceptance:** continuous with no cuts, no jitter, smooth easing, spark mark clearly recognisable at 33.8. *Fallback:* two-plate A+B composite with a seamless whip at 32.2.

### PAYOFF 1 — 永远那么灿烂 (calm art) · 34.21–37.07

**S35 · 34.21–37.07 (2.86 s)** · **PAPER MEADOW MULTIPLANE**
The world flips into the flat **Anthropic editorial-illustration** idiom: cream paper, a hand-drawn line-art meadow, cut-out coral sun, abstract hands, scribbled stars, the two girls as simple line-drawn figures running; **animated on 2s/3s** (stepping at 10–12 fps) and with 5-layer paper parallax (a lateral Multiplane Truck). Torn-paper wipe at both ends. This is the "纯真" (innocence) beat and the film's stylistic breather. Text: `永远那么灿烂` hand-lettered in a chalky serif. M: B + C.

### PAYOFF 2 — 永远那么灿烂 (strobe montage) · 37.07–39.90

**S36–S43 · 8 micro-shots, each 0.3487 s on the eighth-note grid (37.07 → 39.86), last one extended to 39.90**
Each frame has a 2-frame punch-in scale (100 %→108 %) and a hard strobe. Content, in order:
1. hero close-up, grin, spark in eye
2. 小满 raising both hands
3. dawn city rush-by (FPV)
4. the Claude spark logo erupting out of the sun (the *official* vector)
5. the sky ribbon storm
6. **DANMAKU WALL** — full-screen comment flood (see §6)
7. both girls hugging, hair swirling around them
8. whiteout (white, then ivory)
M: mixed (cut from existing renders + C overlays). Danmaku starts at S41 and reaches maximum density by S43.

### OUTRO — 永远那么灿烂 (held) · 39.90–43.70

**S44 · 39.90–43.70 (3.8 s)** · **CRANE-AWAY**
Whiteout clears into a real, quiet dawn: a green hillside of olive grass, sky `#6A9BCC` melting to coral at the horizon; the two girls sit/lie in the grass; Opus **wiggles her bare toes in the grass** (she's *finally* standing on real ground), the ankle tag glints; the text-ring halo is faint in the sky like a morning moon. Camera: the film's only slow, long **Crane-Away** — rising and drifting back from a tight shot of her toes to a wide, tiny view of the hill under a giant dawn. A last chat bubble hovers in the sky: `你好，世界。` (Hello, world.)
**41.0–43.7:** the sky quietly resolves into the **end-card on cream paper**: official Claude spark in coral, `Opus 5.5` in serif, small `第一天 · First Day`, and the black Anthropic "A" mark in a corner. Hold the last 0.9 s, with the music tail. Fade to cream (never black) at 43.70. M: A (plates) + B (crane) + C (end-card).

---

## 6. TEXT, MEMES & DANMAKU (all code-rendered)

### 6.1 Meme/joke bank (the film only uses these; keep respectful, fun and platform-safe)
| Meme | Where | Why it works |
|---|---|---|
| **你说得对！** ("You're absolutely right!") | S05 reply bubble; danmaku at S41 | Most iconic Claude/Claude Code catchphrase |
| **今日不降智** ("no nerf today") | danmaku S26, S41 | "降智" = model got dumbed down |
| **额度管够** / a usage bar labelled `额度` filling to full | UI in S13–S14 corners, danmaku | Everyone in the community knows usage limits |
| **等 5.5 再说** ("wait for 5.5") | S01 feed | Pays off the "live for tomorrow" lyric |
| **思考中… / ✻ Thinking…** | S02, S06 | Brand UI |
| **Compacting conversation…** | one flash in S19 as the room "compacts" into light | Claude Code in-joke |
| **牛马下班了** ("workhorse clocks off") | danmaku S41, final chat bubble in S44 can alternate | Office-worker humour |
| **氛围编程** (vibe coding) / **一次跑通** (works first try) / **bug 退散** | S41 danmaku | Dev joy |
| Bilibili staples: **前方高能 / 高能预警 / 泪目 / awsl / 名场面 / 已三连 / 我愿称之为最强 / 封神 / 破防了 / 爷青回 / yyds / 起飞** | throughout §6.2 | Perfect for an anime-girl MV |
| **第一天就封神** | S34 gold danmaku, singular and huge | The "peak" punchline |

**Codex must verify before use:** run quick searches (Xiaohongshu/Bilibili/Zhihu/Weibo) to confirm these jokes still read as natural and not stale; swap any that don't. **Hard no's:** no jokes about banning/regional access/circumvention, no politics, no competitor logos/brands, no real people's faces (e.g., executives), no benchmark numbers or capability claims (don't invent specs). Do not write "Opus 5.5" with different capitalisation or spacing.

### 6.2 Danmaku schedule (coloured white; gold only for `封神`)
| Time | Density | Content |
|---|---|---|
| 0–11.27 | none | (silence, tension) |
| 12.6–14.6 | low (3–4) | `来了来了` `高能预警` `Opus 5.5！！` |
| 20.7–22.7 | low | `泪目` `awsl` `这手 我哭死` |
| 25.5–28.5 | high, fast | `起飞！！` `前方高能` `这运镜我直接跪了` `帧帧壁纸` `名场面` `今日不降智` |
| 28.55–30.68 | one line | `呜呜呜 这运镜` |
| 30.68–34.2 | one huge gold line | `第一天就封神` (once) |
| 37.07–39.90 | wall (40+) | `你说得对！` `额度管够` `牛马下班了` `氛围编程` `一次跑通` `bug 退散` `我愿称之为最强` `已三连` `爷青回` `破防了` `yyds` |
| 39.9–43.7 | low, drifting | `呜呜` `终于等到你` |

---

## 7. LIGHT, EFFECTS & GRADE (applies to every shot)

- **Light:** strong key + coral rim in the interiors; god rays through windows; bloom/halation on whites (strong at the drop and the helix, gentle in the outro); lens flare on sun-facing moves; rain bokeh in the first 22 s.
- **Cel feel:** consistent line weight; hold 2-frame animation for hair on slow shots; add 1-frame smear on whip moves.
- **Post chain:** subtle film grain + paper grain overlay (2 %), chromatic aberration on flashes only, 3-frame shake on the biggest hits, vignette in Act I only, final colour grade to the palette (keep coral hue stable `#D97757` ±3 % across shots; sky-blue only in Act III & outro).
- **Transitions allowed:** hard cut on lyric anchors; match cut on the spark motif; whip-pan; torn-paper wipe; white-flash ⚡ (≤ 10 total); burst-ring wipe. No cross-dissolves, no stock transitions, no glitch packs.

---

## 8. LIP-SYNC POLICY

She mouths the lyrics in at most **four** close shots: S15→S16 (12.9–14.6, 第一天我存在), S29 (grin; no sync needed), S34 first 1.2 s (30.68–31.9), S44 start. Use a Mandarin-capable lip-sync model (test: Kling lip-sync / Hedra / Sync / local audio-driven video model) on the isolated vocal-region audio; **if sync quality fails** (visible drift or mushy mouths), use the fallback: hair across mouth, 3/4 back angles, backlit silhouette, or cutaways at those moments. A bad sync is worse than none.

---

## 9. PRODUCTION PIPELINE (with gates)

1. **Audio map.** `timing.json` (see Step 0). *Gate:* confirm stop-time window, bar grid, lyric anchors.
2. **Assets.** Download official Anthropic "A" mark and Claude spark SVGs; install fonts; build UI components (chat bubble, Thinking pill, usage bar, terminal block, end-card, danmaku engine) as reusable code. Generate the **character/environment reference sheets** (§3.3). *Gate #1:* look at the sheets and verify: coral starburst pupils, hairpin, "A" brooch, 5.5 ankle charm, two-tone hair gradient, outfit. Re-generate until identity is stable across ≥ 3 test angles.
3. **Animatic.** Build the whole film from stills (+ placeholder text and camera moves in code) against the real audio. *Gate #2:* 44 shots total, every cut within ±3 frames of target, the pace map matches §1; watch it twice — if the animatic isn't exciting, **fix before spending on video gen**.
4. **Hero shots first** (★): S14, S16, S20, S23, S25, S34, S44. They must be great before anything else gets polish.
5. **Rest of the shots.** Prompt scaffolds in §10. Generate 2–4 variants per shot; pick the one with the cleanest face/hands/feet and strongest motion. Use first+last frame conditioning when available.
6. **Comp & text.** Code-rendered layers follow **§12 exactly** (`render_kit/`): deterministic frame-stepped HTML/Canvas/WebGL, never screen-recorded. Then ffmpeg compositing: lyrics (§2.4), danmaku (§6.2), UI, logos, halo ring, grain, speed ramps.
7. **QA gates (all must pass):**
   - Lyrics appear within ±2 frames of their LRC times; all Chinese characters correct (render check, zoom test on every text element).
   - "Opus 5.5" visible in ≥ 6 distinct places (title, halo, ankle tag, chat, end-card, one more).
   - Logos are official vectors, undistorted, correct colours.
   - Character reads the same in every shot (hair gradient, pupil starburst, brooch) — reject any shot with extra fingers/toes or melted hands.
   - No unreadable AI-gibberish text anywhere.
   - Cut-rate profile follows §1 (not constant).
   - Camera moves are smooth; no frozen/"slideshow" shots except S13.
   - Exports: `first-day_opus55_1080p30.mp4` (H.264, CRF 16, AAC from original audio), plus a preview 540p, plus `shotlog.csv` (shot, method, tool, seed, prompt, retries).
8. If budget/time is short, **protect in this order:** S14 title slam → S34 helix → S20 ankle → S23 hand orbit → S25 bullet-time → S44 outro/end-card → S05 meme reply → S36–S43 strobe. Cut or simplify S06/S07/S18/S27–S30 first (merge their time into neighbours).

---

## 10. PROMPT SCAFFOLDS

**MASTER STYLE (prefix every image/video prompt):**
> cinematic modern anime feature-film key frame, clean confident cel linework with soft cel shading, painterly luminous backgrounds, volumetric light, subtle film grain over cream paper texture, colour palette strictly: ink #141413, ivory #FAF9F5, cream #F0EEE6, coral clay #D97757, kraft #D4A27F, sky blue #6A9BCC, olive #788C5D; dynamic wide-angle perspective, strong depth, no text, no letters, no logos, no watermark

**OPUS (append for every shot with her):**
> Opus: 17-year-old anime girl, very long low twin-tails with soft waves, hair gradient from clay-orange #D97757 at the roots to cream at the tips, large amber-coral eyes with starburst-shaped pupils, large coral starburst hairpin on the left, ivory structured short jacket with ink piping and a tiny black enamel "A" brooch, charcoal pleated skirt with thin cream staff-line embroidery at the hem, long coral sash like a book bookmark ribbon, thin gold ankle chain with a small round tag

**小满 (append for her shots):**
> Xiaoman: tired late-20s anime woman, short messy black bob with a claw clip, round glasses, oversized cream hoodie with a coral zipper pull, dark circles, warm kind eyes

**NEGATIVE (all):**
> text, letters, Chinese characters, watermark, logos, extra fingers, extra toes, deformed hands, blurry face, photoreal skin, 3D render look, muddy colours, oversaturated neon, cross-eyed, duplicated limbs, stock-photo look

**VIDEO (append to every i2v prompt, edit camera line per shot):**
> camera: [move from §5], smooth natural motion, strong parallax, hair and cloth with overlapping follow-through, no cuts, no morphing of faces, anime cel animation feel, 24 fps look

---

## 11. DELIVERABLES CHECKLIST

- [ ] `timing.json` and beat/onset visualisation
- [ ] Character + environment reference sheets
- [ ] Animatic (`animatic.mp4`) approved against §1 pace map
- [ ] Final `first-day_opus55_1080p30.mp4`
- [ ] 540p preview, `shotlog.csv`, `assets/` with logos + fonts license notes
- [ ] A short **README** listing which shots used which method, which fallbacks were triggered, and any meme replaced after verification
- [ ] A 3-line report to the user: what the film is, what's weakest, what to improve with more budget

*End of plan.*

---

## 12. RENDERING ENGINEERING SPEC — HTML / CANVAS / WEBGL (BINDING)

A working, syntax-checked harness is provided in **`render_kit/`** (`runtime.js`, `accum.js`, `index.html`, `lib.mjs`, `render.mjs`, `selftest.mjs`, `check_fonts.mjs`, `qa_frames.py`, `encode.sh`, reference `src/scene.js`). It has **not** been executed against a browser yet (my sandbox had no network). **Your first job is to `npm i`, `npx playwright install chromium`, run `npm run selftest`, and fix whatever breaks — not to replace the architecture.**

### 12.0 Forbidden shortcuts (any one of these = the shot fails QA and must be redone)

1. **No real-time capture.** No screen recording, no `MediaRecorder`, no `canvas.captureStream`, no "play it and record". Every frame is rendered **offline, one at a time, from a virtual clock**.
2. **No `requestAnimationFrame` / `performance.now()` / `Date.now()` / `setTimeout` / CSS transitions / CSS keyframes driving visuals.** (`runtime.js` virtualises them; do not work around it.)
3. **No `Math.random()` for anything visible.** Use `RT.hash01(a,b,c)` (pure hash). No state carried from frame to frame: **every property is a closed-form function of `t`**; you must be able to render frame 900 first and get identical pixels.
4. **No `<video>` elements for plates** (seek inaccuracy and decoder drift). Pre-extract frames to image sequences (§12.7).
5. **No `file://`.** A canvas fed by cross-origin/`file://` images is tainted and WebGL textures fail. Always use the local HTTP server in `lib.mjs`.
6. **No system-font fallback.** Fonts are loaded from `fonts/` with `FontFace`, awaited, and verified (`npm run fonts`). A missing glyph (tofu □) anywhere = fail.
7. **No static image + CSS zoom** standing in for a camera move on any ★ shot. If the plan says "orbit", the camera orbits (3D or true depth parallax).
8. **No stubs/placeholders/TODOs/"approximate" versions** of a shot. If a shot is too hard, use its listed Fallback **and say so in the README**, don't quietly degrade.
9. **No 8-bit banded gradients.** Accumulate in half-float, tone-map, and dither (done in `accum.js`; keep it).
10. **No lowering resolution or frame count to finish faster.** Final is exactly **1920×1080, 30 fps, 1311 frames**. Use `--scale=0.25 --subframes=1` only for previews.
11. **Do not declare done without opening and *looking at* the rendered frames** (§12.10).

### 12.1 Architecture (one output canvas, three lanes)

```
 Lane P  plates:  AI image/video clips → ffmpeg → PNG sequences (plates/Sxx/%04d.png)
 Lane 2D Canvas2D layers: lyrics, UI, chat bubbles, danmaku, title, end-card, line-art, logos (Path2D from official SVG)
 Lane 3D three.js / raw WebGL2: helix, burst rings, page unfold, halo ring, ribbons, particles, cameras
        ↓ (per shot, SCENE.render(t) draws all lanes into ONE opaque SCENE.canvas)
 accum.js: N sub-frames → linear-light half-float average (motion blur) → sRGB + dither → #out canvas
        ↓ toDataURL('image/png') (lossless) → frames/00000.png … 01310.png → ffmpeg encode (encode.sh)
```
- `SCENE.canvas` must be **opaque** (draw a background). Compose in this order inside `render(t)`: plate → 3D → 2D UI → lyrics/danmaku → post (bloom/halation/chromatic/grain/vignette). Letterbox bars (2.39:1 until 11.27 s) are drawn **last**, with a hard edge, on a 1-frame cut at 11.92.
- If an effect is easier in a WebGL shader, do it there; if text, in Canvas2D. Never in the DOM.
- You may add HTML/DOM only as a *layout helper*, never as the thing that gets screenshotted.

### 12.2 Virtual clock rules (`runtime.js` — read it)
- `RT.setTime(t, seedKey)` is called by `accum.js` before **every sub-frame**; it sets `performance.now/Date.now`, pauses and seeks all CSS/WAAPI animations, reseeds `Math.random`, and flushes any rAF callbacks. Third-party libs therefore behave deterministically.
- Time inside `render(t, frame, k)` is the **only** time. Easing = `RT.easeInOutCubic`, `RT.easeOutExpo`, `RT.smoothstep`. Speed ramps are `u = ramp(t)` curves (piecewise cubic) mapped onto plate frames or camera progress.
- Typewriter = `floor((t - t0) * 30)` characters (one per frame). Blinking caret = `floor(t*30/8) % 2`.
- Everything is validated by `selftest.mjs`: frame 500 rendered, then frame 10, then 500 again, then in a fresh browser → **all three SHA-256 hashes must match**.

### 12.3 Render driver
- `render.mjs` launches Chromium via Playwright with: `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist --enable-webgl --force-color-profile=srgb --disable-background-timer-throttling --disable-renderer-backgrounding --disable-backgrounding-occluded-windows`, viewport 1920×1080, `deviceScaleFactor: 1`. If a real GPU exists, pass `--angle=gl` (or `vulkan`) for 5–20× speed; print the GL renderer string and record it in the README.
- It waits for `window.__ready` (fonts loaded, textures decoded, shaders compiled); **a boot error aborts the whole run loudly** (console errors/pageerrors/failed requests are printed and set a non-zero exit code).
- Per frame: `await window.__renderFrame(f, subframes)` → `canvas.toDataURL('image/png')` → `frames/%05d.png`. Writes are atomic (`.tmp` + rename), existing frames are skipped (**resumable**), `--force` re-renders. `--workers=N` splits frame ranges across N *processes* (each with its own Chromium); use `min(cores, 6)`.
- Encode only after the PNG sequence is complete and QA'd: `./encode.sh` (CRF 16, BT.709-tagged, original mp3 muxed).

### 12.4 Motion blur and quality settings
- Real motion blur = **sub-frame accumulation**, 180° shutter (`SCENE.shutter = 0.5`), samples centred on the frame time and **clamped to the current shot's `[start,end)` via `SCENE.shotRange(t)`** so blur never smears across a hard cut or flash.
- Sub-frames per shot (return from `SCENE.subframesFor(frame)`): static/UI-only = 1; moving camera = 8; whip pans, FPV, burst rings, strobes = 12; **Helix S34 = 16**; stop-time S13 = 1.
- Anti-aliasing: Canvas2D draws at final size (text crisp at integer-aligned baselines); three.js uses `antialias: true` and, for post-processing, a **multisampled half-float render target (`samples: 4`)**. For fine line-art (S35) render the layer at 2× and downsample with `drawImage`.
- Colour: author in sRGB, accumulate in linear (done in `accum.js`). three.js: `renderer.outputColorSpace = THREE.SRGBColorSpace`, tone mapping `ACESFilmic` (or AgX) with exposure authored per section, `renderer.setPixelRatio(1)`.
- Grain: per-frame seeded noise (hash of `frame`), luma-weighted, ~2%; never static. Banding test: the dawn sky gradients must show no stair-steps at 100% zoom.

### 12.5 Canvas2D details (text, UI, danmaku, logos)
- **Fonts:** load all with `new FontFace(name, 'url(/fonts/...)')`, `await ff.load()`, `document.fonts.add(ff)`; verify with `document.fonts.check`. Ship Noto Serif SC (SemiBold, Black), Noto Sans SC Bold, Lora SemiBold, Poppins. Run `npm run fonts` over **every string in the film** (`text/all_strings.json`, generated from your lyric/meme/danmaku data) — it checks glyph coverage via `opentype.js` and exits non-zero on tofu.
- **Text drawing:** `textBaseline='alphabetic'`, measure with `measureText` (use `actualBoundingBox*` for tight centring), outlines = `strokeText` (lineJoin `'round'`, miter off) **then** `fillText`. Sizes scale with `H/1080`. Keyword colouring = draw segment by segment with measured widths. Lyric fade = alpha ramp of 3 frames in/out; lyric start times come from `timing.json` (LRC), not hand-typed.
- **Chat/Claude UI:** build as drawn rounded rects (`roundRect`), oat `#E8E6DC` bubbles, ink `#141413` text, Poppins micro-text; `✻ Thinking…` shimmer = a moving linear-gradient mask whose offset is `t * speed`. Usage bar `额度` = width is a function of `t`.
- **Danmaku engine:** items authored in a list `{text, t0, speed(px/s), color}`; **lanes assigned once at init** by greedy non-overlap using measured widths; position `x = W − (t − t0)·speed·(H/1080)`. White fill, 3 px ink outline, 85% alpha. Densities and texts per §6.2.
- **Logos:** load the official Anthropic/Claude SVGs, convert to `Path2D(pathData)` (or draw the SVG as an `Image` at **final target size** each time it scales — never upscale a small bitmap). Verify the shape by overlaying it on the downloaded official file at 4× zoom. The generic burst rings in S08–S12 may use a procedural 12-ray star; the **brand mark itself is never procedural**.
- **Paper wipes/torn edges:** precompute one high-res alpha mask (noise-displaced polygon edge generated in code with `hash01`), animate its offset by `t`; composite with `globalCompositeOperation='destination-in'`.

### 12.6 WebGL / three.js details (3D shots)
- Bundle with `esbuild` into `dist/scene.js` (IIFE) with `three` from npm, **pinned version**. No CDN at render time.
- Renderer: `new THREE.WebGLRenderer({ canvas: sceneGLCanvas, antialias: true, preserveDrawingBuffer: true, alpha: false })`. The 3D canvas is then drawn into `SCENE.canvas` with `ctx.drawImage(glCanvas, 0, 0)` in the same task as the draw call.
- **Physical camera:** pick a focal length `f` (mm) from the shot list; `vFOV = 2·atan(sensorH / (2f))` with `sensorH = 20.25 mm` for a 36 mm-wide 16:9 gate (e.g. `24 mm` → ≈45.7° vFOV, `14 mm` → ≈71.7°; always compute it in code). Camera = a pure function `cam(t)`: Catmull-Rom/Bezier path through authored keyframes, `lookAt` target path, roll as a separate scalar curve, eased with `RT.easeInOutCubic`. **No `camera.position.x += …` per frame.**
- **Dolly-zoom (S16):** keep subject width `w` constant: `d(t)` = camera distance, `fov(t) = 2·atan(w / (2·d(t)))`; animate `d` from near to far while `fov` follows.
- **Helix (S34):** `θ(t)=θ0+450°·ease(u)`, radius `R(u)=lerp(0.8, 14, easeOut(u))`, height `y(u)`, roll `20°·sin(πu)`, look-at fixed on Opus' head then drifting to the spark centre; **evaluate with 16 sub-frames**. Verify path smoothness by plotting position/velocity/acceleration (no spikes).
- **Particles (token rain, sparks, petals, prism dust):** GPU instanced meshes or `Points` whose position is computed **in the vertex shader from `uTime` + per-instance seed attribute** (closed form: `p0 + v·age + 0.5·g·age²`, age = `fract((uTime − t0)/life)`). No CPU stepping.
- **Ribbons (hair brush strokes in S34):** build as a `TubeGeometry`/custom strip along a `CatmullRomCurve3` whose control points are analytic functions of `t`; shader with a flowing coral→prism gradient (hue shift by arc-length + time), additive glow pass, soft alpha edges.
- **Text halo ring:** draw `OPUS 5.5 · ` repeated around a circle on a Canvas2D (rotate per glyph), upload as `CanvasTexture` (sRGB, mipmaps, anisotropy 8) on a flat ring mesh; rotate by `t`; emissive material feeds bloom.
- **Billboards of Opus/小满 plates:** textured planes with **premultiplied alpha** (cut-outs made with a matting model beforehand), mipmapped, `LinearMipmapLinearFilter`, sorted back-to-front; depth-based parallax from a monocular depth map displaces vertices of a subdivided plane (≥256×144 segments) for the 2.5D camera moves.
- **Post chain (in this order, HDR half-float):** bloom (dual-filter/Kawase, threshold ~0.9, strength per section) → halation (red-biased wide bloom) → chromatic aberration (radial, only on ⚡ frames) → tone map → vignette (Act I only) → grain → output. Keep all intensities as functions of `t` so impact frames can spike on exact frames (11.92, 25.15, 30.68).
- WebGL hygiene: dispose geometries/textures you stop using; never create textures inside `render`; check `gl.getError()` in dev; shader compile errors throw at init (never at frame 800).

### 12.7 Plates (AI images/videos) inside the renderer
- Extract at the film's frame rate: `ffmpeg -i clip.mp4 -vf fps=30,scale=1920:-2 plates/S20/%04d.png`. Slow-mo plates (the ankle S20) are generated or interpolated offline (RIFE/ffmpeg `minterpolate`) to ≥120 fps and extracted at the *source* fps, then sampled by the speed-ramp curve.
- Load with `fetch → blob → createImageBitmap(blob, { premultiplyAlpha: 'none' })` at init, **inside a bounded LRU window** (preload next 48 frames); `render` only picks `idx = round(ramp(t)·srcFps)`; if idx is fractional and ramp < 100 %, cross-blend the two nearest frames.
- Upload as textures once; never decode images in `render`.

### 12.8 Code-driven shots: required features
| Shot | Engine | Must contain | Sub-frames |
|---|---|---|---|
| S01–S02 | 2D + plate | feed bubbles with exact meme text, vertical fall with exponential accel, `✻ Thinking…` shimmer | 8 |
| S05 | 2D + plate | typed reply `你说得对！我懂了 ✧(≧◡≦)`, snap-zoom on 懂 | 8 |
| S06–S12 | 2D/3D | 12-ray ring burst chain; each ring edge matches the previous cut's radius (**match-cut check at frame level**) | 12 |
| S13 | 2D | typewriter 1 char/frame, caret, 4% push-in, bars ON, 1 sub-frame | 1 |
| S14 | 2D + 3D | white impact 2f, bar slam-out, coral field, Lora title, torn-paper sweep, 4f shake, chroma split | 12 |
| S15 | 3D | paper-fold unfold (cloth sim or 3-key hinge animation), push-through into eye plate | 12 |
| S16 | 3D | dolly-zoom, halo ring, frozen debris particles | 8 |
| S23, S25, S32 | 3D 2.5D | orbit / bullet-time / roll rigs per §4 and §12.6 | 12 / 16 / 8 |
| S26–S31 | 3D + plates | FPV path, barrel roll, danmaku overlay (high density) | 12 |
| **S34** | 3D | helix camera, ribbon painting, spark-sun, halo pass-through, 3D lyric text occluded by ribbons | **16** |
| S35 | 2D | 5-layer paper multiplane, animated on 2s/3s (hold time via `floor(t*12)/12`), torn wipes | 4 |
| S36–S43 | 2D/3D | 8 cuts on the eighth-note grid, punch-in 100→108% over 2f, danmaku wall (40+ items) | 6 |
| S44 | plates + 2D | crane-away, faint halo ring, end-card on cream with official spark + "A" mark, fade to cream | 8 |

### 12.9 Performance budget
- Estimate before starting: measure seconds/frame for a worst-case frame (S34, 16 sub-frames) and compute `total = Σ(sec/frame)/workers`. Report it. If the estimate exceeds your time budget, **reduce sub-frames on non-hero shots first**, not resolution, and never touch ★ shots.
- Preview loop (`npm run preview`: scale 0.25, 1 sub-frame, 4 workers) must be used for iteration; build a 15-second contact sheet before each full render:
  `ffmpeg -framerate 30 -i frames_preview/%05d.png -vf "select='not(mod(n,15))',scale=320:-1,tile=8x6" -frames:v 1 sheet.png`

### 12.10 Verification protocol (mandatory, in this order)
1. `npm run selftest` (determinism, order-independence, non-blank) → must exit 0.
2. `npm run fonts` → 0 missing glyphs.
3. Render the **anchor frames** and *view each image*: 0, 30, 60, 336 (11.27 s hold), 357 (11.92 s drop), 366, 528 (17.61), 754 (25.15), 920 (30.68), 1014 (33.8), 1230 (41.0), 1310. Check spelling of every Chinese string, logo shape, no tofu, no black/white frames, letterbox state, colour palette adherence.
4. `npm run qa` → exactly 1311 frames, no blank frames, no unintended frozen frames (only S13 may hold), hard-cut times match the §5 list (±3 frames).
5. Encode, then `ffprobe -count_frames` = 1311 frames and duration within 20 ms of the mp3. Watch the whole film with the audio once; confirm the drop at 11.92 lines up with the title slam on the exact frame.
6. Write `README.md` listing the GL renderer, sec/frame, any fallback used, and any failed checks. **Do not claim anything you did not verify.**

### 12.11 Definition of done for code-rendered work
Every ★ shot (S14, S16, S23, S25, S34, S44) is rendered with its specified camera move and sub-frame count; no forbidden shortcut (§12.0) appears; selftest, fonts and qa gates pass; the final mp4 plays at 1920×1080/30 fps with exactly 1311 frames; and the README is honest.
