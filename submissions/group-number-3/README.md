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
pip install -r requirements.txt
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

| # | Experiment | Report section | Notebook |
|---|-----------|----------------|----------|
| 1 | Baseline: TF-IDF (word + char n-grams) + Logistic Regression | Model comparison | `experiments/01_baseline_tfidf_logreg.ipynb` |
| 2 | Model comparison (NB, SVM, boosting, neural) | Model comparison | `experiments/02_model_comparison.ipynb` |
| 3 | Learning curves vs. training set size | Effect of data size | `experiments/03_learning_curves.ipynb` |
| 4 | Pseudo-labeling with `unlabeled.csv` | Unlabeled data | `experiments/04_pseudo_labeling.ipynb` |
| 5 | Error analysis and generalization | Generalization | `experiments/05_error_analysis.ipynb` |

## Results

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
