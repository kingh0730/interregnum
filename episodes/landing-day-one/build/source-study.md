# p(doom) source study — 2026-10-03

Inspected https://github.com/mexicat/pdoom-video at `a048746d25fa0333ca884fb79fe4482b9c89250d` (current clone). The supplied planner cited an earlier revision; this production records the revision actually inspected.

1. **Clock:** `app/src/engine/scene.ts` passes absolute `t`, local `lt`, progress `p`, beat/bar phase and seek flags. Separate character pose clock is needed for our held animation.
2. **Audio:** `analysis/analyze.py` writes normalized 100 Hz RMS/band/stem envelopes and onset events; `engine/audio.ts` interpolates and decays event pulses. Our local analysis uses full-mix bands, explicitly not invented vocal stems.
3. **Particles:** `engine/util.ts` provides seeded mulberry32 and stateless hash; stable IDs and analytic trajectories make arbitrary-time render possible.
4. **Seeking:** Scene API distinguishes pure scenes from bounded preroll stateful scenes. Our scenes will use analytic state and replay timestamped paint stamps.
5. **Text:** `engine/type.ts` preloads FontFace data, caches outline fonts, lays out glyphs. Its Latin registry is not copied; this film uses a separate CJK renderer and per-glyph Chinese treatments.
6. **Colour:** `gl.ts` HalfFloat targets, linear palette and sRGB texture input; `post.ts` seven-level bloom pyramid, warm halation, highlight shoulder and final explicit linear-to-sRGB.
7. **Export:** `scripts/render.ts` drives browser frames through WebSocket to raw RGBA FFmpeg input, explicit BT.709 matrix/tags and bounded in-flight frames. Its audio is AAC; our archival master must carry PCM to preserve the source samples.
8. **Sampling:** source supports adaptive 12/36/108/324 subframe integration with a short shutter. Our planned baseline is four samples, with pose time quantized independently of camera time and samples clamped inside shot boundaries.
9. **Licence:** MIT code © 2026 Giacomo Magnanini. Code files copied under `src/vendor/pdoom/` retain LICENSE. Bundled fonts have separate licences. No reference music, lyrics, artwork or rendered footage enters our movie.
10. **Transitions:** `Frame.under`, `tin`, `tout` and `handlesTransition` let a scene composite its own incoming boundary. Our boundary is the floor-projected heel ring, not a generic dissolve.

Directly adapted files: `gl.ts`, `post.ts`, `util.ts`, `palette.ts`, `scale.ts`, `glsl/common.ts`. Changes will be limited to output dimensions, scale handling and integration. This is concrete code reuse authorized by the user, with attribution, rather than a claim of aesthetic superiority. Full-speed comparison remains a review task.
