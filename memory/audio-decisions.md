---
name: audio-decisions
description: "Audio rules on INTERREGNUM — Claude casts voices and picks scores itself; final voices only from King's Starter ElevenLabs account; underplay voices (Kuleshov)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b27232ca-5280-4208-9826-f1156f716aae
  modified: 2026-09-29T16:44:15.775Z
---

- **Claude picks all audio.** King said (2026-09-30): "i won't be picking audios you make your best decision." Claude casts the voices and chooses the score takes itself, judging from metrics and the sound plan. Don't send King audition reels. He listens to the finished mix only.
- **Two ElevenLabs keys live in `~/.zshenv`,** which the home dotfiles repo ignores:
  - `ELEVENLABS_API_KEY_STARTER` is King's real account on the Starter plan, with a commercial licence. Every audio asset that ends up in the film must be generated with it.
  - `ELEVENLABS_API_KEY` is an older free account with no commercial licence. Use it only for throwaway tests.
- **Voices over-act, just like video models.** King: "voice models just like video models tend to over-exaggerate too much, maybe we need some kind of Kuleshov effect here too".
  - Direct behaviour, not emotion: pause tags, no emotion tags.
  - Use high stability.
  - Select takes by measured flatness: low pitch variance and an even level.
  - Let silence, rooms and the cut carry the feeling.
- **Nana must sound genuinely 82.** King said the stock stand-ins didn't sound 82 at all. Design her voice with ElevenLabs Voice Design.

Related: [[director-owns-creative-calls]], [[fal-paused]].
