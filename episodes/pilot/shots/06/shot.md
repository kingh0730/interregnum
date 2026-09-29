# Shot 06 — HOLD STILL

**Duration:** 7 s (0:30–0:37; abs 30.0–37.0)  **Tool:** Codex plate p04 (from 04) + JS (the Proof's picture, the lamp
legends, the flaps) + comp. The pen moves on a plate matte (v1) or in a silent Seedance take (v2).
**Camera:** locked, on the framing 04 ended on: an insert at the operator's eye line

**Action:** Back at the glass. Her pen hovers over the ghost ear. The ring button clicks and the overlay circles the
tip; she drags a few millimetres and the ghost slides home. "Hold still." The flag redraws in cold strokes: L EAR ·
LOCKED. Down the column, the red lamps clack over to cold white one by one: MOLE · L CHEEK, BLINK INTERVAL, SKIN TONE,
BREATH CYCLE, VOICE WARMTH. The flaps above them clack toward air each second. She touches his face through glass;
the gesture replaces v1's mouse cursor. It shows her craft and her detachment, and it is a quiet joke about drift (our
own pipeline's problem). "Hold still" is said to a face she is touching.

**Build:**
- **Plate:** p04, the framing 04 ended on. After the wide of 05, we return to the work.
- **Picture:** JS **J03 v3** (below), inserted into the tube quad with the tube artefacts, as in 04.
- **The pen, v1:** a matte of the hand and pen cut from p04 (GrabCut; no Codex cutout), translated −6 px in x over
  1.1–2.2 s (easeInOutCubic) and lifted at 2.2 (2 px up, scale 0.98). Its shadow on the glass is the same matte,
  darkened, blurred 6 px and offset 5 px down and right: the picture sits a centimetre behind the glass, so the tip,
  its shadow and the picture are three layers. The shadow reaches the ghost ear (0.3–1.0 s) before the tip does.
- **The pen, v2:** a 5 s silent Seedance take from p04 with the picture comped in (`work/pilot/v3/p04_picture.png`).
  Track the pen tip in the take and drive the ghost's offset from its measured movement, so hand and picture agree.
  Test both routes; keep the stiller one.
- **Lamps:** each lamp is a flat red ink shape in the plate, which gives a trivial mask. On its switch: a 2-frame dip,
  then cold white `#DDFBFA` with its legend re-lit.
- `letterbox(2.39)`, `grade(HALL)`, grain 2 %.

**Keyframe prompt:** reuses **p04** (full prompt in `shots/04/shot.md`); no new generation.
**Refs:** none (no generation; the plate is `work/pilot/keys_v3/p04_proof.png`).
**Layers:** none.

**JS spec (J03 v3 · the Proof, the column of legend lamps and the flap repeater):**
- **The picture** (picture space 1440×1080, into the tube quad): `f04_frozen.png` at 30 % desaturation, with the J16 v3
  mesh at 35 %, the ghost ear (+6 px, 40 %) and the red drift flag, as they stood at the end of 04.
- **1.0 s:** the ring button clicks, and the overlay draws a small circle around the tip's screen position (Stroke
  Hand, 6 facets, cold, drawn in 3 frames).
- **1.1–2.2 s:** the ghost follows the pen −6 px, then fades 40 % → 0 at 2.2 (over 0.1 s).
- **2.3 s:** the flag redraws in cold strokes (`#5FE1E6`) as L EAR · LOCKED, stroke by stroke over 5 frames.
- **The column:** six rectangular legend lamps. Each legend is engraved into the lens and filled black, so it reads
  dark on the lit colour, and each new legend sits over the ghost of an older, paint-filled one (VOICE WARMTH over
  AUDIO GAIN). Engraved State Capitals, module 3 px, laid onto the lamp masks by homography. OPEN is red; locked is
  cold white.
  1. L EAR · DRIFT → cold at 2.3
  2. MOLE · L CHEEK → cold at 3.0
  3. BLINK INTERVAL → cold at 3.6
  4. SKIN TONE → cold at 4.2
  5. BREATH CYCLE → cold at 4.8
  6. VOICE WARMTH → cold at 5.4
- **The flap repeater:** four split-flap cards in Flap numerals (condensed square numerals with rounded corners, cream
  `#E8DDC4` on black, split by the hinge line) reading TO AIR 08:38 → 08:31, one flip per whole second. In each flip
  the top half falls in 3 frames and the bottom lands with a 1-frame bounce, on the tick.
- **Tube artefacts:** as in 04: scanlines, bloom and halation, misconvergence, dust, the smear at the ear, and the 8 %
  reflection of her head and the Wall.
- **Removed:** v1's top bar, SUBJECT F header, timeline and waveform strip. The voice is heard, not graphed.

**Sound:**
- **IDA (V.O.)** (`Samantha`, 150, VO-MURMUR: close, dry, under her breath): **"Hold still."** at shot +1.0 (abs
  31.0), on the grab.
- Stylus click at +1.05 (grab) and +2.2 (release).
- UI blips (−30 dB) at each flip: 2.3, 3.0, 3.6, 4.2, 4.8, 5.4 (abs 32.3 …).
- Hall clock every second. DRONE continues.

*v3 sound note:* the stylus clicks are the light pen's ring button, and the UI blips become relay clacks, at the same
times.

**Motion prompt (v2, optional, Seedance: start `work/pilot/v3/p04_picture.png`, 5 s, `--no-audio`):** Colour woodcut
print animation; keep the first frame's exact carved shapes, flat inks and designs. A macro insert at an operator's
desk: a hooded monitor shows an old man's still face, and a woman's hand holds a slim pen on a coiled cable a
centimetre from the glass. The face on the monitor does not change, and nothing else in the frame moves. After one
second her hand moves the pen a few millimetres to the left, holds it there, then lifts it slightly away from the
glass. Understated movement: only her hand and the pen move. Locked-off camera. No sound.

**Takes:** —
