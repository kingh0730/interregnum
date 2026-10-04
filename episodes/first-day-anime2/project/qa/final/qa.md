# Final-media QA evidence

Status: **TECHNICAL-REVIEW**

Input: `/Users/kingh0730/repos/interregnum/episodes/first-day-anime2/project/out/opus55_first_day_1080p30.mp4`
SHA256: `e9edb78e1299b558ed81ea0d58dc627fa39494cba0ab0c23e86c6d932869d191`

## Measured technical checks

| Check | Result |
|---|---|
| resolution | PASS |
| fps | PASS |
| frames | PASS |
| duration | PASS |
| codec | PASS |
| pixelFormat | PASS |
| videoBitrate | PASS |
| shotManifest | PASS |
| fullDecode | PASS |
| decodedPreviewFrames | PASS |
| rendererSourceHashBinding | PASS |
| hold_S10 | PASS |
| hold_final12 | PASS |
| sceneDetectionCoverage | EVIDENCE-REVIEW |
| originalMP3PacketPayloads | PASS |
| decodedAudioAlignment | PASS |
| audioVisualWindowMedian | PASS-measured-median-only |

Full measurements, raw scores, per-window lags, source packet hashes, file paths and evidenceSHA256 values are in [qa.json](qa.json).

## Evidence for inspection

- Four-frame-per-shot contact sheets: [sheet1](contact_sheet_01.jpg), [sheet2](contact_sheet_02.jpg), [sheet3](contact_sheet_03.jpg), [sheet4](contact_sheet_04.jpg)
- Three-frame camera strips:52 actual-video images in `camera/`.
- Six full-input-resolution cues in `hard_cues/`; resolution is reported and cannot exceed the input.
- [Typography candidate frames](typography_peak_candidates.jpg):75% into each LRC interval; these are reproducible candidates, not a claim of true text peak.
- [Audio/visual cross-correlation](av_correlation.png) and [raw values](av_correlation.json).
- [Scene detection scores](scene_changes.json), fixed thresholds0.03/0.10/0.30; S37→S38 continuous transition explicitly exempt.
- [Duration histogram](duration_histogram.png) and [scopes](scopes.png).
- [Hold differences](hold_metrics.json): strict decoded holds distinguished from loss-compatible low variation; uncertain holds are not silently passed.

## Manual approval remains pending

- [ ] Character on-model in every appearance: coral inner hair, spark pupils, tie, costume and silhouettes.
- [ ] All generated text/logos absent; all required OPUS5.5/Anthropic identity moments legible.
- [ ] All six memes present and approved; no generated pseudo-Hanzi visible.
- [ ] Lyrics use correct glyphs, avoid eyes, and stay in the required safe area.
- [ ] Every named camera direction is visible; reduced camera angles and retained fractions reviewed.
- [ ] Every shot/action/pose is present; rendered contact and choreography satisfy the brief.
- [ ] Depth/layer borders and disocclusions inspected at100% final resolution.
- [ ] Contact sheets, type peaks, six hard cues, scopes and camera strips visually reviewed.
- [ ] Normal-speed final playback in VLC and a browser: motion, dropped frames and perceptual audio reviewed.
