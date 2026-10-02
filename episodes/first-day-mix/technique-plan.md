# Technique exploration: contact, folding and mixed cadence

This is an **original art-direction experiment**, separate from production shots and final character design. Source: `episodes/first-day-mix/build/contact-study.html`. No external libraries, copied reference source or media assets are used. It explores one controlled composition rather than attempting a miniature finished episode.

The 1920×1080 Canvas uses cobalt, ivory and apricot. A compact folded tile starts over an open oval socket. Thirteen rigid leaves expand around a common hinge, then the tile disappears as a new human silhouette emerges above it. The end state is one body and an empty socket; the tile does not remain as a duplicate. The mannequin-like silhouette is a graphic pose proxy, not an approved character or a claim of character beauty. It tests timing and scale only.

## Time and compositing graph

`window.renderFrame(t)` renders any timestamp in seconds without state accumulation. `window.ready` resolves immediately. The default page offers play/pause and a 0–6 s scrub control; export calls hide those controls. The six-second preview ends with an explicit paper wipe before restarting, rather than pretending the consumed tile can reappear continuously.

Compositing order:

1. Paper background, cobalt wall and floor lines.
2. Far particles.
3. Pedestal body, top plane and empty socket.
4. Hinged folded tile.
5. Emerging quantized silhouette pose.
6. Front rim mask.
7. Near particles and a brief contact ring.
8. Study labels and ending wipe.

The shared socket coordinates are `(1210,698)` with oval radii `(169,67)`. The foreground rim is an annulus rendered with an even-odd fill and clipped to its front half; **no opaque fill covers the inner opening**. The tile starts at `(1210,697)` and rises 110 px as it unfolds. Its leaves then move into the emerging body's lower region and fade out. The body emerges on the same x coordinate and rises a further 90 px. The dark socket remains visible underneath it. This is **2.5D compositing**, not a depth-buffered 3D simulation. The source preserves the count-level transition “one tile → one body; tile absent afterward,” not literal material-volume conservation.

## Motion math

- All easing uses clamped cubic smoothstep `u²(3−2u)`.
- Leaf expansion interval: 0.45–2.15 s. Tile consumption: 1.95–2.80 s. Body appearance: 1.95–3.25 s. The overlap makes a continuous transformation rather than a hard replacement.
- Thirteen rigid diamond-ended leaves share a hinge. Each rotates from a compact angular spread of 0.10 radians toward 1.12 radians, with shorter outer leaves. Alternating ivory/cobalt-tinted faces and center seams establish the folded surface without texture assets.
- The silhouette samples time as `floor(t×12)/12`; joint positions hold between those samples. Tile, lights and particle positions use continuous `t`. A 60 fps export would therefore show five rendered frames per held pose while effects continue smoothly. The HTML does not itself impose a 60 Hz display refresh.
- Particles use stable integer IDs, deterministic sine hashing and fixed birth times `2.2+id/70`. Lifetime, angle and radial velocity are derived from ID. Their trajectories are analytic functions of age: expanding elliptical orbits with vertical launch and quadratic fall. A sine lifetime envelope controls opacity.
- Orbit depth uses the sign of the angular sine. Far particles draw before the pedestal; near particles draw after the foreground rim, with corresponding size/opacity differences. This establishes the ordering principle but not physically accurate volumetric occlusion against arbitrary body shapes.
- The final wipe occupies 5.35–6.0 s. It is a preview reset device, not a proposed episode transition.

## How to inspect

Open `episodes/first-day-mix/build/contact-study.html` in a browser and scrub to 0, 2, 2.8, 3.3 and 4 s. The existing deterministic renderer can consume it:

```sh
/Users/kingh0730/.nvm/versions/node/v22.23.1/bin/node tools/web/render.mjs episodes/first-day-mix/build/contact-study.html work/first-day-mix/fx/stills/ 6 0.5
```

That command requests only three stills (0, 2, 4 s), not a motion render. Higher sampling and video output are later production work. The initial sandboxed Chrome launch failed. The escalated retry succeeded. Three 1920×1080 stills were captured at 0, 2 and 4 s in `work/first-day-mix/fx/stills/00000.png`, `work/first-day-mix/fx/stills/00001.png` and `work/first-day-mix/fx/stills/00002.png`. The final source was recaptured after correcting the transformation direction; the 4 s frame shows the new body above a visibly empty socket, with no surviving tile. The captured images were visually inspected. This is still-frame QA, not a normal-speed motion review.

## What this proves and what it does not

The source implements deterministic ordering, mixed time sampling, a composited socket and a coherent palette. Captured stills can verify drawing, composition and visible occlusion states; they cannot establish normal-speed timing quality. The body is a deliberately simplified rigid-chain proxy whose emergence is a graphic substitution with overlapping opacity, not a physically simulated reconstruction. No finger articulation, deformation, collision physics, cloth simulation, singing or natural human performance is implemented.

For final production, use approved character artwork/plates, a hand-contact pose, masks or actual depth geometry, shot-specific particle interactions and accurate light response. Preserve authoritative identities across mediums. Do not substitute this silhouette for adorable named AI characters, reuse this six-second timing as the song beat grid, or claim that the illustrated morph solves the final material-to-character transformation.
