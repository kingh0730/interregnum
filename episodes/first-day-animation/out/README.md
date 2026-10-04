# DAY ONE / 第一天 — production record

Deliverable: `opus55_first_day.mp4` — H.264, 1920×1080, 30 fps, 1,311 frames, 43.70 seconds.

This production uses **Codex built-in image generation** for both selected character sheets, all 32 keyframes, and generative corrections. No Luma calls or assets were used. Motion uses MiniMax H3 Max; native and parallax shots use the bundled deterministic three.js/WebGL2 compositor. Original MP3 audio is stream-copied, without remixing, stretching, or re-encoding.

## Source record

- Creative source: `../director-response.md`.
- Verbatim extraction, expanded prompts and specification conflicts: `../build/manifest/`.
- Actual image prompts and correction provenance: `../build/image-generation-log.json`; authoritative reference sheets: `../assets/ref/wuwu.png`, `../assets/ref/support.png`.
- Built-in imagegen does not expose an image seed. Procedural PRNG seeds are in `../compositor/src/`; the main particle seed is 1234 and lyric particles use 77.
- Motion requests: `../build/motion.json`, `../build/retakes.json`, `../build/s08-motion/motion.json`. All accepted requests are logged locally; existing requests were resumed instead of resubmitted.
- Frame windows and take-selection reasons: `../build/selected-takes.json`.
- Depth: local Depth Anything V2 Small ONNX, 16-bit near-white PNG maps. No pseudo-depth fallback.
- Research, font download sources, and live price snapshot: `../build/research.json`.

44 accepted motion takes × 5 seconds; estimated ledger cost **$6.60** at the returned per-second rate. Image generation consumed subscription quota, not fal image calls.

## Resolving source conflicts and production limits

- The actual shot table contains 37 rows: 20 V, 9 P, 6 H, and two hybrids. All are retained in order. No V shot was substituted with a still fallback.
- Seconds are rounded to 30 fps frames. The 11.92-second title lands on frame 358 (11.9333 seconds); the quiet section is frames 336–357. Detected onset adjustments within 80 ms are recorded in `../build/timing-adjustments.json`; lyric anchors take priority.
- The measured MP3 is 43.67 seconds, not the brief's 43.70. Picture lasts exactly 43.70; every encoded audio packet is retained unchanged. The final 30 ms of picture extends past the source audio.
- The source examples reversed the crash zoom and color wipe. The implementation follows the written wide-to-close and line-to-color direction.
- The six version values begin during S04a and finish in S04b, because they cannot each occupy a full beat within S04b alone. S13 retains the specified five shot intervals rather than adding unlisted cuts.
- The 360° breath-camera take is conformed in full to its short slot; it does not also apply the contradictory literal 50% time stretch. S03a uses a 40%-speed source window with interpolation.
- V images retain their original source bytes for request reproducibility; video plates are conformed to 1920×1080. Generated P/H images are Lanczos-conformed where necessary.
- Parallax is a single-view depth reconstruction, not unseen character geometry. A rear image layer covers disoccluded frame edges during the large authored moves.
- Native cosmic shot uses 800,000 galaxy particles and 12,000 character-sheet silhouette instances. Native scene motion blur uses six deterministic subframes.
- Official press-kit retrieval failed. The authorized logo fallback is used: procedural 12-blade spark and serif ANTHROPIC. Generated brooch/eye symbols are stylized interpretations, not exact official SVGs.
- The final hold stops animation while preserving the clean end-card lockup, resolving the brief's fade-to-ivory versus stable-final-card conflict.

Review performed: character and keyframe inspection, depth-map inspection, both initial motion takes per V shot, targeted third takes, three frames per native/hybrid shot, every shot boundary, full contact sheets, frame-based determinism checks, luminance trace, and encoded-stream checks. Sampled-frame review does **not** certify normal-speed motion or musical feel; the delivered film is ready for playback review.

## Shot sources actually used

| Shot | Frames [start,end) | Source | Selected asset / take | Video seed |
|---|---:|---|---|---:|
| S01a | 0–42 | H | `Native WebGL / Canvas scene` | — |
| S01b | 42–85 | V | `assets/clips/S01b_take1.mp4` | 5501 |
| S02a | 85–120 | V | `assets/clips/S02a_take1.mp4` | 5511 |
| S02b | 120–173 | V | `assets/clips/S02b_take1.mp4` | 5521 |
| S03a | 173–196 | V | `assets/clips/S03a_take1.mp4` | 5531 |
| S03b | 196–217 | P | `assets/keyframes/S03b.png + assets/depth/S03b.png` | — |
| S03c | 217–236 | P | `assets/keyframes/S03c.png + assets/depth/S03c.png` | — |
| S03d | 236–247 | H | `Native impact lines/bubble over S03c plate` | — |
| S04a | 247–288 | V | `assets/clips/S04a_take2.mp4` | 5542 |
| S04b | 288–319 | H | `Native WebGL / Canvas scene` | — |
| S04c | 319–336 | P | `assets/keyframes/S04c.png + assets/depth/S04c.png` | — |
| S05 | 336–358 | P/H | `assets/keyframes/S05.png + assets/depth/S05.png` | — |
| S06a | 358–390 | V | `assets/clips/S06a_take1.mp4` | 5551 |
| S06b | 390–439 | V | `assets/clips/S06b_take2.mp4` | 5562 |
| S07a | 439–472 | V | `assets/clips/S07a_take3.mp4` | 8833 |
| S07b | 472–503 | P | `assets/keyframes/S07b.png + assets/depth/S07b.png` | — |
| S07c | 503–528 | V | `assets/clips/S07c_take2.mp4` | 5582 |
| S08 | 528–590 | V | `assets/clips/S08_take3.mp4` | 8870 |
| S09a | 590–636 | V | `assets/clips/S09a_take3.mp4` | 8834 |
| S09b | 636–681 | H/P | `assets/keyframes/S09b_line.png + S09b_color.png; WebGL reveal` | — |
| S10a | 681–721 | V | `assets/clips/S10a_take1.mp4` | 5611 |
| S10b | 721–764 | V | `assets/clips/S10b_take2.mp4` | 5622 |
| S11a | 764–800 | V | `assets/clips/S11a_take2.mp4` | 5632 |
| S11b | 800–841 | V | `assets/clips/S11b_take1.mp4` | 5641 |
| S11c | 841–857 | P | `assets/keyframes/S11c.png + assets/depth/S11c.png` | — |
| S12a | 857–892 | V | `assets/clips/S12a_take2.mp4` | 5652 |
| S12b | 892–920 | V | `assets/clips/S12b_take2.mp4` | 5662 |
| S13a | 920–941 | P | `assets/keyframes/S13a.png + assets/depth/S13a.png` | — |
| S13b | 941–963 | P | `assets/keyframes/S13b.png + assets/depth/S13b.png` | — |
| S13c | 963–984 | P | `assets/keyframes/S13c.png + assets/depth/S13c.png` | — |
| S13d | 984–1004 | P | `assets/keyframes/S13d.png + assets/depth/S13d.png` | — |
| S13e | 1004–1026 | H | `Native WebGL / Canvas scene` | — |
| S14 | 1026–1112 | V | `assets/clips/S14_take3.mp4` | 8835 |
| S15 | 1112–1197 | H | `Native WebGL / Canvas scene` | — |
| S16a | 1197–1235 | V | `assets/clips/S16a_take2.mp4` | 5682 |
| S16b | 1235–1274 | V | `assets/clips/S16b_take1.mp4` | 5691 |
| S16c | 1274–1311 | H | `Native WebGL / Canvas scene` | — |

## Reproduce

Run from the repository root. Install the episode's pinned npm dependencies with `npm ci --prefix episodes/first-day-animation`. The existing Python environment needs librosa, NumPy, Pillow, OpenCV, ONNX Runtime, huggingface-hub and matplotlib. FFmpeg and local Google Chrome are used.

1. Serve `episodes/first-day-animation` on localhost port 8123.
2. Bundle `compositor/src/main.js` using esbuild into `compositor/dist/bundle.js`.
3. Run `MODE=final node episodes/first-day-animation/render.mjs` using the working Node binary. Frames go to `work/first-day-animation/frames/`.
4. Encode the JPEG sequence at 30 fps with libx264, map the original MP3, and use `-c:a copy -frames:v 1311 -t 43.70`.
5. Run `build/verify.py`. QA artifacts are under `out/qa/`.

Generation files and media remain local and are not committed. Do not regenerate paid requests merely to reproduce the final assembly.

Final verification: 1,311 frames at 30/1 fps; video duration 43.700000 seconds; 1,673 MP3 packet payloads identical to source; no all-black frames. Six representative frame indices rendered identically after out-of-order rendering. See `qa/technical-report.json`, `qa/determinism.json`, `qa/visual-review.json`, `qa/contact-sheet.jpg` and `qa/luminance.png`.
