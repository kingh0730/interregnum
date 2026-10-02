# COMMON ROOM — motion handoff

Prepared through stage 6 only. **No video request has been submitted.** All 30 motion inputs now use the final director-approved source paths from `build/assets.json`. Local media preflight and the shared runner's dry-run quote pass. The final sound and story reel are the current deliverables; this document specifies a later motion pass without authorizing it.

`build/motion_plan.json` is a direct input to `tools/video/h3_batch.py` with the repository root supplied explicitly. `build/motion_triage.json` covers all 40 shots, including the 10 that are deliberately kept as authored graphics, typography or held material inserts. The manifest has 23 lip-sync jobs and 7 useful silent-motion jobs. Every output is reserved beneath `work/ep01/motion/`.

## Model and audio contract

Use MiniMax H3 Max at 768P. Silent-motion jobs request integer durations from 5–15 seconds, rounded up to cover the cut, with prompt expansion disabled. Their prompts describe small visible behavior and closed mouths; they contain no dialogue, quoted words or voice instructions. Seven source durations total 51 seconds.

The lip-sync route receives an image and our isolated audio, not an action prompt. Its minimum input is 5 seconds and output duration follows the audio. Therefore shots 17, 18 and 20 use new 5-second submission copies: the exact original 2–3-second shot audio followed only by silence. The other 20 dialogue jobs use their original shot-length WAVs unchanged. Total billable lip-sync duration is 135 seconds. The three short derivatives, hashes and original source paths are retained in `work/ep01/audio/motion_inputs/manifest.json`. Each final cut still starts at source time 0 and ends at its original shot duration. These constraints follow the [current lip-sync schema](https://fal.ai/models/minimax/h3-max/lip-sync/image-to-video/api).

`duration` in a lip-sync job is planning metadata: the runner does not send it to that endpoint. The shared `prompt_expansion_mode` default likewise applies only to the normal motion route. Lip-sync `enable_transcription` is explicitly false so the supplied audio drives synchronization directly. The current normal route describes `target_audio_url` as replacing the soundtrack; that is not evidence of controllable action plus mouth synchronization, so no job relies on it. See the [normal H3 Max schema](https://fal.ai/models/minimax/h3-max/image-to-video/api).

Discard every returned model audio track. Preserve the 230-second approved master, measured onsets and bilingual captions; change action Foley positions only where observed motion requires it during final finishing.

## Actions and result states

Dialogue jobs begin in readable poses. Do not expect the no-prompt lip-sync endpoint to deliver a reach, pat, pan placement, tray handoff, carton fold or salt exchange on command. Optional movements are usable only if the returned clip actually contains them.

The important physical changes already have explicit editorial states:

- Shots 02, 08 and 29 retain the exact authored paper layers and switches in `build/paper_states.json`, at global 00:08, 00:40 and 02:32. No talking paper or generated lettering.
- The doorway changes across the authored address insert and k03 result cut. No room morph.
- k12 holds the offered tray; k28 separately shows it down with the small spill. k31 separately shows Sen's raised pan. Neutral reused frames cannot replace those results.
- Updated k14 shows the remaining strip beside the pan and Eda's hand. There is no drawer. Eda's line stays off screen.
- k25 shows the displaced bowl on the chair; k29 separately shows it retrieved. k30 holds the salt/pattern request; k26 separately shows the spare cup weighting the pattern and salt with Sen.
- The carton return completes across the following paper insert. If lip-sync footage contains no usable fold, carry the closure sound into shot 29; do not claim a fold merely because it was requested or heard.

Held result inserts are 04, 13, 16, 19, 22 and 36. They are deliberate editorial tableaux, not evidence of an animated action. Title 40 is exact authored typography. Silent generated shots are 01, 23, 30, 31, 32, 33 and 39. The decision shot 23 preserves 240 uninterrupted frames; its supplied plate already holds the considered result pose, so a delayed new gaze is not a mandatory action. No additional romantic gesture or concluding shared look belongs in the ending.

## Three tests and proposed budget

The price snapshot in `work/ep01/prices.json` is $0.03/second for normal H3 Max and $0.05/second for lip-sync, observed 2026-10-02. The former differs from the runner's older $0.025 fallback; refresh and reconcile prices before a paid pass.

| Test | Why this clip | Seconds | Estimate |
|---|---|---:|---:|
| m07 | Eda's longest ordinary table line; mouth sync, pauses and stable identity | 7 | $0.35 |
| m23 | Two-person decision tableau; fixed geography, closed mouths and an uninterrupted hold | 10 | $0.30 |
| m30 | One ordinary onward step with carried objects and full feet visible | 8 | $0.24 |

The first three tests are estimated at **$0.89**, included in the all-pass first-take estimate of **$8.28**. The remaining 27 jobs are estimated at $7.39 if the test takes are accepted. A proposed **$4.00 retake reserve** gives a **$12.28 maximum envelope**. No automatic retakes are planned. This budget excludes later upscaling or an exceptional model comparison; neither is currently requested. Current motion spend is $0.

After future authorization, test those three jobs before the other 27. Review the entire returned takes and the intended cuts: a technically valid file, an attractive pose or an isolated frame is insufficient. Use one explicit replacement at a time for identified failures, retain earlier takes, and stop replacements at the reserve cap. The shared runner does not enforce an episode spending cap itself; `motion_preflight.py --quote-retakes <ids>` reports the quote against recorded retake spending.

## Preflight and review

All 30 `image` fields resolve to 21 distinct approved files in `build/assets.json`, including the corrected opening, doorway, module and decision plates. The manifest records each approved image's SHA256; triage records the resolved paths for generated and held shots. Never substitute a conditioning reference or an earlier rejected take. `motion_prepare.py` now uses the approved map whenever present; canonical `kNN.png` paths are bootstrap placeholders only when the map is absent. Any regenerated manifest must pass local preflight again.

The independent preflight decodes every image, checks its canvas and approved-map identity, verifies all 23 isolated audio sources sample-for-sample, confirms silence-only padding, checks 40-shot coverage and the 30-job exclusion logic, and prices the manifest. It never submits video. The shared runner's own dry-run only prices jobs and does not validate their media, which is why the local gate comes first.

```sh
uv run python episodes/ep01/build/motion_preflight.py
uv run python episodes/ep01/build/motion_preflight.py --runner-dry-run
```

The second command calls the existing runner with `--dry-run` only, and only after local inputs pass. The completed check reports no errors or missing sources; all 23 conditioning files preserve the exact original isolated samples, and all three extended tails contain only silence. The live runner quote is $8.28, matching the captured estimate. Evidence is in `build/motion_preflight.json` and `work/ep01/motion/runner_dry_run.txt`. No request or billing ledger was created. The final audio master remains unchanged, with SHA256 `cd40a5cd19413d5b95ca1e10b269dc0e11b403382e7207fd24b5276feb57622d`.

Future footage must be decoded and counted at its actual returned frame rate and length. Verify mouths during every silent section and during the padded voice tails; verify every visible hand, prop count, doorway destination, bowl stripe, counter boundary and garment against its starting frame and neighboring cuts. For the ordinary step, locate full onset, planted foot and settled finish without camera crop. Review the final edited clip separately; keep measured action timestamps in the triage record, whose values are currently null. Preserve the exact 01:49 score/action stop and continuous room air. Uncertain naturalness or motion remains explicitly pending playback review.
