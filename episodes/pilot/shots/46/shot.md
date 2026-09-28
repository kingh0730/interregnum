# Shot 46 — NIGHT 213 (alternate ending, a separate tail; not in the main cut)

**Duration:** 10 s (alt cut 4:02–4:12; abs 242.0–252.0)  **Tool:** JS text + JS ident + Codex keyframe (reuse k01) +
comp (broadcast, full frame)  **Camera:** as shot 02 (locked-off MCU, push 1.00→1.035)

**Action:** The cynical ending, built so King can compare the two tones side by side (questionnaire Q2 and Q17). The
next night: NIGHT 213. The chime plays in the **old** key, whole and warm; the sweet hymn is back. The Father, as if
nothing happened: "Good evening, my children." A beat. "I am well." Black. Someone else is at Desk 4, or no one is and
the machine is running free. The old refuses to die, and the new cannot be born.

**Build:** render as `work/pilot/shots/46.mp4`. **Append it only in the alt reel**
(`renders/pilot/continuity_v1_reel_alt.mp4` = main cut + 46).
- **0.0–1.0 s:** JS card `NIGHT 213` in Menlo 36 px `#5FE1E6`, centered on black, fading in over 0.2 s and holding.
- **1.0–4.0 s:** JS **J01 `ident`**, variant `alt` (the `fast` timings offset by 1.0), full frame, `broadcast()`
  without the bug, `grade(BROADCAST)` at normal warmth (not the cold version).
- **4.0–9.6 s:** reuse **k01**, exactly as shot 02: `push(1.00→1.035)`, `broadcast()` with the J14 bug including
  `LIVE`, `grade(BROADCAST)`. No stutter; the picture is perfect.
- **9.6 s:** hard cut to black and hold to 10.0.
- No letterbox anywhere in this shot.

**Keyframe prompt:** reuses **k01** (full prompt in `shots/02/shot.md`); no new generation.
**Refs:** `assets/pilot/keyframes/k01_father_mcu.png`.
**Layers:** none.
**JS spec:** the `NIGHT 213` card (above), J01 `alt`, and the J14 bug.

**Sound (1M7):**
- **CHIME A4, F♯4, D4 at abs 243.3, 243.8, 244.3**: the original, warm and full.
- HYMN D major 243.8–246.5.
- **FATHER** (`Daniel`, 135, BROADCAST): **"Good evening, my children."** at abs 246.8; **"I am well."** at abs
  249.6.
- 251.6: cut to silence.

**Motion prompt (v2):** Television broadcast, flat 2D cel-painted style. The elderly man sits perfectly composed and
speaks directly into the lens, warm and slow: "Good evening, my children." A pause, then: "I am well." Minimal head
movement, an almost unnaturally smooth stillness. Locked-off camera, very slow push-in. Soft studio room tone, no
music.

**Takes:** —
