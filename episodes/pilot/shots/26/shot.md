# Shot 26 — "EAT …"

**Duration:** 9 s (2:16–2:25; abs 136.0–145.0)  **Tool:** JS (world screen)  **Camera:** none (screen insert)

**Action:** Two more lines are on the page now: *I'm sorry I stayed so long. / Tomorrow, you'll have to talk to each
other.* She types "Eat", and for the first time the machine completes something new, **in amber**: *something warm
before you sleep.* PREDICTION 0.97. After 62 nights of her typing it, it has learned the one new thing she ever taught
it: a grandmother's phrase. She looks at it, then presses TAB and it is committed. One more line, a stage direction:
*[EYES CLOSE]*. SCRIPT LOCKED · 6 LINES. The phone keeps ringing. **This is the grace note of the AI theme:** the
only future the machine learned came from love.

**Build:** JS **J10 `script`** (the same page as shot 24), range 2, 9.0 s. Keystroke timestamps go to
`work/pilot/js/keys_26.json`. Comp: `letterbox(2.39)`, monitor feel, `grade(HALL)`.

**Keyframe prompt:** none (JS only).
**Refs:** none.
**Layers:** none.

**JS spec (J10, range 2; same layout, fonts and colors as shot 24):**
- **0.0: the state.**
  - Line 1 (template, 40 %): `Good evening, my children.`
  - Line 2: `I died in the spring.`
  - Line 3: `I'm sorry I stayed so long.`
  - Line 4: `Tomorrow, you'll have to talk to each other.`
  - The cursor is at the start of line 5.
  - `TO AIR 00:32` (red) counts down to `00:23`, and `● COMMITTEE — VIEWING` keeps blinking.
- **Timeline:**
  - 1.00–1.45: types `E`, `a`, `t`.
  - **1.7: amber ghost text** ` something warm before you sleep.` in **`#F2A441` at 55 %** with a soft 8 px amber
    glow. It breathes 45–65 % at 0.5 Hz. The tag below reads `PREDICTION 0.97`, also in amber.
  - 1.7–4.0: hold (reading time; the most important 2.3 seconds on this screen).
  - **4.0: TAB.** The ghost commits and becomes solid `#E9E2D0`. A 0.3 s amber flash sweeps left to right along the line.
  - 4.8–6.2: new line 6: types `[EYES CLOSE]` (0.11 s per character). The brackets and text are `#5FE1E6` (the
    stage-direction style).
  - 6.6: a status line at the bottom of the field: `SCRIPT LOCKED · 6 LINES` in DIN Alternate 24 px `#5FE1E6`. The
    cursor disappears, and the field border goes from `#1E2A44` to `#5FE1E6` at 60 %.
  - 6.6–9.0: hold.

**Sound:**
- Keystrokes on the timestamps.
- **THE AMBER NOTE:** PLUCK A4, dry and close, at +1.7 (abs 137.7). It is the only warm note in the countdown.
- **TAB thock** at +4.0 (abs 140.0). The SCRIPT LOCKED confirm (D5–A5 blips) at +6.6 (abs 142.6).
- The red phone rings at abs 137, 140 and 143 (hall reverb, −12 dB).
- PULSE and RISER rising; the hall clock.
- No dialogue.

**Motion prompt:** n/a (JS in v2).
**Takes:** —
