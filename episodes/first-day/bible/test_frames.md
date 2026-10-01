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
