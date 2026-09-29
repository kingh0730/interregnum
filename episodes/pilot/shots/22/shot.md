# Shot 22 — ONE MINUTE

**Duration:** 2 s (1:57–1:59; abs 117.0–119.0)  **Tool:** Codex plate p14 (from 14) + JS J08 (alarm) + comp
**Camera:** the same long-lens framing as 14, then a short push onto the red 00, accelerating

**Action:** The Air Clock again, the same framing: 20:59, TO AIR 01:00. On the tick the minutes card falls to its
red-printed 00, and the last minute arrives in the Committee's colour. "One minute." A pulse starts under everything,
one beat a second, and it won't stop until the cut to black at 2:29. Repetition is the ritual; the change is the
story.

**Build:**
- Plate **p14** (full prompt in `shots/14/shot.md`); no new generation.
- JS **J08 v3** with `time="20:59"`, `toAir=60`, `alarm=true`.
- `push(1.00→1.06, focus=the minutes card, easeInQuad)`: the pulse begins. A comp push on a far object through haze
  (with a 200 mm lens there is no parallax to fake).
- `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt:** reuses **p14** (full prompt in `shots/14/shot.md`); no new generation.
**Refs:** none (no generation; the plate is `work/pilot/keys_v3/p14_air_clock.png`).
**Layers:** none.

**JS spec (J08 v3, as shot 14, except):**
- **Hands** at 20:59; the second hand steps at 0.0 and 1.0.
- **Flaps:** TO AIR 01:00 at 0.0. At 1.0 the minutes card flips to its **red-printed 00** (the face printed `#CC3A2B`
  on black; the only red flap) and the seconds pair to 59: TO AIR 00:59. The red 00 stays up for the rest of the film
  (shots 24 and 26 repeat it on the desk).
- Removed: v1's red TO AIR text and pulsing frame line. The alarm is a printed flap, not a colour change.

**Sound:**
- **PA** (`Karen`, 165, PA chain): **"One minute."** at shot +0.3 (abs 117.3).
- Heavy clock ticks at 0.0 and 1.0.
- **PULSE starts at 0.0 (abs 117.0)**: a 50 Hz thump on every tick, ramping to 149.0 (1M4).

*v3 sound note:* add the flaps' clack under the tick at 1.0, as in 14.

**Motion prompt:** n/a (plate, JS and comp).

**Takes:** —
