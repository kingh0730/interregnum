# Final cut / 最终剪辑

This describes the implemented film. The earlier script and per-shot plans are development intent; this table and final-config.json define the rendered choices. Generated performance uses observed gestures, and ensemble animation uses authored cutouts/replacement poses.

| Cell | Seconds | Implemented picture | Source interval / focus |
|---|---|---|---|
| 01 | 0.000–0.450 | video | macro 0.1s ×2.0 |
| 02 | 0.450–1.350 | birth | gpt |
| 03 | 1.350–2.833 | fan | gpt |
| 04 | 2.833–3.183 | video | macro 1.1s ×1.8 |
| 05 | 3.183–3.867 | birth | deepseek |
| 06 | 3.867–4.717 | video | dance 1.0s ×1.5 |
| 07 | 4.717–5.233 | attention | gpt, deepseek |
| 08 | 5.233–6.083 | birth | claude |
| 09 | 6.083–6.783 | attention | gpt, deepseek, claude |
| 10 | 6.783–7.567 | birth | doubao |
| 11 | 7.567–8.233 | birth | gemini |
| 12 | 8.233–9.033 | birth | grok |
| 13 | 9.033–10.033 | video | cyber 0.6s ×1.6 |
| 14 | 10.033–10.583 | cel | doubao |
| 15 | 10.583–11.183 | video | night 0.7s ×1.8 |
| 16 | 11.183–11.367 | pixel | deepseek |
| 17 | 11.367–11.917 | video | dance 3.0s ×2.0 |
| 18 | 11.917–12.867 | video | canopy_detail 3.1s ×1 |
| 19 | 12.867–13.617 | birth | qwen, kimi |
| 20 | 13.617–14.300 | cel | qwen, kimi |
| 21 | 14.300–14.633 | video | cyber 3.1s ×2 |
| 22 | 14.633–15.583 | birth | yuanbao, wenxin, step, baichuan |
| 23 | 15.583–16.283 | video | night 2.7s ×1.5 |
| 24 | 16.283–17.183 | birth | glm, spark, sense, pangu |
| 25 | 17.183–17.433 | attention | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu |
| 26 | 17.433–17.617 | video | ankle 0.7s ×1 |
| 27 | 17.617–19.667 | video | ankle 0.87s ×0.9 |
| 28 | 19.667–20.117 | video | canopy 0.2s ×1 |
| 29 | 20.117–21.400 | video | canopy_detail 0.5s ×1.4 |
| 30 | 21.400–22.700 | ensemble | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu |
| 31 | 22.700–23.033 | video | canopy 1.2s ×1.3 |
| 32 | 23.033–23.933 | birth | minimax, copilot, alexa |
| 33 | 23.933–24.933 | birth | meta, perplexity, siri |
| 34 | 24.933–25.450 | ensemble | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu, minimax, copilot, alexa, meta, perplexity, siri |
| 35 | 25.450–26.250 | video | dance 5.8s ×1.4 |
| 36 | 26.250–26.700 | cel | gpt, deepseek |
| 37 | 26.700–27.050 | paper | gpt, deepseek |
| 38 | 27.050–27.300 | pixel | gpt, deepseek |
| 39 | 27.300–28.550 | explosion | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu, minimax, copilot, alexa, meta, perplexity, siri |
| 40 | 28.550–29.400 | video | portal 0.5s ×1.8 |
| 41 | 29.400–30.683 | future | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu, minimax, copilot, alexa, meta, perplexity, siri |
| 42 | 30.683–31.383 | ensemble | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu, minimax, copilot, alexa, meta, perplexity, siri |
| 43 | 31.383–32.033 | reserved tile insert | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu, minimax, copilot, alexa, meta, perplexity, siri |
| 44 | 32.033–33.233 | video | canopy 4.0s ×1 |
| 45 | 33.233–34.217 | ensemble | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu, minimax, copilot, alexa, meta, perplexity, siri |
| 46 | 34.217–34.567 | video | canopy 5.15s ×0.8 |
| 47 | 34.567–35.667 | birth | future |
| 48 | 35.667–37.067 | ensemble | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu, minimax, copilot, alexa, meta, perplexity, siri, future |
| 49 | 37.067–37.617 | paper | future_open |
| 50 | 37.617–39.417 | ensemble | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu, minimax, copilot, alexa, meta, perplexity, siri, future |
| 51 | 39.417–39.900 | cel | doubao |
| 52 | 39.900–42.350 | ensemble | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu, minimax, copilot, alexa, meta, perplexity, siri, future |
| 53 | 42.350–43.683 | ensemble | gpt, deepseek, claude, doubao, gemini, grok, qwen, kimi, yuanbao, wenxin, step, baichuan, glm, spark, sense, pangu, minimax, copilot, alexa, meta, perplexity, siri, future |

The final title is an overlay on the existing closing shot. Patches replace exactly frames494–714 (meme ownership) and1883–1921 (reservedtile). The two four-person births are also fitted within frame by replacing878–934 and978–1030. Total2621frames remains unchanged. User music preserved with only13.333ms ending silence padding for the60fps frame boundary. No generated audio is used.

## Actual production choices

- 23 original character cutouts and five alternate poses, eight generated motion clips, five Luma environment/prop plates, two edited hero frames plus an exact ankle crop.
- Code supplies births/empty sockets, folded geometry, aerial canopy and harness lines, particle depth order, fractured material, perspective curves, pixel treatment, held replacement poses, Chinese labels/lyrics and title.
- Separate practical day, night, cyberpunk, ancient theatre, photographic dance, cel/paper/pixel/woodblock and speculative scenes.
- The source dance supplies visible weight shifts and arm gestures; the literal originally prompted footstep sequence is not claimed. The lead contact is an upper-forearm hold, as actually pictured.
- Final story is visual successive awakenings, shared flight, speculative branches, the last intact tile, and the unlabelled newcomer. No explanatory narration or product capability ranking.
