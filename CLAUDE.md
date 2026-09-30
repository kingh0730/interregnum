# INTERREGNUM: working notes for Claude

An anthology of short films (see `README.md`). King is the showrunner; Claude writes, directs and runs the
production toolchain. Start with `README.md` (status) and `docs/playbook.md` (how an episode is made, end to end,
with every lesson from the pilot; the `make-episode` skill follows it), then `docs/strategy.md` (v1 story reel → v2 polish with
Seedance 2.5 and Suno), `docs/pipeline.md` (which tool for what) and `docs/history.md` (what failed and why).

## Working agreements
- Reasoning effort: while King is at the keyboard (assume so unless he says he is away), everything runs at the default, with no `--effort` flag. When he is away, checking work (critics, reviews, hunting bugs, flaws and mistakes, small pure improvements) runs at `--effort max`, and everything else stays at the default until clear evidence says higher effort adds a lot.
- Claude cannot watch video. Judge stills and frame metrics, and say plainly when motion needs King's eyes. Don't claim a clip "works" from metrics alone: in v3 the metrics improved while the motion got worse.
- Codex runs through `tools/imagegen/gen.sh`: medium effort, stdin closed, and exit code 2 means a safety-filter false positive, so reword and retry.
- Codex and API usage costs King's quota or money: estimate before large batches, and test small first.
- Disk is nearly full. Keep intermediates in `work/`, delete them when a shot is final, and never commit media.
- API keys only come from environment variables.
- The repo is public. King's questionnaire answers and candid views live in gitignored `bible/private/`; never quote them or attribute political opinions to him in committed files. Committed docs carry only the fictional creative choices.

## Shell gotchas (zsh is the login shell)
- Arrays are 1-indexed, `$var[...]` is a subscript, and `$var:s...` is a modifier. Brace variables (`${D}`) or put multi-step scripts in bash files.
- `g` is an alias; don't define a shell function named `g`.
- `node` is a broken nvm lazy-loader in non-interactive shells: use `~/.nvm/versions/node/v22.23.1/bin/node`.
- `codex exec -i` takes several files; put `--` before the prompt.
