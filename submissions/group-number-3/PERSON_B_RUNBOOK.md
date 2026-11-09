# Person B: Q2 learning curves and Q3 unlabeled data

Owner: Yuchen Feng. These are the two experiments assigned to Person B in the shared planning document (15 points total). Experiments are local; they do not submit to Kaggle or edit Overleaf.

## Inputs and fixed protocol

Use the teacher-linked competition's original `train.csv` and `unlabeled.csv`, and the unchanged shared `splits/splits.csv` supplied by Aarushi. Expected SHA256 values are committed in `config/person_b.json`. The runner checks them before every stage. Data provenance and installation checks are in `PERSON_B_DATA_CHECK.md`, `person_b_data_audit.json`, and `splits/shared_split_manifest.json`.

Do not run `python src/data.py`: that entrypoint generates a split. This runner only reads the verified shared file. Original data, the virtual environment, and model caches stay ignored by Git. The shared split and small result tables are eligible for tracking.

The model is the existing `src/models.py::tfidf_logreg(C=4.0)`, unchanged: word TF-IDF (1–2 grams, min_df=2, max_features=200000) plus character-within-word TF-IDF (3–5 grams, min_df=3, max_features=300000), followed by logistic regression (C=4, max_iter=2000). All remaining parameters and library versions are recorded in `results/person_b/run_manifest.json`. The installed scikit-learn defaults use L2 regularization and the lbfgs solver; the model constructor is not modified.

- **Baseline:** evaluate separately on the fixed random and OOD folds. Historical `results/val_results.jsonl` is preserved. The random-fold model is cached locally for the controlled comparisons.
- **Q2:** nested, class-balanced subsets of 500, 1000, 2000, 5000 and 8000 labeled examples, drawn with seed 42 from the same 8000-example pool. Every size uses the same untouched 2000-example random validation fold. Each model fits its TF-IDF vocabulary and IDF on its own training subset. Hyperparameters stay constant. The 8000-example result reuses the exact full-pool baseline fit; it is not a new or averaged measurement. Save both training and validation AUROC, subset IDs, predictions, and the curve.
- **Q3:** one round of self-training. The supervised 8000-example baseline predicts all 3000 original unlabeled examples. Accept pseudo-human when p(AI) <= 0.05, pseudo-AI when p(AI) >= 0.95. Discard the uncertain middle. Freeze the baseline's fitted vectorizers and IDF; clone and refit only the classifier on the original labeled rows plus selected pseudo-labeled rows, with equal weight. If none qualify, retain the supervised model. Compare on the same 2000 validation IDs. Thresholds, weight, representation and number of rounds are fixed before fitting; validation labels are used only for AUROC, never for pseudo-labeling, fitting or threshold selection. TF-IDF fingerprints must remain identical.

The hidden test set is not read by these experiments. No external model labels the competition data. Confidence scores are model estimates, not verified pseudo-label accuracy.

## Run from the repository root

The environment is locked in `requirements-person-b.lock.txt`. On this Mac, the repository root contains `.venv`; see `PERSON_B_ENVIRONMENT.md` for setup details.

```bash
.venv/bin/python -m unittest discover -s submissions/group-number-3/tests -v
.venv/bin/python submissions/group-number-3/src/person_b.py verify
.venv/bin/python -u submissions/group-number-3/src/person_b.py baseline
.venv/bin/python -u submissions/group-number-3/src/person_b.py q2
.venv/bin/python -u submissions/group-number-3/src/person_b.py q3
```

Run the fitting stages sequentially. The runner limits native numerical libraries to two threads and retains sparse matrices. It refuses to overwrite a completed stage, preserves failure records, checks its own cache hash, and records source-code hashes and Git commits. Keep the default result directory for the primary run. For a fresh reproduction, provide the **same new directory** to all four commands, for example `--output-dir submissions/group-number-3/results/person_b_reproduction`; allow several minutes and adequate memory. A cache may be reused only as the already fitted full-pool control within that protocol; `baseline` itself always fits from scratch.

Finish baseline → Q2 → Q3 in one output directory before starting another reproduction of the same protocol. The disposable model cache is shared per protocol, and a fresh baseline replaces it; this does not change saved result tables, but an earlier unfinished run will reject a cache whose file hash no longer matches. Concurrent runs of the same protocol are not supported.

## Outputs

`results/person_b/` contains `run_manifest.json`, stage completion/failure records, baseline scores, five-row learning-curve table and PNG/SVG, subset IDs and held-out predictions, plus the two-row Q3 comparison and selected pseudo-label IDs. No raw passages are included in these result artifacts. Each completed experiment should receive a descriptive local commit; pushing and the internal team PR are a later delivery step.

The original historical log has random AUROC 0.9506 and OOD AUROC 0.9359 (November 1). These are reference values, not results from this runner. There is no historical file hash proving byte-for-byte identity of the old split; report fresh measurements as fresh measurements, even if their rounded values agree.

## Preserved first attempt

`results/person_b_attempt1/` preserves the first baseline/Q2 measurements and the Q3 failure record. That Q3 attempt stopped because a whole-estimator `joblib.hash` included scikit-learn's process-local `_stop_words_id` cache, which changes when a loaded word analyzer is first used. Direct checks showed the vocabulary and IDF values stayed identical. The corrected representation check hashes vectorizer parameters, vocabulary-to-column mappings, IDF values and union weights; a regression test checks that cache refreshes pass while real vocabulary/IDF changes fail. The current `results/person_b/` uses the corrected source hash and starts from a fresh baseline. No thresholds, model parameters or data were changed in response to a validation score.
