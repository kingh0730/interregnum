# Shot <NN>

**Duration:** <s>  **Tool:** <video model | Blender | JS | comp>  **Camera:** <move, lens>
**Action:** <what happens, acting beats and timing>
**Keyframe prompt:** <original/edit prompt, with actual reference IDs and source files>
**Motion prompt:** <video model prompt>
**Takes:** <take number: model, seed, notes. The winner is marked>

## Scene state and visibility

**Scene / occurrence:** <scene ID and this shot's occurrence in the edit>
**State in → out:** <state IDs in continuity.md; people positions and prop counts/conditions that persist or change>
**Change basis:** <shown action, ordinary implied move, ellipse, montage or transformation; story reason if relevant>
**Actual camera/crop:** <set-relative viewpoint, visible area and any final crop>

| Entity ID | Established position / state | Visibility in actual selected frame | Evidence or permitted change |
|---|---|---|---|
| <person/prop> | <position; count/condition> | <visible / occluded / outside view> | <visible landmark or named occluder; do not infer absence from the prompt> |

One speaker does not mean one person. An absent entity cannot leave its established, still-visible position empty
without a story-supported change. Framing style is free; its spatial explanation must fit the actual image.

## Selected source and review

**Selected source / recipe:** <path, source version or hash, actual generation/edit method and recipe>
**Reuse:** <all occurrences of this source; state compatibility checked separately at each use>
**Technical validation:** <evidence / pending issues>
**Spatial review:** <actual incoming and outgoing cut comparisons, including reused neighbors; finding and reviewed versions/crops>
**Status:** <approved / pending / stale; motion and perceptual audio status separately>

Changing the source, crop, state or edit order invalidates affected spatial review. Recheck the changed occurrence
and both neighboring cuts, plus dependent states; a shared-source change affects every occurrence that uses it.

## Dialogue performance review (when applicable)

**Intended speaker / visible listeners:** <entity IDs; speaker label is not an H3 face-selection control>
**Audio and take:** <exact input audio version/hash, selected video version/hash, line interval and final source trim>
**Speaker assignment:** <who actually makes speech-like mouth movements; observations/timestamps and status>
**Sync to our audio:** <onset, articulation and ending in audiovisual playback; pending if not reviewed>
**Listener behavior:** <each visible listener during the line and surrounding silence; distinguish natural reactions from fake-talking>
**Review scope / result:** <full take and retained final cut; actual method, reviewer, approved / blocked / pending>

Frame samples alone do not approve exact sync. Recheck after a take, audio-alignment or trim change. If performance
fails, retake within budget or revise camera coverage while preserving occupants, props and adjacent-cut continuity.
