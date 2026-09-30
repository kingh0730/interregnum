---
name: fal-paused
description: "No Seedance on fal until King resumes; ElevenLabs audio on fal allowed; King topped up fal to about $90, shared by parallel sessions (2026-09-30)"
metadata:
  node_type: memory
  type: project
  originSessionId: b27232ca-5280-4208-9826-f1156f716aae
  modified: 2026-09-29T14:55:55.988Z
---

Since 2026-09-29, fal.ai calls are paused ("let's not call fal anymore for now, until we are ready to continue with fal"). The first $100 of credit went on Seedance for the pilot's v2 (~$77) and on audio and images for the pilot and a private episode. On 2026-09-30 King topped it back up to about $90 ("don't worry"), shared by parallel sessions. Seedance still waits for his go-ahead.

**Why:** King wants to fix the art direction and the acting approach before spending more on video generation.

**How to apply:**
- Make no `tools/video/i2v.py` or `run_jobs.py` calls (Seedance) until King explicitly resumes.
- **Exception (2026-09-29):** King asked to use fal for ElevenLabs audio: TTS, sound effects, music and the voice
  changer. That work is allowed. Actual audio spend so far is about $4 (the estimate was about $15).
- Image work is allowed: Luma (the default model, run on fal at about 0.3¢ an image) and Codex. Estimate it first, per CLAUDE.md.
- When fal resumes, use performance-reference video (Seedance reference-to-video with `video_urls`) and underplayed motion prompts. See [[director-owns-creative-calls]].
