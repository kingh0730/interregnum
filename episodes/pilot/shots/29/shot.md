# Shot 29 — THE ADDRESS

**Duration:** 5 s (2:32–2:37; abs 152.0–157.0)  **Tool:** Codex keyframe (reuse k01) + comp (broadcast, full frame)
**Camera:** identical to shot 02: locked-off MCU, push-in 1.00→1.035 on the eyes

**Action:** The Father, exactly as every night: the same frame, the same bug, the same greeting. The audience
expects the lie. One thing is missing: the sweet hymn pad is gone, and the ear should notice its absence. **Start pose
(v2):** as shot 02.

**Build:** no new Codex image. Reuse **k01** with shot 02's comp recipe:
- `push(1.00→1.035, focus=(0.50, 0.40))` over 5 s (the same speed curve, scaled).
- `broadcast()` with the J14 bug, `grade(BROADCAST)`, luma breathing.
- **No stutter** this time: the picture is flawless.
- No letterbox.

**Keyframe prompt:** reuses **k01** (full prompt in `shots/02/shot.md`); no new generation.
**Refs:** `assets/pilot/keyframes/k01_father_mcu.png`.
**Layers:** none.
**JS spec:** the J14 bug; broadcast-style captions.

**Sound:**
- **FATHER** (`Daniel`, 135, BROADCAST): **"Good evening, my children."** at shot +0.8 (abs 152.8).
- Broadcast studio tone only. **No music.**

**Motion prompt (v2):** Television broadcast, flat 2D cel-painted style. The elderly man sits perfectly composed and
speaks directly into the lens, warm and slow: "Good evening, my children." Minimal head movement, an almost
unnaturally smooth stillness. Locked-off camera, very slow push-in. Soft studio room tone, no music.

**Takes:** —
