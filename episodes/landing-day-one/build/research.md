# Production research, 2026-10-03

## Cultural slots

- DeepSeek 「蓝色大肥鱼」 is visibly still used in a 2026-09-04 creator video description: https://www.youtube.com/watch?v=buYQ-_V2Wv0 . Keep the affectionate whale motif and the sticker. This is evidence of usage, not a claim about universal sentiment.
- Gemini 「北美大豆包」 appears in a 2026-07-19 Bilibili video title: https://www.bilibili.com/video/BV1xpKK6VEJc/ . Keep the oversized-person/small-bun-hat gag.
- 「豆包型人格」 appears in dated 2026 coverage and a June article about easy acknowledgement of mistakes, low rumination and empathetic behavior: https://www.51ldb.com/shsldb/zg/content/019e6d92b994c001000066d533acd97d.html and https://www.fcipub.org/articleDetail/5328?periodicalId=3 . Keep the title as affectionate internet shorthand, not a performance claim.
- 「@Grok 这是真的吗」 is attested in April 2026 social discussion: https://www.reddit.com/r/KanagawaWave/comments/1sqbnnt/ . Use a question, without a factual product claim.
- No adequate current attribution established for Claude's default phrase or ChatGPT's proposed meme. Use the planner's nod-only / 好问题 fallback. DeepSeek busy-server claim is replaced with the verified 蓝色大肥鱼 sticker and a spinner. Remove open M7 instead of inventing a newest meme.

## Concepts and categories

SGI has conflicting expansions. Scientific General Intelligence is explicitly used by https://github.com/InternScience/SGI-Bench ; structural and super-general uses also surfaced. Preserve the planner's ambiguous S/SGI doorway; do not silently replace it with ASI or assert a technology timeline.
Roster names are fictional character labels, not endorsements or rankings. ChatGPT, Claude, Grok, DeepSeek, 豆包, Gemini are leads; Qwen, Kimi, 文心, 元宝, GLM, MiniMax, 讯飞星火, Llama, Mistral form the ensemble. Llama is a model family; several others are apps or providers. Distinctions do not imply a genealogy. Additional systems may appear as rung Easter eggs.

## Current production capabilities and costs

Luma Uni-1 Max current public page: https://fal.ai/models/luma/agent/uni-1/v1/max — $0.102/image at lookup, not the old $0.003 repository estimate.
H3 Max reference workflow: https://fal.ai/models/minimax/h3-max/reference-to-video/api — explicit reference_video_urls, 2–15 second reference clips, optional first frame, 480P/768P/1080P. Initial 3s test quote $0.15. Request returned downstream_service_unavailable (504), so no usable motion result and no creative pass.
H3 Max I2V: https://fal.ai/models/minimax/h3-max/image-to-video/api . Small replacement test submitted with identity frame and simple phrase; no bulk motion authorized by a failed test.
Ray 3.2: https://fal.ai/models/luma/agent/ray/v3.2/image-to-video/api — single-first-frame 5s duration, 540p/720p/1080p. Small per-shot comparison follows H3 reference outage.
Initial production spending ceiling: $25, stated to user after Full access instruction. No publication. Generation logs and provider request IDs retained; accepted requests are not blindly re-posted.

## Fonts and delivery

Ma Shan Zheng and ZCOOL KuaiLe downloaded from google/fonts with original OFL notices in assets/fonts. Other fallback system fonts are not bundled. Brush and rounded fonts preload before frame zero.
Master: 2560x1440 at 60 fps, 2621 frames; source WAV PCM24 stereo 44.1kHz copied without trimming. Archival .mov carries PCM24; viewing .mp4 uses AAC and is explicitly not bit-identical audio. No target platform has been requested, so no upload or loudness normalization.

## Reference code

See source-study.md. MIT source from mexicat/pdoom-video is copied with attribution under src/vendor/pdoom. No reference song, text or artwork used.

## Historical dates verified

ELIZA 1966: original ACM paper https://doi.org/10.1145/365153.365168 . Deep Blue 1997: https://www.ibm.com/history/deep-blue . AlphaGo's Lee Sedol match 2016: https://deepmind.google/research/alphago/ . Transformer paper 2017: https://arxiv.org/abs/1706.03762 . Tiles identify selected milestones, not a single biological family tree.

## Further test outcomes

H3 Max I2V returned a 1344x768, 24fps, 4.458s clip. Sampled frames show raised hand, palm to chest and heel lift/plant with full-body camera lock. This is evidence for action selection, not a claim of full-speed human playback approval. Reference-to-video remained unavailable. Ray 3.2 returned invalid-input for its initial small test; no usable clip, no bulk Ray calls.
