# COMMON ROOM / 一室两家 — shot 01

**Series:** AI SI - I. **Section:** opening. **Frames:** [0, 144) at 24 fps. **Timecode:** 00:00:00–00:06:00. **Duration:** 6 seconds.

**Selected plate:** k01 → `work/ep01/keys/k01_edit.png`. **Actual method:** Codex built-in image edit of approved photographic sources. **Type:** scene.

**Recipe:** `episodes/ep01/build/codex_edits.json` — edit `k01_edit`, immediate base `ref_kitchen`.

**Selected SHA-256:** `cf1d7361790552336051a0dae2b9c3618b2fe05a0b832f597e12cc86aa24161c`.

**Original plan:** Luma original photographic composition (`t2i`); historical output target `work/ep01/keys/k01.png`. The preserved original prompt below records that plan and is not a claim that the selected file came from that original request.

**Camera/coverage:** Guest eye from SOUTH slightly east of center, 32 mm, height 1.35 m, stable wide; Eda left / Sen right. Lens values in inherited plans describe intended coverage, not measured photographic metadata.

## Script and sound

The shared kitchen in its opening packed-room state. Eda stands LEFT over two open houseletters; Sen stands RIGHT beside the ash table. The left doorway shows stacked cartons in her old room; the right doorway shows his rainy landing. The single blue bowl with one crooked white stripe holds one cherry.

Selected state: Hold the reviewed opening pose: paper under Eda’s hands, Sen beside the bowl, one cherry visible.

Sound: Continuous kitchen air; faint rain beyond right door; dry paper contact. No score.

## Original planned prompt — preserved verbatim

```text
New original photographic live-action cinema composition, landscape16:9. Use the supplied references for exact identities, garments, set and object designs while creating the specified new framing. Ordinary adult domestic comedy; dry natural surfaces, motivated daylight, clear moderate depth. Preserve the referenced kitchen: two rear doors flank one continuous pale worktop, Eda doorLEFT, Sen doorRIGHT, deep sinkLEFT, hobRIGHT, ash table foreground, one slightly crooked pale-yellow lamp over the TABLE. Daylight enters from camera-right. START STATE. Wide32mm from1.35m, south side slightly right of centre; see the whole table top and both full doorframes. Eda stands left of the table, Sen right; their heads sit in the upper half, with waists and hands readable, rather than faces cropped along the bottom. Eda wears her ink-blue overshirt; Sen his clay shirt. LEFT door shows her ordinary packed old bedroom, without planetary ring. RIGHT door shows his sheltered rain-dark vestibule. Two pale blank folded houseletters lie on the table. Exactly ONE shallow BLUE bowl with ONE crooked WHITE stripe faces camera and holds exactly ONE dark-red cherry. Eda places her blue-edged address slip beside her houseletter; Sen watches the bowl. Their faces are restrained, mouths closed. Clear floor routes, only the established useful furniture.
```

## Executed selected edit — preserved verbatim

Entry `k01_edit` in `episodes/ep01/build/codex_edits.json`; immediate base `ref_kitchen`.

```text
Edit the FIRST photograph of the empty kitchen. Preserve its camera, architecture, door positions, furniture and lighting exactly, filling it with two people from the identity portraits. Eda (SECOND reference), age42, stands to LEFT of the foreground table. Sen (THIRD reference), age44, stands to RIGHT, facing her. Both visible from head to hips; full heads, relaxed closed mouths, both hands clearly in frame. Eda wears ink-blue overshirt, bone crewneck and charcoal trousers. Sen wears clay cotton shirt and dark olive trousers. Two open folded off-white paper houseletters rest at center of table with blank paper surfaces and ink-blue/clay edging, no tiny invented lettering. Eda's fingertips rest beside one narrow blue-edged paper tab. At the NEAR edge of the table, closer to camera, put exactly ONE cobalt-blue bowl from FOURTH reference with its ONE crooked WHITE stripe and exactly ONE dark red cherry. Sen watches that bowl. Preserve the left doorway's packed old room without planetary ring, and the right rainy covered landing. Keep one sinkLEFT and one hobRIGHT along the one continuous back counter, two ash shelves, and one yellow pendant over the table. Photographic ordinary domestic cinema. Keep both exact reference faces and their clear even skin, same age42/44: add no blemishes, dark spots, weathering or extra lines. No panel layout or border. Landscape16:9.
```

Actual referenced source files:

- `work/ep01/refs/ref_kitchen.png`.
- `work/ep01/refs/ref_eda.png`.
- `work/ep01/refs/ref_sen.png`.
- `work/ep01/refs/ref_props.png`.

## Planned future motion — preparation only

Hold the camera. Eda places the single blue-edged slip beside her houseletter once, then leaves her hands still. Sen remains still beside the one bowl. Do not animate any room or door destination here.

If dialogue is on-screen, preserve only the named speaker’s visible mouth and use the approved separate voice take for lip sync. If the speaker is off screen in this insert, do not invent a visible speaker. Motion generation is outside the current production stage.

## Static acceptance and essential checks

- Status: selected static continuity approval, as registered by root in `episodes/ep01/build/selected_assets.json` and the final composite review. No generated motion, lip-sync or perceptual-audio approval is implied.
- Establish one kitchen, two fixed thresholds, one identifiable bowl. No opening title or branding overlay; the only title card is shot 40.
- Preserve Eda/left and Sen/right, sink/left and hob/right wherever kitchen geography is visible.
- The selected pose above takes precedence over obsolete start-state directions in the historical original prompt.
