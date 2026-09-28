# Shot 24 — "I …"

**Duration:** 8 s (2:05–2:13; abs 125.0–133.0)  **Tool:** JS (world screen)  **Camera:** none (screen insert)

**Action:** The script field for Night 212. The template line is locked: *Good evening, my children.* She types
"I", and the machine completes it in grey: *am well.* PREDICTION 0.99. She doesn't take it. The cursor blinks twice.
She types over it: "died". The suggestion stutters (*am we—*) and dies: NO PREDICTION. She finishes: "I died in the
spring." A red dot appears top right: COMMITTEE — VIEWING. A second later, somewhere in the hall, the red phone
starts to ring. **This is the thesis:** the model can only continue the past; the new has to be typed by hand.

**Build:** JS piece **J10 `script`** (shared with shot 26: one page, two time ranges), 8.0 s. Every keystroke emits
a timestamp to `work/pilot/js/keys_24.json` so the sound lands on the frame. Comp: `letterbox(2.39)`, monitor feel,
`grade(HALL)`.

**Keyframe prompt:** none (JS only).
**Refs:** none.
**Layers:** none.

**JS spec (J10, inside the band, background `#0A0F1C`):**
- **Header** (y 170):
  - Left: `SCRIPT · NIGHT 212 · 21:00`, DIN Alternate 26 px `#5FE1E6` at 70 %.
  - Right: `TO AIR 00:53` in `#E0412F`, counting down per second (00:53 → 00:46).
- **Field** (x 200–1720, y 250–820): Menlo **50 px**, line height 80 px, text `#E9E2D0`. Line 1 is prefilled
  `Good evening, my children.` at 40 %, with a small lock glyph in front. The cursor is a 4×60 px `#E9E2D0` block.
- **Timeline:**
  - 0.0: the cursor at the start of line 2, blinking.
  - 0.6: types `I`.
  - 0.9: ghost text ` am well.` appears after the cursor in `#E9E2D0` at 30 %. Under the field, a tag
    `PREDICTION 0.99` in Menlo 20 px `#5FE1E6`.
  - 0.9–2.8: hold. The cursor blinks twice; the ghost breathes 25–35 %.
  - 2.8: types a space. The ghost re-flows after it.
  - 3.0–3.6: types `d`, `i`, `e`, `d` (0.15 s each). At `d` (3.0) the ghost flickers for 2 frames, shows ` am we—`
    breaking, and vanishes at 3.2. The tag turns `#E0412F` and reads `NO PREDICTION` at 3.2.
  - 3.8–5.6: types ` in the spring.` (15 characters at about 0.12 s each, ±30 % jitter).
  - 5.8: top right, under TO AIR: `● COMMITTEE — VIEWING` in DIN Alternate 22 px `#E0412F` fades in and blinks at 1 Hz.
  - 5.8–8.0: hold, with the cursor blinking at the end of `spring.`

**Sound:**
- **Keystrokes** on the JS timestamps: a noise burst plus a low thock, with jitter.
- The ghost-text "tink" at 0.9 (abs 125.9).
- **SUB HIT** (dull) at 3.0 (abs 128.0), on the "d". The NO PREDICTION blip at +3.8 (abs 128.8).
- **The red phone starts at +6.0 (abs 131.0)**, off-screen: the electromechanical bell through the hall reverb at
  −12 dB, on a 3 s cycle, and it never stops (cues §5).
- PULSE; the hall clock; the DRONE.
- No dialogue.

**Motion prompt:** n/a (JS in v2).
**Takes:** —
