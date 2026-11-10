# Group Number 3 — Human or AI?

Members: Yuchen Feng (`yf467`); Aarushi (NetID to confirm); Vivian (full name and NetID to confirm).

## Setup

Tested with Python 3.14.8 on macOS arm64. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r submissions/group-number-3/requirements.txt
cd submissions/group-number-3
```

Download the official [competition data](https://www.kaggle.com/competitions/cornell-tech-cs-5785-combined-2026-ai-vs-human-text/data)
into `data/`: `train.csv`, `unlabeled.csv`, `test.csv`, `train_starter_2000.csv`, and `sample_submission.csv`.
Keep the committed `splits/splits.csv`; do not regenerate it.

## Train, evaluate, and predict

Run these commands from the team directory:

```bash
python src/evaluate.py --model tfidf_logreg
python src/predict.py --model tfidf_logreg --out submission.csv
```

Evaluation fits on each fixed random/OOD training fold and scores its validation fold.
Prediction fits word+char TF-IDF logistic regression (`C=4`, `max_iter=2000`) on all
10,000 labeled rows and writes 3,000 AI-class probabilities with columns `id,label`.
This command regenerates the baseline submission; final team model selection is pending.

## Experiments

```bash
python src/model_table.py
python src/tune.py
python src/tune_gbm.py
python src/complete_person_b.py
python src/error_analysis.py
python src/robustness.py
python src/newline_check.py
python src/style_importance.py
```

`complete_person_b.py` freshly fits Q2 TF-IDF curves and all Q3 teacher/threshold settings.
Use `--rerun-style` to also fit style-model curves, or run `learning_curve.py` and
`pseudo_label.py` separately. Q2 uses stratified subset seeds 0/1/2 and sizes
250/500/1000/2000/4000/5000/8000; the full 8,000-row pool is fitted once.
Q3 uses self/style teachers, thresholds 0.99/0.95/0.90, and refits the complete student pipeline.
Style models and the original split generation use seed 42. Other parameters are in `src/models.py`.
Generated metrics and figures stay local in ignored `results/`; no prior results are required.

The earlier seed-42 frozen-feature study uses `config/person_b.json`:

```bash
python src/person_b.py verify
python src/person_b.py baseline
python src/person_b.py q2
python src/person_b.py q3
```

```bash
python -m unittest discover -s tests
```
