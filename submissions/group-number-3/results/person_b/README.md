> Supplementary historical seed42/frozen-feature study. The current primary Person B report follows Aarushi and is report/PERSON_B_REPORT_EN.md; current required results are results/learning_curve_required.csv and results/pseudo_label_report.csv.

# Completed Person B local experiments

Run date: November 9, 2026. Source commit: `bb8eaf5f8811755b3cc3f3c19b8eaaf6944c10de`. Protocol signature: `54caca721159447a2001c9375b87a7fc6adcd32abefff5078aef8ed8c959624f`.

The team planning document assigns Person B “learning curves vs. training size + pseudo-labeling with unlabeled.csv — 15 pts”, corresponding to Q2 (10) and Q3 (5). The Yuchen-to-Person-B assignment was confirmed separately in the project group discussion; the document's role paragraph does not itself name an owner.

- Shared document: https://docs.google.com/document/d/1kBn3ITDP76Fbby966O9YKoYWWbYrh2qdT0YQ_SLVfKU/edit
- Original rubric: `Kaggle_Competition_Template_Report-1.pdf`, Q2/Q3; requirements were checked before fitting.
- Inputs: original teacher-linked competition data and Aarushi's unchanged shared split; hashes checked before each stage. The original five CSVs and split are unchanged after the experiments.
- Model: unchanged `src/models.py::tfidf_logreg(C=4.0)`. Versions, complete parameters, hashes and ID fingerprints are in `run_manifest.json`; commands are in `../../PERSON_B_RUNBOOK.md`.

## Baseline

| Fixed fold | Training rows | Validation rows | Validation AUROC |
|---|---:|---:|---:|
| Random | 8000 | 2000 | 0.950644 |
| OOD | 7541 | 2459 | 0.935863 |

Both fresh scores agree with the rounded historical values (0.9506 and 0.9359). The old log is unchanged. Agreement does not independently prove the historical split file's byte identity.

## Q2

| Labeled training rows | Training AUROC | Validation AUROC |
|---:|---:|---:|
| 500 | 1.000000 | 0.872922 |
| 1000 | 1.000000 | 0.906055 |
| 2000 | 1.000000 | 0.922570 |
| 5000 | 1.000000 | 0.944931 |
| 8000 | 1.000000 | 0.950644 |

Rounded to six decimals; the unrounded full-pool training value is 0.999999875. Every row uses identical validation IDs and hyperparameters. Smaller subsets are nested and balanced. The 8000-row point is the exact baseline fit. See `learning_curve_results.csv`, `learning_curve.png` / `.svg` and `q2_analysis.md` (119-word English discussion plus Chinese explanation).

## Q3

| Method | True labeled rows | Pseudo-labeled rows | Validation AUROC |
|---|---:|---:|---:|
| Supervised only | 8000 | 0 | 0.950644 |
| With unlabeled data | 8000 | 628 | 0.950170 |

One predeclared round with thresholds <=0.05 / >=0.95 selected 247 pseudo-human and 381 pseudo-AI rows. Vocabulary, IDF and all transformation parameters remained frozen. Delta AUROC is **-0.000474**: this configuration did not help on this split. See `pseudo_label_results.csv`, `q3_run_details.json` and `q3_analysis.md` (100-word method, 101-word discussion, Chinese explanations). A small difference on one split is not evidence of a statistically reliable effect.

## Checks, history and current boundary

- Six focused unit tests passed, including a regression test for representation fingerprinting. Thirty post-experiment sanity checks passed in `experiment_checks.json`: input/source hashes, shared validation IDs, nested balanced subsets, saved probability/label/score consistency, fixed representation, convergence, and ignored raw data/cache files. PNG layout was inspected visually.
- The first attempt is retained in `../person_b_attempt1/`, including its Q3 failure record. Its whole-object fingerprint erroneously included a process-local analyzer cache. The corrected fresh baseline/Q2 held-out prediction files exactly match the first measurements; Q3 selection is also identical. The correction did not change model parameters, thresholds or inputs.
- Original passages, model binaries and credentials are not included in these result artifacts. There was no Kaggle submission, external model labeling, GitHub push, PR or Overleaf edit.
- These files finish local steps 5–8. Formal reproduction/delivery review (9), integrated report and contribution/AI-use statements (10), internal GitHub delivery (11), Overleaf (12) and group handoff (13) remain. Do not describe the entire Person B handoff as finished yet.
