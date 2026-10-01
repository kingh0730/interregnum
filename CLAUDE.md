# INTERREGNUM: working notes for Claude

An anthology of short films (see `README.md`). King is the showrunner; Claude writes, directs and runs the
production toolchain. Start with `README.md` (status) and `docs/playbook.md` (how an episode is made, end to end,
with every lesson from the pilot; the `make-episode` skill follows it), then `docs/strategy.md` (v1 story reel → v2 polish with
Seedance 2.5 and Suno; the motion model is now MiniMax H3 Max, see the playbook §7), `docs/pipeline.md` (which tool for what) and `docs/history.md` (what failed and why).

## Working agreements
- Older episodes are historical examples, not gold standards or a quality ceiling. Models and the pipeline evolve; use current evidence and the new episode's goals to choose methods. Follow the playbook's guidance on re-evaluating inherited model choices and workarounds.
- Reasoning effort: while King is at the keyboard (assume so unless he says he is away), everything runs at the default, with no `--effort` flag. When he explicitly says he is away (e.g. going to sleep or going out), creative work (concepts, pitches, stories, scripts, design, art direction, and other creative development) and checking work (critics, reviews, hunting bugs, flaws and mistakes, small pure improvements) run at max reasoning effort; routine execution and production plumbing stay at the default. Apply the equivalent setting for the model/tool in use. Return to default for everything when he indicates he is back; do not infer absence from silence.
- Claude cannot watch video. Judge stills and frame metrics, and say plainly when motion needs King's eyes. Don't claim a clip "works" from metrics alone: in v3 the metrics improved while the motion got worse.
- The Codex image-rendering helper `tools/imagegen/gen.sh` retains its existing medium preset for executing prepared image prompts; creative design and prompt development follow the presence rule above. Keep stdin closed, and exit code 2 means a safety-filter false positive, so reword and retry.
- Codex and API usage costs King's quota or money: estimate before large batches, and test small first.
- Disk is nearly full. Keep intermediates in `work/`, delete them when a shot is final, and never commit media.
- API keys only come from environment variables.
- The repo is public. King's questionnaire answers and candid views live in gitignored `bible/private/`; never quote them or attribute political opinions to him in committed files. Committed docs carry only the fictional creative choices.

## Shell gotchas (zsh is the login shell)
- Arrays are 1-indexed, `$var[...]` is a subscript, and `$var:s...` is a modifier. Brace variables (`${D}`) or put multi-step scripts in bash files.
- `g` is an alias; don't define a shell function named `g`.
- `node` is a broken nvm lazy-loader in non-interactive shells: use `~/.nvm/versions/node/v22.23.1/bin/node`.
- `codex exec -i` takes several files; put `--` before the prompt.
