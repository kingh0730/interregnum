# Shot 24 — "I …"

**Duration:** 8 s (2:05–2:13; abs 125.0–133.0)  **Tool:** Codex plate p21 (a 1.25× crop above the keys) + JS (the
terminal, the needle, the lamps, the flaps) + comp (her reflection)
**Camera:** a hardware insert, tight and slightly off-axis (15° from her side, a little above); locked

**Action:** The script for Night 212 on the Script Terminal. Line 1 is the Ministry's template, cold and locked: Good
evening, my children. She types "I", in amber. The machine offers the rest in cold letters at half intensity: am well.
The needle rises to 0.99. She doesn't take it. She types "d": the ghost stutters (am we—) and dies, the needle drops
to its stop pin with a tick, and NO PREDICTION lights red. **A needle falling to zero reads from across a room: the
machine's heart stops at the word "died".** She finishes: I died in the spring. The VIEWING jewel lamp lights red and
blinks, repeating the gallery's pilot lamp: the Committee is watching. A second later, somewhere in the hall, the red
telephone starts to ring. In the dark glass behind the letters lies her own face: the author and her words in one
image. **The thesis:** the model can only continue the past; the new has to be typed by hand.

**Build:**
- Plate **p21** (full prompt in `shots/21/shot.md`), cropped 1.25× above the keys (the tube, the hood's edge at the
  left, the meter and lamps at the right, the repeater on top). No new generation.
- JS **J10 v3** (one page with shot 26, two time ranges). Every keystroke writes a timestamp to
  `work/pilot/js/keys_24.json` so the sound lands on the frame.
- Comp: the terminal into the tube quad with the tube artefacts; the needle redrawn (the plate's needle masked out);
  the lamps on their masks; the flap faces on the repeater's cards; **her reflection** (a mirrored, darkened, blurred
  crop of k07, her face lit from below) in the dark glass behind the letters at 8–10 %.
- `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt:** reuses **p21** (full prompt in `shots/21/shot.md`); no new generation.
**Refs:** none (no generation; the plate is `work/pilot/keys_v3/p21_terminal.png`).
**Layers:** none.

**JS spec (J10 v3 · the Script Terminal, the prediction meter and the legend lamps; range 1):**
- **Tube:** as J09 (shot 21): 48 × 12 Operator Mono, a cold layer and a warm layer, the Operator Rule.
- **Row 1, the template:** Good evening, my children., cold at 60 %, locked: a padlock glyph drawn in Operator Mono's
  7 × 9 matrix before it. Her typing is **warm** (amber, 400 ms persistence); the block cursor is warm and blinks on
  the tick. The Engine's predictions are **cold at half intensity**, in their own layer after the cursor.
- **Timeline:**
  - 0.0: the cursor at the start of row 2, blinking.
  - 0.6: she types I.
  - 0.9: the ghost " am well." appears, cold at half intensity, its intensity breathing 45–55 %. The needle rises to
    0.99 (0.3 s rise, 8 % overshoot, settle).
  - 0.9–2.8: hold. The cursor blinks twice.
  - 2.8: she types a space; the ghost re-flows after it.
  - 3.0–3.6: she types d, i, e, d (0.15 s each). At the d (3.0) the ghost flickers for 2 frames, shows " am we—" breaking,
    and dies at 3.2. **At 3.2 the needle drops to its stop pin in 0.15 s**, and NO PREDICTION (the red lamp under the
    meter) lights.
  - 3.8–5.6: she types " in the spring." (15 characters, about 0.12 s each, ±30 % jitter).
  - 5.8: the **VIEWING** jewel lamp at the housing's top right lights red and blinks at 1 Hz.
  - 5.8–8.0: hold, the cursor blinking after "spring.".
- **The meter:** the scale engraved PREDICTION, 0 to 1.0, in State Capitals on the frosted glass; a black needle with
  moving-coil ballistics (a 0.3 s rise with 8 % overshoot; a drop to the pin in 0.15 s).
- **The lamps** (legends engraved and filled black): NO PREDICTION (red), SCRIPT LOCKED (cold, used in 26), VIEWING (a
  red jewel).
- **The repeater:** TO AIR 00:53 → 00:46, the minutes card on its red 00 since shot 22.
- **Tube artefacts:** scanlines, the persistence of each layer, bloom and halation, barrel curvature, a faint burn-in of
  the template row (3–6 %), and her reflection behind the letters.
- **Removed:** v1's DIN header, red dot label and grey Menlo ghost. The meter and the lamps say it without words.

**Sound:**
- **Keystrokes** on the JS timestamps: a noise burst plus a low thock, with jitter.
- The ghost-text "tink" at 0.9 (abs 125.9).
- **SUB HIT** (dull) at 3.0 (abs 128.0), on the "d". The NO PREDICTION blip at +3.8 (abs 128.8).
- **The red phone starts at +6.0 (abs 131.0)**, off-screen: the electromechanical bell through the hall reverb at
  −12 dB, on a 3 s cycle, and it never stops (cues §5).
- PULSE; the hall clock; the DRONE.
- No dialogue.

*v3 sound note:* the needle's tick against its stop pin lands at 3.2, with the lamp; the NO PREDICTION blip at 3.8
can stay as the lamp's relay clack, or move to 3.2 in the audio pass.

**Motion prompt:** n/a (plate, JS and comp).

**Takes:** —
