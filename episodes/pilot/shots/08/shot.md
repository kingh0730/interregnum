# Shot 08 — ARCHIVE

**Duration:** 9 s (0:41–0:50; abs 41.0–50.0)  **Tool:** JS (world screen, letterboxed)  **Camera:** none (screen insert)

**Action:** The archive of the Evening Address. Forty-one years race past as warm thumbnails, a month to a frame,
and brake to a stop at LAST LIVE CAPTURE · 10 MAR. Silence; a vitals panel draws a flat line: NO SIGNAL SINCE 11
MAR · 04:12. Then the strip moves on in cold cyan: GENERATED 001… 212, ending on an empty dashed frame, 212 ·
TONIGHT. **Reveal 2: he died in the spring, and every address since has been made.** The audience should get it
from the colors alone, even without reading every label.

**Build:** JS piece **J04 `archive`**, 9.0 s. Thumbnails are generated procedurally from k01 and k02 (random crops
of 90–100 % scale, ±3 % offset, slight rotation, tint), so no new images are needed. Comp: `letterbox(2.39)`, monitor
feel, `grade(HALL)`.

**Keyframe prompt:** none (JS only).
**Refs:** `assets/pilot/keyframes/k01_father_mcu.png`, `assets/pilot/keyframes/k02_father_cu.png` (thumbnail source).
**Layers:** none.

**JS spec (J04, inside the band, background `#0A0F1C`):**
- **Header** (y 170): left, `ARCHIVE · SUBJECT F · THE EVENING ADDRESS`, DIN Alternate 24 px `#5FE1E6` at 70 %;
  right, the clock `20:51:31` ticking.
- **Strip:** one horizontal row centered at y 540. Thumbnails are 96×54 px with 6 px gaps (102 px pitch) and a 1 px
  `#1E2A44` border.
- **Part A, CAPTURED (0.0–4.6 s):** 492 thumbnails, one per month over 41 years.
  - Tint: multiply by warm sepia `#B89A78`, with brightness varying ±8 %.
  - Year labels `YEAR 1` … `YEAR 41` sit above each 12th thumbnail (DIN Condensed 26 px, `#E9E2D0` at 50 %).
  - Scroll right→left. Velocity eases in over 0–1.0 s to about 18,000 px/s, cruises, then eases out 3.0–4.6 s so
    that thumbnail 492 stops dead center (x 960) at exactly 4.6 s.
  - Counter below the strip (y 660): `CAPTURED` (DIN Alternate 22 px) and a Menlo 40 px number rolling
    `00001` → `14,763`, tied to scroll progress.
- **4.6 s: STOP.**
  - A cyan bracket frames thumbnail 492.
  - Label above it: `LAST LIVE CAPTURE · 10 MAR`, DIN Condensed Bold 34 px `#E9E2D0`, snapping on at 4.6.
- **4.9 s: VITALS panel** (x 1440–1860, y 760–900, `#0D1426` fill, 1 px `#1E2A44` frame):
  - Header: `VITALS · SUBJECT F`, DIN Alternate 20 px.
  - An ECG area 380×60 with a **flat** `#5FE1E6` line scrolling left (±1 px noise).
  - Text: `NO SIGNAL SINCE 11 MAR · 04:12`, Menlo 20 px `#E0412F`.
- **Part B, GENERATED (5.2–8.2 s):** new thumbnails slide in from the right of the last capture.
  - Tint: multiply by cyan `#5FE1E6` at 60 %, each with a 12 px `GEN` tag (Menlo 10 px).
  - One thumbnail per night, **212 in all**. The scroll accelerates from 3/s to about 150/s, so the strip streaks.
  - A second counter, `GENERATED`, Menlo 40 px `#5FE1E6`, counts `001` → `212`, one per thumbnail.
- **8.2 s:** stops on a final **empty dashed-outline** thumbnail (2 px dashes, `#E9E2D0`) labelled `212 · TONIGHT`
  (DIN Condensed Bold 34 px). A cursor block blinks inside it. Hold to 9.0.

**Sound:**
- 0.0–4.4 s: RISER (the whoosh of years).
- **At 4.6 (abs 45.6): SUB HIT, and everything else drops out** (DRONE ducks −15 dB).
- 4.9–8.9 (abs 45.9–49.9): the flatline tone, 1 kHz at −32 dB.
- 5.2–8.2 (abs 46.2–49.2): 212 soft clicks, one per generated thumbnail, accelerating into a buzz.
- 8.5 (abs 49.5): one low PLUCK D2.
- The hall clock continues underneath, quietly (−4 dB).

**Motion prompt:** n/a (JS in v2).
**Takes:** —
