# Python compositing

numpy + OpenCV, run with `uv run` (dependencies in `pyproject.toml`).

`legacy/` holds the working code from the anime-clip experiments, kept as reference to harvest into a reusable
library as episodes need it. Their import paths still point at the old experiment folders:
- `v2_render.py`: parallax camera, cel deformation, blink cels, procedural petals, sun flare, sparkles, light wrap, bloom/grade/vignette/grain (`finish`)
- `v2_align_layers.py`: SIFT alignment of Codex-edited layers back onto their source keyframe
- `v2_masks.py`: color-based hair/scarf masks and blink-patch detection
- `v4_comp_character.py`: grading a rendered character into a painted plate (rim light from the alpha edge, gradients, flare behind the character)
