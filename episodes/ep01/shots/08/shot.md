# COMMON ROOM / 一室两家 — shot 08

**Series:** AI SI - I. **Section:** division. **Frames:** [888, 1056) at 24 fps. **Timecode:** 00:37:00–00:44:00. **Duration:** 7 seconds.

**Selected plate:** k07 → `work/ep01/paper/k07.png`. **Actual method:** Authored paper graphics on photographic ash-table plate. **Type:** graphic.

**Recipe:** `episodes/ep01/build/paper_graphics.py` — photographic base `ref_paper` with exact authored paper layers.

**Selected SHA-256:** `be83b011305077d093812033f0968c5886645b241628b8cd287fb03ed21b78ed`.

**Original plan:** Luma original photographic composition (`t2i`); historical output target `work/ep01/keys/k07.png`. The preserved original prompt below records that plan and is not a claim that the selected file came from that original request.

**Exact selected states:**

- Local frame 0: `work/ep01/paper/k07.png` — SHA-256 `be83b011305077d093812033f0968c5886645b241628b8cd287fb03ed21b78ed`.
- Local frame 72: `work/ep01/paper/k07_after.png` — SHA-256 `ae42b83255db70a3514d4201dded50442845ecf775537b24b43b70eb52ccf99a`.

**Camera/coverage:** Straight overhead 65 mm, authored plan insert with real paper texture. Lens values in inherited plans describe intended coverage, not measured photographic metadata.

## Script and sound

Overhead plan of the real apartment, two houseletters beside it. Long private room at Eda’s left address, narrow private room at Sen’s right. Kitchen appears exactly once between their tabs.

Selected state: Replace the exact room-allocation paper state at local frame 72, placing Eda’s long-room token in her separate houseletter.

**D05 · EDA · authored cue +0.55s:** I'll take the long room. The cutting table fits.
**ZH:** 长的那间归我。放得下裁剪台。

Sound: Recorded paper scrape beneath Eda off screen; a very sparse performed instrumental figure may enter.

## Original planned prompt — preserved verbatim

```text
New original photographic live-action cinema composition, landscape16:9. Use the supplied references for exact identities, garments, set and object designs while creating the specified new framing. Ordinary adult domestic comedy; dry natural surfaces, motivated daylight, clear moderate depth. Physical plate recipe ONLY for the room-allocation insert; root will author the entire exact diagram and movable tokens. Straight overhead65mm onto the same ash table. One LARGE rectangular blank off-white sheet lies completely flat in the centre; two pale folded blank houseletter enclosures sit separately at left and right, one with a small blue edge and one with a small clay edge. The broad central sheet has an uninterrupted flat field suited to an exact single-kitchen drawing. No hands obscure any paper face. Keep gentle real paper shadows and physically consistent size. No generated writing, map, duplicate room icons or decorative seals. Right-side kitchen daylight.
```

## Actual authored recipe

`episodes/ep01/build/paper_graphics.py` renders the physical paper design on `ref_paper`; `episodes/ep01/build/paper_states.json` supplies the exact frame of each before/after replacement. No generated typography is used.

## Planned future motion — preparation only

No video-model motion. Root moves the exact private-room token on an authored paper layer; one kitchen remains undivided. Eda’s voice is intentionally off screen.

If dialogue is on-screen, preserve only the named speaker’s visible mouth and use the approved separate voice take for lip sync. If the speaker is off screen in this insert, do not invent a visible speaker. Motion generation is outside the current production stage.

## Static acceptance and essential checks

- Status: selected static continuity approval, as registered by root in `episodes/ep01/build/selected_assets.json` and the final composite review. No generated motion, lip-sync or perceptual-audio approval is implied.
- Exact authored room-allocation state change at local frame 72. Two private rooms stay separate and the kitchen appears only once.
- Preserve Eda/left and Sen/right, sink/left and hob/right wherever kitchen geography is visible.
- The selected pose above takes precedence over obsolete start-state directions in the historical original prompt.
