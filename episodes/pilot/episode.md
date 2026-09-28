# EP 1 — CONTINUITY

**Symptom:** *The dead keep talking.* An order that has already ended but cannot stop. Its figurehead is kept alive
by a machine that can only continue the past, because the living can't agree on what comes next and nobody wants
to be the one who says so.
**Logline:** A night-shift technician who has secretly kept a dead leader talking for 212 nights gets a blank
script four minutes before air. She must decide what the dead man says, while her grandmother waits up to watch.
**Runtime:** 4:02 main cut (45 shots). The optional alternate ending adds a 0:10 stinger (shot 46).
**Visual language:** "Nocturne in two lights." A 2D hand-painted cel look: ink line, flat shadow shapes, glow only
at light sources. Cold **broadcast cyan** is the Father's light and amber **lamplight** is Nana's. Red is the
Committee's color, and **dawn rose** appears only in the last shot. Letterboxed 2.39:1 for the world and full-frame
16:9 for the broadcast. Full spec below.
**Tools:** v1 uses 27 Codex keyframes (3 of them edits), 6 transparent cutout layers and 6 lookdev images (39
Codex images in all). It also needs 12 JS pages (J01–J10, J12, J13) rendering the 13 JS-only shots, plus 4 shared JS
overlays, Python comp for every
keyframe shot, macOS `say` scratch voices, and numpy sound and temp score. In v2, Seedance 2.5 animates the 31
keyframe shots listed in the table. The JS and comp effects stay, and Suno replaces 6 cues (`audio/pilot/cues.md`).

Companion files: `script.md` (screenplay with timings), `shots/NN/shot.md` (build specs),
`../../assets/pilot/lookdev.md` (lookdev prompts), `../../audio/pilot/cues.md` (score, SFX, dialogue, Suno).

---

## Why this angle (director's note)

The series takes its name from the gap between the old and the new. The pilot makes that gap literal: a ruler who
has died but cannot be allowed to stop ruling. That one premise brings four of the brief's angles into a single
room. There is **AI** (a model trained on 41 years of speeches that can only predict more of the same), a
**strongman** (the Father), **feeds and propaganda** (one face on every screen at nine o'clock), and **family** (a
grandmother and a granddaughter who can only speak to each other through that face).

**The thesis is one UI gesture, not a speech.** Ida types *"I"*, and the machine offers *"am well."* She types
*"died in the spring."* The model has nothing to predict, because the new is not in its training data. The only new
thing it ever learned is a grandmother's phrase, which it completes in amber when she types *"Eat"*. The old can
only be continued; the new has to be typed by a human hand.

**The form is the content.** v1 cannot animate people, so the pilot is about a man who can't move either: in-world,
the Father's face really is a still image being corrected frame by frame, and his stillness is the horror. The
people in the story are *watchers* who hold still because they are watching. The things that really move are the
things that move in this story: screens, text, clocks, light in windows, rain, steam. Sound carries time: a clock
ticks at 60 BPM, and the temp score is locked to it. Ida's job also mirrors this production: she fights drift ("L EAR
· DRIFT +3.2 PX") in a generated face. An AI-made film about a woman making a man with AI is part of the calling card.

**The heart is Nana.** For 212 nights Ida has slipped her grandmother's sayings into the dead man's sign-off:
*"Close the window. The wind is sly." "Eat something warm before you sleep."* It's a love letter in a dictator's
mouth. The final turn: Nana knew all along. *"Since he started telling me to eat."* She watched every night to hear
her granddaughter. The political thriller ends as a phone call about soup.

**Why it plays like a blockbuster:** it has a ticking clock (a four-minute countdown to air) and cathedral-scale
images (a woman the size of a thumbnail under a 20-metre face). There is a confession broadcast to a whole city,
three reveals that each re-read what came before, and a final image the whole palette has prepared: a city of cold
blue windows turning, one by one, to lamplight.

**Fiction guardrails (public repo):** the nation, the Father, the Committee and the emblem are invented and never
named after, or designed to resemble, any real state or person. The Father is a blend of every "father of the
nation" archetype and belongs to no one. The film targets a *mechanism* (continuing the dead because nobody can
agree on the living) rather than any country, and it treats the believer (Nana) with dignity, not mockery. There are
no slogans; the Father's last public words are about soup.

**Kin, not copies:** *Zima Blue* (LDR) for held graphic frames carried by a voice, and *Blade Runner 2049* for scale
and cyan/amber. *Good Bye, Lenin!* is the inverse: there a son fakes broadcasts to protect a mother, here a
granddaughter fakes them for a nation and the grandmother protects *her*. From *Arrival*, the key to everything is a
phrase. From *Your Name*, two people bridge a distance with written words. From *The Lives of Others*, a
functionary's conscience.

## What King's questionnaire answers could change

| Question | What the pilot assumes now | What would change it |
|---|---|---|
| Q1 whose eyes | A late-20s night worker and her 82-year-old grandmother in an invented, placeless city | For Chinese or diaspora eyes, relocate without changing the structure: Nana becomes Nainai, the soup becomes congee, and *eat something warm* is already a deeply Chinese grandmother line. Names, faces and dialogue language would change; the beats would not. |
| Q2 / Q17 ending tone | Bittersweet-hopeful: the city turns to lamplight, then the epigraph says the new cannot be born | Cynical or devastating: use the **alt ending (shot 46)**, where the next night the Father is back on air saying *"I am well."* Both are built tonight so King can choose. |
| Q4 angle ranking | AI + leaders + family, with family as the heart | If AI ranks first, the autocomplete becomes the climax (let the model *choose* the amber line). If leaders rank first, the Committee gets faces and one scene. If family ranks first, add a dawn scene of Ida and Nana at the table. |
| Q5 what AI is | A **mirror of the past** that can only continue its data, with one grace note of **student** (it learns Nana's line) | If AI is child, successor or lover, the model's amber prediction can grow into its own arc. |
| Q6 China narrative / red lines | Deliberately *not* China: there are no Chinese signifiers | If a red line forbids "a dead leader kept alive", move the premise into a company: a founder whose model keeps giving the keynote for the share price. The shots and structure survive intact. |
| Q7 leaders: satire / myth / tragedy; blended? | A blended mythic figure treated as tragedy (he is kindly; the machinery is the target) | For *House of Cards* bite, add the Committee in the room. For one figure per real person, the pilot is the wrong vehicle. |
| Q9 which love | Grandparent and grandchild bridged by a phrase | Nana can become a mother or father without any other change. |
| Q12 dislikes | One short final address, no speeches | If King dislikes twists, drop shot 46. If he dislikes quotes on screen, cut the epigraph and keep only INTERREGNUM. |
| Q15 language | English, with burned-in subtitles for the review cut | For Mandarin, the scratch voices become Tingting/Meijia/Sinji. Seedance speaks Chinese, and the text screens need a translation pass. |
| Q16 look | Flat 2D cel / graphic painting (it hides Codex drift and makes screens and windows easy to mask) | A photoreal or 3D pilot means more drift risk and a new lookdev pass. |
| Q18 audience / platform | A public YouTube-style release | For **Bilibili**, a dead-leader premise is sensitive however fictional, so use the company variant above. |

## Cast (3 faces, all recurring; every keyframe attaches their sheet)

- **IDA** (27): night continuity operator, Desk 4, Ministry of Continuity. She has a blunt black bob, a charcoal
  turtleneck, and the mustard-amber scarf Nana knitted (the only warm color in the hall). She is precise, exhausted
  and dryly funny, and she speaks less than anyone in the film. Voice: `Samantha`.
- **NANA** (82): Ida's grandmother. Silver bun, round gold glasses, green cardigan. She has watched the Evening
  Address every night for 41 years; for the last two months she has watched it for Ida. Warm, unfoolable. Voice:
  `Moira`.
- **THE FATHER** (~85, dead for 212 days): a kindly patriarch with a white beard and a high-collared charcoal coat. He
  exists only as broadcast frames: 2 keyframes plus 1 edit, reused everywhere, and **every other screen that shows
  him is a comp insert of those same frames**, so his face never drifts. Voice: `Daniel`, pitched down.
- Off-screen: **THE COMMITTEE** (a sealed capsule, a red phone and a red dot, never a face) and **THE PA** (`Karen`).
  Crowds are silhouettes with umbrellas, and no one else is seen.

## Locations (3)

1. **The Hall**, Ministry of Continuity: a concrete cathedral of shrouded desks with a 12×8 monitor wall, a red
   signal lamp, brass pneumatic pipes, and one lit desk.
2. **Nana's room**: a tower-block flat with a boxy TV, an amber lamp, a cream rotary phone, two teacups, a pot on a
   two-ring stove, and rain on the window.
3. **The City**: identical towers across a canal, with every window lit by the same broadcast cyan. There is also a
   tram street with a giant facade screen.

## Story

**Cold open: THE EVENING ADDRESS (0:00–0:22).** The national ident (a lamp emblem and a three-note chime), then
the Father, full-frame and utterly still: *"Good evening, my children. The harvest is in. The sea is calm. I am
well. Eat something warm before you sleep."* The picture freezes, a cyan wireframe snaps onto his face, and a red box
flags his left ear: DRIFT. The letterbox slides in. **Reveal 1:** he is a render, and someone is fixing him.

**1. NIGHT DESK 4 (0:22–0:54).** A vast dark hall: the 20-metre frozen face, and one small woman at one lit desk.
Ida drags the ear back into place (*"Hold still."*) while a checklist of tiny corrections ticks through. The
archive then shows 41 years of addresses racing past as warm thumbnails, stopping at LAST LIVE CAPTURE · 10 MAR. A
flat vitals line reads NO SIGNAL SINCE 11 MAR, and cyan thumbnails count GENERATED 001…212. **Reveal 2:** he died
in the spring and she has made him every night since. Title: **CONTINUITY**.

**2. NO AGREEMENT (0:54–1:17).** A capsule slams into a brass tube: *NO AGREEMENT. NO TEXT TONIGHT. LET HIM SPEAK.
THE OPERATOR ANSWERS FOR CONTENT.* The rulers can't agree on the next lie, so they hand it to the machine and the
blame to her. She lets the model speak on its own, and it can only loop: *I am well. I am well. I am well.* The
screen and the soundtrack fill with it until she stops it. *"No, you're not."* PA: *"Four minutes."*

**3. THE WARM WINDOW (1:17–1:57).** The city in rain, thousands of windows all showing the same blue stand-by
emblem, and one amber window. Inside it, Nana waits in front of the TV with two cups of tea. Ida calls. *"Nana.
Don't wait up tonight." / "I always wait up. He's on soon." / "Why do you still watch him?" / "For the ending."*
Then: *"Eat something warm, love."* **Reveal 3 (for the audience):** Ida opens `signoffs.txt`. Among 212 cyan
"Sleep safely." lines are amber ones, Nana's words, and from Night 150 every night ends *"Eat something warm before
you sleep."* She has been writing to her grandmother through the Father. Night 212 is blank.

**4. NIGHT 212 (1:57–2:32).** *"One minute."* Ida stands under the colossal face. She types *"I"* and the model
offers *"am well."* She types *"died in the spring."* instead, and gets NO PREDICTION. A red dot appears:
COMMITTEE — VIEWING. Off-screen, a red phone starts to ring and never stops. Her wet eyes. More lines are written. She
types *"Eat"*, and for the first time the machine completes something new, in amber: *"something warm before you
sleep."* She adds a stage direction: *[EYES CLOSE]*. *"Ten seconds."* Her finger over the red key. Black. The chime.

**5. THE ADDRESS (2:32–3:08).** In full frame, the Father says *"Good evening, my children."* In a rain-soaked
street a crowd freezes under a giant screen: *"I died in the spring."* The Father, close: *"I'm sorry I stayed so
long."* Ida in the hall hears her words come out of him: *"Tomorrow, you'll have to talk to each other."* Nana with
her tea: *"Eat something warm before you sleep."* The smallest smile. The Father closes his eyes, and dead air
follows. The clock stops, and the red ON AIR lamp clicks off.

**6. COME HOME (3:08–4:02).** The red phone rings; her hand stays still. Her own phone lights up: NANA. *"Nana—" /
"I know, love." / "How long?" / "Since he started telling me to eat."* **Reveal 4:** Nana knew. Ida breaks into a
laugh through tears. *"Come home. The soup's still warm."* The hall wide again: the desk is empty and the red phone
rings for no one. The city at first light: starting from Nana's window, the blue windows turn to amber lamplight one
by one, to the murmur of a city talking to itself. The sky turns a color the film has not used: rose. *The old is
dying and the new cannot be born.* **INTERREGNUM.**

**Alt ending (shot 46, a separate tail):** NIGHT 213. The chime, in the old key. The Father: *"Good evening, my
children. … I am well."* Black.

## Script
See `script.md` (screenplay with timecodes). Dialogue is 21 short lines for 3 speakers (Father 9, Nana 6, Ida 6),
plus the generated loop and 3 PA calls. The full list with timings and voices is in `audio/pilot/cues.md` §6.

## The grammar of stillness (how v1 avoids "PPT")

1. **Stillness is diegetic.** The Father *is* a still image; people are *watching* (a phone call, a TV, a giant
   screen). Nothing in the story asks a body to move.
2. **Only light and text move.** That means typing, scrolling, counters and cursors; TV flicker on faces; windows
   breathing in sync; rain, steam and dust; a lamp clicking off; a handset rattling. All of it is real motion
   from JS or comp.
3. **The frame shape says whose image it is.** Letterboxed 2.39:1 is the world, and full-frame 16:9 with scanlines
   is the broadcast. The bars slide in at the first freeze (shot 04). During the Address the frame keeps changing
   shape between the Father and the watchers. After he dies the film never returns to full frame, except in the alt
   stinger.
4. **Sound carries time.** A clock ticks every second (60 BPM) in the hall, and a wooden one ticks in Nana's room. The
   PA counts down, the red phone rings on a 3-second cycle from 2:11 to 3:43, and the rain never stops until dawn.
   **Every cut lands on a whole second, on the tick.** The hall clock stops when the Father closes his eyes; Nana's
   keeps going.
5. **The cut is the performance.** Each Ida and Nana keyframe is a distinct emotional state (Kuleshov), and
   shot/reverse on every line is the acting.
6. **Camera moves are slow and motivated:** push-ins of 2–10 %, one pull-back per bookend, and **no pans across a
   flat image**. Parallax only where a cutout layer exists, and no push over 4 % on a face.
7. **Hard cuts only.** The two exceptions: the Father's eyes closing (a 1.5 s dissolve, the only one in the film) and
   the end titles.

## Visual language (the look Codex must hold)

- **Medium:** single frames from a premium adult 2D animated film. Clean, confident **dark-navy ink contour lines**;
  **flat color shapes with one hard-edged shadow tone**; soft airbrushed glow only around light sources; subtle paper
  grain. Faces have realistic proportions and simplified planes (no chibi, no oversized eyes). Backgrounds are
  graphic, with bold silhouettes and large dark negative space. Flat shapes also make screens, windows and
  silhouettes easy to mask in comp.
- **Palette** (used as hex in JS and grading, and in words in prompts):

  | Name | Hex | Where |
  |---|---|---|
  | Ink navy | `#0A0F1C` | shadows, UI background |
  | Blue-black | `#121A2E` | night mids |
  | Broadcast cyan | `#5FE1E6` | **only** light from screens: the Father's light |
  | Lamp amber | `#F2A441` | **only** household lamps, Ida's scarf, the thermos, Nana's lines, Ida's phone |
  | Signal red | `#E0412F` | ON AIR, the red phone, the Committee's seal and dot, the commit key |
  | Cream | `#E9E2D0` | paper, UI type |
  | Dawn rose | `#F4C6C0` | **only** shot 44's sky and the rule under the series title |

- **Light:** one hard, motivated source per shot (a screen, a lamp or the wall), with deep shadows, haze in the hall,
  and cyan rim light from screens. Nana's face sits where the two lights meet.
- **Lens language:** the hall is extreme-wide and symmetrical, one-point perspective (power, scale). Ida is tight and
  off-center (isolation), and faces screen-left on the phone. Nana is a warm eye-level medium-close and faces
  screen-right, so the two face each other across the cut. The city is long-lens compression (towers stacked,
  windows as a grid). The Father is dead-center and frontal, eyes on the lens.
- **Frame:** a 1920×1080 master. World shots get a 2.39:1 letterbox (bars 138 px top and bottom), and keyframes keep
  their action inside the central band. Broadcast shots (01, 02, 03, 28, 29, 31, 34, 46) are full frame.
- **Grade presets:** see the comp vocabulary below.
- **Rule for every screen:** Codex never paints screen content. Every monitor, TV, facade screen and the monitor wall
  is prompted as a *blank, evenly glowing panel*, and comp fills it with the canonical frame (k01/k02/k20 or a JS
  render) by homography. This keeps the Father identical everywhere.

## JS design system: "Ministry UI" (shared by all JS pieces)

- **Convention:** `tools/web/README.md` applies: one page per piece exposing `window.renderFrame(t)`, rendered at
  1920×1080 and 24 fps with deterministic time. Suggested source location is `episodes/pilot/js/<piece>.html`
  (code only; renders go to `work/pilot/js/`).
- **Colors:** as in the palette table, plus `PANEL #0D1426` and `LINE #1E2A44`.
- **Fonts (all installed):** `DIN Condensed` Bold (display, clocks, titles); `DIN Alternate` Bold (labels);
  `Menlo` (script, archive, file text); `Courier New` Bold (the Committee's slip); `Baskerville` Italic (epigraph);
  `Futura` Medium (series title); `Avenir Next` (Ida's phone).
- **Safe band:** world screens lay out inside y 138–942 (the letterbox band), while broadcast pieces (ident, bug) use
  the full frame.
- **Motion rules:** clocks and counters change on the film's whole-second tick. The cursor blinks 0.5 s on and 0.5 s
  off. Typing runs at 0.10–0.16 s per character with ±30 % jitter, and every keystroke gets a sound. Moves ease with
  easeInOutCubic. No bouncy UI; the only overshoot is the emblem's flame.
- **The emblem ("the Lamp"):** a circle (r 150, 10 px stroke) around a teardrop flame (70×130) standing on a short
  horizontal base line, all in broadcast cyan with a pale core. It appears on the ident, the broadcast bug, the
  Committee seal (in red) and the stand-by card.
- **Shared overlays** (render once, reuse): **J14 bug**: the emblem at 60 px, top-left at (70, 60), 60 % opacity,
  with "LIVE" in DIN Alternate 26 px cream at the bottom-right (1790, 1010). **J15 stand-by**: a radial gradient
  `#123A5E`→`#07111F` with the emblem centered, breathing ±3 % at 0.25 Hz, and no text. **J16 mesh**: about 120
  landmark points hand-placed once on k02 in `mesh_k02.json`, Delaunay-triangulated, cyan 1.5 px lines at 55 %.
  **J17 captions**: subtitle styles (see Sound).

## Comp vocabulary (implement once in `tools/comp/`; every shot's **Build** uses these names)

- `push(s0→s1, focus=(x,y), ease)`: scale about a focus point in normalized keyframe coordinates. The default ease
  is easeInOutSine over the whole shot.
- `pull(s0→s1, …)`: the same move in reverse. `truck(dx%, dy%)`: a translation as a percentage of frame size.
- `parallax(layer=factor, plate=factor)`: layers from `assets/pilot/layers/`. Align each cutout onto its keyframe
  with SIFT (`tools/comp/legacy/v2_align_layers.py`) and fill the revealed slivers with `cv2.inpaint` (moves are
  small).
- `insert(src, target=auto|corners)`: a homography insert into a blank screen. `auto` finds the largest flat,
  bright-cyan region and fits 4 corners with `approxPolyDP`. For the monitor wall, add `bezels(12×8, 6 px)`,
  per-tile brightness jitter of ±4 % (slow noise), a 15 % haze mix toward `#1A3550`, and bloom.
- `flicker(mask, driver, amount)`: light modulation on the cyan-lit (or amber-lit) pixels of a keyframe. The mask
  comes from the pixels where that channel dominates, blurred at 25 px. The driver is `insert_luma` (the luminance of
  the content on that screen over time), `noise(hz)` or a constant.
- Particles: `rain(layers=2)` (far: fine, dense, 20° slant; near: long, sparse streaks); `drops(window_mask)` (beads
  and runs on glass); `rainshadow` (droplet shadows sliding down a face or wall, luminance only, ≤6 %); `dust(n)`
  (lit only inside the light cone); `steam(origin)`; `puff(origin)`.
- `shake(amp_px, decay_s)`, and `jitter(mask, amp_px, hz, on/off windows)` for a ringing handset.
- `glitch(slices, rgb_px, frames)`, `desat(amount, t)`, `letterbox_in(t0, dur)`.
- `broadcast()`: scanlines (a 1 px dark line every 3 px at 8 %), 1 px chroma offset, small bloom, 15 % vignette, the
  J14 bug and **no letterbox**.
- `grade(preset)` plus `finish()` (bloom, filmic shoulder, vignette and grain, as in `legacy/v2_render.py`):
  - **HALL**: blacks lifted to navy `#0B1020`, cool highlights, cyan bloom, grain 2 %, vignette 25 %.
  - **HOME**: split lighting, with warm bloom on the amber practicals and the TV side cyan. Mids a touch warm, grain 2 %.
  - **CITY**: teal-cyan with rain haze, lifted distance, bloom on windows, grain 2.5 %.
  - **DAWN**: navy shadows, rose-gold mids and highlights, grain 1.5 %. This is the only warm-pink grade.
  - **BROADCAST**: soft and slightly lifted (`#101826`), mild saturation. Always used with `broadcast()`.
- `letterbox(2.39)` on every world shot. Output is 1920×1080, 24 fps.

## Sound language (full plan in `audio/pilot/cues.md`)

- **Tempo 60 BPM = the clock.** Every cut is on a tick. D is home: the state's chime is D major and Nana's theme is D
  minor, and both start on the same note, A. The ending lifts to **E♭** (the "new color" in sound), and the chime's
  final note is withheld.
- **Motifs:** *The Chime* (A–F♯–D, an FM bell). *Nana's theme* (A–F–G–E–F–D, a piano-like pluck) never completes
  until *"Come home."* *The Loop* (a choir of "I am well"). *The Red Phone* rings on a 3-second cycle from 2:11 to
  3:43. *The Walla* at dawn is a city talking to itself.
- **Subtitles:** burned into the review cut. In world shots they sit in the bottom letterbox bar (Avenir Next 30 px,
  cream at 85 %), never over the picture. In broadcast shots they use a closed-caption style (Menlo 30 px, white on an
  80 % black box at y≈950). An `.srt` is exported too.
- **Mix:** −16 LUFS integrated, −1 dBTP. Dialogue sits around −20 LUFS short-term, with music under it at −30 to
  −26. Seedance stems in v2 are generated with **no music**.

## Asset budget

| Kind | Count | Where |
|---|---|---|
| Lookdev (Codex) | 6 | `assets/pilot/lookdev/ld1..ld6` (prompts in `assets/pilot/lookdev.md`) |
| Keyframes (Codex) | 24 new + 3 edits = **27** | `assets/pilot/keyframes/kNN_*.png` |
| Cutout layers (Codex, `ALPHA=1`) | **6** | `assets/pilot/layers/kNN_*.png` (k03, k05, k08, k09, k14, k17) |
| **Codex total** | **39 images** (33 keyframe-side ≤ 40), leaving 7 spare for retakes | about 80 min of Codex time sequentially, ~25 min at 3–4 in parallel |
| JS pieces | 13 shots + 4 overlays | `episodes/pilot/js/` → `work/pilot/js/` |
| Voices | 22 lines + 3 PA + walla | `work/pilot/audio/vo/` |

**Test small first (Codex costs King's quota):** generate `ld1_hall` and `k01_father_mcu` first, check that the
look holds, then batch the rest in dependency order: lookdev → k01 → k02 → k20; k03 → k26 and its layer; k08 →
k27 and its layer; the others in any order.

## Production order for the overnight pass

1. **Lookdev** (6), then **keyframes and layers** (33), following the dependency order in each `shot.md`'s **Refs**.
   Exit code 2 means a safety false positive: reword neutrally and retry. If a take drifts badly, retake once and move
   the reject to `work/pilot/rejects/`.
2. **JS kit and pieces**: pipe frames straight into ffmpeg (no PNG sequences, because disk is at 99 %).
3. **Audio**: `say` lines → processing → SFX and ambience → temp score, per `cues.md`. Render stems, then the mix.
4. **Comp** every keyframe shot, one mp4 per shot in `work/pilot/shots/NN.mp4` (CRF 16, `-tune animation`).
5. **Conform** in shot order, lay in the mix, burn in subtitles, and export
   `renders/pilot/continuity_v1_reel.mp4`, `renders/pilot/continuity_v1_reel_alt.mp4` (with shot 46), the `.srt`, and
   `renders/pilot/contact_sheet.png` (one mid-frame per shot). Delete per-shot intermediates once the reel is
   verified.
6. **QA before handing to King**: the total runtime is 4:02 (4:12 alt). Every cut is on a whole second. No Father
   face differs from k01/k02/k20. No text appears inside a Codex image. The letterbox follows the rule. Loudness is
   on target. Spot-check stills at every reveal (04, 08, 21, 24, 26, 34, 44). **Say plainly in the handoff that
   motion needs King's eyes.**

## Shot list

Timecodes are the main cut. Tool key: **JS** = JS render only; **KF** = Codex keyframe + Python comp; **KF+JS** =
comp with a JS overlay or insert. "v2" = the shot gets a Seedance clip in v2.

| # | In | Shot | Dur | Tool | Camera | Action / acting | Keyframe | Status |
|---|---|---|---|---|---|---|---|---|
| 01 | 0:00 | Ident | 5 | JS (broadcast) | locked | Lamp emblem draws itself; THE EVENING ADDRESS; chime A–F♯–D | — | todo |
| 02 | 0:05 | The Father | 7 | KF (broadcast) · v2 | push 1.00→1.035 on eyes | Still as a portrait: "Good evening, my children. The harvest is in. The sea is calm." | k01 | todo |
| 03 | 0:12 | Eat something warm | 7 | KF (broadcast) · v2 | push 1.00→1.04 | "I am well." … "Eat something warm before you sleep." | k02 | todo |
| 04 | 0:19 | Freeze | 3 | KF+JS | held (push frozen) | Glitch, mesh snaps on, red DRIFT box on the ear, letterbox slides in, tape-stop | k02 + J16 | todo |
| 05 | 0:22 | The Hall | 8 | KF+JS · v2 | push 1.00→1.07 toward the lit desk, parallax | 20 m frozen face on the wall; one tiny woman with an amber scarf | k03 (+layer) | todo |
| 06 | 0:30 | Hold still | 7 | JS | — | Cursor drags the drifting ear home; checklist ticks; VO "Hold still." | — | todo |
| 07 | 0:37 | Ida | 4 | KF · v2 | push 1.00→1.03 | First look at her: stylus poised, tired, unopened amber thermos | k04 | todo |
| 08 | 0:41 | Archive | 9 | JS | — | 41 years race past, stopping at LAST LIVE CAPTURE; flatline; GENERATED 001→212 | — | todo |
| 09 | 0:50 | Title | 4 | JS text | — | CONTINUITY | — | todo |
| 10 | 0:54 | Capsule | 3 | KF · v2 | static, micro push | A black capsule slams into the brass cradle | k05 (+capsule layer) | todo |
| 11 | 0:57 | The order | 6 | KF+JS · v2 | push 1.00→1.05 on the paper | NO AGREEMENT / NO TEXT TONIGHT / LET HIM SPEAK / THE OPERATOR ANSWERS FOR CONTENT | k06 | todo |
| 12 | 1:03 | The loop | 8 | JS | — | The model free-runs: "I am well" floods the screen and the soundtrack; STOP | — | todo |
| 13 | 1:11 | No, you're not | 4 | KF · v2 | push 1.00→1.025 | Ida to the machine: "No, you're not." | k07 | todo |
| 14 | 1:15 | Four minutes | 2 | JS | — | 20:56, TO AIR 04:00; PA "Four minutes." | — | todo |
| 15 | 1:17 | The city | 7 | KF+JS · v2 | truck left 3 % + push 1.00→1.06 onto the amber window | Every window the same blue; rain; one warm window | k08 (+layer) | todo |
| 16 | 1:24 | Nana's room | 6 | KF+JS · v2 | push 1.00→1.04, parallax | Nana before the TV; two teacups; the phone rings | k09 (+layer) | todo |
| 17 | 1:30 | Ida calls | 4 | KF · v2 | push 1.00→1.03 | "Nana. Don't wait up tonight." | k10 | todo |
| 18 | 1:34 | Nana answers | 5 | KF · v2 | push 1.00→1.03 | "I always wait up. He's on soon." | k11 | todo |
| 19 | 1:39 | The question | 4 | KF · v2 | push 1.00→1.03 | "Why do you still watch him?" | k12 | todo |
| 20 | 1:43 | For the ending | 6 | KF · v2 | push 1.00→1.035 | "For the ending." … "Eat something warm, love." | k13 | todo |
| 21 | 1:49 | signoffs.txt | 8 | JS | — | 212 sign-offs scroll: cyan boilerplate, amber Nana-isms, a wall of "Eat something warm…"; Night 212 blank | — | todo |
| 22 | 1:57 | One minute | 2 | JS | — | 20:59, TO AIR 01:00 in red; PA "One minute."; the pulse begins | — | todo |
| 23 | 1:59 | The face | 6 | KF+JS · v2 | push 1.00→1.10 into his eyes (accelerating), parallax | Ida's silhouette under the colossal face; red lamp on standby | k14 (+layer) | todo |
| 24 | 2:05 | "I …" | 8 | JS | — | "I" → ghost "am well." → she types "died in the spring." → NO PREDICTION; COMMITTEE — VIEWING; the red phone starts | — | todo |
| 25 | 2:13 | Her eyes | 3 | KF · v2 | push 1.00→1.02 | Wet eyes reflecting text; she doesn't look away | k15 | todo |
| 26 | 2:16 | "Eat …" | 9 | JS | — | Lines written; "Eat" → **amber** autocomplete; TAB; [EYES CLOSE]; SCRIPT LOCKED | — | todo |
| 27 | 2:25 | The key | 4 | KF · v2 | push 1.00→1.06 (accelerating) | Finger over the red key; PA "Ten seconds."; the riser peaks, then a hard cut | k16 | todo |
| 28 | 2:29 | Ident | 3 | JS (broadcast) | locked | Faster, colder chime | — | todo |
| 29 | 2:32 | The Address | 5 | KF (broadcast) · v2 | as 02 | "Good evening, my children." | k01 | todo |
| 30 | 2:37 | The street | 6 | KF+JS · v2 | push 1.00→1.04 onto the screen, parallax | Crowd frozen under the facade screen: "I died in the spring." The tram hum dies | k17 (+layer) | todo |
| 31 | 2:43 | Sorry | 5 | KF (broadcast) · v2 | as 03 | "I'm sorry I stayed so long." | k02 | todo |
| 32 | 2:48 | Ida looks up | 6 | KF · v2 | **pull** 1.06→1.00 | Her words from his mouth: "Tomorrow, you'll have to talk to each other." | k18 | todo |
| 33 | 2:54 | Nana listens | 6 | KF · v2 | push 1.00→1.04 | "Eat something warm before you sleep." The smallest smile | k19 | todo |
| 34 | 3:00 | Eyes close | 6 | KF (broadcast) · v2 | push 1.04→1.06, then hold | The only dissolve: k02 → k20. Dead air; the hall clock stops | k02 → k20 | todo |
| 35 | 3:06 | ON AIR off | 2 | KF · v2 | static | The red lamp clicks off; the hum winds down | k21 | todo |
| 36 | 3:08 | Red phone | 4 | KF · v2 | push 1.00→1.03 | The Committee's phone rattles; her hand stays still | k22 | todo |
| 37 | 3:12 | NANA calling | 3 | JS | — | Her own phone lights amber: NANA | — | todo |
| 38 | 3:15 | "Nana—" | 3 | KF · v2 | push 1.00→1.02 | She answers the small phone, not the red one | k23 | todo |
| 39 | 3:18 | I know, love | 4 | KF · v2 | push 1.00→1.03 | Lamplight only; TV dark: "I know, love." | k24 | todo |
| 40 | 3:22 | How long? | 3 | KF · v2 | punch-in 1.25→1.28 | "How long?" | k23 | todo |
| 41 | 3:25 | Since he started… | 5 | KF · v2 | punch-in 1.20→1.24 | "Since he started telling me to eat." | k24 | todo |
| 42 | 3:30 | Come home | 7 | KF · v2 | push 1.00→1.04 | A laugh through tears; V.O. "Come home. The soup's still warm." Nana's theme finally resolves | k25 | todo |
| 43 | 3:37 | Empty hall | 6 | KF+JS · v2 | **pull** 1.07→1.00 (mirror of 05) | Chair pushed back; the wall shows only the emblem; the red phone rings for no one | k26 (edit of k03) | todo |
| 44 | 3:43 | The warm windows | 10 | KF + comp · v2 | **pull** 1.06→1.00 from the amber window | Dawn: from Nana's window outward the windows turn cyan → amber; the sky turns rose; walla | k27 (edit of k08) | todo |
| 45 | 3:53 | Epigraph / title | 9 | JS text | — | "The old is dying and the new cannot be born." → INTERREGNUM · EPISODE ONE · CONTINUITY | — | todo |
| 46 | alt | Night 213 (alt tail) | 10 | JS + KF (broadcast) | as 02 | NIGHT 213 → ident (old key) → "Good evening, my children. … I am well." → black | k01 | todo |
