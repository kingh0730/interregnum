# Visual craft: the series rules

The rules every INTERREGNUM episode holds, whatever its medium, story or tempo. They were learned on the pilot and
the mom film, and each one is either a craft truth or a lesson about the tools.

Everything else is an episode's own choice, and it lives in that episode's bible: `<episode>/bible/` holds
`art_direction.md` (the medium), `production_design.md` (what things are), `cinematography.md` (how they're shot),
`test_frames.md` and `sound.md`. The pilot's bible is `episodes/pilot/bible/`, and the mom film's is
`private/mom-future/bible/`. A choice that worked in one film, such as the pilot's locked-off camera, its darkness
or its palette, belongs to that film. It is not series law, and a new episode starts from these rules and
`bible/taste.md`, not from the pilot's bible.

Sound has its own series rules in `bible/sound.md`.

**Visual ambition (King, 2026-10-02).** Every episode must be aesthetically exceptional, eye-catching and
visually memorable; aim for images that make the audience say "wow," even feel astonished. This is a series-wide
quality bar, not an optional flourish for spectacular stories.

Visual impact can come from a simple composition, extraordinary light, colour, scale, material, staging or an
unexpected visual idea. Complexity, ornament and crowded detail do not establish quality. Quiet scenes still need
strong visual craft; they need not compete with the episode's major visual moments. Preserve the contrast and
restraint of §1 rather than turning every shot into a spectacle.

Apply the same aesthetic bar to generated imagery, code-rendered pictures, inserts, diagrams, screens and titles.
Technical correctness, legibility and deterministic control are not aesthetic approval. Reject generic or
presentation-slide-looking substitutes that weaken the chosen visual world. Judge the actual image and its place
in the sequence, not the tool used to make it; a deliberate graphic style can be exceptional too.

---

## 1. No constant dial

King (2026-09-30), about camera, pacing and every other art aspect: constant is not a virtue. The craft is the
balance of **familiarity, variety and surprise**, and overuse is worse than constancy ("super super bad").

- **Familiarity:** each episode picks a home register for every dial (camera, cutting, palette, shot size, sound
  density, performance) and holds it most of the time, so the audience learns the film's rules.
- **Variety:** small, deliberate departures from section to section. Sections differ in degree, not by a new trick
  each time.
- **Surprise:** one, perhaps two, per film, saved for the biggest turn of the story. A surprise only works because
  the home register came first, and a second or third cheapens the first.
- When in doubt, cut the trick. The tempo map (`docs/playbook.md` §1, Pacing) sets every dial per section.

## 2. The medium rule

By default, a character differs from the world in *technique*, not *medium*. A change of medium is allowed only
when all three conditions hold:
1. **Fully committed.** It is truly another medium (real photographic footage, archive video, live action, a
   different animation technique) and not a half step. The pilot's v3 Father failed because he was smoother than
   the woodcut but not a photograph: an uncanny valley of style that reads as a mistake.
2. **Motivated.** The story explains it: another world, a machine's output, a memory, a document.
3. **Set up or saved.** Either the audience learns the rule early (*Roger Rabbit*, *Spider-Verse*, *The Wizard of
   Oz*), or the break happens once, as a revelation it has earned (*Waltz with Bashir*'s final archive footage,
   *The Lego Movie*'s live-action turn).

The series may change medium per episode, as *Love, Death & Robots* does.

## 3. The copy

Each episode names its "copy": the one image that belongs to the machine or the regime. Only the copy gets the
frictionless look (even soft light, perfect symmetry, smooth gradients, skin without texture). The model's default
polish is quarantined in the one thing that is generated, and everything alive is made by hand and shows it. The
pilot's copy is the Father, a steel engraving (`episodes/pilot/bible/art_direction.md`).

## 4. Image rules

1. **Light has a source.** Every lit surface can point to its lamp, screen, window or sky. Nothing is lit by the
   air. How dark a film is belongs to the episode.
2. **Silhouette first.** Threshold any keyframe at 25 % luminance: every figure and key object must still read.
3. **Faces are restrained.** Eyes have no highlights, and nobody opens their mouth unless they're speaking.
   Keyframes never show tears, grins or anguish. The acting is staging and cutting (§6).
4. **The palette has meanings.** Each episode's production design gives every colour family a meaning and keeps to
   it, like physics.
5. **Texture must survive motion.** Video models make fine surface texture swim. Put texture in static things (sets,
   solid blacks, walls) and keep figures, hands and faces simple. Add paper grain or film grain as a static layer in
   comp, never as painted per-frame detail.
6. **Detail at one point.** Each frame has one sharp, detailed focal point, and everything else is simplified.
7. **Spare prompts.** One subject, negative space, no over-described texture (see `docs/playbook.md` §2b).

### What image models do by default, and the counter-move
| Default | Counter (write it into the prompt) |
|---|---|
| Even, soft light everywhere; lifted blacks | One named hard source; "everything else falls into shadow" |
| Centred, eye-level medium shots | Name the lens, camera height and the subject's position on the frame |
| Anime eyes: large, glossy, with a highlight | "Eyes are small dark shapes without highlights" |
| Rain-soaked neon-city wallpaper | The episode's own light sources, named, and one motivated colour |
| Airbrushed glow halos, god rays, bokeh balls | "Light is a shape where it lands, with no glow"; only light sources glow |
| Generic, clean, unowned objects | Named materials and one repair per object |
| Teal-and-orange grading | The exact palette, named per source |
| Detail spread evenly | Detail at the focal point; the rest simplified |
| Emotion on the face | A physical state: posture, hands, where the eyes rest |

## 5. The camera

- **Every setup belongs to someone.** Decide whose eye the camera is (an institution's, a colleague's, a guest's, a
  neighbour's) before choosing a lens. The pilot's table is in `episodes/pilot/bible/cinematography.md` §1.
- **Name the lens, the camera height and the subject's place in the frame** in every image prompt. Models honour
  explicit lens and height language and default to centred eye-level shots without it.
- **Negative space is the scale.** How much of the frame a figure takes says how big the world is around them.
- **Three planes:** a foreground occluder, the subject and a light source behind. It gives depth to a still and
  real parallax to a video model.
- **A change of frame shape is always an event** (the pilot's 4:3 broadcast inside its 2.39:1 world).

### When the camera moves
The camera is a dial on the tempo map, under §1. In the pilot's v1 nearly every still got a 2–10 % push, so every
shot drifted and no move meant anything. The pilot's v2 swung to the opposite constant: locked off everywhere except
eight moves.
1. **Home register.** Each episode picks its camera's resting habit (still, gliding, restless, handheld) and its
   grammar of moves, and holds it most of the time.
2. **Every move has a reason:** a reveal, a decision, a release, a change of whose eye it is. Moves have owners and
   characters. In the pilot, institutions move like machines (rails, constant speed, on the axis) and people's world
   breathes (ease in and out).
3. **Surprise:** one, perhaps two, per film, on the biggest turn: a sudden whip, the first handheld shot, a move
   that breaks the axis, or a sudden hold in a moving film.
4. **Two bans, because they are slideshow tells rather than choices:** a micro-push on every still
   (`bible/taste.md` MADE-2), and a pan across a flat image. Zoom and handheld are allowed when an episode chooses
   them.
5. **One mechanism per move.** A move is either comp on a plate (≤ 10 % scale, with parallax layers) or one plain
   instruction to the video model ("the camera dollies slowly forward along the aisle at a constant speed"), never
   both.
6. **QA:** list each section's camera register and moves in the tempo map. Revise if the film never leaves home,
   and also if big moves or surprises pile up.

### Shot-size grammar (the default; break it on purpose)
- **The ladder.** A scene opens wide (where we are, and who is watching), then steps in one shot size per exchange,
  and saves its tightest size for the line that turns the scene. It doesn't skip two sizes on a cut, except as
  punctuation: a jump from a wide to an insert.
- **The reaction is an object.** After a line, cut to what the character holds or looks at, not to a face. The
  audience supplies the emotion (Kuleshov).
- **Inserts** are real objects, at the operator's eye line or straight overhead. They last as long as it takes to
  read, plus one beat.

## 6. Acting for video models: behaviour, not emotion

Video models read an emotion word as an instruction to perform it, and they turn it up. "Stunned, eyes glistening"
comes back as a soap-opera close-up. The emotion has to come from what surrounds the face: the cut before and after,
the sound, the light and the objects. The pilot's before-and-after rewrites are in
`episodes/pilot/bible/cinematography.md` §8.

1. **Write behaviour, never emotion.** Never use: stunned, hollow, glistening, trembling, tears, crying, laughing
   through tears, overwhelmed, barely able to speak, contempt, defiance. Replace each with what the body does: where
   the eyes rest, what the hands do, one breath.
2. **Stillness is an action.** Say what doesn't move: "Her head does not move." "Her hands stay on the desk."
3. **One small action per shot, and late.** Hold one to two seconds of stillness, make one small movement, then
   return to stillness.
4. **Dialogue gets volume and pace, nothing else:** "She says quietly, lips barely moving: '…'"
5. **The start frame is the first frame of the performance.** Write keyframes neutral: a composed face, the mouth
   closed or on the first syllable, the eyes on an object. An emotional keyframe forces an emotional clip.
6. **The sound carries what the face doesn't.** A laugh can live in the mix while the face only lets it happen.
7. **End every prompt with the performance line:** "Understated performance: her face stays composed; only the
   described movements happen." Then the camera line.
8. **Choose the stiller take.** Generate two. If both overact, trim the clip and cut before the gesture.

These rules are the default register. A film whose tone is bigger (the mom film is bubbly) turns the performance up
by choice and says so in its own bible; it never does it by writing emotion words.

**The style line.** A clip inherits its look from the start frame, so a motion prompt carries one short style line
for the episode's medium, not the image prompt's full style block.

**The motion-prompt template:** `[style line]. [Shot size, lens, angle, composition]. [Who, where, holding what].
[What stays still]. [One action, with its timing: "after two seconds…"]. [Dialogue, with volume and pace].
[Performance line]. [Camera]. [Diegetic sound only; no music.]`

## 7. Checks Claude can run on stills

Claude can't watch video, but most rules have a still-frame test. Motion needs King's eyes, and every handoff says so
plainly. Each episode sets its own thresholds (darkness, palette families, framing) in its cinematography file.

| Check | Test | Pass |
|---|---|---|
| Silhouette | threshold the keyframe at 25 % luminance | every figure and key object still reads |
| Eyes | zoom on the eyes | no specular highlights; no tears in keyframes |
| Palette | hue histogram against the episode's colour families | no stray hues |
| Lens and height | horizon line and perspective against the shot's spec | matches the spec |
| Motion prompt | scan for the banned words in §6 | none |
