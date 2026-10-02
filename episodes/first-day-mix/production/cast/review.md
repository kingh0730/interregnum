# Cast asset delivery

Six built-in image-generation calls produced six source sheets. No external paid API was used. Exact prompts are in `all-prompts.json`; source origins are recorded separately. Originals are preserved in `work/first-day-mix/production/cast/`.

`manifest.json` contains 23 primary `characters` (22 named roster IDs plus `future`) and five `variants`: `gpt_dance_a`, `gpt_dance_b`, `deepseek_dance_a`, `deepseek_dance_b`, `future_open`. Every path is repo-relative. All PNG sprites are RGBA and tightly cropped with transparent padding where the source allows. `extract_sheets.py` rebuilds them from the source sheets using the project `.venv/bin/python`.

## Actual visual inspection

Inspected all six full-resolution source sheets and the combined checkerboard-alpha review. All requested figures exist and have distinct human faces, complete shoes and hands. Core lead facial identities, hair colours and folded costumes remain recognizable from C3. Claude and Doubao preserve the C3 longer-hair/folded-paper design rather than the earlier prose haircut shorthand; these sprites are the production visual reference. The two lead alternates are illustrated cel/paper interpretations, fully committed replacements rather than photographic bodies with drawn patches.

The first sheet separates photographic leads, apricot cel, orange paper, violet pixel and black woodblock characters clearly. Secondary costume colours and individual silhouettes are distinct. Pangu's woodblock texture and Copilot's visible pixel clusters add medium variation beyond the main six. Future is an adult ivory-paper human with a face, not a faceless mannequin; both tucked/reaching and open-catch poses are available.

Checked the extracted figures against contrasting checker squares. Adjusted measured crop boundaries where hair or fingertips crossed the nominal grid; no neighboring figure remains in the reviewed contact board. MiniMax/Copilot use a disjoint stepped mask to preserve both MiniMax's fingers and Copilot's coat. The exact alpha process and all extraction regions remain in the recipe; no generative repair or hidden repainting was used for extraction.

22 named base sprites are approximately 500–780 pixels high. The future's deliberately tucked pose occupies 402 pixels including padding; its open pose is taller. These source-resolution figures suit ensemble shots and moderate hero scale, not 4K facial closeups.

## Using the replacement poses

The A/B lead poses genuinely differ: knee tuck/anticipation versus high diagonal kick/extension. Show them as authored replacement poses with brief impact holds; do not dissolve between them or advertise interpolated anatomy as natural dance. Match their **waist and head scale**, not the tightly cropped image rectangle: a tuck has a shorter image height than a kick. The renderer must preserve that difference rather than enlarge the tucked body until its feet reach a common baseline.

`future.png` reaches forward with both knees tucked. `future_open.png` opens both arms and extends the legs for the final catch. These are pose assets; harness attachments and on-screen hand contacts still require scene-specific compositing and playback review.

Native green-screen pixels were mathematically unmixed into alpha. Muted jade/celadon/olive costume interiors were retained by the saturation threshold; no pure green garment was requested. Fine hair edges have been reviewed at contact-board scale, but an extreme enlarged shot may reveal source antialiasing. No claim of motion, dance timing or final shot approval is implied by this still-asset review.
