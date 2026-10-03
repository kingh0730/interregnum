# Production archives

Archives preserve production history and reproducibility. They are not gold standards for future episodes:
models and the pipeline evolve. Use their examples and lessons critically, following the current playbook's
guidance on evaluating methods for each new production.

## Episode archive (2026-10-04)

All episodes except `first-day-anime-test` and `first-day-animation` were moved to iCloud Drive at
`interregnum-archives/episodes-2026-10-04/`, including their tracked source files and untracked assets.
The archived episodes are `ep01`, `first-day`, `first-day-anime`, `first-day-extremely-fast`,
`first-day-mix`, `first-day-show-off`, `landing-day-one`, and `pilot`.

The archive preserves repository-relative paths for the episode directories, associated work and renders,
pilot assets/audio, the pilot-specific audio builder, and the saved episode conversation export.
It includes 805 tracked files and 17,277 filesystem entries totaling 8,708,022,271 file/link bytes.
`inventory.json` records exact paths and metadata; `tracked-files.txt` identifies the tracked sources.
`shared-source/` preserves current shared tools, docs, scripts and root configuration files for reference.
The main repository retains Git history; the move does not erase historical commits.

Same-filesystem identity and metadata verification passed for every moved entry. Both protected episode
directories and their associated work/renders were verified unchanged using content hashes and metadata.
The episode template and shared production infrastructure remain in the checkout.

Earlier archives were left in place. Pilot media are still in `interregnum-archives/pilot/`, and previously
offloaded episode outputs remain in `interregnum-archives/storage-offload-2026-10-02/`. To restore an episode,
combine the required paths from these archives with the latest source snapshot in the 2026-10-04 archive,
checking for newer local files before copying. Restore original physical repository-relative paths;
build scripts may depend on them. Retain generation logs and existing assets instead of regenerating them.

iCloud upload completion was not verified; placement in iCloud Drive does not establish remote sync or
reclaimed disk space.

## Pilot: CONTINUITY

Archived on 2026-10-02 in the owner's iCloud Drive at `interregnum-archives/pilot/`.
The archive contains complete copies of these directories, preserving their repository-relative layout:

- `episodes/pilot/`
- `assets/pilot/`
- `audio/pilot/`
- `work/pilot/`
- `renders/pilot/`

All 1,790 entries were moved with same-filesystem identity and file-metadata verification.
Copies of the 281 Git-tracked source files were retained in this checkout, with their working-tree
contents and Git status preserved. Those retained source files were subsequently moved into the 2026-10-04 archive above. Generated media,
renders, caches, and other untracked files from these directories live in the archive.

The archive also contains `shared-source/`, a snapshot of tracked shared tools, documentation, and
dependency files at archive time, plus an inventory and `ARCHIVE-README.txt`. This is not a complete
installed environment. The main repository retains its Git history.

## Resuming the pilot

1. Fully download the archive from iCloud before reading or restoring its assets.
2. Use the 2026-10-04 archive for the latest source snapshot; do not overwrite newer local edits blindly.
3. Restore needed media to the same repository-relative paths above. Existing build scripts and
   manifests expect those locations; some also contain paths to the original checkout.
4. Compare the archived shared tools with the current versions before rebuilding. Preserve generation
   logs and reuse existing assets rather than submitting new paid requests merely because local files
   are absent.

Archive upload completion was not verified during the move. Moving into iCloud does not itself free
local disk space. After upload completes, Finder's **Remove Download** can release local storage;
**Delete** removes the cloud copy too.

For private productions, consult the gitignored `private/ARCHIVES.md` when available. Keep private
archive details and contents outside public commits.

## Completed experiments and working-output offload (2026-10-02)

Completed image/model experiments and selected bulky working outputs were moved to iCloud Drive at
`interregnum-archives/storage-offload-2026-10-02/`, preserving their repository-relative paths.
The archive's `inventory.json` records the exact moved paths; consult it before regenerating absent
experiment assets. At that time, episode source media, audio and story-reel exports remained local; the 2026-10-04 archive above now holds the other episodes.

Archived working outputs include `work/first-day/qa/export_frames/`, `work/first-day/qa/export/`, and
`work/ep01/render/`. Download and restore required directories to their original paths before reviewing
those saved frames or reusing those render intermediates; do not overwrite newer local work.
The archive also preserves experiment prompts, generation logs and comparisons with their assets.

The move verified file identity and metadata and preserved the existing Git working status.
Local verification records are in the ignored `work/storage-offload-20261002/` directory.
Moving into iCloud alone does not free local storage; upload and local-download removal are separate steps.
