# 第一天 — look tests and frame acceptance

All six initial files were visually inspected on 2026-10-02. Their exact prompts, outputs and no-reference setup are recorded in `episodes/first-day/build/lookdev_images.json`. That manifest is the prompt authority; do not maintain a second slightly different copy here. These are look experiments with invented stand-in faces, not final character-reference tests.

## Initial comparison

| Frame | Observed strengths | Observed problem / disposition |
|---|---|---|
| `episodes/first-day/assets/lookdev/test_porcelain_world.png` | Physical stone, controlled sunlight, generous space | Repetitive office windows and enclosed campus massing dominate. Little maritime identity; no convincing future transport. Do not approve as the world master. |
| `episodes/first-day/assets/lookdev/test_porcelain_body.png` | Clear complete bodies, luminous ivory/ink contrast, grounded shoes, readable fabric | Ordinary institutional entrance behind them. Useful body/light reference only; unreferenced faces and hair are not Lin/Yu. |
| `episodes/first-day/assets/lookdev/test_prism_world.png` | Strong dark facets, restrained refracted colour, a glimpse of sea | Another contemporary plaza with tiered office blocks. More facets have not supplied a distinct future function. |
| `episodes/first-day/assets/lookdev/test_prism_body.png` | Full bodies and clean separation from one another | Heavy faceted facades and stairs dominate; only shallow change from present architecture. Hair and faces remain test identities. |
| `episodes/first-day/assets/lookdev/test_nocturne_world.png` | Strongest colour event; luminous surfaces have visible sources | Giant coral rectangle makes the image a staged amphitheatre; dark ground and little open water. |
| `episodes/first-day/assets/lookdev/test_nocturne_body.png` | Bodies remain readable under architectural light; bold backdrop | Contemporary blocks behind the lights; heavy coral focal competition and dark feet. Not the lightness of the chosen story. |

**Director decision:** develop porcelain's photographic body/light register into a more ambitious maritime world. None of the six generic campus/amphitheatre plates was accepted as the location master. Subsequent reference work, described below, supplied the missing future silhouette and functional geography.

These are single outputs per prompt, with differing invented body identities. They support a project-specific design decision, not a model ranking or a general statement about what a generator can do.

## Approved reference development

A first maritime candidate established the intended scale and skyline, but made the three locations enclosed saucers. Their dance floors disappeared under roofs, and their broad curving access structures resembled footbridges. It was not approved as the location master.

The **revised open-deck master**, currently `episodes/first-day/assets/references/world.png`, is approved as the general design/geography reference. Its open floors, ivory/dark-blue side-deck distinction, central island, separate broad pedestrian approach and visible bogies make the premise readable. The giant hollow towers and elevated urban connections establish a far future beyond the initial office-campus tests. This is an oblique view across the bay, not the common north-to-south dance camera.

The overview does not prove all subsequent geography. In particular, it depicts lateral dock connections present at both sides; actual story shots need the correct passing/docked/departing state. The island's three rib assemblies contain paired members, so local angles must preserve the approved structural family rather than inventing another canopy. Local A/B/I masters remain subject to their own inspection for floor space, dock side, bench position, lighting and background.

`episodes/first-day/assets/references/lin_costume.png` is approved as a wardrobe/body reference: ivory high neck, pleated straight trousers, complete shoes and a restrained silver seam. The face is recognizably close at full-body scale, but that does not certify exact identity or make the costume frame a new face authority.

The first Yu costume introduced notched lapels, clipped shoes and stray pale trouser marks; it was rejected. The revised `episodes/first-day/assets/references/yu_costume.png` restores the collarless silhouette, plain trousers and visible footwear and is approved as a wardrobe/body reference. Head and shoe margins are tight; this framing should not become the dance template. Its studio source light also does not govern location lighting.

The original bases in `episodes/first-day/assets/characters/lin_base.png` and `episodes/first-day/assets/characters/yu_base.png` remain the face authorities. Costume and world references answer different questions. Their approval does not establish multi-angle identity consistency, shared-floor contact or motion quality.

## Supporting references and local-angle findings

`episodes/first-day/assets/characters/lin_sheet.png` keeps Lin recognizable across its three views, with the bob and correct left-ear cuff. It adds some texture relative to the base. Use it as a supporting angle reference only, with the original portrait primary.

**Exclude `episodes/first-day/assets/characters/yu_sheet.png` from scene conditioning.** It preserves recognizable features but adds conspicuous granular skin texture and lines on cheek and neck, making Yu harsher and older than the approved base. Its existence is not approval. Use `yu_base.png` as face authority and the revised costume image for clothing; judge any later needed angle from its actual result.

`episodes/first-day/assets/references/phase_model.png` has **sixteen visible bobs**. It is adopted as a fictional adaptation of the fifteen-pendulum Harvard demonstration, not a photograph or exact reconstruction of that apparatus. Film descriptions and shot prompts should call it a physical phase model without claiming fifteen elements or transferring the source apparatus's exact oscillation counts to it. The original research remains correctly attributed to Harvard's fifteen-pendulum apparatus. The prop is optional visual texture and does not teach the plot.

The initial `loc_i.png` angle made the right-hand touring gallery's arch ivory rather than dark titanium and failed to show the side decks' perimeter rails clearly. The first targeted repair did not resolve the arch. The latest second repair was visually inspected: B's right arch is now dark, A's left arch remains ivory, and glass rail segments are visible on the side decks. The director approves `episodes/first-day/assets/references/loc_i.png` as I's local reference. Use its actual foreground floor, bench, ribs and dock positions consistently. Approval does not validate every subsequent dock state or character placement.

The latest repaired `episodes/first-day/assets/references/loc_a.png` was inspected and is approved by the director as A's local reference. It replaces the broad canopy with one narrow ivory arch, retains the bench at the far left, and shows a curved glass perimeter with the apricot docking threshold at the right. Open sky and water now separate the architecture clearly. In this actual angle the arch is on the docking side; use the approved picture consistently rather than silently restoring an earlier verbal arrangement. Its open dock edge is a state to manage explicitly in shots, not evidence that an undocked crossing is possible.

`loc_b.png` has a usable dark arch, coral inset and bench, but its floor reads almost rectangular in the local angle. Its relationship to the general oval-deck master needs scene-level continuity checks; the beauty of an isolated reference does not establish those checks have passed.

`episodes/first-day/assets/references/gate.png` is a useful material/detail view of a copper reel and apricot ribbon. Its crop does not show the receiving end or a traversable connection, so an insert of this object cannot by itself establish whether a dock is open, closed or safe to cross. Establish those states in the actual scene views.

## Frame approval

### Scene-reference tests: k10

The two rejected versions are preserved separately and were both inspected at native full-frame resolution against the original Lin portrait. Both keep Lin recognizable through her bob, facial proportions and closed-mouth restraint. At these relatively small face scales there is no obvious new age/skin failure; they do not prove exact facial fidelity. The ivory silhouette is elegant, although the tops are more wrinkled and the costume's silver seam less readable than in its reference.

| Preserved test | Actual result / disposition |
|---|---|
| `episodes/first-day/assets/lookdev/k10_rejected_tight.png` — portrait-base edit | Complete shoes but too little lower clearance; Lin looks left away from partner space; skyline is on the right rather than the approved A angle's left. The relaxed stance does not clearly anticipate the heel touch. Rejected. |
| `episodes/first-day/assets/lookdev/k10_rejected_t2i.png` — reference-conditioned t2i | Restores skyline left and ivory arch right. Still too tightly framed and still looking left. The free shoe at screen right points down onto its toe rather than showing a heel touch; trouser hems bunch around both shoes. Rejected. |

The third test, `episodes/first-day/assets/keyframes/k10.png` at modification time 05:06:08 on 2026-10-02, uses A's local image as the edit base with the original Lin portrait as face reference. It fixes rightward attention and preserves the local set arrangement. It still fails dance framing: the body occupies roughly seventy percent of the picture height, soles remain near the bottom edge, and the free foot points onto its toe. The trousers also become plain and slightly flared rather than the approved pleated silhouette, and the mouth is slightly open. Lin is recognizable at this scale without an obvious skin-age failure. The image could support a looking-right story beat after appropriate reframing, but it does not establish the intended heel-touch.

Do not mirror a picture to fix gaze: that would reverse the cuff and set. Subsequent tests should preserve the third take's successful head direction and location while actually supplying floor below the complete shoes and a readable grounded pose. Compare actual results to these observed shortcomings, not merely revised prompts.

### Wider scene-reference tests: k10, k42 and k05

The wider builtin-image candidates ending `exec-6f7bebfb-abe1-469b-a0f7-c131ce656be0.png` (k10) and `exec-7c9bb029-328e-4ae8-9d4d-20cbf5aa0a76.png` (k42) were inspected against the original portraits and local masters before copying into the production keyframe paths. Their provenance belongs in the generation record; the observations here refer to those specific candidates.

**k10 passes composition as a start-frame anticipation.** Lin has generous floor below complete shoes, open travel space to her right, and the intended rightward attention. The ivory arch, left skyline, left bench and source-light direction agree with A's approved local angle. Her face remains recognizable at the wide scale without an obvious age/skin failure, though this small profile cannot certify exact portrait fidelity. The free shoe still reads toe-led rather than a completed heel touch. Do not describe the held picture as proving that choreography; the motion take must supply the weight transfer.

**k42 passes composition as the shared-floor duet start.** Both people stand fully visible on I, facing one another with separate raised palms. There is ample lower clearance and room for the planned modest partner turn. The pearl floor, left bench, three silver rib assemblies and sea agree with the island master; the outside deck arches sit beyond the crop. At this scale the original identities are recognizable, wardrobe is consistent and no new coarse skin or obvious extra/merged limb defect is visible. This approves the common-floor and anticipation state, not hand contact, synchronization or a completed turn.

The revised Luma `episodes/first-day/assets/keyframes/k05.png` was inspected at full frame. It visibly places Lin on the ivory left touring deck and Yu on the blue right touring deck; the large central island is empty and has three rib assemblies. Separate floor rims and perimeter rails distinguish the three spaces, and the broad public approach remains visible. **It passes the apart/empty-island story fact.** Side floors sit very close to I, and rails obscure the exact transfer openings, so this picture alone does not establish a passing versus docked state or prove deck movement. Later crossing views must show their level connection explicitly. The side arches extend out of frame; this crop does not establish their colour or full outline.

### Late-sequence first pass and targeted repairs

The first bulk late-sequence review inspected k37–k55 as actual complete images and native detail crops in edit order, with k55 before k42. The SHA-bound findings are in `episodes/first-day/build/visual_review_late.json`. Several individually polished pictures failed story geography: swapped side galleries, a departing island instead of departing A, duplicated B architecture, or both people placed aboard B when the story required I. These are substantive retake findings; attractive faces do not make them acceptable continuity.

The targeted builtin repair candidates and exact provenance are in `episodes/first-day/build/repair_batch04.json`, saved non-destructively under `episodes/first-day/assets/repairs/`. The k43, k44 and k49 repairs use k42 as the sole environment/framing authority and the earlier picture only as a pose guide. They restore complete bodies with deep floor margins. k55 lowers the arms on the same island plate for the arrival pause. k47 and k48 replace the two-face/selfie-like crops with matching reactions: Lin at left looks right and Yu at right looks left, with only the opposite person's blurred shoulder/hair at the foreground edge. Original face portraits remain the identity authorities.

The repaired k51 now walks away toward the existing sea rail. Repaired k52 stands at that rail facing the water, Lin left and Yu right; it can be deliberately reused as k54's final tableau without asserting a new pose. Repaired k53 shows four resting shoes from behind in the same direction, matching the coda. All nine candidates were inspected full-frame and with native face/hand/foot detail where applicable. Their small-scale hand contacts still need motion review, and peripheral docked decks in the coda do not themselves prove departure. The director independently approved all nine v1 repairs, and their exact hashes were adopted into the canonical frame set. The settled k52 v1 tableau is also used deliberately for k54.

### Final canonical still acceptance

`episodes/first-day/build/visual_review_final.json` binds every one of the **55 canonical keyframe slots** to its current SHA-256 and reviewed/adopted evidence. There are **52 distinct image hashes**: k36 deliberately reuses k16's pre-crossing position, k39 reuses k33's on-B reaction, and k54 reuses k52's settled sea-facing tableau. The final report combines the actual-pixel early/middle reviews, the late full-frame/native-detail review, repair reviews and the director's independent adoption decisions. It preserves the separate historical reports instead of treating their rejected first-pass images as current failures.

The final geography repairs were inspected again after adoption. In k37 Lin is wholly on fixed I, empty ivory A is behind left and Yu remains aboard dark B at right. k38 leaves her on the same island while A becomes distant behind a closed departure barrier. k40 offers her palm into the island's empty right space without the duplicated B architecture. k41 separates Yu's blue B floor from Lin's pearl I floor with a visible level, glass-guarded bridge over water. Together with k55 and k42, these pictures now communicate the intended occupancy changes. They do not demonstrate a continuous crossing, completed landing or mechanical motion.

Three later coda removal variants were retained in the recipe history but rejected: they either removed the permanent viaduct or made the sea visibly painterly. The final choice remains the approved **k52 v1**, also used for k54. Partial peripheral galleries remain visible in that ending picture. The held coda establishes the pair standing together at the rail; their departing rides are a future-motion target, not a fact proved by that still. This does not undo the earlier k37/k38 separation-and-staying story state.

Current limitations are specific. k10 and related preparations do not prove a heel touch or complete phrase. Small clasps and the hand insert still need close motion inspection for finger separation, weight and stable contact. Crossing spans require several natural steps and action-duration checks. Tiny geography figures establish costume and occupancy rather than portrait-scale identity. Footwear texture and fine garment folds vary mildly between retained frames and need motion continuity checks. Keep the actual offered arm consistent within each supplied shot; the director locks inward screen direction rather than an arbitrary anatomical side across all differently angled poses.

**This is still-keyframe acceptance only.** At the time of this report the reviewer has not inspected baked Chinese subtitles or a finished export. Check captions against shoes and gestures in the rendered reel, especially the tighter seated/story frames k29, k32, k37 and k40. Performance, deck movement, action timing, lip restraint, listening and final rendered-overlay clearance remain separate checks; no motion approval is implied.

### Checks for each delivered frame

| Check | Pass evidence |
|---|---|
| Ambition | The world reads as a striking future place from its massing and function, without relying on a caption or coloured strip lights. |
| Elegance | One dominant focal point; clear silhouette; generous negative space; surfaces and joints are plausible at the photographed scale. |
| Geography | In a common wide, A, B, I, water gaps, level dock and public shore connection can be pointed out independently. |
| Identity | Original face, apparent age, hairstyle and costume survive reference transfer; Lin retains her left-ear cuff where visible. |
| Anatomy | Correct number of bodies and limbs; credible hands when visible; no merged wrists, crossed supporting legs or impossible shoe contact. |
| Dance readability | Complete shoes, head and gesture; body separates from rail/background; travel room; lyrics need not cover the action. |
| Light and medium | A named source accounts for illumination; photographic faces match their world; no plastic-render skin or decorative glow on every edge. |
| Continuity | Adjacent shots agree on dock side/state, arches, three island ribs, benches, horizon and source-light direction. |
| Story | The required fact is visible, not merely described in a prompt. Before 160 seconds the island remains empty; at 164 Lin is on it while A departs. |

Inspect complete frames at fit size first, then faces/hands/feet at full resolution. Review a sequence strip as well as individual images. Do not reject a frame solely because a pixel threshold dislikes a naturally dark garment; use the series silhouette test to find actual loss of the person or gesture, then judge the image.

## Motion is a separate approval

Still approval cannot establish a heel transfer, rotation, crossing, hand contact, synchronized phrase or convincing gallery motion. The current reel demonstrates compositions and story states through held frames and selected pose changes. It should be labelled accordingly.

For future motion, the first useful test is the final simple partner turn in full-body view. Verify feet remain on the same floor, hands meet without fusing, weight changes plausibly, face identities hold and the action completes inside the selected cut. Next verify one dock crossing with established level surfaces. Record action timestamps from full takes and recheck the final render. Metrics and sampled frames supplement playback; they do not replace it.

## Subsequent rendered-export check

The director subsequently inspected nine native decoded export frames, including the tighter k29/k32/k37/k40 compositions, the shared dance master, title and credits. Captions are legible and leave the complete shoes and key gestures visible. All 377 sampled shot midpoints and lyric/title on/off boundaries match their expected composition within encoding tolerance. `build/export_frame_review.json` binds this check to the actual Chinese MP4 hash; `build/export_audit.json` records independent audio and full-decode checks. This resolves the selected baked-overlay checks above without implying listening or motion approval.
