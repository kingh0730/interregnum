# Shot 29 — THE ADDRESS

**Duration:** 5 s (2:32–2:37; abs 152.0–157.0)  **Tool:** the address take (one 22 s Seedance take from k01, cut across
29–34) in v2, or comp on k01 in v1 (broadcast, 4:3)
**Camera:** as 02: the broadcast camera, a centred medium close-up, with the take's slow push

**Action:** The Father, exactly as every night: the same frame, the same bug, the same greeting. The audience expects
the lie. One thing is missing: the sweet hymn pad is gone, and the ear should notice its absence. **Start pose:** as
shot 02.

**Build:**
- **v2:** the **address take**: one continuous take from k01 with all five of his lines and the closing of his eyes
  (prompt below). It is cut across the Address: 29, 31 and 34 are segments of its picture, and the lines heard in 30,
  32 and 33 come from its audio (the v2 lesson: off-screen lines from the same take hold the voice by construction). In
  the v2 conform, 29 used take 0.1–5.1, 31 used 7.0–12.0, and 34 used 18.0 to the end, holding the last frame. Re-time
  these to the new take's voiced onsets.
- An optional `--end work/pilot/keys_v3/k20_father_eyes_closed.png` lands the close exactly on k20. If it makes the
  push morph, drop it and let the take close his eyes on its own, as v2 did.
- **v1 fallback:** k01 with shot 02's recipe: `push(1.00→1.035, focus=(0.50, 0.40), linear)` over 5 s, luma breathing.
- Both: the 4:3 crop and pillarbox, `broadcast()` with the J14 bug, closed captions, `grade(BROADCAST)`. **No stutter**
  this time: the picture is flawless. No letterbox.

**Keyframe prompt:** reuses **k01** (full prompt in `shots/02/shot.md`); no new generation.
**Refs:** none (no generation; the start frame is `work/pilot/keys_v3/k01_father_mcu.png`).
**Layers:** none.
**JS spec:** the J14 bug and closed captions (shot 02).

**Sound:**
- **FATHER** (`Daniel`, 135, BROADCAST): **"Good evening, my children."** at shot +0.8 (abs 152.8).
- Broadcast studio tone only. **No music.**

**Motion prompt (v2, Seedance: the address take for 29–34; start `work/pilot/keys_v3/k01_father_mcu.png`, optional
`--end work/pilot/keys_v3/k20_father_eyes_closed.png`, 22 s, audio on):** A smooth, polished television broadcast
picture; keep the first frame's exact face, soft even light and colours. A medium close-up of an elderly man, perfectly
centred, looking straight into the lens against a deep blue backdrop with a round pale lamp behind his head. One
continuous take. He speaks directly into the lens, slowly, with long pauses between lines: "Good evening, my
children." (pause) "I died in the spring." (pause) "I'm sorry I stayed so long." (pause) "Tomorrow, you'll have to talk
to each other." (pause) "Eat something warm before you sleep." Between lines his face does not move: minimal head
movement, one slow blink, an almost unnaturally smooth stillness. After the last line he keeps looking into the lens
for two seconds, then slowly closes his eyes and keeps them closed, completely still. The camera pushes in very slowly
at a constant speed, from medium close-up to close-up, and stays centred on his eyes. He speaks in a deep, slow,
resonant old man's voice with a neutral General American accent, warm and grandfatherly, with measured broadcast
pacing. Soft studio room tone. No music.

**Takes:** —
