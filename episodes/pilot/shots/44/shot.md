# Shot 44 — THE WARM WINDOWS

**Duration:** 10 s (3:43–3:53; abs 223.0–233.0)  **Tool:** Codex edit of k08 + cutout layer (reuse) + comp (window
wave, sky)  **Camera:** starts on shot 15's end framing (1.06 on Nana's window) and **pulls back 1.06→1.00** to reveal
the whole city, with parallax

**Action:** First light. The rain has stopped, and we're looking at the same towers as shot 15 with the same thousand
blue windows and Nana's warm one. Then, starting from hers and spreading outward, the windows change one by one from
screen-blue to lamplight: people switching the television off and a lamp on. The wave rolls across the city. Some
windows go dark (someone finally sleeps); a few stay stubbornly blue. Above it all, the sky turns a color the film
has never used: **dawn rose**. Under everything rises the murmur of a whole city talking to itself. **The palette's
whole argument pays off here: cyan was the Father's light, and amber is theirs.** **Start pose (v2):** the dawn city
with blue windows and one amber window.

**Build:**
- Codex **k27**, an **edit** of k08 (attach only k08):
  `tools/imagegen/gen.sh assets/pilot/keyframes/k27_city_dawn.png "<prompt>" assets/pilot/keyframes/k08_city_night.png`
- **Acceptance:** the window grid must be identical to k08's. Difference-check it and SIFT-align to k08, because the
  window masks from shot 15 (`work/pilot/k08_windows.npz`) are reused here. If the edit moved windows, recompute the
  masks on k27 with the same HSV threshold.
- **Window wave:**
  1. Take the connected components of the cyan window mask. The **seed** is the amber window's centroid.
  2. Give each window *i* a switch time `t_i = 1.0 + 7.0·(d_i/d_max)^0.8 + U(−0.4, 0.4)` s, where `d_i` is its
     distance from the seed (a fixed RNG seed, so renders are repeatable).
  3. At `t_i`, crossfade the window over 0.35 s from cyan to lamp amber (`#F2A441`, luminance ×1.1). Add a soft 6 px
     warm glow and a 1-frame brightness pop (+10 %).
  4. **8 %** of windows (random) go to near-black instead of amber (the set is off; bedtime). **3 %** never switch
     (holdouts, still blue at the end).
  5. Canal reflections: each reflection blob takes the switch time of the window directly above it (nearest x),
     plus 0.2 s.
- **Sky:** k27 already carries the dawn gradient. Animate its intensity: from 60 % (blend toward k08's sky) at 0.0 to
  100 % at 10.0 (easeInOutSine), plus a slight +8 % warm lift on the cloud undersides in the last 4 s.
- **No rain.** Add a few slow drips from the tram wires (particles, 1 every 1.5 s).
- **Camera:** `pull(1.06→1.00, start focus=the amber window, end focus=(0.5, 0.5))` over 10 s (easeInOutSine), with
  `parallax(k08_fg_tower=1.0, plate=0.4)` (the shot 15 layer, aligned to k27).
- `letterbox(2.39)`, `grade(DAWN)`.
- **v2 note:** Seedance can animate the sky and water, but the window wave stays a comp effect on top of the v2 clip
  (or the whole shot stays comp). Don't prompt the model to switch windows.

**Keyframe prompt (k27, edit of k08):**
> STYLE (keep exactly): a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean,
> confident dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only
> around light sources; subtle paper grain; simplified graphic backgrounds with bold silhouettes. Wide 16:9;
> important content in the central horizontal band. No text, letters, numbers, logos or watermarks anywhere; every
> screen is a blank glowing panel.
> EDIT the attached image: the rain has stopped, and it is the first light before dawn. The sky above the towers
> shades from deep blue at the top to pale rose-pink and pale gold at the horizon, and the low clouds are touched with
> rose underneath. The canal is still and mirror-like, reflecting the sky and the windows. All the windows still glow
> cold cyan, except the one warm amber window at the lower right. The billboard at the far left is dark. Keep the
> buildings, the window grid, the tram wires and the framing exactly identical and pixel-aligned with the original.

**Refs:** `assets/pilot/keyframes/k08_city_night.png` (the image being edited).
**Layers:** reuses `assets/pilot/layers/k08_fg_tower.png` (no new cutout).
**JS spec:** none.

**Sound:**
- **No rain.** Gutters dripping; the canal still.
- A first tram bell, far away, at abs 229.5. Birds (sparse FM chirps) from abs 227.0.
- **WALLA** (cues §7) rises from abs 224.0: a city of voices, unintelligible except "What happens now?" (230.2) and
  "I don't know." (231.4).
- Score: **E♭maj9 dawn swell** from abs 223.0, with the high shimmer from 226.0 (1M6).
- **Sync:** time the first 10 window switches (all near Nana's window, about shot +1.0–2.0) to land between walla
  onsets. Do not put a sound on each window.

**Motion prompt (v2):** Flat 2D cel-painted style. Dawn over a dense city of tower blocks across a still canal; the
rain has stopped. Water drips from tram wires, the canal ripples faintly, and the sky slowly brightens from deep blue
to rose and pale gold. Slow pull-back revealing the whole city. Dripping water, a distant tram bell, birds, a murmur
of many people talking. No music.

**Takes:** —
