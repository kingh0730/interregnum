# Pilot v1 review: CONTINUITY (built overnight 2026-09-29)

## v3 redesign (2026-09-29): documents rewritten, no images generated yet

**Why.** Two of King's notes on the v1 and v2 reels. The look: "it looks like claude generated some websites". The
in-world screens were 2020s web UI (dark cards, DIN and Menlo, cyan accents), and the Codex frames were the image
model's default: polished, rain-soaked, softly lit anime. The acting: the expressions were over-exaggerated. The
prompts asked for emotions (stunned, glistening eyes, a laugh through tears), and Seedance played them louder.

**What changed.** The story, the dialogue, the 45 shots and the 242 s timeline stand.
- **The medium is RELIEF, a colour woodcut** (`bible/visual/art_direction.md`): carved blacks, flat inks, gouge-stroke
  half-tones everywhere, and nothing that reflects or shades smoothly. Only the Father is smooth: the machine's copy of
  a man, the one image with the model's default polish (the Copy Rule).
- **Every screen is a machine** (`bible/visual/production_design.md`): tubes, flaps, a needle, legend lamps, film,
  carbon paper and handwriting, in the state's own alphabets. The broadcast is a 4:3 picture, and shot 04 pulls out of
  it to a monitor at Ida's desk. The smartphone is now the grey House Line with an amber call lamp and a card
  pencilled NANA; `signoffs.txt` is SIGN-OFFS · DESK 4; the wax seal is a red rubber stamp on a carbon copy; and in
  42 she opens the thermos.
- **Behaviour, not emotion** (`bible/visual/cinematography.md` §8): neutral start frames, one small action per shot,
  dialogue with volume and pace only, and the laugh in 42 heard, not seen. The camera is locked unless the story
  moves, and every setup has a lens, a height and an owner.
- **New lookdev and keyframes:** 43 Codex images (`images_v3.json`, `assets/pilot/lookdev.md`), no cutout layers. The
  opening broadcast becomes one take, like the Address.

The reels below still show the old look.

---

**Watch:** `renders/pilot/continuity_v1.mp4` (4:02). Then `continuity_v1_alt_ending.mp4`, which is the same cut plus
a 10 s cynical tail (shot 46). Subtitles are burned in; `.srt` files sit next to both.

This is the v1 story reel: Codex keyframes, compositing, JS screens, `say` scratch voices, and a synthesized temp score.
There's no video model and no Suno. Judge it on story, pacing, images and sound design, not on character motion.

## What Claude could not check
Claude judged stills and audio metrics only. These need your eyes and ears:
- **Overall pacing and whether it plays or feels like "PPT".** The writer designed stillness into the story (the Father
  *is* a frozen image), but you're the judge.
- **Motion events:** the capsule drop (10), the glitch and freeze (04), the archive scroll (08), the loop overflow (12),
  the typing rhythm and amber autocomplete (24, 26), the dissolve (34), and the window wave (44).
- **Sound:** balance, the tape-stop at 0:19, the "I am well" choir building to STOP at 1:10, and the walla near the end.
  The `say` voices are timing placeholders.

## Weakest shots (the compositors' own notes)
- **07, 13, 17, 19, 25, 32:** quiet pushes on stills. Correct to the spec, but closest to "PPT"; they're the best
  candidates for Seedance in v2.
- **10:** the capsule turns mid-fall and looks a little oversized.
- **37:** a flat phone screen.
- **40:** a 1.28× digital punch-in that's visibly softer.
- **30, 43:** soft inpainted edges may show behind the parallax layers.

## Director's decisions
1. **Ending:** the main (bittersweet-hopeful) ending is the cut. The alt tail (46) is cynical in a way the rest of the
   film doesn't earn: it undoes the one act of courage the story is about. It stays on disk as a curiosity only.
2. **Opener:** CONTINUITY is the series opener. It states the series' title as a literal premise, and it covers AI,
   leaders and family in one small room. If your questionnaire answers draw a red line, `episode.md` has the relocation
   plan, and the structure survives it.
3. **Look:** flat 2D cel with navy ink, cyan screens and amber lamps. It hides Codex drift, and it gives Seedance clean
   start frames.
4. **v2:** Seedance replaces every keyframe shot that has a face in it. The bake-off (`work/pilot/v2/`) decides the
   prompting recipe.

## Rebuilding
- **Recipes:** they're in `build/`.
  - `images.json` holds every Codex prompt; run `tools/imagegen/batch.py` with `--prefix-file`.
  - `comp/NN.json` holds the shot specs for `tools/comp/reel.py`. Run the prep scripts in `comp/c1`, `comp/s16_30` and
    `comp/c31_46` first.
  - `audio/main.json` is the mix, rendered with `tools/audio/mix.py`.
  - `edit_*.json` are the conforms, run with `tools/comp/assemble.py`.
- **Paths:** the recipes point at `work/pilot/`. Copy them back there to re-run.
