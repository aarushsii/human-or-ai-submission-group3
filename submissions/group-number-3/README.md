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

### Person B: checked Q2/Q3 experiments

Yuchen Feng (`yf467`), with Codex assistance. From the **repository root**, use the pinned environment in `submissions/group-number-3/requirements-person-b.lock.txt` and the verified original competition CSVs. Use the committed `splits/splits.csv`; do not generate a replacement. Completed primary results are under `submissions/group-number-3/results/person_b/`.

To reproduce into a fresh directory:

```bash
.venv/bin/python -m unittest discover -s submissions/group-number-3/tests -v
.venv/bin/python submissions/group-number-3/src/person_b.py verify --output-dir submissions/group-number-3/results/person_b_reproduction
.venv/bin/python -u submissions/group-number-3/src/person_b.py baseline --output-dir submissions/group-number-3/results/person_b_reproduction
.venv/bin/python -u submissions/group-number-3/src/person_b.py q2 --output-dir submissions/group-number-3/results/person_b_reproduction
.venv/bin/python -u submissions/group-number-3/src/person_b.py q3 --output-dir submissions/group-number-3/results/person_b_reproduction
.venv/bin/python submissions/group-number-3/src/check_person_b_results.py --candidate submissions/group-number-3/results/person_b_reproduction --report submissions/group-number-3/results/person_b_reproduction/comparison.json
```

The runner refuses to overwrite completed stages. After intentionally integrating a refactored `models.py` that preserves this baseline configuration, the comparison tool accepts `--allow-model-refactor`; it still requires matching parameters, inputs, subset IDs, scores and predictions. See [the full runbook](PERSON_B_RUNBOOK.md), [QA evidence](results/person_b_qa/README.md), and [report integration materials](report/README.md).

Random baseline AUROC: 0.950644; OOD: 0.935863. Q2 validation AUROC rises from 0.872922 (500 rows) to 0.950644 (8000 rows). Fixed-feature Q3 adds 628 pseudo-labels and obtains 0.950170, a change of -0.000474. These are local validation scores, not Kaggle leaderboard scores. Additional experiments by other team members retain their own methods and attribution.

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
