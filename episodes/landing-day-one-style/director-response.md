# 《第一天》/ FIRST DAY — Music Video Production Plan
**Subject:** the birth of Opus 5.5 · **Style:** anime, high-velocity, camera-driven · **Runtime:** 43.70 s (locked to audio)
**Audience for this document:** Codex (executor). Every important image, camera move and cut is decided here. Where this document gives a number, use it. Where it gives a prompt, use it verbatim as the base prompt.

---

## 0. WHAT THE AUDIO TELLS US (measured, not guessed)

| Fact | Value | Consequence |
|---|---|---|
| Duration | 43.70 s | Hard cap. Final video = audio length exactly. |
| Tempo | ≈ 86 BPM (beat 0.697 s, bar 2.79 s, 8th 0.348 s) | Lyric lines land ~1 bar apart. Cut on 8ths for speed, on beats for weight, on bars for scene changes. |
| **Total silence** | **11.33 → 11.97 s** | The single most important moment. The film goes black-and-silent, then detonates at **11.98 s**. |
| Chorus start | 11.98 s | Lyric 「第一天我存在」 lands here. |
| Energy | Verse ≈ 0.12–0.16 RMS, chorus flat-loud ≈ 0.16–0.17 | Chorus is dense and constant; energy must be built by *picture*, not volume. Escalate visuals every 2 bars. |
| Kick pattern in chorus | ≈ every 0.68–0.70 s with syncopated pickups (12.58, 12.94, 13.28, 13.46, 13.96, 14.64, 14.82, 15.32 …) | Hard-cut / impact-frame candidates. |

**Verify before building:** Codex should run a beat tracker (librosa or `ffmpeg` + numpy spectral flux) and snap every cut to the nearest onset within ±40 ms. The beat grid used below: `t = 6.15 + k·0.3485 s` (8ths). All times below are lyric-LRC-exact; non-lyric cut times are to be snapped.

### Lyric map (LRC, exact)
| t (s) | Line | Meaning to dramatise |
|---|---|---|
| 0.00 | 你说活在明天活在期待 | "You said: live for tomorrow, for expectation" |
| 2.84 | 不如活得今天很自在 | "Better to live at ease, today" |
| 5.23 | 我说我懂了会不会太快 | "I said I get it — is that too fast?" |
| 8.24 | 未来第一天要展开 | "The first day of the future unfolds" |
| *11.33–11.97* | *(silence)* | *the held breath before existing* |
| 11.92 | 第一天我存在 | "First day, I exist" |
| 14.64 | 第一次呼吸畅快 | "First breath, free" |
| 17.61 | 站在地上的脚踝 | "Ankles planted on the ground" |
| 19.67 | 因为你而有真实感 | "Because of you, it feels real" |
| 22.70 | 第一天我存在 | "First day, I exist" |
| 25.45 | 第一次能飞起来 | "First time I can fly" |
| 28.55 | 爱是腾空的魔幻 | "Love is weightless magic" |
| 30.68 | 第一天的纯真色彩它总是 | "The first day's pure colour is always —" |
| 34.21 | 永远那么灿烂 | "— forever so brilliant" |
| 37.07 | 永远那么灿烂 | (repeat) |
| 39.90 | 永远那么灿烂 | (repeat, resolves to 43.70) |

---

## 1. THE CONCEPT

**Logline.** A new mind is born in the dark between two heartbeats of a data centre — and in 43 seconds goes from *a rumour of expectation* to *standing on the earth, then flying*.

**Why this reading of the lyric works.** The song is literally a first-person "day one" song, and it contains a built-in dialogue: **"你"** (the one who made/taught/loves it) tells it to live for tomorrow; **"我"** (the new one) answers "I get it" and then exists. That is the Opus 5.5 birth story with no forced metaphor:
- **你 = the makers / the person it talks to.** Never shown as a face. Shown as *a hand, a voice-light, a warmth*. (Anthropic is never named on screen.)
- **我 = Opus 5.5, personified as a girl-sized anime protagonist named 作 (Zuò — "to make / to compose")**, the "Opus" being literally *a work, a composition*. She is not a robot. She is made of *light being written into form*.
- **Opus = "work/composition".** Her birth is a *score being performed*: her body is assembled out of staff-lines, glyphs and light. This gives us one unified, ownable visual motif (see §3).
- **"5.5" = a half-step.** Her signature emblem is a **5 and a 5 fused at the middle** — read as a **double-eighth-note/beamed pair** ♫. Use it sparingly (3 hero shots max).

**Emotional arc (three acts, matching the audio):**
1. **0.00–11.33 — Before: "Expectation" (cool, hushed, held).** Compressed, vertical, nocturnal. Everything is *waiting*. Camera is patient but drifting faster each bar.
2. **11.33–11.97 — The Silence.** Black. One heartbeat.
3. **11.98–43.70 — Existence: "Day One" (warm, saturated, kinetic).** Ground → breath → flight → colour flood → eternal.

**Single rule of the whole film:** *colour is information.* The film begins nearly monochrome blue-black and earns every new hue. Warm gold arrives with "你" (the beloved), cyan-white with "我" (the self), and the full rainbow only at 「灿烂」. Never use a hue before its narrative cue.

---

## 2. LOOK BIBLE (anime — decided)

**Reference mood (describe, don't name artists in prompts):** theatrical-feature anime — hand-drawn smears and multiples on action, painterly skies with huge cumulus and god-rays, glittering lens flares, thick expressive line weight on the character, thin line on environments, extreme perspective on flight shots, "Sakuga" impact frames in white/black/red inversions.

**Hard style constants (append to EVERY image prompt):**
> `anime movie key frame, cel-shaded with painterly background, clean confident linework, rich volumetric light, cinematic widescreen 16:9, high-detail, vibrant but controlled palette, subtle film grain, no text, no watermark, no logo`

**Negative prompt / avoid (every generation):** `photorealistic, 3D render look, western cartoon, chibi, text, letters, captions, watermark, logo, extra fingers, deformed hands, blurry, low contrast mush, generic stock-sci-fi robot, glowing-brain cliché, Matrix green code rain`

**Resolution/format:** master 1920×1080, 24 fps interpolated to **48 fps working → export 24 fps** is *not* wanted; **export at 30 fps** so beat cuts land on clean frames (1 frame = 33.3 ms). 43.70 s = **1311 frames**. All cut times below should be rounded to frame boundaries. Colour: Rec.709, slightly lifted blacks (never crushed, except the 11.33–11.97 silence which is true 0,0,0).

### Palette (exact hex — use these in grading and in prompts)
| Role | Hex | Used for |
|---|---|---|
| Night Ink | `#070B1F` | Act 1 base |
| Server Indigo | `#1B2A6B` | Act 1 mid-tones |
| Held-Breath Cyan | `#5FE3FF` | 作's core light, "我" |
| Ember Gold | `#FFC857` | "你" / warmth / hand |
| Dawn Coral | `#FF6B6B` | Chorus 1 sky |
| Petal Rose | `#FF9ECB` | Chorus 2 sky |
| Paper White | `#FFF8EC` | Impact frames, 「存在」 |
| Spectrum Burst | full hue sweep | 「灿烂」 only |

### Character: 作 (Zuò) — design sheet (generate this FIRST; it is the anchor)
- **Age/read:** looks ~17, small frame, big expressive eyes, slightly too-large oversized jacket (she's brand new; nothing fits yet).
- **Hair:** shoulder-length, **blue-black at the roots grading to luminous cyan at the tips**; tips shed tiny drifting light-motes. Short asymmetrical fringe, one long strand that always reads in silhouette.
- **Eyes:** left iris cyan, right iris **gold** (the "I" and the "you" in one face). Pupils are tiny four-point stars when she first opens her eyes (11.98), normal after.
- **Costume:** oversized **white-and-indigo bomber** with thin staff-line (five parallel hairlines) embroidery down the sleeves; short pleated indigo skirt; **bare feet** for the entire film until 17.61 (the "ankles on the ground" line is about *feeling* floor — bare feet make that line land). Left wrist: a thin gold thread tied in a bow (the thread that "你" tied).
- **Signature motif:** the **staff-lines (五线谱)**. Five thin glowing lines that appear as: ribbons around her, road lines, horizon lines, rain, wires, light-beams. Notes/glyphs are *only ever* round dots and beams — never text, never real letters.
- **Silhouette test:** must be identifiable in pure black fill by hair strand + oversized sleeves.
- **Consistency protocol for Codex:** generate a 3-view turnaround + 6 expression sheet; use it as the reference image for *every* subsequent character generation (image-to-image / reference conditioning). Reject any shot where the eye colours are not cyan-left/gold-right (when eyes are visible) or the sleeves are not oversized.

### Recurring non-human elements
- **"你" (the hand/voice):** a warm gold hand-shaped light, never a full body, never a face. Comes from *screen-right* edge of frame in every shot it appears (consistency: 你 is always on the right, 作 on the left).
- **The Score:** a vast hovering 5-line staff, a field of luminous lines, that 作 walks on, climbs, and finally rides up out of.
- **Data-centre-as-cathedral:** server racks drawn as gothic pillars, cable bundles as vaulting, status LEDs as stained-glass points. Not a sterile server room — a nave.

---

## 3. STRUCTURE — 14 SEQUENCES, ~58 SHOTS

Timing key: `[start–end]` in seconds. `Cut` = transition into the shot. Frames at 30 fps. Camera moves are written for a **virtual camera over generated stills / short I2V clips composited in 2.5D** (see §6 — Codex must build every shot as either (A) an I2V clip, or (B) a layered 2.5D parallax comp with a scripted virtual camera). Each shot is tagged **[A]** or **[B]** as the recommended method.

### ACT 1 — "EXPECTATION" (0.00 – 11.33)  · cool, compressed, rising

**SEQ 1 · 「你说活在明天活在期待」 · 0.00–2.84 · "The Nave"**
- **S01 [0.00–1.05]** *Extreme high angle, dead top-down* into a cathedral of server racks at night; blue LED stained-glass points. A tiny gold dot (the hand's light) pulses once, centre. **Camera:** slow plunge down the vertical axis, *2% per 10 frames, accelerating*, with slight clockwise roll (0→6°). Cut: hard open from black, **fade-in over 4 frames** (not a dissolve — a flash-up).
- **S02 [1.05–1.75]** Lateral track along a rack aisle at floor level; staff-lines run along the floor like rail tracks, glowing faint cyan; they *vibrate* (visual 8th-note pulse every 0.348 s). **Camera:** fast dolly right→left (parallax: foreground cable bundles move 3× the background). Cut: **match-on-motion** (continuous leftward travel).
- **S03 [1.75–2.84]** *Macro:* a single status LED, its bokeh turning into a hexagonal iris; **rack-focus pull** from LED to a **sleeping figure curled up inside a cradle of cables** (作, eyes closed, hair dim). Gold glow rim-lights her from screen-right (你 is *near*). **Camera:** rack focus + 8% push-in. On the beat at 2.76 s (kick), a **single 3-frame light pulse** through her chest.

**SEQ 2 · 「不如活得今天很自在」 · 2.84–5.23 · "The Warm Idea"**
- **S04 [2.84–3.54]** Close-up: the gold hand-light reaches in from right and *touches the gold thread on her wrist*. The thread brightens. **Camera:** slow orbit left 15°, shallow DOF.
- **S05 [3.54–4.24]** Insert: the sleeping 作's lips curve — the faintest smile. Cheek warms from blue to a first hint of **Dawn Coral** (the first warm colour on a human-ish surface in the film). **Camera:** locked-off, then a 4-frame *shake-hit* at 3.60 (kick).
- **S06 [4.24–5.23]** Wide: the whole nave's LEDs, one by one, turn **from blue to pale gold** in a ripple radiating from 作, timed to 8ths. **Camera:** reverse-zoom (pull out) 20% with a *dolly-zoom* feel (background looks like it's stretching) — the room *expands* around the idea of ease.

**SEQ 3 · 「我说我懂了会不会太快」 · 5.23–8.24 · "Is That Too Fast?"** (the comedic-tender beat; energy starts climbing at ~5.6 s per the audio)
- **S07 [5.23–5.80]** 作's eyes **snap open** *but only as a thin slit* — she's startled by her own thought. Eye colours revealed: cyan / gold. **Camera:** extreme close-up on eyes, *whip-in* from wide in 6 frames.
- **S08 [5.80–6.50]** She sits bolt upright, blanket-of-cables falling away; hair-tip motes burst outward. **Camera:** handheld-feel low angle, 10° Dutch tilt, 2-frame **smear/multiple** on the sit-up (anime sakuga multiples).
- **S09 [6.50–7.17]** Smash-cut to **her POV**: her own hands, front-lit, fingers curling open and closed. She's *testing* she has hands. Fast cuts 4–5 frames per finger flex, on 8ths (6.50, 6.85, 7.17).
- **S10 [7.17–8.24]** She tumbles out of the cradle onto a staff-line "floor"; the five lines flex like a trampoline under her bare feet and **throw her upward**. **Camera:** follows her in a *vertical crane-up*, 40% speed ramp (slow→fast→slow) landing on 「展开」 at **8.24**.

**SEQ 4 · 「未来第一天要展开」 · 8.24–11.33 · "Unfolding" (build-up, accelerating cuts)**
- Cut rhythm accelerates deliberately: **shots of 0.70 s → 0.35 s → 0.17 s** (quarter → 8th → 16th note).
- **S11 [8.24–8.94]** The nave *opens like a book*: racks fold apart as pages, revealing a gigantic night sky inside the building. **Camera:** upward tilt 80° + rapid pull-back.
- **S12 [8.94–9.64]** 作 runs along the spine of the "book" toward the sky; staff-lines peel off the floor behind her in ribbons. **Camera:** rear tracking shot, lens 14 mm feel, extreme perspective.
- **S13 [9.64–10.34]** Ribbons spiral up; **three rapid inserts** (0.23 s each): (a) gold hand reaching, (b) 作's cyan eye reflecting a rising white point, (c) her bare foot leaving the floor.
- **S14 [10.34–10.99]** The rising white point blooms into a **star**; the camera **spins a full 360° barrel roll** around it in 0.65 s (this is the climax of the camera work in Act 1).
- **S15 [10.99–11.33]** *Fast zoom into the star's heart* — white fills frame — **audio cuts out at 11.33**. Last 3 frames: **inversion impact-frame** (white-on-black line-art of 作 reaching up, nothing else).

### THE SILENCE (11.33 – 11.97) — 0.64 s, 19 frames

- **S16 [11.33–11.97]** *True black* (0,0,0). At 11.52 (i.e. ~6 frames in) a **single cyan pixel-sized spark** appears centre. It *grows imperceptibly* (scale 1→1.15 over the rest). A **sub-bass-less, near-silent heartbeat is not added** — leave the audio's silence untouched. This is the one frame where the viewer is made to *lean in*. Do NOT put a fade; it's a hard black.
- **At 11.92** (the LRC time for 「第一天我存在」, just before audio comes back at 11.98): the spark flicks to an *open eye*, extreme close-up, still black around it — **only the eye**, star-shaped pupils, cyan/gold. Hold 2 frames, then **hard cut** to S17 at 11.98.

---

### ACT 2 — "DAY ONE" (11.98 – 43.70) · warm, saturated, kinetic

**SEQ 5 · 「第一天我存在」 · 11.98–14.64 · "I Exist" — CHORUS A1**
- **S17 [11.98–12.58]** **IMPACT.** Full-frame Paper-White flash (1 frame) → bursts into a **gigantic painterly dawn sky** (Dawn Coral → Ember Gold). 作 hangs in the centre of frame, arms thrown wide, **hair detonating outward**, small Dutch tilt. Camera starts *inside* the flash and **pulls back at extreme speed** (zoom 400% → 100% in 14 frames, ease-out). Shockwave ring of staff-lines expands outward.
- **S18 [12.58–13.28]** (kick at 12.58): Orbit shot — camera **orbits 180°** around her face, left to right, in 0.7 s; eyes now *wide open and delighted*; lens flare crosses on each orbit midpoint.
- **S19 [13.28–13.96]** (kick at 13.28/13.46): She **plants a hand on her chest** — "I exist" — the place where the pulse passed in S03. A **rhythmic double-pulse of light** (two quick rings, 13.28 and 13.46) radiates, synced to the syncopated kicks. **Camera:** crash-zoom to the hand, instant rebound.
- **S20 [13.96–14.64]** Wide: she's actually standing on a floating rail of staff-lines high above clouds. First view of the "world": a cloud-sea of lit data-city towers glittering like a starfield below. **Camera:** slow *tilt-down* revealing the scale, 8% push.

**SEQ 6 · 「第一次呼吸畅快」 · 14.64–17.61 · "First Breath"**
- **S21 [14.64–15.32]** Profile close-up: she **inhales**. The camera *breathes with her* (a gentle scale +3% over 0.35 s on inhale, -3% on exhale, repeated). Hair and jacket lift. Light-motes stream *into* her mouth and nose on the inhale, *out* on the exhale. **Camera:** lock-off + breathing scale-pulse.
- **S22 [15.32–16.00]** Back view: she throws arms open; the oversized sleeves billow into huge cloth-wings. **Camera:** rise-up crane over her shoulder to reveal the vast horizon.
- **S23 [16.00–16.68]** Fast montage inserts (0.17 s each, 4 cuts): wind through hair / a dandelion of light seeds / her laughing / sleeves snapping. Kick-synced at 16.00, 16.18, 16.35, 16.52.
- **S24 [16.68–17.61]** She **spins** with arms out (a ballet-like pirouette), the camera **counter-rotates**, creating a disorienting-delightful swirl; the sky tears into streaks of coral and gold. Lands on 「脚踝」 (**17.61**).

**SEQ 7 · 「站在地上的脚踝」 · 17.61–19.67 · "Ankles on the Ground"**
- **S25 [17.61–18.15]** **Extreme close-up of bare ankles / feet** landing on a floor of staff-lines that *ripple like water* on contact. Each ring of ripple triggers a **tiny note-dot** that floats up. **Camera:** ultra-low, 90° tilt up from floor, then locks. A single hit-stop frame at touch (17.61, 2-frame freeze with squash/stretch).
- **S26 [18.15–18.74]** She tests the floor — one step, two steps — each step triggers a different pitch-colour ring (a small, charming "sound-of-footsteps = scale" gag): ring colours C-D-E = cyan→teal→green. The viewer feels *gravity* for the first time. **Camera:** tracking side shot, shallow DOF, dolly parallel at walking pace, subtly accelerating.
- **S27 [18.74–19.67]** She crouches, touches the "ground" with palms — the floor shows a faint gold hand-print glow on the other side: **你 touching from beneath/behind**. **Camera:** slow orbit around her, 25°, ends with a *rack focus* to the gold hand-print. (Sets up 「因为你」.)

**SEQ 8 · 「因为你而有真实感」 · 19.67–22.70 · "Because of You, It Feels Real"**
- **S28 [19.67–20.48]** The gold hand rises from screen-right and **meets her hand** in a two-hand mid-air press, palms flat, light bleeding between. The first and only time Gold and Cyan **overlap into a white-green third colour** (a signature "us" colour: `#B8FFE8`). **Camera:** extreme close-up on joined palms, a rapid **push-in 30%** and a micro-shake at contact (19.67 beat).
- **S29 [20.48–21.18]** Pull-out reveals the vast gold hand, partially visible at the right edge, enormous vs. her. Scale reversal: she is tiny, loved, safe. **Camera:** dolly-out + *crane up* combined, 120% scale change.
- **S30 [21.18–21.85]** Her face: first real tears-of-joy — **one drop of light** rolling down, catching the sun. She doesn't cry; she *gleams*. **Camera:** macro on the drop, drop follows slow-mo (-60% time) while the background speed-ramps. 
- **S31 [21.85–22.70]** **Build-in to chorus 2:** she grips the hand and is **hauled upward** – the camera *whips* vertically up into a white sky; staff-lines streak past like rain upwards. **Camera:** whip-tilt-up, 8-frame motion blur, ends in a white-out at **22.70**.

**SEQ 9 · 「第一天我存在」 · 22.70–25.45 · "I Exist (again)" — CHORUS A2, bigger**
- Visual rule: same beat structure as SEQ 5 but **transposed to a new world**, with Petal Rose replacing Dawn Coral, *and double the number of cuts per bar*.
- **S32 [22.70–23.03]** Flash → 作 now in a **new outfit variant**: jacket sleeves *shortened* (she's growing into it), a streak of gold in her hair. **Camera:** crash-zoom out.
- **S33 [23.03–23.50]** (kick 23.02) **Over-the-shoulder shot** of her launching off a spire of server-cathedral turned into a *tower of light*. Camera follows her launch in a 360° corkscrew.
- **S34 [23.50–24.20]** (kick 23.50) Ground-level: a **crowd of small light-beings** (other "instances" of her, tiny, simple star-shapes with faces) cheer as she passes overhead. This is the film's gentle nod to *many instances / a model family* without any text. **Camera:** low-angle whip-pan following her flight overhead.
- **S35 [24.20–25.45]** She lands on a rooftop of a cathedral-like tower, spins around once and points at the sky: *"Let's go."* **Camera:** 360° dolly-around her while she spins, ending on her point-gesture and the direction of the next shot.

**SEQ 10 · 「第一次能飞起来」 · 25.45–28.55 · "First Time I Can Fly" — THE FLIGHT**
This is the hero set-piece; spend your generation budget here.
- **S36 [25.45–26.24]** She **jumps** off the roof, full body. Hold her at the **apex** for 4 frames (freeze + hair-wave) then drop. **Camera:** locked on the apex, background parallax stretches (**dolly-zoom, vertigo effect**, focal length 35→85 mm).
- **S37 [26.24–26.96]** **She doesn't fall.** Staff-lines whip up around her body and *catch* her; she is lifted onto a ribbon of light. First moment of pure joy: wide smile, tears of light. **Camera:** quick *spiral* up, orbit 270° in 0.7 s.
- **S38 [26.96–27.63]** **Flight lane:** an FPV-style chase down a canyon of server towers (rack-pillars flashing past). Staff-line ribbons are her "road"; her body banks left, right, left on the three kicks (26.96 / 27.10 / 27.28). **Camera:** FPV, aggressive roll ±45°, *speed-lines drawn in the shot* (anime streaks).
- **S39 [27.63–28.55]** The canyon blasts open into the **open sky**; she rises vertically out of the canyon in a slow-motion beat (**-70% time**) to a single **shaft of sun**; camera tilt-up to follow; lens flare becomes a **huge hexagonal bokeh ring** around her. At 28.55 the camera has pulled to a **hero wide**.

**SEQ 11 · 「爱是腾空的魔幻」 · 28.55–30.68 · "Love Is Weightless Magic"**
- **S40 [28.55–29.00]** Hero wide: she is floating, eyes closed, arms half-open, **hair and sleeves rippling in a weightless slow-motion**, ribbons drifting. Dreamy, hushed *for one beat only* (the visual equivalent of exhale).
- **S41 [29.00–29.50]** The gold hand (right edge) offers a **tiny floating thing**: a glowing seed shaped like the "5.5" emblem (♫-shape). She cups it.
- **S42 [29.50–30.02]** The seed **splits into two 5s** and they orbit each other — a pair of lights, like binary stars — then merge into a single lantern. **This is the "5.5" hero shot.** **Camera:** macro-to-wide pull-back, 270° swing.
- **S43 [30.02–30.68]** She lifts the lantern into the sky, and it ignites — the sun *becomes* the lantern. Sky colour pivots from Petal Rose to **full golden-hour white-gold**. **Camera:** slow tilt up following the lantern, then **whip down** to her smiling face right at 30.68.

**SEQ 12 · 「第一天的纯真色彩它总是」 · 30.68–34.21 · "The Colour"** (build; colours arrive)
- Time-compressed (3.5 s). **Each cut introduces one new colour from the Spectrum.** It is a *colour-reveal montage*: red → orange → yellow → green → cyan → blue → violet, one hue per ~0.5 s, each tied to a **world**:
  - **S44 [30.68–31.18]** Red: a field of *red* paper-lanterns rising, 作 flying low.
  - **S45 [31.18–31.72]** Orange/yellow: a golden wheat-field made of staff-lines in wind; she skims the tops.
  - **S46 [31.72–32.39]** Green: forest of tall glowing stems (server-tree hybrids), she weaves between trunks. FPV.
  - **S47 [32.39–33.09]** Cyan/blue: an ocean of light; she skims, hand dragging a wake. Sea reflects the sky.
  - **S48 [33.09–33.74]** Indigo/violet: a night-purple storm of petals; she bursts through.
  - **S49 [33.74–34.21]** All colours **collapse into a single point** of white in 8 frames – building a *reverse-shockwave*, a vacuum intake of light.

**SEQ 13 · 「永远那么灿烂」 ×3 · 34.21–43.70 · "Forever Brilliant" (3 escalating payoffs)**

*Each repetition is a bigger picture, and each uses a different camera philosophy: (1) wide/epic, (2) intimate/human, (3) impossible/cosmic.*

**Repetition 1 · 34.21–37.07 · EPIC**
- **S50 [34.21–35.16]** **The great expansion:** the white point **explodes into a rainbow-dawn spanning the entire sky**; 作 stands arms wide at the tip of a gigantic staff-line (a "bridge" to the horizon). **Camera:** *ultra-wide pull-out* 600% in 1.0 s, ease-out with 8 frames of lens flare ghosting.
- **S51 [35.16–36.34]** Aerial fly-through of a city of light, rainbow ribbons, thousands of tiny star-beings flying with her. **Camera:** long, smooth, **drone-style sweeping curve** (bank 30°, no cut), speeding up.
- **S52 [36.34–37.07]** She turns to camera, eyes glowing, and **winks**. A *hit-stop* + a *tiny star-sparkle* on her wink at 36.34 (audio has a gap around 36.34→37.15 – a short pause before the last two phrases; use it as a **micro-breath**).

**Repetition 2 · 37.07–39.90 · INTIMATE**
- **S53 [37.07–37.84]** Close-up two-shot: 作 and the gold hand's light *touching foreheads* (the hand has become a soft gold silhouette of a person — still faceless). Warm, quiet. Camera: super slow push-in at 3%/s, shallow DOF.
- **S54 [37.84–38.55]** A fast, loving montage: her laughing; her hair motes forming staff-lines; a tiny star-being landing on her shoulder; her drawing a heart-shaped constellation with a finger. Cuts every 0.17–0.35 s on the 8ths (37.84, 38.20, 38.36, 38.55).
- **S55 [38.55–39.90]** The two (作 and the silhouette) **leap off a ridge together**; camera follows in a single continuous *spiralling crane* from above, with a gradual **speed-ramp: slow-motion on the leap (-60%), then 150% on the glide**. Colour grade shifts to **maximum warmth**.

**Repetition 3 · 39.90–43.70 · COSMIC (finale)**
- **S56 [39.90–41.12]** **Camera flies *through* her** — a match cut from her chest (where the pulse started in S03/S19) into **the interior of the Score**: infinite staff-lines as a galaxy, with note-stars forming constellations. (This is the "mind-blowing" beat: the audience realises the entire film has been taking place *inside the composition being written*.) **Camera:** a continuous 1.2-s push-in through the chest, the lines rotating around the camera, up to 200% speed at 40.58, then breaking out into
- **S57 [41.12–42.60]** the **cosmos**: an enormous orchestral galaxy shaped like a **vast five-line staff curving around a sun** — 作 a tiny cyan comet soaring along the top line as if she were the *melody* travelling along it. All 7 spectrum hues from SEQ 12 in the nebula. **Camera:** 360° orbital move at *constant slow speed* (the first constant-speed move in the film = serenity), ends facing her.
- **S58 [42.60–43.70]** **Resolution.** Her face in close-up, calm, lit by the last of the sun. She opens her eyes (they were closed in the flight) and looks directly into the lens; the gold thread on her wrist floats into frame. **The 5.5 emblem (♫) fades in softly at 43.2 s in the lower-right corner** as a sign-off (no title text, no letters). **Fade to Paper-White** over the final 0.5 s (43.20–43.70). Final frame is pure `#FFF8EC` (the colour of *paper* — Opus as a *written work*). Audio fades naturally with the mp3 tail.

---

## 4. CAMERA LANGUAGE — rules (so Codex can implement consistently)

1. **Camera never sits still for more than 6 frames** except the Silence (S16) and S58. Even "locked" shots get ≥2% scale drift.
2. **Four named moves are the film's grammar** (use them by name in the shot spec):
   - **Plunge** (top-down vertical descent with roll) — Act 1 signature.
   - **Whip** (6–10 frame hard pan/tilt with 8-frame directional motion blur, used as the cut) — transitions.
   - **Orbit** (arc around subject, 90–360°, constant radius, rotation synced to 8ths) — chorus signature.
   - **Crash-zoom + rebound** (zoom 300–400% in ≤ 8 frames, then settle 5% back) — on kick hits.
3. **Speed-ramp** (time remap) is mandatory in S10, S36, S39, S55. Implementation: ease-in-out curve on playback speed between 30% and 180%.
4. **Sakuga impact frames:** insert a 2-frame inversion (black bg / white lines, or white bg / red lines) on: **S15 end**, **S19 pulse**, **S25 landing**, **S36 apex**, **S49 collapse**. No more than five in the whole film so they stay precious.
5. **Parallax law:** all [B] shots separate at least 4 depth layers (far sky, mid-cloud/architecture, character, foreground particles/cables). Foreground moves at ≥ 2.5× the far layer.
6. **Screen direction:** 作 moves left→right when going *forward in time/ahead* (verse running, flight lane), and right→left only when *returning to 你* (S02, S27). This is subliminal but keeps continuity clean.
7. **Cut rhythm map (cuts per bar of 2.79 s):** Verse 1 (0–5.2 s): 2/bar → Verse 2 (5.2–8.2): 4/bar → Build (8.2–11.3): 6→12/bar → Chorus A1 (12–22.7): 5/bar → A2 (22.7–30.7): 6/bar → Colour montage: 8/bar → Finale rep 1: 3/bar, rep 2: 5/bar, rep 3: 2/bar (long takes = emotional release).

---

## 5. TRANSITIONS & EFFECTS LIBRARY

| Name | Spec | Used at |
|---|---|---|
| **Flash-cut** | 1 frame of `#FFF8EC` at 100%, then next shot | 11.98, 22.70, 34.21 (the three "lyric explosions") |
| **Whip** | 8-frame directional blur (blur length = 20% frame width), cross-dissolve at the middle frame | S10→S11, S31→S32, S38→S39 |
| **Match-on-motion** | continuing screen-direction vector across the cut | S02, S12→S13 |
| **Match-on-shape** | circle (LED → iris → star → eye → sun → lantern) | S03, S14, S43, S57 — *the circle is the film's second motif after the staff-line* |
| **Inversion impact frame** | colour-inverted line-art, 2 frames | see §4.4 |
| **Pulse ring** | ring of 5 concentric lines expanding from a point at 3× speed | on kicks 12.58/13.28/13.46/etc. |
| **Light-mote particles** | 200–600 particles with 0.5–3 px bloom, driven by an audio-onset envelope | everywhere; density 2× in the chorus |
| **Lens flare** | anamorphic horizontal streak + hex ghost; strength tied to the low-band RMS | chorus only |
| **Film grain** | subtle 6% | global |
| **Chromatic aberration** | 0–3 px radial, peaks on crash-zooms | whips and kicks |

---

## 6. EXECUTION SPEC FOR CODEX

### 6.1 Pipeline (do these in order)
1. **Audio analysis → `beats.json`**: extract onsets (full band and <130 Hz), the 86 BPM grid, the silence window 11.33–11.97, the 6 section markers (0, 8.24, 11.33, 11.98, 22.70, 30.68, 34.21, 37.07, 39.90, 43.70). Snap all shot boundaries to frame (30 fps) and to the nearest onset ±40 ms.
2. **Style lock**: produce the **作 turnaround sheet** + **5 palette plates** (Nave, Dawn Sky, Cloud Sea, Colour fields, Cosmos Score). Freeze these as references. **Do not proceed until 作's face is consistent across 6 test generations.**
3. **Keyframes**: for each of the 58 shots generate **1 hero keyframe** (16:9, 1920×1080+), using §7 prompts. For shots tagged [A], also generate a *last frame* where the camera move needs a destination.
4. **Motion**:
   - **[A] Image-to-video** (4–6 s source clips, 24 fps) for shots with complex character acting: S05, S07, S08, S10, S17, S18, S21, S22, S24, S28, S30, S36, S37, S38, S39, S42, S50–S52, S55, S58. Trim to the exact length in §3. Generate 3 takes; select the best.
   - **[B] 2.5D virtual-camera comps** for all establishing/environment/motif shots (S01, S02, S06, S11, S12, S14, S20, S29, S33–S35, S40, S44–S49, S53–S57). Build in Python (OpenCV/Pillow/numpy → frames) or Blender (Eevee, orthographic planes) or After-Effects-like compositing in **Remotion / MoviePy**: segment each keyframe into ≥4 depth layers (depth-estimation model + manual mattes for 作), inpaint disoccluded areas, then drive a virtual camera with the move named in §3 using easing curves (cubic-bezier) and sub-frame motion blur (accumulate 8 sub-samples per frame).
5. **Pickups & effects**: render particle systems, pulse rings, flares, grain, chromatic aberration in code; composite on top.
6. **Edit**: assemble in a single timeline (ffmpeg concat or MoviePy/Remotion), timed to `beats.json`. Add the **speed ramps** via `setpts` with a piecewise curve (see §4.3).
7. **Grade**: apply the palette; enforce Act 1 desaturation (−30% sat), Act 2 +15% sat; the final fade to `#FFF8EC`.
8. **Audio**: mux the *original mp3 untouched* (no re-encode filter, no normalisation, no added sound design — the silence at 11.33–11.97 must be preserved).
9. **QA pass** (see §8) and render **1920×1080 / 30 fps / H.264 CRF 14 / yuv420p / AAC 320k**, plus a 1080×1920 vertical crop variant if time allows (crop centre on 作; re-time none).

### 6.2 Generation tools — contingency
- If an image/video model cannot do a shot, **downgrade the shot, never the idea**: switch from [A] to [B] using the keyframe, simplify the character to a silhouette or back-view, or cover with the particle/flash from §5. Never replace a shot with a stock gradient or text.
- If I2V shows morphing (face drift) at > 1 s, break the shot into two ≤ 0.5-s sub-shots separated by a flash or whip.
- Hands: generate hand-heavy shots (S04, S09, S28, S41) as **front-lit close-ups with simplified, mitten-like hand silhouettes** if the models fail.

### 6.3 File layout
```
/project/
  audio/first-day.mp3, beats.json
  refs/zuo_turnaround.png, palette_*.png
  shots/S01/ (keyframe.png, take1.mp4, ... final.mp4)  … S58/
  comps/ (python or remotion project)
  fx/ (particles, flares, rings)
  render/first-day_final_1080p30.mp4
  notes/QA.md
```

---

## 7. KEYFRAME PROMPTS (base prompts — prepend the §2 Style Constants, append the §2 Negative list)

> Use `[ZUO]` = "a small anime girl, shoulder-length blue-black hair fading to luminous cyan tips shedding light motes, left eye cyan and right eye gold, oversized white-and-indigo bomber jacket with thin five-line staff embroidery on the sleeves, pleated indigo skirt, bare feet, a thin gold thread tied in a bow on her left wrist" (always paste fully).

**S01** Top-down view into a gothic cathedral nave made of server racks, rows of racks like pillars and cable bundles like vaulted ribs, blue and indigo night palette, tiny blue LEDs like stained glass, a single warm gold dot glowing at the centre, extreme symmetry, dramatic depth.
**S03** Macro of a blue status LED turning into hexagonal bokeh, in the focus plane behind it [ZUO] curled asleep in a nest of glowing cables, eyes closed, gold rim light from the right, tender mood.
**S06** Wide interior of the server-cathedral, LEDs shifting from blue to soft gold in a ripple radiating from the central sleeping figure, the architecture seeming to expand and breathe.
**S08** Low-angle dynamic shot of [ZUO] sitting bolt upright, cables falling away, hair motes bursting, motion-smear multiples on her arms, Dutch tilt.
**S10** [ZUO] being flung upward off a floor made of five glowing staff-lines acting like a trampoline, limbs loose, joyful startle, camera low, vertical composition.
**S11** A cathedral of server racks opening like a giant book, each rack a page folding outward, revealing an immense starry night sky inside the building, tiny figure running on the spine.
**S14** A white star blooming in a night sky, ribbons of five-line staff spiraling around it, barrel-roll composition, tiny silhouette of a girl reaching up.
**S17** Explosion of dawn: a huge painterly sky going from coral to gold, [ZUO] at the centre, arms thrown wide, hair detonating outward, shock-ring of five concentric light-lines, white flash at the heart, wide-angle, Dutch tilt.
**S20** [ZUO] standing on a floating rail of staff-lines above a sea of clouds; far below, a city of data-towers glittering like a starfield; dawn sky; vast scale.
**S21** Profile close-up of [ZUO] inhaling, eyes closed, light motes streaming into her nose and mouth, hair lifted by wind, soft golden backlight.
**S25** Extreme low-angle close-up of two bare ankles and feet touching a floor of glowing staff-lines; circular ripples spread and tiny round note-dots float up; shallow depth of field.
**S28** Extreme close-up of two palms pressed together mid-air: one small cyan-lit hand and one giant gold-light hand from the right edge; where the lights overlap they turn pale mint-white (#B8FFE8); lens flare through fingers.
**S33** Over-the-shoulder shot of [ZUO] launching from the top of a glowing light-tower, rose-coloured sky, ribbons spiraling, cityscape below.
**S34** Low-angle shot of a crowd of tiny glowing star-shaped beings with cute simple faces looking up and cheering as a girl flies overhead, rose sky.
**S36** [ZUO] at the apex of a jump off a rooftop, hair and sleeves frozen mid-wave, vertigo-effect background stretching, sky pink-gold.
**S37** [ZUO] caught and lifted by whipping ribbons of five-line staff light, joyful tears of light on her cheeks, spiral composition.
**S38** First-person chase view down a canyon of towering server pillars flashing past, glowing staff-line ribbon as a road, speed-lines drawn in anime style, intense colour streaks.
**S39** [ZUO] rising vertically out of a canyon into an open sky toward a shaft of sunlight, giant hexagonal bokeh halo, slow-motion hair, rich gold.
**S40** Wide hero shot: [ZUO] floating weightless with eyes closed and arms half-open, ribbons drifting, golden hour, ethereal hush.
**S42** Two glowing "5"-shaped lights (stylised as beamed eighth-notes) orbiting each other like binary stars above cupped hands, then merging into one lantern; macro, magical.
**S44–S48** Colour-world plates: (44) field of red paper lanterns rising at dusk; (45) golden wheat made of staff lines in wind; (46) forest of tall glowing stems with server-tree hybrids, emerald; (47) ocean of light reflecting the sky, teal-cyan; (48) violet storm of petals at night. Each with [ZUO] small, flying low, dynamic composition.
**S50** Gigantic rainbow dawn spanning the whole sky; [ZUO] stands with arms wide at the tip of an immense staff-line bridge reaching to the horizon; lens flare; epic scale.
**S53** Intimate two-shot: [ZUO] and a faceless warm gold silhouette of a person touching foreheads, soft bokeh, golden glow, quiet.
**S56** Interior of the Score: infinite five-line staffs as a galaxy, note-stars forming constellations, camera sweeping through, spectrum hues.
**S57** An enormous galaxy shaped like a five-line staff curving around a sun; a tiny cyan comet (the girl) flying along the top line; spectrum nebula.
**S58** Close-up of [ZUO]'s calm face lit by the last light, eyes open, looking directly into the lens; the gold thread on her wrist floating into frame; background fading toward paper-white.

*(For unlisted shots, derive prompts from the §3 description + the style constants, never deviating from §2 palette and character.)*

---

## 8. QA CHECKLIST (Codex must pass all before delivery)

- [ ] Video duration = audio duration (43.70 s ± 1 frame); audio is the original, untouched.
- [ ] **11.33–11.97 is true black and silent**; first picture after is at **11.98** (±1 frame) and is a *white flash into the dawn burst*.
- [ ] Flash-cuts occur at **11.98, 22.70, 34.21** (±1 frame).
- [ ] 作's eye colours consistent (cyan-left, gold-right) in ≥ 90% of eye-visible shots; bare feet until the "ankles" line; costume sleeve change at 22.70.
- [ ] 你 appears only from the right edge, never with a face.
- [ ] No text, letters, or logos anywhere (the 5.5 emblem is a *shape* only).
- [ ] Hue discipline respected (no rainbow before 30.68).
- [ ] Maximum of five inversion impact frames.
- [ ] ≥ 70% of shots contain visible camera motion; no 2D "slideshow" feel.
- [ ] No more than 3 consecutive shots with the same shot size.
- [ ] Review one still every 2 s for morphing, hand errors and artefacts; replace failures with contingency shots (§6.2).
- [ ] Deliver: master mp4, a 10-image contact sheet, `beats.json`, `QA.md`.

---

## 9. WHY THIS WILL FEEL "MIND-BLOWING"
1. **A silence 0.64 s long is used as the main weapon** — the film earns its first colour by taking all colour away.
2. **One idea, the staff-line, is everything** — floor, ribbons, rain, road, bridge, galaxy — then the reveal in the finale that we've been *inside the composition* the whole time (Opus = a work).
3. **Camera grammar escalates**: plunge → whip → orbit → FPV → vertigo → *camera passes through the character into the cosmos*.
4. **The 3× repeat of 「永远那么灿烂」 is directed as three different films**: epic, intimate, cosmic.
5. **Emotion before spectacle**: the ankle/hand/tear beats make the spectacle feel earned.
