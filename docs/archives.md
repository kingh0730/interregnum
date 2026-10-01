# Production archives

Archives preserve production history and reproducibility. They are not gold standards for future episodes:
models and the pipeline evolve. Use their examples and lessons critically, following the current playbook's
guidance on evaluating methods for each new production.

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
contents and Git status preserved. They remain useful references for future episodes. Generated media,
renders, caches, and other untracked files from these directories live in the archive.

The archive also contains `shared-source/`, a snapshot of tracked shared tools, documentation, and
dependency files at archive time, plus an inventory and `ARCHIVE-README.txt`. This is not a complete
installed environment. The main repository retains its Git history.

## Resuming the pilot

1. Fully download the archive from iCloud before reading or restoring its assets.
2. Compare archived source files with the retained versions; do not overwrite newer edits blindly.
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
