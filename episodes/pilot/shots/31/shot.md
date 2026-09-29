# Shot 31 — "I'M SORRY I STAYED SO LONG."

**Duration:** 5 s (2:43–2:48; abs 163.0–168.0)  **Tool:** a segment of the address take (v2), or comp on k02 (v1)
(broadcast, 4:3)  **Camera:** as 03: the broadcast camera, closer, the take's push continuing

**Action:** The Father, close, apologizes: "I'm sorry I stayed so long." A dead man apologizing for 212 ghost nights
and for 41 years. It is Ida's line in his mouth, and it is the most human thing he has ever said, delivered with the
same frictionless calm as everything else. **Start pose:** as shot 03.

**Build:**
- **v2:** the address take (prompt in `shots/29/shot.md`), the 5 s segment with this line (v2 used 7.0–12.0; re-time to
  the new take's onset).
- **v1 fallback:** k02 with `push(1.00→1.04, focus=(0.50, 0.42), linear)` over 5 s. **Hold the push at its end value**
  so that 34 continues from 1.04.
- Both: the 4:3 crop and pillarbox, `broadcast()` with the J14 bug, closed captions, `grade(BROADCAST)`. No letterbox.

**Keyframe prompt:** v2 uses the address take from **k01** (prompt in `shots/02/shot.md`); v1 reuses **k02** (prompt
in `shots/03/shot.md`). No new generation.
**Refs:** none (no generation).
**Layers:** none.
**JS spec:** the J14 bug and closed captions (shot 02).

**Sound:**
- **FATHER** (`Daniel`, 130, BROADCAST): **"I'm sorry I stayed so long."** at shot +0.8 (abs 163.8).
- Broadcast studio tone. No music.

**Motion prompt (v2):** a segment of the address take; its prompt is in `shots/29/shot.md`. Generate it once.

**Takes:** —
