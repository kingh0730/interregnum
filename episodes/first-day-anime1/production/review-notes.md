# Production review log

The 44-shot first animatic is saved as `../animatic.mp4` (480×270, 30 fps, 1,311 frames; original MP3 copied into the container). It is a timing and composition draft, not the final export. The production camera rigs and selected motion passes are now implemented. No claim of having watched/listened to the whole film is made: review so far uses rendered frames, contact sheets, timing analysis and geometry checks.

Audio: decoded duration is 43.670 s. The required 1,311 frames at 30 fps last 43.700 s, so the plan's 20 ms audio-duration tolerance is incompatible with its exact frame count. Preserve the original audio and required video frame count. Librosa detected 88.34 BPM; the regular spectral-flux fit is 87.99 BPM, rather than the approximate 86 BPM in the plan. Lyric anchors remain fixed; other cuts snap only to observed onsets within three frames.

Use `round(t*30)` consistently: 11.27 s is frame 338, 11.92 s is frame 358, and 25.15 s is frame 755. Some example anchor indices in the plan differ from its own rounding rule.

Initial harness determinism passed. A startup deadlock was fixed by giving Playwright explicit timer polling rather than waiting on the virtualized rAF clock. Boot/network/shader errors now fail loudly and clean up the browser. Native Metal on the Apple M3 Pro passed the fresh-browser / out-of-order test at helix frame 952. Full-resolution warm frames measured around 0.15–0.36 s before lossless PNG optimization; cold helix benchmark was 1.18 s. SwiftShader was substantially slower (5–8 s for helix). Final preflight determinism passed at frames 500, 952 and 1230; all 197 film characters have font coverage. Full-sequence/export checks follow rendering.

Pillow lossless PNG optimization preserved decoded pixels in two representative tests and reduced file size by 22% and 30%. It is being used for final-size output because disk space is limited; resolution, bit depth, frame count and blur samples are unchanged.

Rejected / corrected assets:
- Opus reference v1 had short twin-tails; v2 fixes their length. Composite reference v1/v2 had misregistered marks; v3 corrects the visible full-body and detail placements. Expressions remain clean source artwork for later overlays.
- The first helix sprite sheet had overlaps and inconsistent view ordering. Separate front, side and back images replace it.
- The original front cutout composites cleanly over blue. The standalone matting test wrongly removed a twin-tail and is rejected. Raw transparent-image previews can show RGB that is not visible after alpha compositing; alpha must be checked on a contrasting background.
- S16 v1 had an early sunrise and keycap lettering. v2 fixes those; v3 adds halo headroom. S17 and S22 also have corrected night backgrounds.
- S35 v2 commits to the specified flat editorial line-art style.
- S19's two standalone image requests failed with network errors. Its specified method is B, so it is being constructed from existing approved room/character artwork in the 3D exterior rig; no Luma or other image generator is substituted.

S25 fallback: the requested 90°/270° pair views remained near-frontal and changed relative occlusion. They do not support a credible 360° frozen orbit. This fails the primary multi-angle plate gate. Use the plan's explicitly listed two-view image-to-video fallback, with front/back conditioning, and retain the 16-sample compositing requirement. The helix retains its full code-driven 450° path.

S20 MiniMax test: submitted 4 s at quoted $0.03/s ($0.12 estimate), returned 4.48 s, 1916×1080 at 24 fps. A 12-frame contact sheet shows a continuous foot descent and contact with clean visible anatomy. This is frame-based review, not an assertion of full playback QA. The source will be interpolated to ≥120 fps for the specified speed ramp; source audio is discarded.

Final compositing preflight: hand matte repairs and wrist restoration were inspected; S35 is barefoot; S44 includes the original painted foreground grass in its live depth plate. The official-vector render matched source SVGs pixel-for-pixel at 4×. The helix camera plot was inspected for continuity. Full-resolution render and export checks are in progress.

The first full render paused at frame 238 because Node synchronous pipe input and Python stdin reading deadlocked during lossless PNG optimization. Compression was switched to file arguments with a timeout; completed shots are resumed. The visual scene inputs are unchanged.


Final delivery: all 1,311 full-resolution PNGs passed sequence QA, all requested anchors and four all-shot contact sheets were inspected, and both H.264 exports were generated. S23 room coverage was repaired after the first render and its 60 frames replaced. The first encode lost primary/transfer tags; explicit setparams in the final filter chain corrected this, and export QA passed. Zero-sample audio lag in four segments; source audio timing unchanged. Manual audiovisual playback and phoneme review remain unverified. See README and the QA JSON files for final evidence.
