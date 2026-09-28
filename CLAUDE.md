# INTERREGNUM: working notes for Claude

An anthology of short films (see `README.md`). King is the showrunner; Claude writes, directs and runs the
production toolchain. Read `docs/pipeline.md` before choosing a tool for a shot.

## Working agreements
- Creative work (bible, stories, scripts, shot design) is done at max or xhigh effort; production plumbing at medium.
- Claude cannot watch video. Judge stills and frame metrics, and say plainly when motion needs King's eyes. Don't claim a clip "works" from metrics alone: in v3 the metrics improved while the motion got worse.
- Codex runs through `tools/imagegen/gen.sh`: medium effort, stdin closed, and exit code 2 means a safety-filter false positive, so reword and retry.
- Codex and API usage costs King's quota or money: estimate before large batches, and test small first.
- Disk is nearly full. Keep intermediates in `work/`, delete them when a shot is final, and never commit media.
- API keys only come from environment variables.

## Shell gotchas (zsh is the login shell)
- Arrays are 1-indexed, `$var[...]` is a subscript, and `$var:s...` is a modifier. Brace variables (`${D}`) or put multi-step scripts in bash files.
- `g` is an alias; don't define a shell function named `g`.
- `node` is a broken nvm lazy-loader in non-interactive shells: use `~/.nvm/versions/node/v22.23.1/bin/node`.
- `codex exec -i` takes several files; put `--` before the prompt.
