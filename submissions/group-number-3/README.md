# Group Number 3 — Human or AI?

Yuchen Feng (`yf467`); Aarushi Singh (NetID pending); Vivian Li (registered name/NetID pending).

## Setup

Core experiments tested with Python 3.14.8 on macOS arm64. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r submissions/group-number-3/requirements.txt
cd submissions/group-number-3
```

Download the five official [competition CSVs](https://www.kaggle.com/competitions/cornell-tech-cs-5785-combined-2026-ai-vs-human-text/data)
into `data/`. Use the committed `splits/splits.csv`; do not regenerate it.

## Core commands

```bash
python src/evaluate.py --model tfidf_logreg
python src/predict.py --model tfidf_logreg --out submission.csv
python src/complete_person_b.py
python -m unittest discover -s tests
```

`complete_person_b.py` runs fresh Q2 TF-IDF curves and Q3 full-pipeline pseudo-labeling.
Add `--rerun-style` for style-model curves. Q2 uses subset seeds 0/1/2 and one full-pool fit;
split/style seed is 42. Parameters are in `src/models.py` and `config/person_b.json`.
Prediction trains on all 10,000 labels and writes 3,000 `id,label` AI probabilities.
The command above generates the baseline; the final team model is selected separately.

Other experiment entrypoints: `src/model_table.py`, `src/tune.py`, `src/tune_gbm.py`,
`src/error_analysis.py`, `src/robustness.py`, `src/newline_check.py`, `src/style_importance.py`.
The earlier frozen-feature study remains in `src/person_b.py`; run stages
`verify`, `baseline`, `q2`, `q3` in that order.

## Transformer and ensemble

Run from the team directory. Transformer dependencies are separate from the tested core environment.

```bash
pip install -r requirements-transformer.txt
python src/finetune_transformer.py --mode val
python src/ensemble.py --mode val
python src/finetune_transformer.py --mode full
python src/predict.py --model tfidf_logreg --out submission.csv
python src/ensemble.py --mode test --a sub_distilroberta-base.csv --b submission.csv --w 0.5 --out sub_ensemble.csv
```

The default transformer is `distilroberta-base` (seed 42, two epochs, learning rate `2e-5`,
maximum length 256). Validation mode generates the intermediate predictions used by the ensemble.
Generated results, reports, submissions, data and model caches stay local and are ignored by Git.
