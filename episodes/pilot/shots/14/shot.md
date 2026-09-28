# Shot 14 — FOUR MINUTES

**Duration:** 2 s (1:15–1:17; abs 75.0–77.0)  **Tool:** JS (world screen)  **Camera:** none

**Action:** The clock slams into frame: 20:56 · TO AIR 04:00. The PA speaks. It is a hard punctuation before we leave
the hall for the city.

**Build:** JS piece **J08 `clock`** (parameterized; also used by shot 22), 2.0 s. Comp: `letterbox(2.39)`,
`grade(HALL)`.

**Keyframe prompt:** none (JS only).
**Refs:** none.
**Layers:** none.

**JS spec (J08, params `time="20:56"`, `toAir=240`, `alarm=false`):**
- Background `#0A0F1C`, with a thin 1 px `#1E2A44` frame inset 40 px inside the band.
- Big numerals `20:56`: DIN Condensed Bold 300 px `#E9E2D0`, centered at y 500. The colon blinks (on 0.5 s, off 0.5 s,
  starting on).
- Below them: `TO AIR 04:00`, DIN Alternate Bold 48 px `#5FE1E6`, y 700. At 1.0 s it rolls to `03:59` with a 3-frame
  vertical roll of the changed digits.
- When `alarm=true` (shot 22), the TO AIR line is `#E0412F`.

**Sound:**
- A heavy clock tick at 0.0 (+4 dB) and at 1.0.
- **PA** (`Karen`, 165, PA chain): **"Four minutes."** at shot +0.3 (abs 75.3).
- The DRONE begins to fade (77.0–78.0).

**Motion prompt:** n/a.
**Takes:** —
