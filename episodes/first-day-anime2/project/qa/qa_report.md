# OPUS 5.5 · 第一天 — delivery QA

**Rendered film delivered. All measured media checks pass.** Full camera/choreography fidelity and native/perceptual playback are qualified below; this is not an assertion that every original-plan checkbox passed.

[Movie](../out/opus55_first_day_1080p30.mp4) · [Local review player](review.html) · [Project/rebuild instructions](../README.md) · [Machine report](final/qa.json)

Final SHA256: `e9edb78e1299b558ed81ea0d58dc627fa39494cba0ab0c23e86c6d932869d191`. Size: 151,683,461 bytes.

## Measured results

| Check | Result and evidence |
|---|---|
| Audio/grid preflight | PASS; offset error 0 seconds, 52 contiguous shot intervals; every cut within one frame of supplied grid. [Preflight](preflight.json), [waveform](waveform_grid.png). |
| Delivery format | PASS; 1920×1080, 30 fps, 1,311 frames, 43.700 seconds; H.264, yuv420p, CRF 14; video bitrate 27.44 Mbps. [FFprobe](final/ffprobe.json). |
| Complete decode | PASS with FFmpeg error checking. |
| Original audio | PASS; all 1,673 MP3 packet payload hashes match the input exactly. No audio re-edit or re-encode. Decoded alignment lag 0 samples; waveform similarity essentially 1. [Audio alignment](final/decoded_audio_alignment.json). |
| Audio/visual diagnostic | PASS; median four-second-window lag 0 frames. This statistical result does not establish perceptual musical quality. [Plot](final/av_correlation.png), [raw values](final/av_correlation.json). |
| Frozen picture | PASS; S10 frames 339–358 and final frames 1299–1310 each have identical source PNG hashes, bound to this movie. Tiny decoded H.264 variation is separately recorded. [Hold evidence](final/hold_metrics.json). |
| Shot presence | All 52 shot intervals rendered with no missing assets; all four final contact sheets reviewed, four samples per shot. [Visual review](final/visual_contact_review.json), [camera diagnostics](final_camera_diagnostics.json). |
| Browser playback | PASS; Chromium played to 43.7 seconds: 1,311 frames, zero dropped/corrupted frames, no errors or stalls. [Browser report](final/browser_playback.json). |
| Mosaic provenance | 600 placed tiles, 164 unique actual-film samples through frame 1217. Frame 1217 and frame 1218 have identical source PNG hashes. [Atlas provenance](../assets/mosaic/atlas.json), [seam check](mosaic_seam.json). |
| Pacing | Supplied 52-shot duration pattern preserved; dance shots are 10/11 frames. [Histogram](final/duration_histogram.png). |

Scene detection was measured at three thresholds fixed before final rendering. At 0.03, every non-exempt planned boundary has a detection within one frame; motion/flashes also create extra detections. S37→S38 is intentionally continuous and is exempt from a forced visible cut. This remains an evidence-review flag in the machine report, not a measured delivery failure.

| Fixed threshold | Missed non-exempt boundaries | Extra detections |
|---|---:|---:|
| 0.03 | 0 | 124 |
| 0.10 | 1 | 20 |
| 0.30 | 12 | 6 |

## Visual evidence and corrections

Final contact sheets: [1](final/contact_sheet_01.jpg), [2](final/contact_sheet_02.jpg), [3](final/contact_sheet_03.jpg), [4](final/contact_sheet_04.jpg). The `final/camera/` directory contains all 52 three-frame camera strips. [Scopes](final/scopes.png), [typography candidates](final/typography_peak_candidates.jpg), and six native-resolution cues in `final/hard_cues/` are saved.

Source-registered exact sparks, title extrusion, local-font Hanzi architecture, billboard copy, screen UI, stamps, and quota/cloud gags are composed in code. Sampled final review found no new material anatomy, identity, clipping, or compositing defect. Corrections included projective depth geometry, clean eye-to-wide compositing, fingertip contact, readable chat reply, server lights, safe stamp framing, and the final pointing pose. S37's label now has an ivory backing over dark hair. S35 retains the original artwork's tight crown crop.

Large poster lyrics stay behind the subject. A smaller foreground reading line preserves supplied character timing and phrase continuity across S11–S36h. S37's final phrase begins at frame 1197; its letter cadence is compressed so the complete phrase appears before S38. The final lockup has complete title, wordmark, and tagline before the frozen last 12 frames.

[Identity and cue samples](final/identity_cues.jpg) document these timing resolutions: the bubble spring begins at 157 with zero size and becomes visible at 158 (within one frame); full-white impacts at 359 and 686 precede readable titles at 362 and 689; the dolly endpoint is 1013, immediately before the next-shot white impact at 1014. These conflicts are explicitly recorded in [execution decisions](../helper/execution_decisions.json).

All six supplied meme phrases are retained. [Research notes](meme_research.json) distinguish current circulation of the underlying expressions from the film's original 5.5/co-authorship pun; they do not claim objective product degradation or precise live billing behavior.

## Substitutions and remaining limits

- **Codex image generation used; no Luma.** All selected artwork, depth maps, masks, five S25 layers, and project source remain local.
- H3 pilot requests failed before an accepted generation ID because of network access. Production uses the plan's still-plus-2.5D fallback: illustrated pose changes, real displaced depth meshes, separately layered scenes, camera rigs, smears, and procedural effects. No generated character-animation footage was received. This is an infrastructure substitution, not a model-quality conclusion.
- Single-image coverage limits constrain 24 pre-ending shots' camera movement. Large requested orbits/cranes and full body choreography are not reproduced exactly; e.g. corrected S13 retains only about 5% of its requested travel. S25 uses five separately registered layers and a full authored camera move. Camera diagnostics disclose requested and retained movement.
- Remotion installation failed. `Film.tsx` provides the adapter, but the delivered frames use the local Three.js/Playwright renderer and FFmpeg. A successful `npx remotion render` is not claimed.
- The brief requests both AAC and an untouched MP3. The delivery prioritizes the original MP3 packets. Optional ProRes was not produced.
- **Native VLC and perceptual motion/audio review remain unverified.** QuickTime computer control lost its transport. VLC was absent; the official ARM64 distribution checksum was verified, but mounting failed because DiskManagement/DiskArbitration was unavailable. No installed apps were changed. [Attempt record](vlc_distribution.json). Automated browser playback is the verified playback result.

Use `qa/final/` as the delivery evidence. `qa/film/` and other preview folders retain iterative probes, including rejected earlier versions. Reproducible anchor overlays were compacted to JPEG; [path aliases](../helper/evidence-path-aliases.json) preserve their references. Superseded firstpass movies and temporary download caches were removed; selected artwork, final segment inputs, provenance, source hashes, and final deliverables were preserved.
