# Shot 44 — THE WARM WINDOWS

**Duration:** 10 s (3:43–3:53; abs 223.0–233.0)  **Tool:** Codex k27 (an edit of k08) + comp (the window wave, the
pull, the sky, the drips); an optional silent Seedance take for the water and the clouds
**Camera:** 300 mm across the canal, as 15. It starts tight on Nana's window and **pulls back** to 15's full framing:
the only move in the film that breathes, a long ease.

**Action:** First light. The rain has stopped: the same towers as shot 15, the same thousand blue windows and Nana's
warm one. Then, starting from hers and spreading outward, the windows change one by one from screen blue to lamplight:
people switching the television off and a lamp on. The wave rolls across the city. Some windows go dark (someone
finally sleeps), and a few stay stubbornly blue. Under the clouds the sky turns a colour the film has never printed:
**dawn rose**, a new block cut for a single image. The Transmitter's red beacon still blinks over the warming windows:
the old is still standing. Under everything rises the murmur of a whole city talking to itself. **The palette's whole
argument pays off here:** cold was the Father's light, and amber is theirs. **Start pose:** the dawn city, blue windows
and one amber window.

**Build:**
- Codex **k27**, an **edit of k08**. **Acceptance:** the window grid is identical to k08's. Difference-check it and
  SIFT-align it to k08, because shot 15's masks (`work/pilot/v3/k08_windows.npz`) are reused. If the edit moved
  windows, recompute the masks on k27 with the same luminance-blob method.
- **The window wave (comp; primary in both versions):**
  1. Connected components of the window mask. The **seed** is the amber window's centroid.
  2. Each window *i* switches at `t_i = 1.0 + 7.0·(d_i/d_max)^0.8 + U(−0.4, 0.4)` s, where `d_i` is its distance from
     the seed (a fixed RNG seed, so renders repeat).
  3. At `t_i` the window changes ink over 0.35 s, from cold cyan to lamp amber `#F2A441` (luminance ×1.1), with a
     1-frame brightness pop of +10 %. It is an ink change, not a glow: lamps aren't soft in RELIEF.
  4. **8 %** of the windows (random) go to near-black instead (the set is off; bedtime); **3 %** never switch (the
     holdouts, still blue at the end).
  5. The canal's cuts under each window take that window's switch time (nearest in x), plus 0.2 s.
- **The pull:** `pull(1.08→1.00, start focus=the amber window, end focus=(0.5, 0.5), easeInOutSine)` over 10 s, with
  `parallax(near_tower=1.0, plate=0.4)` on a matte of the nearest tower cut from k27 (GrabCut; v1's `k08_fg_tower`
  layer is cut). One mechanism: the move is comp, on a plate or on a locked take.
- **The sky:** k27 carries the dawn in flat bands. Animate the rose band's strength from 60 % (a blend toward k08's
  night sky) at 0.0 to 100 % at 10.0 (easeInOutSine). Per the v2 lesson, add no second sky grade on top of a take.
- **No rain.** A few slow drips fall from the railing in the foreground (carved particles, one every 1.5 s).
- **v2 (optional):** a 10 s silent locked-off take from k27 for the water, the drips and the clouds; the wave and the
  pull go on top in comp. Don't prompt the model to switch windows: the bake-off gave one good spread in two takes,
  and the wave must start from her window on cue.
- `letterbox(2.39)`, `grade(DAWN)`.

**Keyframe prompt (`k27_city_dawn`, an edit of k08):**
> STYLE (RELIEF): a frame from an animated film printed by hand as a colour woodcut and linocut on warm cream paper. A
> carved blue-black key block holds the image; large areas stay solid black, with faint wood grain. Every surface (skin,
> cloth, hair, concrete, metal, glass, floor) is matte printed ink: no reflections, no sheen, no specular highlights, no
> smooth gradients. Light is a shape cut out of the black with crisp, slightly irregular knife edges. Middle tones
> everywhere, on walls, floors and machines as on faces, are parallel gouge strokes that follow the form. Colour is flat
> spot ink, never blended, with paper grain showing through: pale cold cyan where screens light things, amber where lamps
> light things, signal red only on red objects. Slight misregistration; no drawn outlines. Only screen light is soft.
> Faces are a few carved planes, calm; eyes are small dark shapes without highlights. Avoid: anime, airbrush, digital
> painting, 3D render, photorealism, lens flare, bokeh, neon, glossy or wet floors.
> FRAME: wide 16:9; keep everything important inside the central horizontal band, because the top and bottom 13% will
> be cropped to 2.39:1. No text, letters, numbers or logos anywhere; every screen is blank and evenly glowing.
> EDIT the attached image: it is the first light before dawn, and the rain has stopped. Print the sky above the towers
> in flat horizontal bands of ink, never blended: deep blue-black at the top, then a band of pale rose, then pale gold
> at the horizon; the undersides of the low clouds are cut out in rose. Rose is a new ink, printed only in this image.
> The canal is still, cut with short horizontal strokes of sky colour beneath the towers. All the windows still glow
> cold pale cyan, except the one warm amber window, which stays exactly where it is. The red lamp on the far mast is
> lit. Keep the towers, every window, the mullions, the embankment and the framing exactly as they are, aligned pixel
> for pixel.

**Refs:** `work/pilot/keys_v3/k08_city_night.png` (the image being edited).
**Layers:** none.
**JS spec:** none. The wave is comp on the masks.

**Sound:**
- **No rain.** Gutters dripping; the canal still.
- A first tram bell, far away, at abs 229.5. Birds (sparse FM chirps) from abs 227.0.
- **WALLA** (cues §7) rises from abs 224.0: a city of voices, unintelligible except "What happens now?" (230.2) and
  "I don't know." (231.4).
- Score: **E♭maj9 dawn swell** from abs 223.0, with the high shimmer from 226.0 (1M6).
- **Sync:** time the first 10 window switches (all near Nana's window, about shot +1.0–2.0) to land between walla
  onsets. Do not put a sound on each window.

**Motion prompt (v2, optional, Seedance: start `work/pilot/keys_v3/k27_city_dawn.png`, 10 s, `--no-audio`):** Colour
woodcut print animation; keep the first frame's exact carved shapes, flat inks and designs. Dawn over a wall of tower
blocks across a still canal; the rain has stopped. The buildings and every window stay exactly as they are. Water drips
slowly from a railing in the foreground, the canal's surface shifts very slightly, the low clouds drift slowly to the
left, and a small red lamp on a far mast blinks every two seconds. Locked-off camera. No sound.

**Takes:** —
