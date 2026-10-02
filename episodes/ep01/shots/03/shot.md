# COMMON ROOM / 一室两家 — shot 03

**Series:** AI SI - I. **Section:** opening. **Frames:** [240, 360) at 24 fps. **Timecode:** 00:10:00–00:15:00. **Duration:** 5 seconds.

**Selected plate:** k03 → `work/ep01/keys/k03_fix.png`. **Actual method:** Codex built-in image edit of approved photographic sources. **Type:** scene.

**Recipe:** `episodes/ep01/build/codex_edits.json` — edit `k03_fix`, immediate base `k03_edit`.

**Selected SHA-256:** `7f65cba151b24f6eb779b4306cc55921b150f2a0561c191e0da4e52c842e3c1b`.

**Original plan:** Luma original photographic composition (`t2i`); historical output target `work/ep01/keys/k03.png`. The preserved original prompt below records that plan and is not a claim that the selected file came from that original request.

**Camera/coverage:** Kitchen side of Eda’s LEFT doorway, 40 mm, height 1.35 m; established axis preserved. Lens values in inherited plans describe intended coverage, not measured photographic metadata.

## Script and sound

Eda stands within the unchanged LEFT doorway, wearing the established dark charcoal trousers and ink-blue overshirt. The ordinary bedroom beyond has its wide dark-framed window above the bed, now showing the huge red ringed planet. Her empty hand extends toward the kitchen.

Selected state: Hold Eda’s doorway return pose and extended empty hand during her line; the readdressed bedroom is already visible.

**D01 · EDA · authored cue +0.50s:** Leave the bowl there. I'll be back for it.
**ZH:** 碗先放着。我一会儿回来拿。

Sound: The new room’s dry air becomes faintly audible at left; rain persists at right. Eda speaks plainly.

## Original planned prompt — preserved verbatim

```json
"Eda is EXACTLY42, matching the supplied Eda identity reference: same face proportions, full cheeks, jaw-length dark bob and clear even skin. Add no extra wrinkles, spots, age lines, gauntness or weathering. Show only the body parts requested by this framing; do not add a face to a hands-only insert. Kitchen AFTER-address state: the unchanged LEFT doorway leads to an ordinary real room whose far window visibly frames a HUGE RED PLANETARY RING. If that doorway is in this crop, preserve this view, never packed cartons. Do not move a doorway into a crop where it does not belong. New original photographic live-action cinema composition, landscape16:9. Use the supplied references for exact identities, garments, set and object designs while creating the specified new framing. Ordinary adult domestic comedy; dry natural surfaces, motivated daylight, clear moderate depth. Preserve the referenced kitchen: two rear doors flank one continuous pale worktop, Eda doorLEFT, Sen doorRIGHT, deep sinkLEFT, hobRIGHT, ash table foreground, one slightly crooked pale-yellow lamp over the TABLE. Daylight enters from camera-right. RESULT STATE after changing Eda’s address. Camera inside the kitchen,40mm at1.35m, frames the unchanged LEFT ash doorway and a small fixed strip of kitchen table at lower right. Through the door is Eda’s ordinary long private bedroom, real safe floor and a large distant window beneath a huge red planetary ring. Eda stands just on the room side of that threshold, three-quarter front, facing the kitchen; she has an empty hand ready to return toward the table. Her face, mouth, whole empty hand, doorway jamb and floor threshold are visible. She is the ONLY visible face. Preserve the frame and nearby kitchen surfaces exactly; the red ring is beyond a real window, without portal glow. Composed ordinary face, mouth closed at the speaking start, lips unobstructed, both eyes and the complete hand/action target visible. "
```

## Executed selected edit — preserved verbatim

Entry `k03_fix` in `episodes/ep01/build/codex_edits.json`; immediate base `k03_edit`.

```text
Make ONE narrow costume correction to FIRST image. Eda's trousers must match SECOND approved wardrobe reference: DARK CHARCOAL tailored straight-leg trousers with a plain flat waistband. Replace the incorrect light-grey gathered elastic-waist trousers in image1. Preserve everything else EXACTLY: face and skin42, hair, blue overshirt/bone shirt, hand pose, frame, door, bed, window, red planet, sink, all lighting and all pixels outside trouser region as closely as possible. Do not reframe or alter her face. Natural photographic16:9. Keep exact clear even skin; add no blemishes, spots, weathering or extra lines.
```

Actual referenced source files:

- `work/ep01/keys/k03_edit.png`.
- `work/ep01/keys/k01_edit.png`.

## Planned future motion — preparation only

One visible speaker, Eda. After her line she shifts her empty hand toward the kitchen. Keep her planted at the real threshold; the following insert supplies the reached-bowl result. No portal movement or room morph.

If dialogue is on-screen, preserve only the named speaker’s visible mouth and use the approved separate voice take for lip sync. If the speaker is off screen in this insert, do not invent a visible speaker. Motion generation is outside the current production stage.

## Static acceptance and essential checks

- Status: selected static continuity approval, as registered by root in `episodes/ep01/build/selected_assets.json` and the final composite review. No generated motion, lip-sync or perceptual-audio approval is implied.
- Exact match-cut doorway replacement teaches a changed address. Eda is a living person returning through an ordinary threshold.
- Preserve Eda/left and Sen/right, sink/left and hob/right wherever kitchen geography is visible.
- The selected pose above takes precedence over obsolete start-state directions in the historical original prompt.
