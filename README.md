# INTERREGNUM

> *"The old is dying and the new cannot be born; in this interregnum a great variety of morbid symptoms appear."* — Antonio Gramsci

An anthology of short films in the spirit of *Love, Death & Robots*: the story of a generation living at the end of an era — confused, excited, exhausted, cynical, hopeful. AI and consciousness, feeds, plague, war, strongmen and prophets of technology, ideology, faith, love and family — told through fictional worlds whose places, times, names, faces and even genders are changed.

Each episode is one "morbid symptom" of the interregnum, with its own visual language, and every one is built to play like a blockbuster.

## Layout

| Path | What lives there |
|---|---|
| `bible/` | Series bible: premise, themes, influences, taste, the series visual and sound rules (`visual.md`, `sound.md`), the questionnaire for King |
| `episodes/` | One folder per episode (copy `_template/`): story, script, shot list, the episode's own bible (`bible/`: art direction, production design, cinematography, sound) and per-shot folders |
| `assets/` | Reusable look development: character sheets, locations, props, style frames |
| `audio/` | Music, sound effects, voice |
| `tools/` | The production toolchain, one folder per tool (see `docs/pipeline.md`) |
| `docs/` | Pipeline, tool strengths and weaknesses, lessons learned |
| `work/`, `renders/` | Scratch and output (git-ignored; large binaries) |

Private productions may be archived outside this checkout. When a private project is absent, consult
`private/ARCHIVES.md` if available for its location and restoration instructions before regenerating assets.
That local index and the archived project contents must remain outside public commits.

## Status

- [x] Step 0: repo set up; toolchain documented (`docs/pipeline.md`); strategy agreed (`docs/strategy.md`)
- [ ] King answers `bible/00-questionnaire.md`
- [ ] Series bible and episode slate (default effort while King is present; max when explicitly away, per CLAUDE.md)
- [ ] v1 story reels (no paid models): **pilot *CONTINUITY* built**, awaiting King's review (`episodes/pilot/review.md`)
- [ ] v2 polish: motion (MiniMax H3 Max; Seedance refuses photoreal faces) + the final finishing pass (playbook §7–7b)
