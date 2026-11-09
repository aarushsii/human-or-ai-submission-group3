# Person B: complete the shared experiments

Primary basis: Aarushi's `0e09450` experiments and submitted reference results. Yuchen Feng (`yf467`) supplies missing Q2 training scores, the 5000-row size, the required plot/report, shared split tracking and reproducibility material. Original methods and attribution are retained.

## Setup and inputs

From the repository root, use the existing `.venv` or create an environment following `PERSON_B_ENVIRONMENT.md`; exact installed versions are in `submissions/group-number-3/requirements-person-b.lock.txt`. Verified on this Mac with Python 3.14.8 and scikit-learn 1.9.1; fresh installation and other platforms are not claimed tested.

Place the five original teacher-linked Kaggle CSVs in `submissions/group-number-3/data/`. Raw files remain Git-ignored. Use the committed unchanged `splits/splits.csv`; never regenerate it for these comparisons. `config/person_b.json` records expected input hashes. The completion runner validates them before and after fitting.

## Canonical completion command

```bash
.venv/bin/python -u submissions/group-number-3/src/complete_person_b.py
```

Or from `submissions/group-number-3` with the environment activated:

```bash
python src/complete_person_b.py
```

The default re-fits the original TF-IDF learning-curve settings plus the missing 5000-row size. It records training and validation AUROC, means/SD over seeds 0/1/2, and one complete-pool fit at 8000. Original style validation records are preserved with their original scores; their training scores are unavailable rather than copied from another run.

The original Q3 submitted table is retained as the primary reference. The default completion command extracts its report rows; it does not claim to independently reproduce the style teacher score exactly. Student TF-IDF is refitted on the augmented texts in Aarushi's Q3 method, unlike the earlier frozen-feature supplementary study.

For a fresh completion directory, append `--output-dir submissions/group-number-3/results/person_b_new_completion`. To independently refit all pseudo-label candidates, use:

```bash
.venv/bin/python -u submissions/group-number-3/src/pseudo_label.py --output-dir submissions/group-number-3/results/person_b_new_pseudo_recheck
```

To refit both learning-curve models, including style, use `src/learning_curve.py --rerun-style --output-dir <fresh-directory>`. Fresh style results may differ from the original submitted values. Keep them separate and record the environment; do not silently overwrite the shared reference. Threads should be limited on memory-constrained machines; the combined runner limits numerical libraries to two threads.

## Required outputs

- `results/learning_curve.csv`: original records retained, training AUROC added for TF-IDF, three new 5000-row TF-IDF fits.
- `results/learning_curve_required.csv`: five-row Q2 main table, with sample SD and repeat counts.
- `results/learning_curve_train_val.png`: required training/validation plot; `learning_curve.png` keeps the original two-model validation comparison and adds the TF-IDF 5000 point.
- `results/pseudo_label.csv`: Aarushi's submitted reference, unchanged; `pseudo_label_report.csv` and `pseudo_label_reference.json` prepare/report its selected comparison.
- `results/person_b_completion_manifest.json`: official input/source hashes, versions, preservation checks and scope.
- `report/PERSON_B_REPORT_EN.md`, `report/person_b_q2_q3.tex`, figure and contribution notes: complete Person B report material.

A full local recheck of all 38 curve fits and all seven Q3 rows is preserved in `results/person_b_team_recheck/`. TF-IDF old points matched exactly, but style scores did not. The guard retained that mismatch; the canonical version preserves the original reference and labels local measurements separately. This is not independent confirmation on a new validation set.

## Supplementary history

`src/person_b.py`, its six invariant tests, and `results/person_b/` retain the earlier seed42 nested-subset/frozen-feature study. They are not the primary current report. Their prior fresh-checkout comparisons and failed fingerprint check are preserved for development history. Do not mix their scores with the current three-seed means or refitted-student method.

Run the invariant checks with `.venv/bin/python -m unittest discover -s submissions/group-number-3/tests -v`. Existing completed historical stages refuse to overwrite; reproducing that supplementary protocol requires a fresh `--output-dir`. No command uploads data, sends messages, edits Overleaf or submits to Kaggle.
