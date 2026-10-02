# COMMON ROOM / 一室两家 — look-development tests

Six independent no-reference Luma originals compare full media, not cosmetic grades. The runner must use the repository root because every output path is repository-relative. All six prompts explicitly name lens, height, primary subject, light source and space. No generation was submitted by the art-direction agent. Root owns generation and has approved A after reviewing all six.

Generate `style_A_room` first, inspect it, then the remaining five. The first item is unchanged from the initial saved version. None of these tests becomes a face master by default.

## style_A_room

Output: `work/ep01/lookdev/style_A_room.png`. Mode: t2i. Aspect:16:9. Refs/deps: none.

Photographic live-action frame, restrained adult speculative comedy, 16:9. A generous ordinary kitchen seen on a 32mm lens from 1.35m high, slightly right of its centre. First read: two adults facing one another across a plain ash table, both three-quarter faces clearly visible. Eda, East Asian woman 42 with compact straight dark bob, in an ink-blue cotton overshirt; Sen, Black man 44 with short tightly curled hair, in a muted clay cotton shirt. They look their ages, ordinary faces with clear even skin, mouths closed, no smile or dramatic expression. A long pale worktop runs along the rear wall between two separate full-height doorways: deep sink at its left end, small hob at its right. Left doorway opens onto a pale bedroom beneath a vast red planetary ring; right doorway opens onto a rain-dark exterior landing. A plain pale-yellow hanging lamp is slightly crooked above the table. One high window off camera right lights faces and tabletop; door worlds remain secondary. Chalk walls, ash wood, restrained mineral colours, clear spatial depth and quiet empty wall. Dry natural surfaces, no gloss or theatrical glow. The room and people feel physically built; the impossible part is only what lies through the doors.

## style_A_scale

Output: `work/ep01/lookdev/style_A_scale.png`. Mode: t2i. Aspect:16:9. Refs/deps: none.

Photographic live-action frame, 16:9. A vast postal sorting hall contains upright apartment-building sections stored like thick folded letters, pale facades alternating with plain backing boards. The architecture is physically convincing and exceptionally spacious. One tall narrow gap between building sections is the focal point. A solitary East Asian woman aged 42 with a compact straight dark bob and ink-blue cotton overshirt stands in the lower right foreground holding a pale folded houseletter; her composed three-quarter face is visible, her clear even skin ordinary. 24mm lens from 0.95m height. A low dark balustrade makes a foreground edge, the woman anchors scale, monumental pale piers recede into empty height. Daylight through high clerestory slots makes clean shapes on a dark stone floor; no glow or haze. Sparse chalk, ash and blue-grey palette. No crowds, tiny decorative machinery, text, logos or holographic interfaces. Magnitude and negative space carry the spectacle.

## style_B_room

Output: `work/ep01/lookdev/style_B_room.png`. Mode: t2i. Aspect:16:9. Refs/deps: none.

Fully flat hand-drawn 2D cinema, 16:9; matte solid colour shapes and charcoal-dark contours, two or three value steps, adult human proportions. No gradients, reflections, painted grain, 3D rendering or paper border. A generous kitchen seen as a 32mm lens from 1.35m high, slightly right of centre. First read: an East Asian woman 42 with compact straight dark bob and ink-blue overshirt, and a Black man 44 with short tightly curled hair and muted clay shirt, facing each other across a plain ash table; both three-quarter faces visible, ordinary clear skin, small dark eyes without highlights, mouths closed. Rear wall: long pale worktop with deep sink at left and small hob at right, BETWEEN two full-height doors. Left door shows a bedroom and distant vast red planetary ring; right door shows a rain-dark landing. One pale-yellow crooked hanging lamp above the table. Window light from offscreen right creates broad warm ivory and blue-grey shapes. One clear spatial hierarchy, empty wall, restrained adult domestic comedy, no cute expressions or extra props.

## style_B_scale

Output: `work/ep01/lookdev/style_B_scale.png`. Mode: t2i. Aspect:16:9. Refs/deps: none.

Fully flat hand-drawn 2D cinema, 16:9. Matte solid ivory, blue-grey and blue-black shapes with charcoal-dark contours; two or three values, no gradients, reflections, painted grain, 3D render or paper border. Monumental postal hall: tall apartment-building sections stand upright in deep racks like thick folded letters. One clean narrow absence between sections is the focus. Broad piers and near-empty upper frame create tremendous scale. A solitary East Asian woman 42, compact straight dark bob, ink-blue overshirt, in lower right foreground holds one folded houseletter; her adult three-quarter face is visible, small dark eyes, mouth closed. Perspective of a 24mm lens from 0.95m high, low balustrade in foreground, woman in middle plane, high clerestory light beyond. Window daylight makes hard cream shapes on the dark floor. Figures and architecture share the same flat graphic medium. No crowds, signs or decorative clutter.

## style_C_room

Output: `work/ep01/lookdev/style_C_room.png`. Mode: t2i. Aspect:16:9. Refs/deps: none.

Photographed stop-motion miniature cinema, 16:9. Paperboard sets, matte painted wooden ADULT puppets and plain woven clothes, all one coherent constructed scale. Simple clear faces, no live-action skin, glossy toys, felt fuzz, visible joints or cute expressions. A generous kitchen photographed at its inhabitants eye level, 32mm-equivalent lens, camera 1.35m-equivalent high slightly right of centre, generous depth of field. An East Asian woman 42 with compact straight dark bob in ink-blue overshirt and a Black man 44 with short tightly curled hair in muted clay shirt face each other across a plain ash table; both three-quarter faces visible, mouths closed. Long rear pale worktop, deep sink left and hob right, BETWEEN two full-height doorways. Left opens onto a bedroom and a vast red planetary ring as a distant practical backdrop; right onto rain-dark landing. Crooked pale-yellow hanging lamp over table. One practical miniature window off camera right lights the figures and table; chalk walls recede into quiet shadow. Restrained adult domestic comedy with real room volume, not an overhead dollhouse.

## style_C_scale

Output: `work/ep01/lookdev/style_C_scale.png`. Mode: t2i. Aspect:16:9. Refs/deps: none.

Photographed stop-motion miniature cinema, 16:9. A monumental postal hall built from paperboard and painted timber: apartment-building sections stand upright like thick folded letters in deep architectural racks. Matte surfaces, simple confident forms, no decorative craft clutter. One narrow missing building section is the focal absence. A solitary matte wooden adult puppet of an East Asian woman 42, compact dark bob, ink-blue woven overshirt, stands lower right holding one folded houseletter; her composed three-quarter face is visible. 24mm-equivalent lens at 0.95m-equivalent height, generous depth of field, low dark balustrade foreground, woman middle plane, vast pale piers behind. Practical light through high clerestory openings makes crisp shapes on the dark floor. Architecture and person belong to the same constructed medium. No live-action face, toy gloss, shallow macro blur, visible joints, text or crowds. Negative space makes the miniature feel enormous.

## Selection and rejection criteria

Judge full uncropped frames and faces at full size. Prefer the direction whose ordinary faces, useful kitchen and immense hall can belong to one film. **Recorded verdict,2026-10-02:** root approved A. Its photographic room supports ordinary adult presence, and `style_A_scale` makes the postal hall much more monumental and physically palpable. B and C reduced the hall to a bookcase/miniature impression despite their different media. Do not reuse the A-room audition faces as identities; separate clean portraits are next. Six original recipes are preserved in `episodes/ep01/build/lookdev_tests.json`; production continues in root-owned `episodes/ep01/build/images.json`.

Reject a room test with reversed doors, an island replacing the rear worktop, hidden faces, a second kitchen, glamour skin, frightening age texture, or an illegible separation between the two external worlds. The first loose test is not sufficient as the final room authority: create the exact empty master afterward. Reject a hall test that reads as envelopes floating in blank space, a decorative bookcase, tiny fussy machinery or a generic glowing futuristic terminal.

Pick the medium first. Then approve character portraits and the exact room geometry. Do not mix A faces with C sets or preserve a favored B face as a live-action identity.
