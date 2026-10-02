# Video model

Animates keyframes (image-to-video) for anything that has to move like drawn or filmed footage.

## H3 runner and recorded continuity approval

`tools/video/h3_batch.py` is the resumable motion-manifest runner. Current production
guidance is in `docs/playbook.md`; the Seedance bake-off notes below are historical.
The runner preserves accepted request IDs across polling/download failures and
does not automatically replace a paid request.

New episode manifests include a top-level `continuity_review` string, a local path
relative to `--root`. Historical manifests without that field retain their existing
behavior. Example:

```json
{
  "continuity_review": "episodes/ep01/build/continuity_review.json",
  "jobs": [{
    "id": "m05",
    "shot_id": "05",
    "image_key": "k05",
    "image": "work/ep01/keys/k05_fix.png",
    "prompt": "The selected pose holds.",
    "out": "work/ep01/motion/m05.mp4"
  }]
}
```

This gate validates the completeness and freshness of **recorded visual review**.
It does not discover object positions, judge a crop, approve motion, or supply
permission to spend. Technical media validity remains a separate check.

The review uses `schema_version: 1` and contains:

- `status`: `pending`, `blocked` or `approved`; an approved review names `reviewer`.
- `story` and `assets`: `{path, sha256}` bindings. The story has ordered `shots`
  with `id` and `asset`; the asset map holds local paths or objects with `path`.
- `additional_inputs`: a list of `{path, sha256}` bindings for relevant framing,
  state or design files, including the actual renderer/composition recipe and
  procedural title/endcard/credits recipes when used. `sources` binds every
  distinct asset-map image path.
- `cuts`: exactly one record for each adjacent story-shot pair, including scene
  and title boundaries. Each records `from_shot`, `to_shot`, `from_asset`,
  `to_asset`, `relation`, `status`, `evidence` and `issues`.
- Optional `states`: a `{path, sha256}` binding to a map of shot IDs to
  `{offset_frame, asset}` lists. Offsets start at zero and increase within explicit
  shot `start_frame`/`end_frame` bounds. When supplied, `state_changes` records
  every nonzero switch using `shot_id`, `offset_frame`, `from_asset`, `to_asset`
  and the same judgment fields. An empty list is valid when no switches exist.

Relations are `continuous`, `ellipsis`, `scene_change` or
`intentional_discontinuity`. Every approved record needs specific evidence and an
empty unresolved-issues list. A legitimate tighter crop or occlusion can preserve
continuity; an intentional time jump or nonphysical style can permit a change.
The evidence must explain that particular transition. An asset's earlier use
does not approve its reuse after the scene's physical state has changed.

Cut endpoints use the preceding shot's last state and the next shot's first.
Procedural `title`, `endcard` and `credits` shots need no image-map source. All
paths in the review resolve relative to `--root`.

New gated submissions require `shot_id`. Their local `image` must match that
occurrence's reviewed first-state path; `image_key`, when present, must match its
asset ID. An optional `end_image` must match its final-state path. URL, data-URI,
chained frames and image URLs passed through `params` cannot claim this local
still review; extract/select a local frame and review its occurrence first.

The gate runs before new/redo preparation and again immediately before the
submission state transition. Missing, pending, blocked, malformed or stale review
prevents a new POST, including a saved `prepared` request. Already accepted
requests can still poll, download and finish after approval is withdrawn; their
existing payload-identity and ambiguous-submission protections remain in force.
A blocked redo preserves the previous take. `--dry-run` still returns a price
quote and reports a blocked gate without treating the quote as approval.

Local callers use `tools/continuity.py`:
`evaluate_review(review_path, root)` returns `approved`, recorded `status`,
`errors`, review path/hash, `source_hashes` and `shot_sources`.
`require_approved(review_path, root)` returns that result or raises
`ContinuityReviewError`. Episode preflight and delivery checks should require
`approved`, rather than inferring artistic approval from decoded media.

The standalone validator is local and read-only:

```bash
python3 tools/continuity.py --help
python3 tools/continuity.py episodes/ep01/build/continuity_review.json --root .
```

It prints JSON diagnostics and exits `0` for current complete approval, or `2`
for a missing, malformed, stale, pending or blocked review. It does not call a
model, fetch media, edit the review or infer a missing visual judgment.

## Historical Seedance bake-off (2026-09-29)

**Status:** working (`i2v.py`, fal.ai queue API, key from `$FAL_KEY`). Bake-off done 2026-09-29, about $24. The chosen model is **Seedance 2.5** (native dialogue with lip-sync; see `docs/strategy.md`). The candidate provider is **fal.ai**: confirm it hosts Seedance 2.5 and check prices. Used in v2 only.

**Plan:**
1. `export FAL_KEY=...` in the shell environment. Never write the key into a file in this repo.
2. Bake-off with Seedance 2.5 on 2–3 keyframes (a character close-up with a quoted line of dialogue, a wide establishing shot, an action beat). Check clip lengths, voice consistency across shots, audio-driven lip-sync, a clean no-music stem, and Chinese vs English. King judges the motion. Compare one other model only if Seedance disappoints.
3. Build `tools/video/i2v.py`: keyframe + motion prompt + duration → `work/<ep>/<shot>/takes/NN.mp4`, logging the model, seed and prompt next to each take.

**Bake-off findings (2026-09-29; pilot shots 16, 17, 19 and 44; stills, transcripts and pitch only, motion unverified):**
- **Endpoint:** `bytedance/seedance-2.5/image-to-video` gives 720p at most, 4–30 s, about $0.47/s at 720p ($0.22/s at 480p), in about 4–8 min per take.
  Output is 1280×720 at 24 fps, upscaled to 1080p in the conform.
- **Style and identity:** the flat cel look and the characters hold from the start frame, with no drift across 4–10 s.
- **Dialogue:** a line written in quotes in the prompt is spoken word for word (Whisper-verified), with visible mouth shapes and acting.
  Reference-to-video with an `[Audio1]` voice keeps the start frame's composition, but it ad-libbed a word, and pitch
  didn't move toward the reference. Voice identity needs ears.
- **Unwanted audio:** a no-dialogue take may carry a spoken phrase. For non-dialogue shots use `--no-audio` and keep our sound design.
- **Story effects:** a "windows switch to amber" prompt gave one gimmick take (a glowing dome) and one good take (patchy
  window-by-window spread). Generate 2 takes of any effect-driven shot; sky or colour changes are left to the grade.
- **Recipe:** the shot's motion prompt as written, 2 drafts at 480p, the winner re-rendered at 720p with its seed (whether a seed reproduces across resolutions is untested).

**Prompting notes (to fill in during the bake-off):** camera language, acting verbs, which negatives help, max useful duration.
