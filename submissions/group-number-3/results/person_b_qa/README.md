# Person B reproduction and team-update integration checks

Verified November 9, 2026. The primary output directory was preserved.

1. Created a detached clean worktree at `75133a08dbcc23f44684290c6911272e18796358`, copied the five hash-verified official CSVs, and used the existing project virtual environment. `pip check` passed and six unit tests passed. Ran `verify`, `baseline`, `q2` and `q3` with a fresh `--output-dir`.
2. In that temporary worktree, merged Aarushi's `0e09450db2be0281ad8ebf47f104a33da5308cdc` without conflicts, producing isolated merge commit `38aef5e595d96e24e4fc578fee08f7ea54c9665b`. Repeated all three fitting stages into another fresh directory. The changed model source refactors the baseline factory but retains identical parameters.
3. Compared both runs with the primary artifacts using `src/check_person_b_results.py`. Both comparisons passed **51/51 checks**, including identical saved validation probabilities (maximum absolute difference 0), all AUROCs, subset IDs, pseudo-label selection, input hashes, fixed representation, convergence and source/configuration scope. Six unit tests also passed after integration.

`reproduction_checks.json` and `team_integration_checks.json` are the machine-readable reports. The complete fresh outputs and console logs are retained in the user's workspace under `output/kaggle_group3_qa_2026-11-09/`; they are not duplicated into this team folder. No model binaries or original passages are included here.

This was a fresh-fit reproduction on the same Mac and installed environment. It was not a fresh dependency installation, cross-platform test, or complete rerun of every new teammate experiment. Original user branch source/results and remote state were not changed by the isolated merge. No push, PR, Overleaf edit or Kaggle submission occurred.
