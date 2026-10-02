# COMMON ROOM / 一室两家 — shot 05

**Series:** AI SI - I. **Section:** opening. **Frames:** [480, 600) at 24 fps. **Timecode:** 00:20:00–00:25:00. **Duration:** 5 seconds.

**Selected plate:** k05 → `work/ep01/keys/k05_fix.png`. **Actual method:** Codex built-in image edit of approved photographic sources. **Type:** scene.

**Recipe:** `episodes/ep01/build/codex_edits.json` — edit `k05_fix`, immediate base `k05`.

**Selected SHA-256:** `63bb24ff065ded1f1a711151986ddab9677f7f03eb962247b2c7f8076e11bb37`.

**Original plan:** Luma original photographic composition (`t2i`); historical output target `work/ep01/keys/k05.png`. The preserved original prompt below records that plan and is not a claim that the selected file came from that original request.

**Camera/coverage:** Eda medium, 50 mm, height 1.35 m from SOUTH; face left of center, gaze screen right/down. Lens values in inherited plans describe intended coverage, not measured photographic metadata.

## Script and sound

Eda in the selected LEFT table medium; both hands rest on the ash tabletop. The ring-bedroom is behind her LEFT shoulder and the rainy landing remains RIGHT. The empty bowl sits beyond the foreground crop.

Selected state: Hold the selected composed Eda pose for her line; no bowl movement is shown.

**D02 · EDA · authored cue +0.80s:** That's still my side.
**ZH:** 那边还是我的。

Sound: Eda at normal low conversational volume; continuous kitchen bed.

## Original planned prompt — preserved verbatim

```json
"New original photographic live-action cinema composition, landscape16:9. Use the supplied references for exact identities, garments, set and object designs while creating the specified new framing. Ordinary adult domestic comedy; dry natural surfaces, motivated daylight, clear moderate depth. Preserve the referenced kitchen: two rear doors flank one continuous pale worktop, Eda doorLEFT, Sen doorRIGHT, deep sinkLEFT, hobRIGHT, ash table foreground, one slightly crooked pale-yellow lamp over the TABLE. Daylight enters from camera-right. Neutral dialogue START used across several Eda exchanges.50mm at1.35m from the south, waist-up Eda left of centre at the left side of the ash table. Her hands rest naturally on the unobstructed table edge; no tool, fruit or bowl must be frozen in her hands. The LEFT ring-bedroom doorway is a recognizable narrow background depth; a glimpse of the left sink establishes orientation. She looks slightly down and screenRIGHT toward Sen’s position, not into camera. Sen’s face and body stay outside the crop. Her exact reference face, dark bob and ink-blue overshirt remain unchanged. Composed ordinary face, mouth closed at the speaking start, lips unobstructed, both eyes and the complete hand/action target visible. "
```

## Executed selected edit — preserved verbatim

Entry `k05_fix` in `episodes/ep01/build/codex_edits.json`; immediate base `k05`.

```text
Edit the FIRST image (k05 kitchen shot) into a clean approved film starting frame, using the SECOND image as Eda's exact identity and age reference. Preserve the camera framing, kitchen geometry, table, both hands and costume of the first image. Correct only these compatible details: (1) Eda is the ordinary 42-year-old woman from the second portrait. Restore that exact softer fuller face, relaxed closed lips and clear even skin. The shot currently adds 20 years, heavy lines and rough dark patches; remove that added weathering while keeping her real reference age, not glamour or idealized beauty. She looks slightly down to screen right. (2) Through the LEFT doorway, behind Eda, the bedroom has a far window clearly revealing an enormous RED PLANETARY RING against a dark red-grey sky. It must visibly be an ordinary bedroom with a real floor, bed and far window; no glowing portal, no open space at the threshold. Preserve the ash doorway and entire kitchen outside it. Right doorway remains the same grey rainy covered landing. Photographic live-action film, natural daylight, neutral restrained expression. Preserve all furniture proportions and exact door positions. Keep the exact age and clear, even skin from the identity reference: add no blemishes, spots, weathering or extra lines. Landscape16:9.
```

Actual referenced source files:

- `work/ep01/keys/k05.png`.
- `work/ep01/refs/ref_eda.png`.

## Planned future motion — preparation only

Eda speaks the locked line while looking at the bowl below frame; hands remain on the table. No exaggerated grievance or camera drift.

If dialogue is on-screen, preserve only the named speaker’s visible mouth and use the approved separate voice take for lip sync. If the speaker is off screen in this insert, do not invent a visible speaker. Motion generation is outside the current production stage.

## Static acceptance and essential checks

- Status: selected static continuity approval, as registered by root in `episodes/ep01/build/selected_assets.json` and the final composite review. No generated motion, lip-sync or perceptual-audio approval is implied.
- Her complaint concerns the same object, not a vanished object or a failed door.
- Preserve Eda/left and Sen/right, sink/left and hob/right wherever kitchen geography is visible.
- The selected pose above takes precedence over obsolete start-state directions in the historical original prompt.
