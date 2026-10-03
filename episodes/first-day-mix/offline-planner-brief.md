# First Day Mix — creative director's handoff to an offline planning agent

## Your assignment

You are the creative director, art director, choreographer and editor for a Mandarin music video in **AI SI - I**. Produce a complete production plan that another agent, Codex, will execute later with internet access, image/video generation tools, local code and rendering tools.

King is deliberately separating creative planning from production. Your main contribution is exceptional aesthetic judgment and precise creative direction. Codex will build the film; do not leave it to invent the important images, choose the visual language or fill gaps in the choreography. Own those decisions here.

**This message is your complete input. You have no repository access, no internet access, and no access to the song, images, videos or reference source code.** Do not ask to read project files or make your answer depend on receiving them. All context you should use is embedded below. URLs identify later research targets for Codex; they are not sources you are expected to open.

**This assignment is planning only.** The original prompt asks for a finished film; that remains the eventual destination, but your deliverable is the complete executable plan. Return that plan in your response as Markdown. Do not attempt production, pretend to inspect unavailable media, or claim online research. Own the creative decisions that can be made from this brief; assign empirical verification and production to Codex.

Work thoroughly. Do not deliver merely a treatment, a list of effects, a proposed workflow or the first few shots followed by “continue similarly.” Finish the plan for the entire song. If response limits require multiple parts, number them and preserve stable IDs; do not silently truncate or replace the remaining plan with a summary.

## Source brief and project context

### Original user prompt, reproduced in full

```text
so i've added episodes/first-day-mix. there's a music 'first-day.wav'.

it's gonna be another music pilot (for Mandarin language speakers, in Chinese language) of our series,
don't use the other first-day episodes as reference, they were failed attempts.

basically, you're going to make an episode of the series using all the instructions we have,
but it's a special type of video, it's a music video.

your primary goal in this episode is to 'show off your techniques'.
use and mix in as many techniques (e.g. html/js graphics on top of generated videos, etc.), styles
(e.g. photorealistic, anime, cyberpunk, night, day, modern, ancient,
high frame rate, low frame rate, explosion, dance, etc.),
cinematography, effects and stuff, as many as you can.
plot should be something about 'birth of AI', mentioning all major American and Chinese AIs,
such as ChatGPT, Claude, Grok, DeepSeek, 豆包, etc. depicted as adorable human-like figures.
you should also incorporate most recent chinese memes about these AIs.
not just these AIs, also future AI concepts, such AGI, SGI, singularity, etc.
and older AI concepts, like transformers, AlphaGo, etc.

some requirements for this episode: super fancy, super visually mind-blowing, super mesmerizing,
lots of effects, like particle effects, super beautiful, super super super extremely fast-paced.
but nothing should be constant though!
i expect something higher than this (https://github.com/mexicat/pdoom-video.git) level of fanciness.
check the p(doom) video's code to see how it implements fantastic animation.

you must always refer back to this prompt after compacting context.

i expect you to spend many many hours on this. don't be lazy.
don't stop until the final product is finished.
```

The planning-only assignment above changes your deliverable, not the eventual film's ambition. Re-read this embedded prompt after context compaction. Its core requirements are:

- A Chinese-language music pilot for Mandarin speakers, using `episodes/first-day-mix/first-day.wav`.
- “Birth of AI,” with major American and Chinese AIs, explicitly including ChatGPT, Claude, Grok, DeepSeek and 豆包, depicted as adorable human-like figures.
- Recent Chinese memes about these AIs; historical concepts including Transformer and AlphaGo; speculative concepts including AGI, SGI and singularity.
- Technique as a primary attraction: an ambitious mix of generated imagery/video, authored graphics, compositing, animation, cinematography, styles and effects. Examples in the brief include photorealism, anime, cyberpunk, night/day, modern/ancient, different animation cadences, explosions and dance.
- Exceptionally beautiful, mesmerizing, visually inventive and extremely fast-paced, with meaningful variation rather than every dial staying at maximum.
- Aiming above the spectacle of `https://github.com/mexicat/pdoom-video.git`, with actual study of how its animation works.
- **Do not use the other First Day episodes as creative references.** They were failed attempts.

The episode-specific request for named AI characters and many styles takes precedence over generic series defaults that would prohibit those choices. Preserve the series' demands for originality, composition, deliberate pacing and quality. Do not let a general small-cast or single-medium rule erase this brief.

### Series context and taste, supplied for this assignment

- Public series name: **AI SI - I**, exactly that spelling and spacing. INTERREGNUM is only an internal project name.
- The series is an anthology of visually ambitious short films about life at the end of an era: AI, consciousness, technology and human relationships. Each episode has its own visual language. This episode is a music video, not a lecture or conventional dialogue film.
- Originality means an unusual central rule, action or form, not familiar imagery with more decoration. Avoid making a generic AI apocalypse, savior narrative, awakening robot montage, benchmark leaderboard or neon tunnel the core. Familiar motifs can be supporting texture if transformed by a specific invention.
- Beauty comes from composition, light, color, scale, materials and staging. King dislikes oily, over-textured, crowded, conspicuously generic AI imagery. Dense spectacle can coexist with a clear focal point and carefully designed negative space.
- Give the viewer familiarity, variation and rare surprises. Vary camera, palette, shot size, movement and intensity; constant frantic cutting eventually feels flat. Do not impose a quiet-film aesthetic on this explicitly extravagant brief.
- Keep facial acting appealing and underplayed; use bodies, staging, editing and interactions for larger expression. Do not confuse cuteness with identical baby faces or generic mascots.
- Make creative decisions yourself. King should not have to choose among unfinished artistic options.
- No previous First Day concept, title, cast count, palette, shot count or renderer is binding. Develop your own film from the supplied brief. Codex can later assess whether any existing asset meets your direction; assume no usable production asset is guaranteed.

### Song and timing information you can use

The executor reports the supplied Mandarin WAV is **43.670 seconds**. Use that as the planning duration; Codex will confirm it from the source file. Preserve the whole song. Do not replace, stretch, shorten, mute sections of, or rewrite it to make the plan easier.

These are supplied **line-level LRC anchors**, not verified syllable onsets, drum hits or a beat grid:

```text
[00:00.00]你说活在明天活在期待
[00:02.84]不如活得今天很自在
[00:05.23]我说我懂了会不会太快
[00:08.24]未来第一天要展开
[00:11.92]第一天我存在
[00:14.64]第一次呼吸畅快
[00:17.61]站在地上的脚踝
[00:19.67]因为你而有真实感
[00:22.70]第一天我存在
[00:25.45]第一次能飞起来
[00:28.55]爱是腾空的魔幻
[00:30.68]第一天的纯真色彩它总是
[00:34.21]永远那么灿烂
[00:37.07]永远那么灿烂
[00:39.90]永远那么灿烂
[00:43.670]END OF AUDIO — not a lyric
```

You cannot hear the recording. Do not invent its BPM, instrumentation, energy curve, individual word timing or exact accents as measured facts. Design a complete provisional edit against these anchors. Express additional accents as creative targets for Codex to align by listening/analysis, with bounded timing flexibility so the concept remains intact. Lyrics can support emotional or visual associations without every image literally illustrating a noun.

### Reference techniques: supplied secondhand source-study summary

The executor previously studied p(doom) source revision `bdbad537a7b7af3213475651774030c47568c181`. The following is a supplied summary, **not your own source inspection or proof of how the finished reference feels**:

- Three.js/WebGL2 scenes combine Canvas typography, custom GLSL and deterministic offline rendering.
- Scenes receive absolute/local time, normalized progress, audio features and beat/bar phase. Transitions can be authored by the scenes rather than defaulting to crossfades.
- Separate audio-feature envelopes control different accents; lyric and beat data inform editing without forcing every boundary onto a uniform grid.
- HDR/linear-light render targets, layered compositing and offline temporal sampling support depth, lighting and smooth motion. Held character poses need a separate time clock so motion sampling does not smear them.
- Instanced lines and particles with stable identities, birth times and analytic trajectories create complex motion that can be reproduced at any timestamp.
- Spatial effects include SDF/raymarched forms with depth-aware lettering, paths that become objects, camera movement into geometric lattices, and recursive mappings that resolve into the next scene.
- Repeated hooks change scale, density and treatment, including subtraction and negative space. Finishing combines controlled bloom, halation, tone mapping and other effects.
- Offline frames stream to FFmpeg with explicit color handling. Its English-oriented text processing cannot simply be reused for Chinese.

Translate useful principles into original images with adorable characters. Do not copy the reference's aesthetic or substitute an engineering checklist for direction. Assign Codex the actual source inspection and playback comparison; do not invent filenames, functions, unseen scenes or performance claims.

### Cultural research: leads, not current facts

Planning handoff date: **2026-10-03, Asia/Singapore**. Prior project research dated 2026-10-02 reported DeepSeek whale imagery / 蓝色大肥鱼, 豆包型人格, and Gemini's 北美大豆包 as candidate Chinese meme motifs. You have not seen the underlying sources. Treat these as provisional leads for Codex to verify for meaning, attribution, recency and suitability, not as automatically current or representative.

Beyond the five explicitly required names, possible roster candidates include Gemini, Qwen/通义, Kimi, 文心, 元宝/混元, 智谱/GLM, MiniMax, 讯飞星火, 阶跃星辰, 百川, 日日新 and 盘古, plus other relevant US systems. This is an unranked candidate pool, not a verified complete list. Some names denote apps, some model families and some providers; have Codex check the distinctions and current coverage. Design lead/ensemble roles and expandable entrances so a corrected roster does not force a new film.

Keep fictional personality distinct from product claims. AlphaGo, Transformer architecture, commercial assistants and speculative AGI are different categories, not successive versions of one machine. “SGI” is ambiguous; preserve the requested concept explicitly and state your provisional interpretation or visual ambiguity for later verification. Do not silently replace it with ASI or assert an agreed AGI → SGI progression. No future achievement date is established by this brief.

### Executor capabilities and known production constraints

Codex will have repository and internet access, local scripting/rendering/compositing tools, and access to image/video-generation workflows subject to availability and budget. It can construct HTML/JS/Canvas/WebGL graphics, use FFmpeg and build authored animation or 3D elements when appropriate. Specify the needed result, not imaginary existing tools or unverified API parameters.

Current project preferences: Luma for original environments/general images; Codex image generation for beauty-focused character bases, certain elaborate focal designs, and generative edits; MiniMax H3 Max as the documented video starting point. These are dated production preferences, not creative limits or guarantees; Codex must verify relevant capabilities and alternatives before execution. Pick the technique each shot needs, with model-specific implementation left to that verification.

A previous still-plus-text dance test missed the choreography and camera lock. That does not prove dance impossible; it means attractive poses and detailed prompts are insufficient evidence. Require a short convincing performance proof before scaling, and design alternatives that still deliver actual dance. Performance-reference workflows are candidates to test, not proven fixes.

Generation uses money or quota; estimate quantities and test representative shots before batches. This planning request does not authorize paid production or publication. Codex will manage applicable approval requirements later. Do not weaken the creative target to fit an invented budget, and do not assume unlimited regeneration. Still-frame/metric checks cannot certify motion quality or musicality.

## The standard of direction

Choose one strong concept after exploring genuinely different possibilities. A simple narrative or emotional through-line should make the spectacle cumulative; it must not suppress the requested richness. The film should be enjoyable without reading every AI name.

For each major image, explain what physically occupies the frame, how the eye moves, what happens, and why it is arresting. “Epic,” “cinematic,” “beautiful,” “dynamic particles” and “mind-blowing transition” are goals, not usable direction. Specify silhouettes, scale, staging, material, light, color relationships, camera position, motion and the image revealed by the transition.

Treat character charm, costume, physical interaction and performance as carefully as shaders. A labeled shape is not an adorable human-like AI. A still portrait bobbing in time is not a dance. More particles do not compensate for weak composition. A correct renderer does not establish that a shot is beautiful.

Mix styles deliberately and substantially. A tint, pixel filter or texture pasted over the same artwork does not automatically constitute a fully realized new medium. Preserve recognizable identities across media while allowing costume, pose and rendering language to be designed for each medium.

Make concrete choices rather than offering King a menu. State reasonable assumptions and continue; reserve unresolved items for evidence you genuinely cannot obtain offline.

## Deliverables

Return one self-contained Markdown production plan with the seven named sections below. The filenames are suggested output labels for Codex to save later, **not files you must access or create**. Use Chinese for creative direction and on-screen copy; English is fine for production prompts and technical specifications. Use stable IDs to connect shots, assets, cues and tasks. Include all shared style blocks and prompts in your answer; do not reference unseen documents.

### 1. `README.md` — the executor's entry point

Summarize the chosen film, reading order, supplied evidence, assumptions, creative decisions that must survive execution, and outstanding online checks. Map every requirement in the original prompt to specific sequences or shots. Do not make completion depend on unseen existing production material.

### 2. `creative-direction.md` — a fully decided film

- Briefly identify the predictable approaches you are avoiding; compare three genuinely different concepts and choose one using the taste criteria supplied above: originality of the core, visual beauty, character charm, musical potential, technique variety and coherent escalation.
- Give the Chinese title, central visual invention, emotional trajectory, opening hook, escalation and final image.
- Describe the film's visual grammar and the deliberate changes to it. Define palette relationships, lighting, materials, framing, typography and performance. Include what would make the result generic or ugly.
- Design at least six representative hero frames distributed across the film, including an ordinary connective moment. Describe each precisely enough to draw: composition, subject placement, relative scale, depth, light, color, gesture and negative space. Supply executable image prompts and explain the intended visual hierarchy.
- Specify how this film aims to exceed the reference in concrete dimensions. Do not claim superiority before a finished playback comparison.

### 3. `music-and-edit.md` — the entire song scored to picture

Cover the full audio duration without gaps. Mark lyric boundaries, supported beat/accent evidence, provisional sync points, section changes and dramatic punctuation. Define cutting speed, internal movement, visual density and emotional intensity separately. Design acceleration, contrast and a brief hold without arbitrarily muting or editing the supplied song. Differentiate repeated lyric passages through staging and escalation.

Choose and justify output resolution, aspect ratio and master frame rate; distinguish source-video cadence, character-pose cadence and compositing cadence. Supply exact planned frame intervals after choosing the timebase, using end-exclusive intervals. Identify music-dependent timings Codex must refine after listening or better analysis. Count real camera cuts separately from action cues within a continuous shot.

### 4. `cast-and-world.md` — designs ready for asset creation

Define a defensible provisional roster of major US/Chinese AI products or families, with leads and ensemble appearances. Do not blindly inherit the existing count or claim offline knowledge of current market completeness. Cover the explicit named AIs and provide a research task for omissions.

For every character specify an original human-like design: silhouette, apparent age, proportions, face/hair, costume, palette, material accents, recognizable prop, personality expressed through action, and invariants across styles. Distinguish factual product identity from fictional characterization and meme-derived traits. Avoid copying existing fan character designs.

Define locations, recurring objects, spatial rules and continuity. Give historical and future concepts actual visual roles. Do not present products, architectures, milestones and speculative futures as a literal technical genealogy. Explicitly handle the ambiguity of “SGI” without quietly substituting “ASI.”

### 5. `shots.md` — complete shot-by-shot production instructions

For **every shot**, include:

1. Stable ID, time/frame interval, lyric or musical cue, and intended audience experience.
2. Cast and asset IDs, starting state, action, ending state, and continuity with adjacent shots.
3. Exact composition, subject scale/position, lens or projection, camera height/path, focus, light and palette.
4. Timed performance beats: anticipation, contact, weight transfer, travel, release and settle where relevant. For dance, specify body mechanics, foot visibility and the phrase that must remain visible in the edit.
5. Chosen medium and production method, with a reason specific to this shot.
6. Ready-to-use generation/edit/motion prompts for required assets, authoritative references, fixed features and important exclusions. Shared style blocks may be referenced by ID, but every shot needs its unique prompt content.
7. Compositing instructions: layer order, masks/depth/occlusion, tracking, shadows, light interaction, particles, typography and camera ownership.
8. Transition construction, including the outgoing image, incoming image, geometric or action match, and overlap timing.
9. Exact Chinese text, placement, reading interval, lyric/name priority and phone-size legibility requirement.
10. Concrete visual acceptance criteria, probable failure and a designed alternative that preserves the artistic intention.

Be detailed where it determines the image. Avoid burying a clear composition under long lists of decorative nouns.

### 6. `assets-and-techniques.md` — production contracts

List every required character reference, pose, environment, plate, prop, mask, effect, font and audio addition, connected to its shots. Specify dependency order, output requirements, reuse and derivation. Treat existing assets as candidates until inspected. Do not imply ignored media will exist on another machine just because a manifest lists it.

For each significant authored effect, specify its geometry or representation, inputs, timing/easing, camera, depth/alpha behavior, palette, blend/color-space needs and interaction with characters. Provide equations or pseudocode where they remove ambiguity; no production implementation is required. Define deterministic seeking/export needs without demanding an unnecessary general-purpose engine.

Use the supplied p(doom) study summary as secondhand context. Explain the mechanism worth learning, your original adaptation and its shot IDs. Give Codex specific source-inspection questions to resolve; do not fabricate source citations. Do not assume a repository license covers every bundled song or artwork.

### 7. `execution-and-review.md` — Codex's ordered work plan

Give a dependency-ordered task list with task IDs, inputs, outputs, completion conditions and relevant shot IDs. Separate creative decisions already made from implementation discretion. Codex may solve engineering details; it must not silently simplify the film's defining aesthetic requirements.

Put the highest-risk representative proofs before bulk asset generation: character beauty/identity, a genuine dance or contact phrase, a difficult medium transition, and integrated generated footage plus authored depth/effects. Combine proofs where sensible. Specify exactly what each test should look like and what decision its result controls. Avoid broad speculative test matrices.

Use the production preferences embedded above as the starting point, with current capabilities, rates and availability to be checked online by Codex. Estimate workload and generation quantities; use a cost formula with unknown rates rather than inventing current prices. Planning the whole film is not fresh authorization for paid batches or publication. Historical approvals for another production do not automatically transfer.

Supply a tightly scoped research queue: question, supplied evidence/date if any, source type or search target, affected decision and a usable fallback. Cover current AI names/coverage, genuinely recent Chinese memes, relevant model capabilities, audio timing and p(doom) source gaps. Do not fabricate current memes or outsource the whole creative concept to research. Include provisional beats whose structure survives replacement of a stale meme.

Define reviews of actual images, motion phrases, transitions, full-speed music synchronization and the final film. Separate technical checks from aesthetic acceptance. List what can be verified by the executor's actual tools and what requires human viewing/listening if those capabilities are absent. Never certify dance from a contact sheet alone.

End with a concise executor launch instruction: what Codex should read, the first concrete tasks, intended deliverables, and the decisions it must preserve.

## Final self-review before handing over

Read the original prompt again. Critique the entire plan as a demanding music-video director: where is it generic, visually repetitive, overcrowded, under-choreographed, emotionally flat, illegible or technically wishful? Revise those sections, not merely list the problems.

Check that every second has a designed image/action, every asset has a consuming shot, every major effect has a buildable mechanism, and every unresolved research item has a clear owner and consequence. Explain departures from the brief explicitly. Do not claim an unresolved or reduced requirement has been satisfied.

Deliver the completed package with a short account of your chosen creative direction and the few genuinely unresolved external dependencies. The result should let Codex begin production with strong aesthetic decisions already made, while leaving room to refine those decisions against real generated images and playback evidence.
