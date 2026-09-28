# Shot 40 — "HOW LONG?"

**Duration:** 3 s (3:22–3:25; abs 202.0–205.0)  **Tool:** Codex keyframe (reuse k23, punch-in) + comp  **Camera:** a
punch-in on k23, 1.25→1.28 about her eyes

**Action:** Barely able to speak: "How long?" Tighter than shot 38; the world has narrowed to this call. **Start
pose (v2):** the k23 crop, with trembling lips.

**Build:** no new Codex image. Reuse **k23**:
- Crop and scale 1.25× about her eyes (upscale with Lanczos, plus 0.3 px sharpening, then grain to hide the
  softness). Then `push(1.25→1.28)`.
- The red phone's corner is now out of frame, but its sound remains.
- `flicker(mask=amber_lit, driver=noise(0.3 Hz), 2 %)`, `letterbox(2.39)`, `grade(HALL)` with the amber preserved.
- **v2 start frame:** export this crop at 1920×1080 as `assets/pilot/keyframes/k23b_ida_answers_tight.png` (a derived
  crop, not a new Codex image).

**Keyframe prompt:** reuses **k23** (full prompt in `shots/38/shot.md`); no new generation.
**Refs:** `assets/pilot/keyframes/k23_ida_answers.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **IDA** (`Samantha`, 150, IDA hall chain): **"How long?"** at shot +0.8 (abs 202.8). Quiet, the voice almost
  breaking.
- The red phone at abs 203.0 (hall reverb, −12 dB: she has turned away from it); phone-line hiss; warm PAD.

**Motion prompt (v2):** Flat 2D cel-painted style. Close-up: Ida, phone at her ear, barely able to speak, asks:
"How long?" Her lips tremble; her eyes fill. Static camera. The silence of a vast hall, a distant telephone. No music.

**Takes:** —
