# EP 1 — CONTINUITY

**Symptom:** *The dead keep talking.* An order that has already ended but cannot stop. Its figurehead is kept alive
by a machine that can only continue the past, because the living can't agree on what comes next and nobody wants
to be the one who says so.
**Logline:** A night-shift technician who has secretly kept a dead leader talking for 212 nights gets a blank
script four minutes before air. She must decide what the dead man says, while her grandmother waits up to watch.
**Runtime:** 4:02 main cut (45 shots). The optional alternate ending adds a 0:10 stinger (shot 46).
**Visual language:** RELIEF, a colour woodcut and linocut. Every light is a shape cut out of the dark by a hand, and
the one uncarved image is the Father: the machine's smooth copy of a man (the Copy Rule). Cold phosphor is the
Father's light and amber is the living hand's. Red is the Committee's, and **dawn rose** is printed only at the end.
The world is letterboxed 2.39:1; the broadcast is a 4:3 picture. Full spec below and in `episodes/pilot/bible/`.
**Tools (v3):** 43 Codex images: 6 lookdev, 25 keyframes, 5 keyframe edits and 7 hardware plates, with no cutout
layers (`images_v3.json`). JS renders what every device shows (tubes, flaps, film, meters, paper), Python comp puts it
into the hardware and builds the v1-style fallback of every shot, and the sound design and scratch voices of v1 stay.
In the v2 pass, Seedance 2.5 makes 24 takes (about 153 s, two of them long single takes of the Father), and Suno
replaces 6 cues (`audio/pilot/cues.md`).

Companion files: `script.md` (screenplay with timings), `shots/NN/shot.md` (build specs), `images_v3.json` (every v3
Codex prompt, runnable), `../../assets/pilot/lookdev.md` (the lookdev and the RELIEF block),
`episodes/pilot/bible/` (production design, art direction, cinematography), `../../audio/pilot/cues.md` (score, SFX,
dialogue, Suno). `review.md` opens with the v3 redesign note.

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
| Q12 dislikes | One short final address, no speeches | If King dislikes twists, drop shot 46. If he dislikes quotes on screen, cut the epigraph and keep only AI SI - I. |
| Q15 language | English, with burned-in subtitles for the review cut | For Mandarin, the scratch voices become Tingting/Meijia/Sinji. Seedance speaks Chinese, and the text screens need a translation pass. |
| Q16 look | RELIEF, the colour woodcut (chosen in v3; `episodes/pilot/bible/art_direction.md`): flat inks hide Codex drift, hold in Seedance and make screens, windows and phones trivial to mask | A photoreal or 3D pilot means more drift risk and a new lookdev pass. |
| Q18 audience / platform | A public YouTube-style release | For **Bilibili**, a dead-leader premise is sensitive however fictional, so use the company variant above. |

## Cast (3 faces, all recurring; every keyframe attaches their sheet)

- **IDA** (27): night continuity operator, Desk 4, Ministry of Continuity. She has a blunt black bob, a charcoal
  turtleneck, and the mustard-amber scarf Nana knitted (the only warm color in the hall). She is precise, exhausted
  and dryly funny, and she speaks less than anyone in the film. Voice: `Samantha`.
- **NANA** (82): Ida's grandmother. Silver bun, round gold glasses, green cardigan. She has watched the Evening
  Address every night for 41 years; for the last two months she has watched it for Ida. Warm, unfoolable. Voice:
  `Moira`.
- **THE FATHER** (~85, dead for 212 days): a kindly patriarch with a white beard, large ears and a charcoal coat with a
  soft rolled collar and no insignia. He exists only as broadcast frames: k01, and its edits k02 and k20, which also
  start and end both of his Seedance takes. **Every other screen that shows him is a comp insert of those frames**,
  so his face never drifts. Under the Copy Rule he is the only smooth image in the film. Voice: `Daniel`, pitched
  down.
- Off-screen: **THE COMMITTEE** (a sealed capsule, a red phone, a red lamp in a dark gallery, never a face) and **THE
  PA** (`Karen`). Crowds are silhouettes with umbrellas, and no one else is seen.

## Locations (3)

1. **The Hall**, Ministry of Continuity: a concrete basilica of 400 covered desks, with a columbarium Wall of 96 tubes
   in deep niches, the ON AIR lamp and the Air Clock on its axis, a dark gallery, brass pneumatic tubes, and one lit
   desk (`production_design.md` §3–4).
2. **Nana's flat**: a low one-room flat on the 14th floor, with the State Receiver in its niche, an amber lamp, a cream
   rotary phone, two cups, an amber enamel pot on a two-ring stove, and rain on the outer pane (§6).
3. **The City**: Type-1 towers across a canal, every window lit by the same broadcast cold, antennas turned to the
   Transmitter's red beacon, and a tram street before the Public Receiver (§8).

## Story

**Cold open: THE EVENING ADDRESS (0:00–0:22).** The national ident (a worn film of a lamp being lit, and a three-note
chime), then the Father, 4:3 and utterly still: *"Good evening, my children. The harvest is in. The sea is calm. I am
well. Eat something warm before you sleep."* The picture freezes and we pull back out of it: he is on a monitor at a
desk. A beam draws a mesh over his face, and a red flag marks his left ear: DRIFT. **Reveal 1:** he is a picture on a
tube, and someone is fixing him.

**1. NIGHT DESK 4 (0:22–0:54).** A vast dark hall: the 20-metre frozen face, and one small woman at one lit desk.
Ida touches the glass with a light pen and drags the ear back into place (*"Hold still."*) while a column of lamps
clacks from red to white. The archive then shows 41 years of addresses racing past on warm film, stopping at LAST
LIVE CAPTURE · 10 MAR. A scope's flat trace reads NO SIGNAL beside a doctor's tag, 11 MAR · 04:12, and cold frames
count GENERATED 001…212. **Reveal 2:** he died in the spring and she has made him every night since. Title:
**CONTINUITY**.

**2. NO AGREEMENT (0:54–1:17).** A capsule slams into a brass tube: *NO AGREEMENT. NO TEXT TONIGHT. LET HIM SPEAK.
THE OPERATOR ANSWERS FOR CONTENT.* The rulers can't agree on the next lie, so they hand it to the machine and the
blame to her. She lets the model speak on its own, and it can only loop: *I am well. I am well. I am well.* The
screen and the soundtrack fill with it until she stops it. *"No, you're not."* PA: *"Four minutes."*

**3. THE WARM WINDOW (1:17–1:57).** The city in rain, thousands of windows all showing the same blue stand-by
emblem, and one amber window. Inside it, Nana waits in front of the TV with two cups of tea. Ida calls. *"Nana.
Don't wait up tonight." / "I always wait up. He's on soon." / "Why do you still watch him?" / "For the ending."*
Then: *"Eat something warm, love."* **Reveal 3 (for the audience):** Ida calls up SIGN-OFFS · DESK 4. Among 212 cold
"Sleep safely." lines are amber ones, Nana's words, and from Night 150 every night ends *"Eat something warm before
you sleep."* She has been writing to her grandmother through the Father. Night 212 is blank.

**4. NIGHT 212 (1:57–2:32).** *"One minute."* Ida stands under the colossal face. She types *"I"* and the model
offers *"am well."* She types *"died in the spring."* instead: the needle drops, NO PREDICTION. A red lamp lights:
VIEWING. Off-screen, a red phone starts to ring and never stops. Her eyes stay on the keys. More lines are written.
She types *"Eat"*, and for the first time the machine completes something new, in amber: *"something warm before you
sleep."* She adds a stage direction: *[EYES CLOSE]*. *"Ten seconds."* Her finger over the red key. Black. The chime.

**5. THE ADDRESS (2:32–3:08).** In 4:3, the Father says *"Good evening, my children."* In a rain-soaked street a
crowd freezes under a giant screen: *"I died in the spring."* The Father, close: *"I'm sorry I stayed so long."* Ida
in the hall hears her words come out of him: *"Tomorrow, you'll have to talk to each other."* Nana with her tea:
*"Eat something warm before you sleep."* The smallest smile. The Father closes his eyes, and dead air follows. The
clock stops, and the red ON AIR lamp clicks off.

**6. COME HOME (3:08–4:02).** The red phone rings; her hand stays still. Her own grey desk phone rings too, its amber
lamp flashing beside a card pencilled NANA. *"Nana—" / "I know, love." / "How long?" / "Since he started telling me
to eat."* **Reveal 4:** Nana knew. *"Come home. The soup's still warm."* Ida opens the thermos she hasn't touched all
night; steam rises, and we hear her laugh. The hall wide again: the desk is empty and the red phone rings for no one.
The city at first light: starting from Nana's window, the blue windows turn to amber lamplight one by one, to the
murmur of a city talking to itself. The sky turns a color the film has not used: rose. *The old is dying and the new
cannot be born.* **AI SI - I.**

**Alt ending (shot 46, a separate tail):** NIGHT 213. The chime, in the old key. The Father: *"Good evening, my
children. … I am well."* Black.

## Script
See `script.md` (screenplay with timecodes). Dialogue is 21 short lines for 3 speakers (Father 9, Nana 6, Ida 6),
plus the generated loop and 3 PA calls. The full list with timings and voices is in `audio/pilot/cues.md` §6.

## The grammar of stillness (how the pilot avoids "PPT")

1. **Stillness is diegetic.** The Father *is* a still image; people are *watching* (a phone call, a TV, a giant
   screen). Nothing in the story asks a body to move.
2. **Machines, light and hands move.** A beam writes, flaps fall, a needle drops, a lamp switches, film runs through
   a gate, a pen touches glass, rain and steam rise. All of it is real motion from JS or comp, on real hardware. The
   Seedance takes add breath and one small behaviour a shot, never a performance.
3. **The frame shape says whose image it is.** 2.39:1 is the world; 4:3, pillarboxed, is the broadcast. Shot 04 turns
   the 4:3 picture into a tube in a 2.39 room. During the Address the frame keeps changing shape between the Father
   and the watchers. After he dies the film never returns to 4:3, except in the alt tail.
4. **Sound carries time.** A clock ticks every second (60 BPM) in the hall, and a wooden one ticks in Nana's room. The
   PA counts down, the red phone rings on a 3-second cycle from 2:11 to 3:43, and the rain never stops until dawn.
   **Every cut lands on a whole second, on the tick.** The hall clock stops when the Father closes his eyes; Nana's
   keeps going.
5. **The cut is the performance.** Keyframes are neutral start frames, and the Kuleshov effect does the acting: the
   cut before and after, the sound, the light and the object a character holds. After a line, cut to the thermos, the
   cord, the red phone, the cup (`cinematography.md` §7).
6. **The camera is locked unless the story moves.** Only eight shots move: 04 (out of the picture), 05 and 43 (down
   and back up the nave on rails), 22 (onto the red 00), 23 (past her into his eyes), 27 (onto the fingertip), 32
   (back from Ida) and 44 (the one move that breathes). The Father's takes carry the broadcast camera's own slow push.
   There are no micro-pushes on faces, no pans across a flat image and no zooms.
7. **Hard cuts only.** In v2 the Father closes his eyes inside the take, so the only transition left is the titles'
   fade; the v1 fallback keeps the k02 → k20 dissolve in 34.

## Visual language v3: RELIEF (the look every image must hold)

The specs live in `episodes/pilot/bible/` (this episode's bible, under the series rules in `bible/visual.md`): `art_direction.md` (the medium), `production_design.md` (what things are) and
`cinematography.md` (how they're shot). This is the summary the pilot works from.

- **Medium:** a colour woodcut and linocut, printed by hand. A carved blue-black key block holds the image; light is a
  shape cut out of the black; middle tones are parallel gouge strokes following the form, on architecture and floors
  as on faces; colour is flat spot ink, never blended, with paper grain showing through. Nothing reflects, shines or
  shades smoothly. The block that leads every Codex prompt is in `assets/pilot/lookdev.md`; test frame B2
  (`work/pilot/tests/B2.png`) is the reference, and B1's glossy floor is the failure it fixes.
- **The Copy Rule:** the Father's broadcast picture is the one smooth image in the film: soft even light, perfect
  symmetry, gradients, skin without texture. The model's default polish belongs to the machine's copy alone, and the
  audience should feel the change of material before they understand it.
- **Inks and lights** (hex for comp and JS):

  | Name | Printed ink (plates) | Emitted light (JS devices) | Where |
  |---|---|---|---|
  | Key block | `#11151F` | — | the carved black: at least half of every night frame |
  | Cold | `#8ED8D6`, `#D8F4F1` at sources | phosphor `#5FE1E6` bloom, `#DDFBFA` core | **only** light from tubes and mercury lamps: the Father's light, the copy |
  | Amber | `#E9A23B` | filament `#F2A441` bloom, `#FFD9A0` core | **only** a living hand: lamps, the scarf, the thermos, her typed words, the call lamp, the archive's light table |
  | Red | `#CC3A2B` | `#E0412F` | the Committee: the Red Line, the stamp, VIEWING, NO PREDICTION, ON AIR, the commit key, the red 00, the beacon |
  | Paper | `#E8DDC4` | cream `#E9E2D0` | paper, engraved fill, the brightest cut lights |
  | Nana's green | near-black bottle green | — | her cardigan only |
  | Rose | `#EDB9B0` | `#F4C6C0` | **only** 44's sky and 45's raking light |

  There is no sodium light anywhere, and brass in the Hall is olive-black, never warm.
- **Light:** every lit surface can point to its lamp, tube or window. Light is cut where it lands, with no glow; only
  screen light is soft, and the tubes' bloom is added in comp.
- **Frame:** a 1920×1080 master. World shots are letterboxed 2.39:1 (bars of 138 px), with all action inside the band
  y 138–942. Broadcast shots (01, 02, 03, 28, 29, 31, 34, 46) are a 4:3 picture pillarboxed at 1440×1080, generated at
  16:9 and cropped at the centre.
- **Camera:** `cinematography.md` §1–7. Every setup has an owner: the institution's eye in Hall wides, a colleague's
  at Desk 4, the nation's for the Father (the only face that looks into the lens, and the only one centred), a
  guest's in Nana's flat, a neighbour's across the canal. Ida is short-sided in the Hall until 42, when she gets lead
  room for the first time. Ida and Nana mirror each other across the cut: Ida faces screen-left, Nana screen-right, and
  the phone cord crosses Ida's frame in every call.
- **Acting:** behaviour, not emotion (`cinematography.md` §8). No keyframe shows tears, grins or anguish. Every motion
  prompt names one small action and when it happens, gives dialogue volume and pace only, and names its camera. The
  prompts with a person in them end on the performance line, the Father's keep §8's "almost unnaturally smooth
  stillness", and every speaking take carries the speaker's voice-bible line (`v2_jobs.json`). The laugh in 42 is
  heard, not seen.
- **Rule for every screen:** Codex paints the hardware with a blank, evenly glowing face; JS renders what the device
  shows; comp puts it into the device by homography, with that device's artefacts. The Father's face comes only from
  k01, k02, k20 and his two takes.

## JS: the Apparatus (every screen is a machine)

v1's "Ministry UI" is retired: its DIN, Avenir, Menlo, Futura and Baskerville, its dark cards, rules and panels.
Every screen is now hardware (`production_design.md` §4, §5 and §9), and each shot's **JS spec** names its device.

- **Convention:** `tools/web/README.md` applies: one page per piece exposing `window.renderFrame(t)`, rendered at
  1920×1080 (or in the device's own picture space) at 24 fps with deterministic time. Source goes in
  `episodes/pilot/js/`, renders in `work/pilot/js/`, piped straight to ffmpeg.
- **Devices:** raster colour tubes (the Wall, the Proof, the State Receivers), the two-layer Script Terminal (cold for
  the Engine, warm for the operator: the Operator Rule), the Proof's stroke overlay, the 12 cm vitals scope, split-flap
  boards, drum counters, a moving-coil meter, legend lamps, a teleprinter, 35 mm film on a light table and on the
  telecine, and paper.
- **Letters:** State Capitals (the 4 × 6 module alphabet, in cast, engraved, stencil and phosphor finishes), Operator
  Mono (the terminal's 7 × 9 dot matrix), Stroke Hand (the overlay's faceted capitals), Caption Mosaic (the broadcast
  chain's block letters: the bug, the window burn, closed captions), the Committee Typewriter, Flap numerals, and the
  hands: Ida's pencil, the archivist's grease pencil, the doctor's ink.
- **Artefacts:** scanlines, persistence (cold ~60 ms, warm ~400 ms, scope ~1.5 s), bloom and halation, curvature,
  raster breathing, the hum bar, interlace twitter, misconvergence (colour tubes only), burn-in, glass reflections,
  dust and smears, vector beads, split-flap and drum motion, needle ballistics, legend-lamp switches, the collapse to a
  point (`production_design.md` §4, the artefact table).
- **Motion rules:** counters, flaps and clock hands change on the film's whole-second tick. The cursor blinks 0.5 s on,
  0.5 s off. Typing runs at 0.10–0.16 s a character with ±30 % jitter, and every keystroke gets a sound. Nothing
  bounces except the flaps' 1-frame landing and the needle's overshoot.
- **Pieces:** J01 the Lighting (01, 28, 46), J02 the drift flag's Stroke Hand labels (04, 06), J03 the Proof (06), J04
  the Archive Reader (08), J05 the title beam (09), J06 the Committee's carbon (11), J07 the free-running terminal and
  printer (12), J08 the Air Clock (14, 22), J09 the sign-offs page (21), J10 the script page (24, 26), J12 the House
  Line (37), J13 the letterpress card (45), J14 the bug, J15 the standby card, J16 the stroke-overlay mesh (04), J17
  subtitles and closed captions, J18 the window burn, J19 the drum counter (46), J20 the engraved plates, J21 the ON AIR
  relief (35).

## Comp vocabulary (implement once in `tools/comp/`; every shot's **Build** uses these names)

- `push(s0→s1, focus=(x,y), ease)` and `pull(…)`: scale about a focus point. Moves in the Hall are `linear` (rails);
  only 44 eases. `truck(dx%, dy%)` is kept for completeness; no v3 shot uses it.
- `parallax(layer=factor, plate=factor)`: layers are **mattes cut from the plate itself** (GrabCut plus `cv2.inpaint`),
  never Codex cutouts, which don't register with their keyframe (`docs/history.md`). Only the v1 fallbacks of moving
  shots use them.
- `insert(src, target=auto|corners)`: a homography insert into a blank glowing face. **`tiles(96)`** for the Wall:
  find the 96 glowing quads and give each its own homography and tile, with per-tube curvature, colour ±8 %,
  brightness ±10 %, a dead tube, a hum bar and bloom (`production_design.md` §4). It replaces v1's `bezels(12×8)`.
- `tube(k1, corner, vignette, scanlines, persistence, misconvergence, reflection)`: the device artefacts on any insert.
- `flicker(mask, driver, amount)`: light modulation on cyan-lit or amber-lit pixels (flat inks make the masks trivial).
  Drivers: `insert_luma`, `noise(hz)`, or a constant.
- Particles: `rain(layers=2)` drawn as carved cut lines, visible only where they cross light; `drops(window_mask)` as
  carved beads; `dust(n)` lit only inside the light; `steam(origin)` as pale cut ribbons; `puff(origin)`. v1's
  `rainshadow` is dropped: soft moving shadows fight the print.
- `shake(amp_px, decay_s)`, and `jitter(mask, amp_px, hz, on/off windows)` for a ringing handset.
- `glitch(slices, rgb_px, frames)`, `desat(amount, t)`, `letterbox_in(t0, dur)`.
- `broadcast()`: the 4:3 crop and pillarbox, scanlines (a 1 px dark line every 3 px at 8 %), 1 px chroma offset,
  interlace twitter, small bloom, 15 % vignette, and the J14 bug and closed captions **inside** the picture. No
  letterbox.
- `grade(preset)` plus `finish()` (bloom, filmic shoulder, vignette; paper grain and ink squash as a **static** layer,
  never per-frame painted texture):
  - **HALL**: blacks at the key block, cool highlights, cyan bloom on tubes only, grain 2 %, vignette 25 %.
  - **HOME**: two keys, the amber lamp and the cold set, never mixed; mids a touch warm, grain 2 %.
  - **CITY**: cold with rain haze, lifted distance, bloom on the windows, grain 2.5 %.
  - **DAWN**: the key-block shadows, rose and pale gold in the sky bands, grain 1.5 %. The only rose grade; add none
    on top of a Seedance dawn.
  - **BROADCAST**: soft and slightly lifted (`#101826`), mild saturation, no paper grain (the Copy Rule). Always with
    `broadcast()`.
- `letterbox(2.39)` on every world shot. Output is 1920×1080, 24 fps.

## Sound language (full plan in `audio/pilot/cues.md`)

- **Tempo 60 BPM = the clock.** Every cut is on a tick. D is home: the state's chime is D major and Nana's theme is D
  minor, and both start on the same note, A. The ending lifts to **E♭** (the "new color" in sound), and the chime's
  final note is withheld.
- **Motifs:** *The Chime* (A–F♯–D, an FM bell). *Nana's theme* (A–F–G–E–F–D, a piano-like pluck) never completes
  until *"Come home."* *The Loop* (a choir of "I am well"). *The Red Phone* rings on a 3-second cycle from 2:11 to
  3:43. *The Walla* at dawn is a city talking to itself.
- **Subtitles:** burned into the review cut. In world shots they sit in the bottom letterbox bar (Charter 30 px, cream
  at 85 %), never over the picture. In broadcast shots they are closed captions in Caption Mosaic, white on black
  cells, carried inside the signal and scanlined with it. An `.srt` is exported too.
- **Mix:** −16 LUFS integrated, −1 dBTP. Dialogue sits around −20 LUFS short-term, with music under it at −30 to
  −26. Seedance stems in v2 are generated with **no music**.
- **v3 sound notes:** the Sound of every shot is unchanged. Where a device changed its source (the light pen's click,
  the terminal's scroll relay, the House Line's bell, the thermos cap), the shot file carries a short *v3 sound note*
  for the audio pass.

## Asset budget (v3)

| Kind | Count | Where |
|---|---|---|
| Lookdev (Codex) | 6 | `assets/pilot/lookdev_v3/`: hall, ida, nana, father, flat, city (prompts in `assets/pilot/lookdev.md`) |
| Keyframes, new (Codex) | 25 | `work/pilot/keys_v3/`: k01, k03–k19, k21–k25, k28, k29 |
| Keyframe edits (Codex) | 5 | k02 (of k01), k20 (of k02), k05b (of k05), k26 (of k03), k27 (of k08) |
| Hardware plates (Codex) | 7 | p01 the Lighting, p04 the Proof, p08 the Archive Reader, p12 the terminal and printer, p14 the Air Clock, p21 the terminal and keys, p37 the House Line |
| Cutout layers (Codex) | **0** | v1's six are cut: Seedance makes the moves and brings the capsule, and the v1 fallbacks cut mattes from the plates |
| **Codex total** | **43 images**, 2 under the cap of 45 | about 20 min of Codex time, 5 in parallel |
| JS pieces | 20 (J01–J10, J12–J21) | `episodes/pilot/js/` → `work/pilot/js/` |
| Seedance (v2 pass) | 24 takes, about 153 s; 6 optional takes add about 36 s | two 480p drafts and one 720p final each: about $140, optional takes about $33 more |
| Voices | 22 lines + 3 PA + walla | `work/pilot/audio/vo/`, replaced by the takes' voices in v2 |

Every Codex prompt is in `images_v3.json`, in dependency order (run it without `--prefix-file`). The old
`assets/pilot/lookdev/ld*.png` are retired and attached to nothing.

## Production order (v3)

1. **Lookdev, test first** (`assets/pilot/lookdev.md`): `ld_hall` alone, judged against the checks; then the other
   five; then the keyframe test trio k01, k03 and k11. Codex costs King's quota: stop and fix the prompts if the trio
   misses. Exit code 2 is a safety false positive: reword neutrally and retry.
2. **Keyframes, edits and plates** in manifest order. Retake a drifting image once; move rejects to
   `work/pilot/rejects/`.
3. **JS kit and pieces**, piped straight into ffmpeg (no PNG sequences: the disk is nearly full).
4. **Comp** every shot in its v1 form (plates, inserts, the fallback moves), one mp4 per shot in `work/pilot/shots/`.
5. **Audio:** the v1 mix with the v3 sound notes folded in.
6. **Conform** the v3 story reel (242.0 s, every cut on a whole second), with the alt reel adding 46.
7. **v2 pass, when King resumes Seedance:** estimate first (above), draft at 480p, and replace shots take by take as in
   the v2 conform.
8. **QA before handing to King:** the RELIEF checks on every still (`assets/pilot/lookdev.md`: matte surfaces, gouge
   half-tones, inks, darkness, silhouette, no text, no highlights in eyes); no Father face differs from k01, k02, k20
   or his takes; no motion prompt uses a banned emotion word; loudness on target; stills at every reveal (04, 08, 21,
   24, 26, 34, 44). **Say plainly in the handoff that motion needs King's eyes.**

## Shot list

Timecodes are the main cut. Build key: **KF** = Codex keyframe + comp (v1) or Seedance (v2); **PL** = Codex hardware
plate + JS insert + comp; **JS** = JS only; **BC** = broadcast, 4:3. Images in brackets are reused, not generated.
"v2 take" is the Seedance take the shot uses.

| # | In | Shot | Dur | Build (v3) | Camera | Action / acting | Images | v2 take |
|---|---|---|---|---|---|---|---|---|
| 01 | 0:00 | The Lighting (ident) | 5 | PL + film wear, BC | locked | A Year One film: a spotlight finds the lamp, the wick catches, the flame stands; the caption card; chime A–F♯–D | p01 | 5 s silent (from p01 unlit, ending on p01) |
| 02 | 0:05 | The Father | 7 | KF, BC | the broadcast push | The only smooth image, still as a portrait: "Good evening, my children. The harvest is in. The sea is calm." | k01 | opening take, 15 s (02–03, ending on k02) |
| 03 | 0:12 | Eat something warm | 7 | KF (edit), BC | the push continues | "I am well." … "Eat something warm before you sleep." | k02 | opening take |
| 04 | 0:19 | Freeze | 3 | PL + JS (stroke overlay) | pull-back out of the picture | The tear; the picture becomes a tube at Desk 4; the beam draws the mesh; L EAR · DRIFT; the pen's click | p04 | — |
| 05 | 0:22 | The Hall | 8 | KF + Wall tiles | down the nave on rails | The basilica, the field of covers, the frozen face in 96 tubes, one small woman | k03 | 8 s silent |
| 06 | 0:30 | Hold still | 7 | PL + JS | locked | The pen on glass drags the ear home; "Hold still."; the lamps clack from red to white | (p04) | optional 5 s silent |
| 07 | 0:37 | Ida | 4 | KF | locked | Short-sided at the Proof, the pen raised; the thermos behind her; two touches, one breath | k04 | 4 s silent |
| 08 | 0:41 | Archive | 9 | PL + JS | overhead, locked | A carved living man on warm film to 10 MAR; NO SIGNAL and the doctor's tag; the smooth copy to 212; an empty warm frame | p08 | — |
| 09 | 0:50 | Title | 4 | JS | — | CONTINUITY written by a beam, burning in | — | — |
| 10 | 0:54 | Capsule | 3 | KF + edit | locked macro | The capsule slams into the brass cup | k05, k05b | 4 s silent (ending on k05b) |
| 11 | 0:57 | The order | 6 | KF + JS | overhead, locked | Carbon onionskin, the red-ruled form, the Sealed Lamp stamp | k06 | optional 6 s silent |
| 12 | 1:03 | The loop | 8 | PL + JS | locked, focus pull | FREE: I am well floods the tube; the printer hammers it into the room; HALT, the needle pinned | p12 | — |
| 13 | 1:11 | No, you're not | 4 | KF | locked | "No, you're not." Only her lips move | k07 | 4 s |
| 14 | 1:15 | Four minutes | 2 | PL + JS | long lens, locked | The Air Clock: TO AIR 04:00 → 03:59; PA "Four minutes." | p14 | — |
| 15 | 1:17 | The city | 7 | KF + comp | 300 mm, locked | A wall of blue windows breathing together; one amber window; the beacon | k08 | optional 7 s silent |
| 16 | 1:24 | Nana's room | 6 | KF + TV insert | 32 mm, locked | Nana before the State Receiver; two cups; the phone rings; she turns her head | k09 | 6 s silent |
| 17 | 1:30 | Ida calls | 4 | KF | locked | The House Line's handset: "Nana. Don't wait up tonight." | k10 | 4 s |
| 18 | 1:34 | Nana answers | 5 | KF | locked | Two inks meet on her face: "I always wait up. He's on soon." One nod | k11 | 5 s |
| 19 | 1:39 | The question | 4 | KF | locked | Her eyes lift to the Wall: "Why do you still watch him?" | k12 | 4 s |
| 20 | 1:43 | For the ending | 6 | KF | locked | "For the ending." … "Eat something warm, love." | k13 | 6 s |
| 21 | 1:49 | SIGN-OFFS · DESK 4 | 8 | PL + JS | locked | Her lines in her colour; the amber block warms her fingertips; NIGHT 212 blank | p21 | — |
| 22 | 1:57 | One minute | 2 | PL + JS | push onto the red 00 | 00:59 on a red flap; PA "One minute."; the pulse begins | (p14) | — |
| 23 | 1:59 | The face | 6 | KF + Wall tiles | low; past her into his eyes | Standing off the axis under the clean face | k14 | 6 s silent |
| 24 | 2:05 | "I …" | 8 | PL + JS | locked | I → a cold ghost "am well." → died: the needle drops, NO PREDICTION; VIEWING; the red phone starts | (p21) | — |
| 25 | 2:13 | Her eyes | 3 | KF | locked | Her eyes read along the line, blink once, and don't lift | k15 | 4 s silent |
| 26 | 2:16 | "Eat …" | 9 | PL + JS | locked | The first warm ghost; TAB; [EYES CLOSE]; SCRIPT LOCKED | (p21) | — |
| 27 | 2:25 | The key | 4 | KF | onto the fingertip | The finger over the red key; PA "Ten seconds."; hard cut | k16 | 4 s silent |
| 28 | 2:29 | The Lighting (fast) | 3 | the 01 film, BC | locked | Started late, colder | (p01) | 01's take |
| 29 | 2:32 | The Address | 5 | KF, BC | the broadcast push | "Good evening, my children." No hymn | (k01) | address take, 22 s (29–34) |
| 30 | 2:37 | The street | 6 | KF + projection insert | head height, locked | The crowd before the Public Receiver: "I died in the spring." The tram's hum dies | k17 | 6 s silent |
| 31 | 2:43 | Sorry | 5 | KF, BC | the push continues | "I'm sorry I stayed so long." | (k02) | address take |
| 32 | 2:48 | Ida looks up | 6 | KF | back from the Wall's view, on rails | Her words fill the building; she does not move | k18 | 6 s silent |
| 33 | 2:54 | Nana listens | 6 | KF | locked | The mug under her chin: "Eat something warm before you sleep." The corners of her mouth lift | k19 | 6 s silent |
| 34 | 3:00 | Eyes close | 6 | KF + edit, BC | the push arrives and holds | He closes his eyes; dead air; the hall clock stops | k20 | address take (ending on k20) |
| 35 | 3:06 | ON AIR off | 2 | KF + JS relief | locked | The cast letters go dark; the hum winds down | k21 | optional |
| 36 | 3:08 | Red phone | 4 | KF + comp | locked | The Red Line rattles; her hand stays still | k22 | optional |
| 37 | 3:12 | Nana calling | 3 | PL + JS | locked macro | The House Line's amber lamp beside a pencilled NANA | p37 | — |
| 38 | 3:15 | "Nana—" | 3 | KF | locked | She answers the grey phone, not the red one | k23 | 4 s |
| 39 | 3:18 | I know, love | 4 | KF | locked | Lamplight only, the set dark: "I know, love." | k24 | 4 s |
| 40 | 3:22 | How long? | 3 | KF | locked, tighter | "How long?" Her hand closes on the cord | k28 | 4 s |
| 41 | 3:25 | Since he started… | 5 | KF | locked, tighter | "Since he started telling me to eat." | k29 | 9 s (with 42's line) |
| 42 | 3:30 | Come home | 7 | KF | locked; lead room at last | "Come home. The soup's still warm." She opens the thermos; steam rises; the laugh is heard | k25 | 7 s silent |
| 43 | 3:37 | Empty hall | 6 | KF (edit) + Wall | back up the nave on rails | The empty desk; standby over his burned-in ghost; the red phone rings for no one | k26 | 6 s silent |
| 44 | 3:43 | The warm windows | 10 | KF (edit) + comp wave | a long, breathing pull-back | From Nana's window the city turns to lamplight; the sky prints rose; walla | k27 | optional 10 s silent |
| 45 | 3:53 | Epigraph / title | 9 | JS | — | A letterpress card in raking rose light: the epigraph, AI SI - I | — | — |
| 46 | alt | Night 213 (alt tail) | 10 | PL crop + JS + films, BC | locked | The drum rolls to 213; the Lighting in the old key; "Good evening, my children. … I am well." | (p08, p01, k01) | reuses 01 and the opening take |
