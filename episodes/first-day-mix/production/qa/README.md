# Production QA helpers

These scripts use Python standard library plus local ffmpeg/ffprobe. Run from the repository root. They do not run models, spend money, modify shared tools, approve unseen images, or establish motion quality by metrics.

## Technical render evidence

`python3 episodes/first-day-mix/production/qa/check_render.py CONFIG.json --out work/first-day-mix/production/qa/UNIQUE-RUN`

Config uses **inclusive start, exclusive end**, integer frames and actual renderer overlay boxes:

```json
{
  "video": "work/first-day-mix/production/final.mp4",
  "fps": "60",
  "width": 1920,
  "height": 1080,
  "expected_frames": 2620,
  "source_audio": "episodes/first-day-mix/first-day.wav",
  "source_audio_sha256": "BASELINE_SHA256_RECORDED_BEFORE_PRODUCTION",
  "shots": [{"id": "01", "start_frame": 0, "end_frame": 60}],
  "overlays": [
    {"id": "lyric-01", "start_frame": 0, "end_frame": 60, "box": [200,900,1500,100]},
    {"id": "label-01", "start_frame": 0, "end_frame": 60, "box": [100,100,400,80]}
  ],
  "assets": [],
  "generation_logs": [{"path": "work/path/response.json", "expected_cost_usd": 0.2, "actual_cost_usd": null, "cost_evidence": "Estimate; provider invoice unavailable"}]
}
```

Example frame count is illustrative: use the actual approved timeline. Contact frames are shot start, lower midpoint, last frame, prior frame and next shot's first frame where available. Unique frame indices are sorted and extracted by decode index, not keyframe seek. `report.json` records image/frame/time mappings and per-shot samples. Contact sheets contain 20 images each, four columns, ordered left-to-right/top-to-bottom; sheet 2 starts at mapping entry 20. Black unused cells on the final page are padding, not video frames. Use individual PNGs for detailed inspection. Each output directory must be new to prevent stale PNGs entering a sheet.

Loudness uses ffmpeg loudnorm's **input** measurements; its output-normalization fields are also present but do not describe the delivered file. Audio hashes compare identically decoded stereo 48 kHz s32 PCM, plus original file bytes. Exact equality is meaningful for unmodified lossless audio; AAC will differ. A configured pre-production source hash verifies the original source file remains unchanged. No identity or perceptual sync assertion is inferred from lossy mismatch. Absence of a baseline yields null, not true.

Overlay collision is geometric only. Supply every actual text bounding box with stroke/shadow padding; animated text requires separate interval rows. `allow_overlap_with` can list intentional paired IDs; all collisions remain recorded. This cannot establish glyph legibility, facial occlusion, safe composition or subtitle perception.

Generation-log amounts must be explicitly supplied from estimates/invoices. Logs are hashed for provenance, not dumped (they may contain large payloads). Missing actual costs stay null. Image/source dimensions are obtained via ffprobe. Missing or undecodable inputs fail loudly.

## Record a visual review without bypassing the continuity gate

Root reviewer first inspects **every source in the stage assets map and every cut/state transition** and records specific judgments. Create separate root-authored story/assets JSON for a test stage, then a full production stage. A successful test-stage record does not approve the full production stage.

`python3 episodes/first-day-mix/production/qa/make_review.py JUDGMENTS.json --out work/first-day-mix/production/qa/STAGE-review-v1.json`

Root-authored input shape:

```json
{
  "stage": "representative-motion-test",
  "reviewer": "Codex root; visual source inspection",
  "reviewed_visually": true,
  "status": "approved",
  "scope_note": "Source stills only; generated motion remains unreviewed.",
  "story": "work/path/test-story.json",
  "assets": "work/path/test-assets.json",
  "reviewed_input_hashes": {"story": "ACTUAL_SHA256", "assets": "ACTUAL_SHA256"},
  "reviewed_sources": [
    {"path": "work/path/source.png", "sha256": "ACTUAL_REVIEWED_BYTES_SHA256", "status": "approved", "evidence": "Specific observed appearance, pose and source-state judgment."}
  ],
  "cuts": [],
  "state_changes": [],
  "additional_inputs": []
}
```

A one-shot story legitimately has no cuts. Multi-shot stories require each adjacent pair explicitly:

```json
{"from_shot":"01","to_shot":"02","from_asset":"a","to_asset":"b","relation":"continuous","status":"approved","issues":[],"evidence":"Specific observed transition judgment."}
```

If `states` is supplied, add its hash to `reviewed_input_hashes` and explicitly judge every authored switch:

```json
{"shot_id":"01","offset_frame":30,"from_asset":"a","to_asset":"b","relation":"intentional_discontinuity","status":"approved","issues":[],"evidence":"Specific observed and story-motivated change."}
```

Allowed relations: `continuous`, `ellipsis`, `scene_change`, `intentional_discontinuity`; statuses: `pending`, `blocked`, `approved`. Existing `tools/continuity.py` validates all bound paths, source hashes, cut endpoints and state coverage. The helper invokes that validator and returns code 2 if not approved. Pending/blocked judgments can be recorded but cannot pass. No auto-filled evidence or auto-approved cut list is generated. Output records cannot overwrite an existing review. Reviewer attestation is still a judgment, not independently verified by code; scripts cannot determine whether the reviewer actually looked.
