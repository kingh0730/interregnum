# How we got here (experiments, 2026-09-29)

Before this repo existed, four tests in `~/repos/yue/outputs/anime_clip/` tried to make a short anime clip of a
silver-haired girl in a red scarf on a rooftop at sunset with a paper airplane. King's verdicts decided the pipeline.

| Version | Method | King's verdict | Why |
|---|---|---|---|
| v1 | 6 Codex keyframes + ffmpeg zoom/pan + crossfades | "More like PPT than anime" | No motion, only camera moves |
| v2 | Codex layer separation (sky/city/character cutouts, aligned with SIFT), parallax, hair/scarf mesh warp, blink cels, petals, flare, bloom, synth audio | "Interesting, but like an old anime game cutscene" | The character is a puppet: bending a still never changes the silhouette |
| v3 | Codex draws every in-between (key poses, breakdowns, follow-through), timed on twos | Round 1 "a bit weird"; round 2 (held body cel, more drawings) "even worse" | Each Codex image is an independent reinterpretation: no consistency from frame to frame. Head floated on the fixed body; more drawings meant more shimmer. Frame metrics *improved* while the motion got worse |
| v4 | Blender + VRM sample model (pixiv, permissive license), rigged head turn with overlap, blink, spring-bone hair, MToon toon look, composited over the Codex plate | "It does work", but then "this method may not work" | Motion correct and consistent, but it reads as 3D; drawn anime faces need per-character normal editing and more |

**Conclusion:** motion that is both drawn-looking and consistent needs a video model. Codex is excellent for stills,
and everything else stays in-house (see `strategy.md`).

**Other facts established:**
- Sora is gone (app April 2026, API September 24 2026).
- Codex (`gpt-6-astra`) defaults to `xhigh` in `~/.codex/config.toml`. For image jobs, reasoning effort doesn't
  change image quality, so `gen.sh` uses `medium` (about 2 min per image vs about 3 min at xhigh). King chose medium.
- The image model behind Codex's built-in `image_gen` isn't stated anywhere local; the API fallback defaults to `gpt-image-2`.
- `~/.claude/settings.json` allows `Bash(codex exec:*)`; auto mode blocks Claude from changing its own permissions.
- `~/.codex/config.toml` is now tracked in King's home dotfiles repo (only that file; auth and history stay ignored).
