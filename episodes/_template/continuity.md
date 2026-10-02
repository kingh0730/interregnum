# Scene continuity — <episode>

Use this record for intended continuous physical scenes. Track recurring people and story-relevant props, not every
background detail. Stable entity IDs persist across cameras and asset versions. A state is what exists in the scene;
visibility is what a particular camera can see. Detailed rules: `docs/playbook.md` §3.

## Scene <ID>

**Location reference / axes:** <approved set source; positions described relative to fixed landmarks>
**Continuity scope:** <time/place covered; explicit boundaries or story-supported transformations>

| Entity ID | Identity / prop design | Starting position | Count / condition |
|---|---|---|---|
| <ID> | <reference> | <set-relative position> | <held by whom, contents, open/closed, etc.> |

| State change | Shot occurrence | Before → after | Story basis |
|---|---|---|---|
| <state IDs> | <shot ID> | <only the changed facts; other facts persist> | <shown action / ordinary implied move / ellipse / montage / transformation> |

Implied moves and deliberate discontinuities are valid; record the basis where continuity depends on them. This
does not require showing every movement, preserving literal physics in a transformation, or choosing a fixed shot style.

## Occurrence and cut review

| Shot occurrence / neighbors | Selected source version and crop | State in → out | Actual spatial finding | Status |
|---|---|---|---|---|
| <previous → this → next> | <path/hash or version; final crop> | <state IDs> | <visible occupants/props; evidence for exclusions or occlusions; cut compatibility> | <approved / pending / stale> |

Inspect actual frames in edit order. Include every occurrence of a reused source: unique-asset contact sheets are
insufficient. A speaker change does not remove a listener. If a frame exposes an entity's established position,
retain it or explain the state change; "offscreen" text alone does not establish exclusion.

## Approval record

**Technical evidence:** <files, hashes, frame counts, timing and render checks>
**Spatial evidence:** <actual reviewed cut sequence/version, findings and unresolved issues>
**Machine-readable review:** <review path bound to story, asset map, current source hashes and any state/framing plans>
**Review scope:** <stills / actual motion cuts; perceptual audio separately; do not infer an unperformed review>

Keep technical and spatial results separate. Source, crop, state or order changes make affected spatial approvals
stale; recheck changed occurrences and their incoming/outgoing cuts, including all uses of a changed shared source
and dependent states. Record every adjacent cut and within-shot authored state switch in the machine-readable
review. New motion manifests declare its path as `continuity_review`. See `python3 tools/continuity.py --help` for
the current CLI. The gate checks completeness and freshness of recorded findings, not geometry; these planning
notes alone do not constitute visual approval.
