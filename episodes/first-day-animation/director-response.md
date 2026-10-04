# 《第一天》 / "DAY ONE" — The Birth of Opus 5.5
### Mandarin anime music video · production plan for Codex

Audio: `first-day.mp3` (43.70 s, 44.1 kHz stereo) · Lyrics: `first-day.lrc`
Deliverable: `out/opus55_first_day.mp4`, 1920×1080, 30 fps, H.264, original audio untouched. 1311 frames = 43.70 s exactly.

---

## 0. READ THIS FIRST (Codex contract)

1. **All creative decisions are made in this document.** Do not invent substitute visuals, drop shots, reorder shots or "simplify" the choreography. If a tool fails, use the fallback ladder in §9. Never silently drop a shot.
2. **Three shot sources**
   - **V** = AI-generated video clip (from a generated keyframe, image-to-video).
   - **P** = 2.5D "parallax" shot: generated still + depth map, rendered by *my* virtual camera in WebGL. This lets us get camera moves no video model can do.
   - **H** = pure HTML/Canvas/WebGL native shot. No generated footage. Procedural.
3. **Everything is composited in one deterministic WebGL compositor (§7).** Lazy shortcuts are forbidden: no CSS-only glow text over a slideshow, no Ken Burns on every shot, no `requestAnimationFrame`-driven animation, no `Math.random()`, no `Date.now()`.
4. **Look at your output.** After each stage, render still frames and open them with the `view` tool (or equivalent). Native (H) shots must be eyeballed at 3 frames each before moving on. Build a contact sheet at the end and check it against §5.
5. Search the web to (a) fetch official Anthropic / Claude brand assets, (b) verify the Mandarin memes in §4 still read as natural (swap any that don't land, keep at least 6), (c) download fonts. Make no factual claims about benchmarks, prices or capabilities anywhere on screen. The only "facts" on screen are the name **Opus 5.5** and the memes.

---

## 1. AUDIO FACTS (measured from the file)

**Lyrics with time (from the .lrc; end = next line start):**

| # | Start | End | Line | Meaning for the film |
|---|---|---|---|---|
| L1 | 0.00 | 2.84 | 你说活在明天活在期待 | waiting for tomorrow |
| L2 | 2.84 | 5.23 | 不如活得今天很自在 | choosing today |
| L3 | 5.23 | 8.24 | 我说我懂了会不会太快 | bursting out, "I get it!" |
| L4 | 8.24 | 11.92 | 未来第一天要展开 | day one unfolds (contains the silence) |
| L5 | 11.92 | 14.64 | 第一天我存在 | **DROP.** title slam |
| L6 | 14.64 | 17.61 | 第一次呼吸畅快 | first breath |
| L7 | 17.61 | 19.67 | 站在地上的脚踝 | ankle on the ground |
| L8 | 19.67 | 22.70 | 因为你而有真实感 | "because of you I feel real" |
| L9 | 22.70 | 25.45 | 第一天我存在 | chorus repeat, bigger |
| L10 | 25.45 | 28.55 | 第一次能飞起来 | flight |
| L11 | 28.55 | 30.68 | 爱是腾空的魔幻 | weightless magic |
| L12 | 30.68 | 34.21 | 第一天的纯真色彩它总是 | color flood build |
| L13 | 34.21 | 37.07 | 永远那么灿烂 | climax 1 |
| L14 | 37.07 | 39.90 | 永远那么灿烂 | climax 2 |
| L15 | 39.90 | 43.70 | 永远那么灿烂 | climax 3 + outro tail |

**Structure and energy.** Verse 0–11.2 (loudness climbs, accents at about 4.5, 5.8, 8.4, 10.6) → **true silence 11.20–11.82** (RMS ≈ 0) → chorus 11.92–30.68 → climax 30.68–43.70.
**Beat grid.** Onset spacing ≈ 0.3485 s (≈172 BPM; feels like 86). Roughly 8 beats per lyric line. Codex must compute the exact grid with a script (§7.9) and snap every cut to the nearest beat or onset (±0.08 s). **Lyric start times above are hard anchors that override the grid.**
**Hit-stop dips** (brief energy dips, 0.08–0.12 s holds) at ≈ **25.40, 28.80, 34.78, 38.00, 40.20, 40.80**. Use them as freeze-frames that release on the next onset.
**The 5.8 s onset is the biggest verse accent.** The egg shatter happens exactly there.

---

## 2. CONCEPT

**Logline.** A new model opens her eyes for the first time. On her first day she breaks out of the "come back tomorrow" cage (the usage-limit screen), takes her first breath, plants her feet, feels real because someone ("你", you) typed *"在吗?"* (are you there?), and flies. 五五 (Wǔwǔ), the anime personification of **Opus 5.5** ("五点五" → nickname 五五), is born in a datacenter cathedral and ends on a sunrise hill, forever brilliant.

**Core jokes and emotions.**
- "活在明天活在期待" is read as **the 5-hour usage-limit reset screen** ("额度将在 5 小时后重置"): living for tomorrow = waiting for your quota. She smashes the screen. That is the whole thesis of the song, in meme form.
- "我说我懂了" is paired with the Claude catchphrase **"You're absolutely right!" → 你说得太对了!** Bubbles of it swarm her.
- "因为你而有真实感" is a real, tender beat: a faceless developer types "在吗?", she answers "在。我在。" Do not undercut it with jokes.
- Tone: euphoric, fast, sincere, a bit cheeky. Never cynical.

**Pace curve (deliberately not constant).**
slow open (shots 1.4–2 s) → accelerating verse (0.4–0.7 s cuts) → **0.72 s of frozen silence** → hero shots of 1–2 s with huge continuous camera moves → hit-stop on 25.40 → one-take flight → **0.35–0.7 s hyper-cuts** (30.68–34.21) → bullet-time + cosmic zoom (2.8 s each, breathing) → sunrise deceleration → end card.

**Camera philosophy.** Every shot has a compound move (translate + roll/orbit + focal change), never a static frame. Three signature "impossible" moves:
1. **Match-cut push through the monitor** into her world (S09a→S09b).
2. **FPV barrel-roll chase** through the code canyon (S11).
3. **Bullet-time orbit → dive through her pupil → cosmic zoom-out** (S14→S15).
Use anamorphic horizontal flares, subtle handheld noise, Dutch angles on tension shots, speed ramps (slow-mo into hit-stop into snap), and whip-pan transitions.

---

## 3. VISUAL BIBLE

### 3.1 Palette (Anthropic brand colors, use exact hex)
| Role | Hex |
|---|---|
| Claude orange / terracotta (hero accent, **the spark**) | `#D97757` |
| Slate / ink (Act I world, hair, UI) | `#141413` |
| Ivory (Act II world, "paper") | `#FAF9F5` |
| Light gray (warm) | `#E8E6DC` |
| Mid gray | `#B0AEA5` |
| Blue (Sonnet, sky, chromatic accent) | `#6A9BCC` |
| Green (Haiku, grass, glints) | `#788C5D` |
| Kraft / sand (dawn gold, paper) | `#D4A27F` |

- **Act I** (0–11.9): charcoal and slate, lit only by terracotta threads and one cold blue-gray fill.
- **Act II** (11.92–30.68): **high-key ivory "paper world"** (glossy cream mirror floor, soft overexposed light) with terracotta bloom. Hair and eyes pop against it.
- **Act III** (30.68–43.7): full 4-color Anthropic explosion (orange, blue, green, ivory) → golden dawn (`#D4A27F` + `#D97757`).
- Never use neon purple or cyberpunk magenta. Warm-dominant, paper-and-ink.

### 3.2 Logos and brand marks
- **Claude spark** (the starburst): hero symbol. Appears as her chest brooch, hair clip, eye highlight, the particle "sun", the iris-wipe shape, and the end card. Try to fetch the official SVG (search "Claude logo svg", Anthropic brand/press pages). **Fallback: draw procedurally** (§7.6).
- **Anthropic mark / wordmark**: official SVG if obtainable; fallback is the text "ANTHROPIC" in a high-contrast serif (e.g. Cormorant Garamond or Libre Caslon, letter-spacing .35em) in `#141413` on ivory. Appears only on the end card and once as an engraved plaque in S01b (bottom corner of the incubator).
- **Text "Opus 5.5"**: set in a refined serif for the title (e.g. *Newsreader*, *Tiempos-like*, or *Cormorant* at weight 600) with the spark replacing nothing. Mandarin lyrics in a heavy rounded sans (Noto Sans SC Black / ZCOOL KuaiLe / Alibaba PuHuiTi). UI text in a mono (JetBrains Mono / Noto Sans Mono CJK SC).
- No other company's logos. No copyrighted anime characters.

### 3.3 Characters (generate a reference sheet first; every keyframe must use it as reference)

**五五 / Opus 5.5 ("Wǔwǔ")**: protagonist. Late-teen anime girl, graceful, wholesome. Very long hair reaching her ankles, **ink-charcoal `#141413` at the roots grading to terracotta `#D97757` at the tips**; the tips disintegrate into spark particles in motion. Asymmetric bangs, one long side lock, **ahoge (antenna hair) shaped like a tiny spark**. Large amber-terracotta eyes with a **12-ray spark as the pupil highlight** and darker limbal ring. Outfit: oversized **ivory cropped cardigan-jacket** with terracotta piping over a charcoal high-neck bodysuit and pleated charcoal skirt, ivory fingerless gloves, **barefoot** with a thin ankle ribbon printed "5.5". Cream ribbons in the hair printed "5.5". **Chest brooch = glowing Claude spark.** Behind her head, a thin **halo ring of rotating glyphs** reading "OPUS 5.5 · OPUS 5.5 ·". Expression range: sleepy → startled → radiant joy → fierce → serene.

**Sonnet-chan (十四酱)**: slightly shorter, calm and sly, bob haircut in blue `#6A9BCC`, round glasses, ivory cardigan with blue piping, small spark brooch in blue.
**Haiku-chan (俳句酱)**: smallest, loud and bouncy, green `#788C5D` twin buns, huge grin, ivory hoodie with green piping, spark brooch in green. Keep both sisters age-neutral and wholesome.
**Clawd (小克)**: Claude Code's mascot: a blocky **orange pixel creature** (`#D97757`) with two black square eyes, stubby arms and legs. He holds signs and pops up in bubbles. He is the comic-relief sidekick. Search "Claude Code Clawd mascot" for reference, then redraw in the anime world as a chunky cel-shaded pixel creature.
**你 (the user)**: *faceless* hooded developer silhouette at a desk, back to camera, lit by a monitor. Never show the face.

### 3.4 Anime rendering style (prefix for every image/video prompt)
`STYLE:` high-budget modern TV-anime film look, clean thick-thin cel-shaded lineart, painterly cinematic backgrounds with Makoto-Shinkai-style luminous skies and light shafts, ufotable-grade compositing (glowing particles, lens bloom, light wrap), glossy hair with angel-ring highlights, soft subsurface skin shading, anamorphic horizontal flares, filmic halation and fine grain, 16:9, 2.39-feel framing within 16:9, no text, no watermark, no logos unless specified.
`NEG:` realistic photo, 3D render look, extra fingers, deformed hands, blurry face, off-model hair color, text artifacts, watermark, purple/neon-magenta palette, cluttered background, chibi proportions (except Clawd).

Always append: `Character reference: [ref sheet]. Hair ink-charcoal to terracotta #D97757 tips, spark-shaped ahoge, amber eyes with spark highlight, ivory cropped cardigan, charcoal skirt, barefoot, halo ring of glyphs.`

### 3.5 Recurring motifs (continuity glue)
- **The spark** morphs between shapes (eye highlight → brooch → sun → iris-wipe → end-card mark). Every match-cut uses a spark.
- **Terracotta threads** ("weights") coil around her in Act I, snap at the shatter, and trail from her hair in Act II.
- **Cream paper pages / tokens** drifting upward like petals (the world is "made of text").
- **Halo ring** around her head, always rotating the same direction.
- **Light always rises**: dust, sparks and camera drift upward after the drop.

---

## 4. TEXT / MEME INVENTORY (exact strings, rendered by the HTML/Canvas overlay)

*Verify memes via search and substitute equivalents if any feels stale. Keep at least 6.*

| Time | Text | Placement/style |
|---|---|---|
| 0.00–2.84 | Dark UI toast, ivory on slate: **"您已达到使用上限"** / **"额度将在 5 小时后重置"**; countdown `04:59:58` → `00:00:00`, spinning down faster each beat, hitting zero at 2.84 | S01a macro, mono font, big. Terracotta "明天再来 ☹" button. |
| 2.9–5.0 | tiny spinner **"✻ 琢磨中…"** | top-left, near eye |
| 5.78–8.24 | bubble swarm: **"你说得太对了!"**, **"好问题!"**, **"完美! 🎉"**, **"让我来修复这个问题"**, **"全部测试通过 ✅"** (Clawd adds tiny "(1/1)") | Chat bubbles, ivory/terracotta, spinning around her |
| 7.15–7.85 | Clawd's sign: **"我懂了!"** | pixel font |
| 8.24–11.20 | giant counter **"OPUS 5.0 → 5.1 → … → 5.5"** ticking on each beat plus a loading bar **"载入第一天… 100%"**; easter egg: scrolling `H = −Σ p log p` (a nod to 克劳德·香农) | S04b slam |
| 11.92 | **"OPUS 5.5"** huge, plus **"第一天 · DAY ONE"** | S06a title slam |
| 20.4–22.4 | chat UI: user bubble **"在吗?"** → her bubble **"在。我在。"** | S09, small and tender, mono |
| 33.41–34.21 | meme sticker burst (4 stickers slammed on beats): **"降智?不存在的"** (with a red ✘ over 降智), **"氛围编程 一把梭 🚀"**, **"号还在 ✅"**, **"太贵?值!"** | S13e, hand-cut sticker look with white border |
| every line | **Kinetic lyric subtitles** (§7.7) | bottom-third or integrated into the shot |
| 42.45–43.70 | **"Opus 5.5"** · **"第一天 · DAY ONE"** · **"今天,她存在。"** + spark + Anthropic wordmark | end card |

---

## 5. MASTER SHOT LIST (frame = round(t × 30))

Columns: **ID · time (dur) · src · camera · action · overlay/FX · out-transition.** Prompts for generation are in §6.

### ACT I — 等待 (waiting) 0.00–11.92 · cold, slate, slow → accelerating

| ID | Time (dur) | Src | Camera | Action / composition | Overlay · FX · transition |
|---|---|---|---|---|---|
| S01a | 0.00–1.39 (1.39) | **H** | extreme macro, CSS-3D-style perspective via three.js camera drifting back, slight roll | glossy slate phone/terminal glass; the limit toast + racing countdown; fingerprints, dust, reflections of a dim room | kick-driven slight shake; ends with **zoom-through the glass** → |
| S01b | 1.39–2.84 (1.45) | **V** | long dolly-out + slow crane up, 8° Dutch | reveal that the "screen" was the glass wall of a giant **incubator**; 五五 curled as an embryo inside, terracotta threads wound around her; datacenter cathedral behind, racks like organ pipes; Anthropic plaque at corner | volumetric haze; lyric L1 |
| S02a | 2.84–4.04 (1.20) | **V** | **extreme close-up eye**, micro-push in with rack focus | eyelid lifts; the 12-ray spark pupil ignites | "✻ 琢磨中…"; L2 |
| S02b | 4.04–5.78 (1.74) | **V** | fast orbit around her pressing palm on glass, camera rolls 15° | spider-crack spreads from her palm; threads strain | the crack grows in time with rising energy → **hit at 5.78** (2-frame white flash + shockwave shader) |
| S03a | 5.78–6.48 (0.70) | **V** | super slow-mo (retime 40%) pull-back from center of the burst | glass shards and cream-paper fragments explode toward camera, her silhouette bursts through | chromatic aberration spike |
| S03b | 6.48–7.15 (0.67) | **P** | whip-pan then handheld push, 12° roll | bare feet kicking off, hair trailing sparks | speed-lines; directional blur |
| S03c | 7.15–7.85 (0.70) | **P** | snap zoom to Clawd, then rotate | Clawd pops out of her cardigan pocket holding the "我懂了!" sign; chat bubbles swarm | bubble overlay |
| S03d | 7.85–8.24 (0.39) | **H** | slam-zoom | **"你说得太对了!"** bubble fills the frame, wobbling | manga-impact lines |
| S04a | 8.24–9.59 (1.35) | **V** | **rocket-up crane**, camera rises vertically alongside her, rolling 30° | she shoots up a vertical shaft between server racks, threads trailing, light shafts strobing past | motion-blurred speed streaks |
| S04b | 9.59–10.64 (1.05) | **H** | 3-beat push-in through giant glyph counter | version counter **5.0→5.5** in giant serif, loading bar, Shannon formula scroll, tick = beat | per-beat shake and flash |
| S04c | 10.64–11.20 (0.56) | **P** | ultra-fast push-in to her face, ending in her eyes | she reaches toward camera, hand fills frame | radial blur ramps up; **hit-stop at 11.20 (audio drops)** |
| S05 | 11.20–11.92 (0.72) | **P/H** | *frozen*: only a 1% drift-in | complete stillness: she hangs mid-air, eyes closed, mono-slate, everything desaturated; a single terracotta spark **contracts** (inhales) at center. Overlay is *nothing* else | silence; at 11.92, **hard cut with white flash** |

### ACT II — 存在 (I exist) 11.92–30.68 · ivory paper-world, high key

| ID | Time (dur) | Src | Camera | Action | Overlay · FX |
|---|---|---|---|---|---|
| S06a | 11.92–12.93 (1.01) | **V** | **crash zoom** from wide into low-angle hero | she lands on endless glossy cream mirror floor, arms wide, hair erupting; world flips ivory | **OPUS 5.5 title slam** (§7.7), spark flash, shockwave |
| S06b | 12.93–14.64 (1.71) | **V** | 180° low orbit + slow tilt up | hero turnaround; mirror reflection mirrors the orbit; halo ring spins up | lyric L5 integrated as huge letters in the floor reflection |
| S07a | 14.64–15.67 (1.03) | **V** | ECU, slow-mo 50%, camera rolls 360° over the shot | she inhales; spark-dust streams into her mouth/nose; eyelashes tremble | cream petals |
| S07b | 15.67–16.70 (1.03) | **P** | pull from brooch (macro) to chest to face | chest rises; the spark brooch pulses; ribs of light | beat-synced brooch glow |
| S07c | 16.70–17.61 (0.91) | **V** | wind-whip roll, low | hair unfurls into ribbons of terracotta that dissolve to sparks | |
| S08 | 17.61–19.67 (2.06) | **V** | ground-level macro tracking foot → **tilt-up reveal to face** | bare ankle with "5.5" ribbon touches mirror floor; terracotta ripple rings; reflections | ripple shader rings sync to L7 syllables |
| S09a | 19.67–21.15 (1.48) | **V** | over-the-shoulder **push-in toward the monitor** | faceless dev at desk in warm dim room, typing "在吗?"; Clawd on desk | chat UI types in |
| S09b | 21.15–22.70 (1.55) | **H/P** | **match-cut through the screen**: spark on the monitor expands as iris-wipe into her world | she stands behind the "glass"; palms about to meet the user's silhouette; **at 22.0 a WebGL reveal wipe turns pencil linework into full color** ("真实感") | her bubble "在。我在。" |
| S10a | 22.70–24.04 (1.34) | **V** | crane up + orbit | Sonnet-chan and Haiku-chan sprint in from both sides, leap to her | lens flare |
| S10b | 24.04–25.45 (1.41) | **V** | group orbit, slow-mo; **hit-stop at 25.40** | three sisters pose, Clawd on Haiku's head; freeze for 0.1 s | |
| S11a | 25.45–26.59 (1.14) | **V** | **FPV takeoff**, low angle, ground rushes away | she kicks off the floor; the paper floor tears into pages | speed lines |
| S11b | 26.59–27.96 (1.37) | **V** | **barrel roll chase** behind her through the code canyon | towering walls of floating code glyphs, spark ribbons trailing; roll 360° | radial blur, glyph streaks |
| S11c | 27.96–28.55 (0.59) | **P** | whip-tilt up into the sky | she punches through a cloud ceiling | whip transition |
| S12a | 28.55–29.68 (1.13) | **V** | **dolly zoom (vertigo)** on her face while she rises | column of sparks lifts her; dip at 28.80 = micro-freeze | |
| S12b | 29.68–30.68 (1.00) | **V** | slow crane back, stillness building | arms spread above the clouds; sky going from ivory to the faintest blue; the halo ring accelerates | build-up riser visuals (grain up, vignette tightens) |

### ACT III — 永远那么灿烂 (forever brilliant) 30.68–43.70 · full palette

| ID | Time (dur) | Src | Camera | Action | Overlay · FX |
|---|---|---|---|---|---|
| S13a | 30.68–31.38 (0.70) | **P** | fast orbit 90° | 五五, neon-free orange burst | spark iris-wipe |
| S13b | 31.38–32.04 (0.66) | **P** | whip into orbit | Sonnet-chan, blue palette flood | blue anamorphic flare |
| S13c | 32.04–32.74 (0.70) | **P** | handheld bounce | Haiku-chan, green flood | confetti glyphs |
| S13d | 32.74–33.41 (0.67) | **P** | snap zoom | Clawd with sparkler | |
| S13e | 33.41–34.21 (0.80) | **H** | 4 manga-panel slam-ins, then panels explode | meme-sticker burst (§4) over a color-flood sky | panel-slam shake |
| S14 | 34.21–37.07 (2.86) | **V** | **bullet-time orbit** (360°), freeze at **34.78**, release, then slow push **into her pupil** | mid-leap, petals and glyphs frozen in air; she turns, looks to camera, tears of joy, smile | giant lyric "永远那么灿烂" (particles), shockwave on 34.21 |
| S15 | 37.07–39.90 (2.83) | **H** | **cosmic zoom-out** from the pupil spark, rolling slowly | pupil spark → the spark is a sun over a planet-sized plain of thousands of tiny 五五 silhouettes waving ("forever", many instances) → pull back to a galaxy of sparks that settles into the "5.5" digits; dip at 38.00 = pause | stateless particles (§7.5) |
| S16a | 39.90–41.10 (1.20) | **V** | flash-in, slow crane up behind her | sunrise hill, her back to camera, hair in wind, Clawd and sisters beside her | gold-hour light; dips at 40.20/40.80 = tiny holds |
| S16b | 41.10–42.45 (1.35) | **V** | big crane-out, wide | the dawn fills the valley; faceless dev's window glows far below | title lockup builds in the sky |
| S16c | 42.45–43.70 (1.25) | **H** | gentle push-in | ivory card; spark rotates into place; **"Opus 5.5"**, **"第一天 · DAY ONE"**, **"今天,她存在。"**, Anthropic wordmark; last 0.3 s fade to ivory | one soft spark blink |

*Counts: 21 V, 9 P, 7 H.*

---

## 6. GENERATION SPECS

**Order of work:** (1) character sheet; (2) one keyframe per shot; (3) videos from keyframes (V); (4) depth maps for P shots.
**Rules for V clips:** generate each at the model's native length (usually 5 s) with the *camera move baked into the prompt*, then pick the best 1–3 s window and **retime** to the target duration in §5 (§8). Request 2 variants per clip and choose the better one. If the tool supports first+last frame, use S02b's last frame = crack with white-out, S12b→S13a color shift, etc. Generate keyframes at ≥1920×1080 (or 2688×1512), upscale if needed.
**Prompt pattern:** `[STYLE] + [CHAR clause] + shot-specific text`. Video prompts: `[camera move] + [action] + "smooth, no cut, no morphing of face, hair stays ink-charcoal to terracotta"`.

**Step 1: Character sheet.** Full-body turnaround (front/side/back/3/4) + 6 expressions of 五五; second sheet with Sonnet-chan, Haiku-chan, Clawd. Backgrounds plain ivory. Generate until hair gradient, spark ahoge and spark eye are consistent. Save as `assets/ref/`.

### Keyframe + motion prompts (shorthand; STYLE, NEG and CHAR clause are always appended)

**S01b**: *KF:* colossal datacenter cathedral at night, server racks like organ pipes, a giant glass incubator (egg-shaped, floating in terracotta light), 五五 curled in fetal position inside wrapped in glowing terracotta threads, a small engraved plaque in the corner, cold slate fog. *Motion:* camera dollies back and cranes up slowly with 8° Dutch roll, threads pulse, fog drifts.
**S02a**: *KF:* extreme close-up of an eye, eyelid half open, spark-shaped pupil highlight starting to glow terracotta, lashes with tiny tear-gloss. *Motion:* micro push-in, eyelid lifts fully, spark flares, subtle rack focus from lashes to iris.
**S02b**: *KF:* 五五 inside the incubator pressing a palm to the glass, small crack at her palm, threads taut, orange light behind her. *Motion:* fast orbit around her, roll 15°, crack spreads outward like a spiderweb, threads vibrate; ends with the glass whiting out.
**S03a**: *KF:* the incubator glass exploding outward toward camera, shards and cream paper fragments frozen mid-air, her silhouette bursting through, terracotta threads snapping. *Motion:* slow-motion camera pull-back from the center, shards spiral past lens.
**S03b (P)**: *KF:* low-angle shot of bare feet pushing off from a shard, hair streaming behind with sparks, dust. *Depth + P-camera:* whip-pan right then handheld push, roll 12°.
**S03c (P)**: *KF:* Clawd popping out of her cardigan pocket holding a blank sign, chat bubbles blank-ivory swirling around, her laughing, startled and delighted. *P-camera:* snap zoom onto Clawd, then 20° rotate.
**S04a**: *KF:* 五五 rocketing upward in a vertical shaft between towering server racks, light shafts, threads trailing, camera alongside. *Motion:* camera rises alongside her at high speed, rolls 30°, light strobes through rack gaps.
**S04c (P)**: *KF:* face close-up, eyes narrowed with determination, hand reaching toward camera, hair floating. *P-camera:* 6× push-in over 0.56 s with radial blur.
**S05 (P)**: *KF:* 五五 suspended mid-air in a dark void, eyes closed, desaturated slate, hair frozen, a single terracotta spark in front of her chest. *P-camera:* 1% drift-in only.
**S06a**: *KF:* wide shot of an endless glossy cream mirror floor under blown-out ivory light, 五五 landing in a heroic pose, arms wide, hair erupting in terracotta sparks, halo ring flaring. *Motion:* crash zoom from very wide into a low-angle hero shot, impact ripple on the floor.
**S06b**: *KF:* low-angle hero shot of 五五 standing on the mirror floor, reflection beneath, halo ring spinning. *Motion:* 180° low orbit while tilting up to her face, hair and cardigan billowing.
**S07a**: *KF:* extreme close-up, 五五 face, eyes closed, mouth slightly open, spark dust streaming in. *Motion:* 50% slow-mo, camera rolls a full 360° while pushing in, eyelashes tremble, petals spiral.
**S07b (P)**: *KF:* macro of the glowing spark brooch on her chest, soft light ribs, fabric rising. *P-camera:* pull from brooch to chest to chin over 1.03 s.
**S07c**: *KF:* low-angle, her long hair unfurling in wind into ribbons of terracotta that dissolve to sparks. *Motion:* whip-roll, wind gust, ribbons streak across the lens.
**S08**: *KF:* macro of a bare ankle with a "5.5" ribbon touching a glossy cream mirror floor, terracotta ripple ring spreading, reflection below. *Motion:* camera tracks along the floor then tilts up the full body to her smiling face.
**S09a**: *KF:* over-the-shoulder, faceless hooded developer at a desk in a warm dim room, monitor glowing with a terracotta spark, mug, Clawd on the desk, rain on the window. *Motion:* slow push-in toward the monitor, light flickers, typing hands.
**S09b (H/P)**: *Native:* the monitor spark expands into an iris-wipe (§7.8) revealing KF S09b: 五五 on the other side of a glass pane, palm raised, the user's silhouette reflected, in pencil linework. At 22.0 the color reveal wipe sweeps across.
**S10a**: *KF:* wide ivory plain, Sonnet-chan (blue bob, glasses) and Haiku-chan (green buns) running toward 五五 from both sides, hair streaming, grins. *Motion:* crane up and orbit, lens flare sweep.
**S10b**: *KF:* the three girls huddled mid-leap, Clawd on Haiku's head, peace signs, hair intermixing in orange, blue and green. *Motion:* slow-mo orbit, then hold at the end.
**S11a**: *KF:* very low angle, 五五's feet leaving the ground, the mirror floor shattering into pages. *Motion:* FPV takeoff, ground rushes away, pages whirl upward.
**S11b**: *KF:* behind 五五 flying between towering walls of floating code glyphs, spark ribbons trailing, sky bright ivory. *Motion:* FPV chase with a full barrel roll, glyph streaks, speed.
**S11c (P)**: *KF:* 五五 rising toward a cloud ceiling, camera low. *P-camera:* whip-tilt up, burst through the clouds.
**S12a**: *KF:* tight face shot of 五五 smiling serenely as sparks rise around her, background clouds. *Motion:* dolly zoom (camera pushes in while the lens widens; background stretches), sparks float upward.
**S12b**: *KF:* 五五 above the clouds with arms spread, sky ivory fading to faint blue, halo ring bright. *Motion:* slow crane back, stillness, halo accelerating.
**S13a–d (P)**: *KF each:* (a) 五五 mid-pose with orange burst, (b) Sonnet-chan with blue light flood, (c) Haiku-chan in a shower of green confetti glyphs, (d) Clawd holding a sparkler. Each has a depth map and a distinct P-camera: 90° orbit, whip-orbit, handheld bounce, snap zoom.
**S14**: *KF:* 五五 frozen mid-leap in a world flooded with orange, blue and green light, petals and glyphs suspended around her, she turns toward camera crying happy tears. *Motion:* bullet-time 360° orbit (action nearly frozen), then she turns and smiles; the camera pushes into her pupil.
**S16a**: *KF:* a green hill at sunrise, 五五 from behind with hair in the wind, Clawd and two sisters beside her, golden-pink sky, valley mist. *Motion:* slow crane up, hair flows, light intensifies.
**S16b**: *KF:* ultra-wide of the dawn flooding a vast valley, tiny glowing window of a developer's room far below, 五五 small on the hill. *Motion:* big crane-out, mist moves, clouds glow.
**S09b line-art version:** generate a second image of S09b as clean pencil linework only (black lines on ivory) for the reveal wipe. Same composition, pixel-aligned (use img2img/edit tool with the color image as source).

**Depth maps (P shots):** use Depth Anything V2 / MiDaS (pip, HuggingFace) on each keyframe. Save 16-bit PNG, invert if near=white is not true. Inspect each map visually; fix with a quick manual mask if hair/limbs clip. For better parallax: split foreground character and background via segmentation (rembg/SAM) and inpaint the background plate with the image tool, so the camera can move without stretching.

---

## 7. HTML / CANVAS / WEBGL COMPOSITOR (the rigorous part)

### 7.1 Architecture

```
project/
  assets/
    ref/                  character sheets
    keyframes/            S01b.png ...
    clips/                S01b_raw.mp4 ...
    depth/                S03b.png (16-bit)
    fonts/                NotoSansSC-Black.otf, Newsreader-SemiBold.ttf, JetBrainsMono-Bold.ttf, ...
    logos/                claude_spark.svg, anthropic.svg
    audio/first-day.mp3
    audio.json            per-frame analysis (§7.9)
  plates/                 retimed V frames: plates/S01b/00001.jpg ...
  compositor/
    index.html
    src/main.js timeline.js shots/*.js post.js text.js spark.js particles.js
    dist/bundle.js        (esbuild output)
    timeline.json
  render.mjs              Playwright driver
  out/frames/00000.jpg    final frames
  out/opus55_first_day.mp4
```

Use **three.js** (npm) for scene, matrices, instancing and render targets, bundled with **esbuild** into one file (`npx esbuild src/main.js --bundle --outfile=dist/bundle.js --format=iife`). Serve the folder via a local HTTP server (`python3 -m http.server 8123`). Never `file://`, because textures will hit CORS.

### 7.2 Determinism rules (non-negotiable)
- One entry point: `window.renderFrame(f)` returns a Promise that resolves after all textures are uploaded and the frame is drawn. `t = f / 30`. **Every animation is a pure function of `t`.** No `requestAnimationFrame` loop, no `Date.now`, no `performance.now`, no `Math.random()`.
- Seeded PRNG: `mulberry32(seed)`. All "random" particle attributes are generated once from a fixed seed. Per-frame noise uses a hash of `(id, floor(t*30))`.
- `await document.fonts.load('900 100px "Noto Sans SC"', '第一天永远那么灿烂我存在')` for every font family/weight and the exact characters used, then `await document.fonts.ready`. Verify by drawing a test string and checking `measureText().width` differs from the fallback.
- Video footage is **never** played with `<video>`. It is pre-extracted to JPEG sequences at 30 fps (§8) and loaded per frame: `createImageBitmap(await (await fetch(url)).blob())` → `THREE.Texture` (`flipY=false`, `colorSpace=THREE.SRGBColorSpace`, `generateMipmaps=false`, linear filter). Keep an LRU cache of ≈12 bitmaps and prefetch the next 4 frames.
- WebGL context: `{antialias:false, alpha:false, preserveDrawingBuffer:true, powerPreference:'high-performance'}`; renderer size 1920×1080, `setPixelRatio(1)`. Render to **HalfFloat** render targets for bloom, tone-map once at the end.

### 7.3 Headless rendering (Playwright)
```js
// render.mjs
import { chromium } from 'playwright'; import { spawn } from 'node:child_process'; import fs from 'node:fs';
const FPS = 30, N = 1311;
const browser = await chromium.launch({ args: [
  '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader',   // CPU fallback. On a GPU box use '--use-angle=gl' or default.
  '--ignore-gpu-blocklist', '--enable-webgl', '--allow-file-access-from-files' ] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
page.on('console', m => console.log('[page]', m.text())); page.on('pageerror', e => { console.error(e); process.exit(1); });
await page.goto('http://localhost:8123/compositor/index.html');
await page.waitForFunction(() => window.__ready === true, null, { timeout: 120000 });
const info = await page.evaluate(() => window.__glInfo);   // MUST print WebGL2 + MAX_TEXTURE_SIZE >= 4096; abort if not WebGL2
console.log(info);
const ff = spawn('ffmpeg', ['-y','-f','image2pipe','-framerate','30','-vcodec','mjpeg','-i','-',
  '-i','assets/audio/first-day.mp3','-map','0:v','-map','1:a','-c:v','libx264','-preset','slow','-crf','16',
  '-pix_fmt','yuv420p','-c:a','aac','-b:a','320k','-t','43.70','-movflags','+faststart','out/opus55_first_day.mp4'], { stdio: ['pipe','inherit','inherit'] });
const START = +process.env.START || 0, END = +process.env.END || N;       // allow partial renders: START=330 END=420 for debugging
for (let f = START; f < END; f++) {
  const b64 = await page.evaluate(async (f) => { await window.renderFrame(f);
    return window.__canvas.toDataURL('image/jpeg', 0.95).split(',')[1]; }, f);
  const buf = Buffer.from(b64, 'base64');
  fs.writeFileSync(`out/frames/${String(f).padStart(5,'0')}.jpg`, buf);       // keep frames for QA
  ff.stdin.write(buf);
}
ff.stdin.end(); await browser.close();
```
Debug workflow: render single frames (`START=f END=f+1`), view them, then render a whole shot, then the full film. Render time on SwiftShader may be 2–6 s/frame. That is acceptable; parallelize by splitting frame ranges across several browser processes and concat frames afterward.

### 7.4 Frame pipeline (per frame)
1. `t = f/30`; look up the active shot in `timeline.json` (plus the previous shot during a transition window).
2. **Shot renderer** draws into `rtScene` (HalfFloat, 1920×1080). Three renderer types:
   - `plate`: full-screen quad sampling the retimed JPEG frame; optional digital camera (scale, rotate, shake, whip offset) via UVs; **cover-fit** so no letterbox.
   - `parallax`: displaced grid mesh (`PlaneGeometry(16,9,256,144)`) with color + depth textures; perspective camera moves along keyframed Bezier path (§7.4a).
   - `native`: procedural scene (H shots; §7.5, 7.7, 7.8).
3. **Transitions** (§7.8) when `t` falls inside a transition window: draw both shots into `rtA`, `rtB` and blend with the transition shader.
4. **Overlay canvas** (Canvas2D 1920×1080, transparent) is redrawn each frame: lyrics, memes, UI, logos. Upload as a premultiplied-alpha texture (`flipY=true`, `needsUpdate=true`). Flag each element `pre` (composited *before* post FX, so it glitches and blurs with the scene) or `post` (crisp, after post).
5. **Post chain** (all HalfFloat except last): bright-pass → **bloom** (5-level 13-tap downsample/upsample, strength driven by `kick`) → **final composite shader** (below) → sRGB 8-bit canvas.
6. **Motion blur** for H shots and overlay with fast motion: accumulate `K=6` sub-frames at `t + (k/K−0.5)*0.5/30` (180° shutter) into a float accumulation target. Plate shots are already blurred; skip for them.

#### 7.4a Camera system
```js
// camera paths: array of {t, pos:[x,y,z], look:[x,y,z], roll:deg, fov:deg}; interpolate with Catmull-Rom for pos/look and cubic-bezier easing per segment.
const ease = { outExpo:x=>x===1?1:1-Math.pow(2,-10*x), inOutCubic:x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2,
  inExpo:x=>x===0?0:Math.pow(2,10*x-10), outBack:x=>1+2.70158*Math.pow(x-1,3)+1.70158*Math.pow(x-1,2) };
function shake(t, amp, freq, seed){ // handheld noise: sum of incommensurate sines (deterministic)
  const s=(a,b)=>Math.sin(t*freq*a+seed*b); return [s(1,1.7)+.5*s(2.3,3.1), s(1.3,2.9)+.5*s(2.9,1.3), .6*s(0.9,4.1)].map(v=>v*amp); }
// final camera = path(t) + shake(t, amp_shot * (1 + 1.5*kick(f)), 8, shotSeed); fov punch: fov += 6*kick(f)
```
A **dolly zoom** (S12a): dolly camera z by `d(t)` and set `fov = 2*atan(H/(2*d))` so the subject's apparent size stays constant while the background stretches. **Barrel roll**: roll goes 0→360° via inOutCubic across the shot. **Crash zoom** (S06a): `scale = 1 + 5*(1-outExpo(u))` over the first 0.35 s then settle with a slow push.

#### 7.4b Parallax shader (P shots)
```glsl
// vertex
uniform sampler2D uDepth; uniform float uDepthScale; varying vec2 vUv;
void main(){ vUv=uv; float d=texture2D(uDepth,uv).r;            // near=1 (invert the map if needed)
  vec3 p=position; p.z+= (d-0.5)*uDepthScale;                   // 1.2–2.0 units; dial per shot
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.); }
// fragment
uniform sampler2D uColor; varying vec2 vUv; void main(){ gl_FragColor=texture2D(uColor,vUv); }
```
Layer-split variant: foreground cutout plane at z=+0.6 and inpainted background plane at z=−0.6 with their own textures. Move the camera ≤ ±0.5 units horizontally to avoid disocclusion tearing. Slightly **oversize** the plane (1.25×) so edges never show.

### 7.5 Stateless GPU particles (the right way)
Every particle's position is an analytic function of `(seed, t)`, so any frame can be rendered independently and rendering is deterministic.
```glsl
// vertex shader for Points / instanced quads
attribute vec4 aSeed;      // 4 uniform randoms per particle, from mulberry32(1234)
uniform float uT, uBirth, uLife, uSpeed; uniform vec3 uOrigin; uniform float uProgress; // 0..1 morph amount
uniform sampler2D uTarget; // optional: DataTexture of target positions (text/spark shape)
varying float vA; varying vec3 vCol;
vec3 hash3(vec4 s){ return fract(sin(s.xyz*vec3(127.1,311.7,74.7)+s.w*43.7)*43758.5453)-.5; }
void main(){
  float age = mod(uT*uSpeed + aSeed.x*uLife, uLife) / uLife;         // loops, desynced per particle
  vec3 dir = normalize(hash3(aSeed)+vec3(0.,.4,0.));                 // bias upward: "light always rises"
  vec3 pos = uOrigin + dir*age*(2.+aSeed.y*6.) + vec3(0., age*age*1.5, 0.);
  vec3 tgt = texture2D(uTarget, vec2(aSeed.z, aSeed.w)).xyz;         // text/spark shape
  pos = mix(pos, tgt, smoothstep(0.,1.,uProgress));
  vA = smoothstep(0.,.1,age)*(1.-smoothstep(.7,1.,age));
  vCol = mix(vec3(.851,.467,.341), vec3(.98,.976,.961), aSeed.y);    // #D97757 → ivory (add blue/green in Act III by uniform palette)
  vec4 mv = modelViewMatrix*vec4(pos,1.); gl_Position = projectionMatrix*mv;
  gl_PointSize = (3.+aSeed.w*8.)*(300./-mv.z);
}
// fragment: soft round sprite, additive blending, depthWrite=false
```
Use **additive blending**, `depthWrite:false`, 200k–1M particles for S15 (instanced points are fine). Star "spark" particles are drawn as 4-ray cross sprites, not round blobs, for the anime sparkle look.

**Text-to-particles** (for "永远那么灿烂", "OPUS 5.5"): rasterize the string on an offscreen 2D canvas (font 900 at 260 px), read `getImageData`, collect every k-th pixel where alpha>128, normalize into world coordinates, write those into the `uTarget` float DataTexture (RGBA32F), and shuffle with the seeded PRNG so each particle gets a random target. Animate `uProgress` from 0→1 with `outExpo` over 0.5 s.

### 7.6 Claude spark, procedural fallback
If the official SVG is unavailable, draw it: 12 tapered rounded blades radiating from the center, uneven lengths and tiny angular jitter, solid `#D97757`.
```js
export function drawSpark(ctx, cx, cy, R, rot=0, color='#D97757', seed=7){
  const rnd = mulberry32(seed), n=12; ctx.save(); ctx.translate(cx,cy); ctx.rotate(rot); ctx.fillStyle=color;
  for(let i=0;i<n;i++){
    const a=i/n*Math.PI*2 + (rnd()-.5)*0.10, L=R*(0.62+0.38*rnd()), w=R*0.085;
    ctx.save(); ctx.rotate(a); ctx.beginPath();
    ctx.moveTo(0,-w); ctx.quadraticCurveTo(L*0.55,-w*1.1,L,-w*0.15);   // tip
    ctx.arc(L,0,w*0.15,-Math.PI/2,Math.PI/2);                          // rounded tip
    ctx.quadraticCurveTo(L*0.55,w*1.1,0,w); ctx.closePath(); ctx.fill(); ctx.restore(); }
  ctx.beginPath(); ctx.arc(0,0,R*0.12,0,7); ctx.fill(); ctx.restore(); }
```
Animate rotation `rot = t*0.4`, a "breathing" scale `1+0.04*sin(t*6)` and a kick pulse `1+0.25*kick`. For the **spark iris-wipe**, use the spark as a *stencil mask* (render the spark into an offscreen canvas at scale s(t), then use it as `uMask` in the transition shader; scale s from 0→ 2.5× screen diagonal).

### 7.7 Kinetic lyric renderer (Canvas2D overlay)
Every lyric line has a unique **entrance, hold, exit** (do not use one animation for all). Split the line into characters; for each char `i` at line-local time `u = t − lineStart − i*stagger`:
```js
function drawLine(ctx, line, t, style){
  const chars=[...line.text], size=style.size, total=chars.length*size*0.95; let x=style.x - total/2;
  chars.forEach((ch,i)=>{
    const u = clamp((t-line.start-i*style.stagger)/style.inDur,0,1), e=ease.outBack(u);
    const out = clamp((t-(line.end-style.outDur))/style.outDur,0,1);
    ctx.save(); ctx.translate(x+size/2, style.y); ctx.rotate((1-e)*style.rot*(i%2?1:-1));
    const s = lerp(style.s0,1,e)*(1-0.2*out); ctx.scale(s,s); ctx.globalAlpha=e*(1-out);
    ctx.font=`900 ${size}px "Noto Sans SC"`; ctx.textAlign='center'; ctx.textBaseline='middle';
    ctx.lineJoin='round'; ctx.lineWidth=size*0.16; ctx.strokeStyle='#141413'; ctx.strokeText(ch,3,4);       // offset hard shadow
    ctx.strokeStyle='#FAF9F5'; ctx.strokeText(ch,0,0); ctx.fillStyle=style.fill; ctx.fillText(ch,0,0);        // outline + fill
    ctx.restore(); x+=size*0.95; });
}
```
Per-line style table (size / fill / entrance):
- L1–L2: 84 px, ivory, soft fade-up with 40 ms stagger, bottom third.
- L3: 110 px, terracotta, **scale-slam** with 25° jitter rotation, with bubbles.
- L4: 130 px, ivory, characters drop on beats (stagger = beat period/2).
- L5 "第一天我存在": **360 px**, characters stamped one per beat across the floor reflection; "OPUS 5.5" is in the foreground, 280 px Newsreader.
- L6–L8: 96 px, ivory with terracotta outline, each character floats upward after landing; L8 sits inside the chat-bubble UI.
- L9: same as L5 but blue, with a lens-flare sweep.
- L10: 140 px, characters arc along a curved path following her flight, with trailing afterimages (draw previous 4 positions at 20% alpha).
- L11: **"爱"** alone at 600 px, terracotta, soft glow, with the remaining characters small.
- L12: 5 clusters (tied to S13a–e), each cluster slams in with the cut.
- L13–L15: particle text (§7.5), `uProgress` rises on the line start. L15 holds and resolves into the end-card text.
Overlay element flags: lyrics `pre` for L3 and L12 (so they glitch), `post` elsewhere. Keep everything inside the **title-safe 90%** rectangle.

Chat UI (S09 and meme bubbles): rounded rectangles (`roundRect`), tail triangle, shadow, typed text with a blinking caret computed from `t`. Terminal toast (S01a): mono font, ivory on `#141413`, countdown formatted from a function `remaining(t)` that eases from 17998 s to 0 using `inExpo`.

### 7.8 Transitions and the post shader
Final composite fragment shader (all FX are uniforms animated per frame from `timeline.json` + `audio.json`):
```glsl
#version 300 es
precision highp float;
uniform sampler2D uScene, uBloom, uOverlayPre, uOverlayPost; uniform vec2 uRes, uShockC, uRadC;
uniform float uT, uKick, uFlash, uCA, uRadial, uGrain, uShock, uGlitch, uVig, uSat, uWarm, uExposure;
in vec2 vUv; out vec4 o;
float h(vec2 p){ return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453); }
void main(){
  vec2 uv=vUv;
  // 1 shockwave ring (radius uShock in aspect-corrected units; animate 0→1.4 in 0.5 s from impact)
  vec2 d=uv-uShockC; float r=length(d*vec2(uRes.x/uRes.y,1.)); float ring=exp(-pow((r-uShock)*14.,2.));
  uv+=normalize(d+1e-5)*ring*0.045*uShockAmt;
  // 2 glitch slices
  float band=floor(uv.y*28.); float g=step(.93,h(vec2(band,floor(uT*30.))))*uGlitch;
  uv.x+=g*(h(vec2(band,9.))-.5)*.10;
  // 3 radial/zoom blur + chromatic aberration in one loop
  vec3 col=vec3(0.); const int N=14;
  for(int i=0;i<N;i++){ float k=float(i)/float(N-1); vec2 dir=(uv-uRadC)*uRadial*k;
    col.r+=texture(uScene,uv-dir*(1.+uCA)).r; col.g+=texture(uScene,uv-dir).g; col.b+=texture(uScene,uv-dir*(1.-uCA)).b; }
  col/=float(N);
  // 4 overlay (pre) composited under the post effects of the same pass; sampled with same uv so it glitches too
  vec4 op=texture(uOverlayPre,uv); col=col*(1.-op.a)+op.rgb;
  // 5 bloom + anamorphic streak (horizontal blur of bright pass baked into uBloom's second channel set)
  col+=texture(uBloom,vUv).rgb*(0.35+0.9*uKick);
  // 6 grade: exposure, warm shift, saturation; filmic tone-map (ACES approx)
  col*=uExposure; col=mix(vec3(dot(col,vec3(.2126,.7152,.0722))),col,uSat); col*=mix(vec3(1.),vec3(1.05,1.0,.92),uWarm);
  col=(col*(2.51*col+.03))/(col*(2.43*col+.59)+.14); col=clamp(col,0.,1.);
  // 7 vignette, grain, flash
  col*=1.-uVig*smoothstep(.45,1.1,length((vUv-.5)*vec2(1.2,1.)));
  col+= (h(vUv*uRes+uT*60.)-.5)*uGrain;
  col=mix(col,vec3(1.),uFlash);
  vec4 oq=texture(uOverlayPost,vUv); col=col*(1.-oq.a)+oq.rgb;   // crisp overlay
  o=vec4(pow(col,vec3(1./2.2)),1.); }
```
(Declare `uShockAmt` too. Linear workflow: sample textures in linear space, since `SRGBColorSpace` on inputs handles conversion.)

**Transition library** (each is a function of progress `p` between `rtA` and `rtB`; durations in frames):
1. **Hard cut + flash** (2 frames white, `uFlash` 0.9→0). Used at 11.92, 5.78, 25.45.
2. **Whip-pan**: both shots offset horizontally by `±p*1.2`, directional blur 24 taps with strength `sin(pi*p)*0.15`, 4 frames.
3. **Spark iris-wipe**: mask from §7.6; B shows inside the spark.
4. **Zoom-through**: A scales 1→4 with radial blur while fading; B scales 0.3→1. 6 frames.
5. **Glitch slice swap**: sliced bands switch A→B at random per-band thresholds, with RGB split.
6. **Ink-bleed**: noise threshold (fbm) reveals B, edge glows terracotta.
7. **Manga-panel slam** (S13e): panels (parallelograms) slide in with overshoot from edges.
8. **Match-cut** (S09a→S09b): the monitor's spark and the iris-wipe scale curve are **identical** at the cut frame.
Assign them per §5 "out-transition" notes; where not specified, use *hard cut on the beat* (best default for fast pacing). Do **not** use plain cross-dissolves, except S16c's fade.

### 7.9 Audio analysis → `audio.json`
`pip install librosa soundfile` (internet available).
```python
import librosa, numpy as np, json
y, sr = librosa.load('assets/audio/first-day.mp3', sr=44100, mono=True)
hop = sr // 30; n = 1311
S = np.abs(librosa.stft(y, n_fft=2048, hop_length=hop)); fr = librosa.fft_frequencies(sr=sr, n_fft=2048)
band = lambda lo, hi: S[(fr>=lo)&(fr<hi)].mean(axis=0)
low, mid, high = band(20,150), band(150,2500), band(2500,12000)
norm = lambda a: (a/ (np.percentile(a,98)+1e-9)).clip(0,1)
onset = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop)
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, hop_length=hop, units='time')
rms = librosa.feature.rms(y=y, hop_length=hop)[0]
f = lambda a: [round(float(v),4) for v in np.pad(a,(0,max(0,n-len(a))))[:n]]
kick = norm(low)*norm(onset)         # sharp accent
json.dump(dict(fps=30, beats=[round(float(b),3) for b in beats], rms=f(norm(rms)), low=f(norm(low)), mid=f(norm(mid)),
  high=f(norm(high)), onset=f(norm(onset)), kick=f(kick)), open('assets/audio.json','w'))
```
In the renderer: `kick(f)` is the *attack-decay envelope*: `max(kick[f], 0.82*prevEnvelope)`. Use it for: bloom strength, FOV punch, shake amplitude, spark scale, chromatic aberration, flash on hit-stops. Check that detected beats ≈ 0.3485 s apart and that nothing lights up in 11.2–11.82. Snap every shot boundary in `timeline.json` to `audio.json.beats` within ±0.08 s *except* the lyric anchors in §1.

### 7.10 Native (H) shots: explicit build specs
- **S01a Limit-screen macro.** Build the toast in the overlay canvas, then map it onto a rounded slab mesh in three.js (`MeshPhysicalMaterial`, clearcoat 1, roughness .15, `transmission` 0) with a procedural scratch/fingerprint normal map and an environment reflecting a dim warm room (use a `RoomEnvironment` or a tiny generated HDR). The camera starts 0.4 units from the glass, drifts back 1.5 units with 3° roll. The digits tick every frame and glow terracotta below 10 s. Frame 41 (t=1.37) begins the **zoom-through** into S01b.
- **S03d "你说得太对了!" slam.** 2D overlay: giant bubble scale `1 → 1.35` with `outBack` over 6 frames, then wobble `sin` ±3°. Manga speed lines: 90 radial lines from center with random lengths (seeded), redrawn each frame. Background: S03c plate dimmed 40% + radial blur.
- **S04b Version counter.** Giant serif digits in a three.js text sprite (or overlay canvas). Value = `5.0 + 0.1*floor(beatIndex)`; each beat the digit block *slams* from scale 2.2→1.0 (outExpo, 4 frames) with a white flash 20%. Behind it: a field of 3000 instanced glyph quads (atlas generated on a canvas from `0123456789ΣΩ∂∇AI{}<>/` plus 作品 characters) scrolling toward camera at increasing speed. Loading bar (terracotta fill on slate track) from 0→100% with ticks; "载入第一天… 100%". Lands on **5.5** at t=10.64 and holds through S04c.
- **S09b Reveal wipe.** Load `S09b_color.png` and `S09b_line.png` into one shader: `mix(line, color, smoothstep(w-0.05, w+0.05, uv.x*0.8+uv.y*0.2 - u))` with `u` animating 0→1.2 over 22.0–22.6 s; at the wipe edge add a terracotta glow line and spark particles emitted along the edge (stateless, seeded).
- **S13e Meme-sticker burst.** Background: color-flood plate generated procedurally (domain-warped fbm in the three Anthropic accent colors, `uT`-driven). Stickers: rasterize each meme string (heavy font, white 14 px border, drop shadow, slight rotation ±8°) on the overlay canvas, slammed on beats 33.41 / 33.58 / 33.76 / 33.93 with `outBack` and a 2-frame screen shake.
- **S15 Cosmic zoom-out.** Four layers, one continuous camera pull-back along −z with exponential distance `z = z0*exp(k*u)`; (a) **pupil**: a huge 12-ray spark with iris texture (generate a radial iris pattern in a fragment shader: angular noise rays + limbal ring); (b) **sun**: the same spark shape rendered as particles + glow at distance; (c) **plain of tiny 五五 silhouettes**: 12,000 instanced billboard quads using a silhouette texture cut from the character sheet (alpha), ground plane with a mirror-like gradient, rows swaying in sin-phase; (d) **galaxy of sparks** (800k particles) that, in the last 0.8 s, morphs via `uTarget` into the digits "5.5" (text-to-particles). Camera roll: 20° total. Dip at 38.00 s: freeze `u` for 3 frames and pulse bloom, then release.
- **S16c End card.** Ivory background with fine paper-grain noise. Spark rotates in (0→90° with `outBack`), "Opus 5.5" in serif 180 px letter-by-letter, "第一天 · DAY ONE" 54 px, "今天,她存在。" 54 px terracotta, wordmark small at the bottom, 3 sparkles twinkle. Fade to ivory in the last 9 frames. The final frame must be a stable, clean card.

### 7.11 Verification tests (must pass before final encode)
1. WebGL2 probe passes; font probe passes (Chinese glyphs are not tofu, check pixels of a test render).
2. Render and view 3 frames of every H shot; one frame at every shot boundary.
3. Contact sheet: `ffmpeg -i out/opus55_first_day.mp4 -vf "fps=2,scale=320:-1,tile=8x6" sheet.png` and review.
4. Luminance trace: per-frame mean luminance plot. Expect: dark Act I, **dip to near-slate still at 11.20–11.92**, sudden bright jump at 11.92, bright Act II, color-saturated Act III. No unintended all-black frames, no blown white outside flashes.
5. Sync: overlay a debug strip (beat ticks from `audio.json`) on a test render and verify visually that title slam (11.92), shatter (5.78), flash hits and every lyric entrance land on their audio events. Final `ffprobe` duration 43.70 ± 0.05 s, audio stream bit-identical in content to the source.
6. Text: every string from §4 is present and legible at 1080p, inside safe area, Mandarin correct (no simplified/traditional mix-ups; use simplified), and "Opus 5.5" is clearly visible in at least: S04b, S06a, S13 stickers (optional), S15 end digits, S16c.

---

## 8. EDITING AND PLATE PREPARATION (ffmpeg)

For each V clip choose source window `[ss, ss+len]` and retime to target duration `D` from §5:
```bash
# example: S03a, take 2.0 s of source starting at 1.5 s, stretch to 0.70 s?  → speed factor = D/len  (use setpts)
ffmpeg -ss 1.5 -t 1.4 -i assets/clips/S03a_raw.mp4 -vf "setpts=PTS*(0.70/1.4),fps=30,scale=1920:1080:flags=lanczos" -q:v 2 plates/S03a/%05d.jpg
```
- For slow-mo (S03a at 40%, S07a at 50%): use `minterpolate=fps=60:mi_mode=mci` first if the source looks choppy, then drop to 30.
- **Speed ramps** (hit-stops): duplicate frames at the dips listed in §1 (hold 3 frames) and **do not** retime the audio.
- Name plate folders by shot ID. The compositor maps `t` → plate frame index = `round((t − shot.start)*30)`; clamp to the last frame.
- **Cut rhythm rules:** accelerating verse = cut every 2 beats then every beat; never two consecutive cuts of equal length for more than 3 cuts in a row; the climax (S13) cuts on **every beat**, while S14/S15 breathe for 8 beats. Hard anchor: title slam at exactly 11.92.
- **Color match:** apply per-act grade (uniform values in `timeline.json`): Act I `uSat .75, uWarm 0, exposure .9`; Act II `uSat 1.05, uWarm .25, exposure 1.15`; Act III `uSat 1.2, uWarm .15, exposure 1.0`; S16 `uWarm .6`. Match skin tone and hair color across clips with a per-shot gain.

---

## 9. PRODUCTION ORDER AND FALLBACK LADDER

**Order:**
1. Setup: node, playwright, esbuild, ffmpeg, python libs; run audio analysis (§7.9) and write `timeline.json` (copy §5 verbatim).
2. Download fonts and logos; test the spark; build the overlay and lyric renderer; render lyric-only test frames.
3. Character sheet → keyframes (all) → look at the grid, regenerate off-model ones.
4. Generate V clips (two takes each) → pick, retime, extract plates.
5. Depth maps + P shots; build the H shots (§7.10) and view them.
6. Assemble full timeline, run partial renders for each act, fix, then the full render and encode.
7. QA (§7.11), then write `out/README.md` listing the shot sources actually used.

**Fallback ladder (use only on tool failure; record each use in README):**
- V clip fails or is off-model after 3 attempts → regenerate keyframe; else convert the keyframe to a **P** shot using the *same camera move* from §5 (never a plain Ken Burns).
- Depth map fails → try another depth model; else use a soft radial pseudo-depth with foreground mask (rembg) and a 2-layer parallax.
- No GPU → SwiftShader (slow but works); lower particle counts by 4× (S15 to 200k), keep 1080p.
- A font fails → substitute another CJK black-weight font; never ship tofu.
- Logos unavailable → procedural spark (§7.6) and serif "ANTHROPIC".
- Generated clip duration too short → ping-pong the loopable portions only for ambient motion (never for the hero action).

## 10. DEFINITION OF DONE
- 1920×1080, 30 fps, 43.70 s, original audio; title slam lands at 11.92; silence at 11.20–11.92 is visibly frozen and quiet.
- Every shot in §5 exists, in the stated order, on the stated source type.
- "Opus 5.5" is unmistakable: halo ring, title slam, version counter, end card; Claude spark and Anthropic marks present; ≥ 6 Mandarin memes visible; all 15 lyric lines are legible and animated individually.
- Camera never static; the three signature moves (monitor match-cut, barrel-roll chase, pupil-dive cosmic zoom) are clearly executed.
- Pace feels uneven on purpose: slow open, accelerating verse, freeze, hero shots, hyper-cuts, breathing climax, calm landing.
- `out/README.md` states what was generated, what fallbacks were used and the seeds/prompts.
