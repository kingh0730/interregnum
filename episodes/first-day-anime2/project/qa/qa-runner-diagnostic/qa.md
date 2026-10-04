# Final-media QA evidence

Status: **DIAGNOSTIC-NOT-DELIVERY**

Input: `/Users/kingh0730/repos/interregnum/episodes/first-day-anime2/project/qa/timing_cards.mp4`
SHA256: `4498d957ba20dec82678f038a1d5719d45ea530c916fcbad65c0994837dd83d2`

## Measured technical checks

| Check | Result |
|---|---|
| resolution | FAIL |
| fps | PASS |
| frames | PASS |
| duration | PASS |
| codec | PASS |
| pixelFormat | PASS |
| videoBitrate | FAIL |
| shotManifest | PASS |
| fullDecode | PASS |
| decodedPreviewFrames | PASS |
| hold_S10 | REVIEW |
| hold_final12 | REVIEW |
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

This is a diagnostic timing-card input. Expected format/content failures are preserved; this report does not approve a final film.

Correction: decoded hold variation alone does not establish animated content. S10 strip inspection shows the same Frame0339 counter and progress line. Sparse codec outliers remain reported; source-frame hash proof is pending.
