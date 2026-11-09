# Human or AI? — CS 5785 Kaggle Competition (Group Number 3)

Binary text classifier that predicts the probability a passage is AI-generated.
Cornell Tech CS 5785 Applied Machine Learning, Fall 2026.

- **Task:** Human (0) vs. AI-generated (1) text classification
- **Metric:** AUROC
- **Deadline:** November 11, 2026
- **Team:** Group Number 3 — _[Name 1]_, _[Name 2]_, _[Name 3]_

## Setup

```bash
git clone https://github.com/aarushsii/Kaggle_Group3_Competition.git
cd Kaggle_Group3_Competition
python -m venv .venv && source .venv/bin/activate   # or use conda
pip install -r submissions/group-number-3/requirements.txt
cd submissions/group-number-3
```

### Data

The competition data is **not** included in this repo. Download it from the Kaggle competition page
("Download All") and place the files in `data/`:

```
data/
  train.csv
  unlabeled.csv
  test.csv
  train_starter_2000.csv
  sample_submission.csv
```

## Repository Structure

```
README.md
requirements.txt
data/                 # competition CSVs (gitignored)
src/
  data.py             # data loading + fixed validation splits
  features.py         # feature extraction (TF-IDF, stylometric, etc.)
  models.py           # model definitions
  predict.py          # trains final model, writes submission.csv
experiments/          # notebooks for each report section
results/              # metrics, tables, and figures used in the report
```

## Reproducing the Final Submission

```bash
python src/predict.py
```

This writes `submission.csv` (3,000 rows, columns `id,label`) to the project root.
All random seeds are fixed in `src/data.py` and the model configs. _[Update with final command and any flags.]_

## Validation Strategy

- **Random split:** 80/20 stratified split of `train.csv` with a fixed seed.
- **Out-of-distribution split:** passages clustered by topic/style; whole clusters held out to
  approximate the distribution shift in the test set.

All reported validation scores use these shared splits so results are comparable across team members.

## Experiments

| # | Experiment | Report section | Entrypoint |
|---|-----------|----------------|----------|
| 1 | Baseline: TF-IDF (word + char n-grams) + Logistic Regression | Model comparison | `experiments/01_baseline_tfidf_logreg.ipynb` |
| 2 | Model comparison (NB, SVM, boosting, neural) | Model comparison | `experiments/02_model_comparison.ipynb` |
| 3 | Learning curves vs. training set size | Effect of data size | `src/person_b.py q2` |
| 4 | Pseudo-labeling with `unlabeled.csv` | Unlabeled data | `src/person_b.py q3` |
| 5 | Error analysis and generalization | Generalization | `experiments/05_error_analysis.ipynb` |

## Results

### Person B: completion of Aarushi's shared experiments

Original Person B methods and reference results: Aarushi. Missing rubric items and integration: Yuchen Feng (`yf467`), with Codex assistance.

From the repository root:

```bash
.venv/bin/python submissions/group-number-3/src/complete_person_b.py
```

This rebuilds TF-IDF learning curves with the existing seeds 0/1/2, adds 5,000 rows and training AUROC, preserves Aarushi's original style validation points and Q3 reference table, and prepares the required report tables/figure. The original teacher-linked data and fixed committed split are checked by hash. No new split or Kaggle submission is generated.

- Q2 primary table/figure: `results/learning_curve_required.csv` and `results/learning_curve_train_val.png`; validation means for 500/1000/2000/5000/8000 are 0.869945/0.896831/0.924322/0.943272/0.950644.
- Q3 primary reference: Aarushi's unchanged `results/pseudo_label.csv`; `results/pseudo_label_report.csv` extracts control 0.9506 and style teacher 0.9537 (threshold 0.95, 2612 pseudo-labels). Threshold selection on the same validation fold is exploratory.
- A separate local repeat is in `results/person_b_team_recheck/`: style teacher selected 2609 and reached 0.954365 versus 0.950644. Its different style scores are not substituted into the primary table.
- Completed Q2/Q3 text and LaTeX, figure, contribution and AI-use material: [report package](report/README.md). Overleaf is still pending.
- [Runbook](PERSON_B_RUNBOOK.md) documents exact commands, environment and provenance. Earlier seed42/frozen-feature experiments under `results/person_b/` are supplementary historical studies.

| Model | Val AUROC (random) | Val AUROC (OOD) | Public LB |
|-------|-------------------|-----------------|-----------|
| _TBD_ | | | |

## Pretrained Models and External Resources

_List any publicly available pretrained models or embeddings used, with licenses (required by competition rules).
No external labeled datasets and no commercial LLM APIs are used for predictions._

## AI Tool Disclosure

_Briefly describe how AI assistants (e.g. Claude, ChatGPT, Copilot) were used — e.g. code scaffolding,
debugging, concept explanations, report editing. All modeling decisions, experiments, and results were
run and verified by the team._
