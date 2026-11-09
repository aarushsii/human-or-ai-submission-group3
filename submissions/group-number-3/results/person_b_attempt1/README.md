# Preserved initial attempt; not the completed Q3 result

The initial baseline and Q2 fits completed. Q3 selected 628 of 3000 unlabeled rows (247 pseudo-human, 381 pseudo-AI) and fitted its classifier, but stopped before accepting a result because the original whole-estimator fingerprint changed. The failure JSON and console output are retained here. There is no `q3_completed.json` in this directory.

Investigation of the hash-checked original model cache found:

- `joblib.hash(features)` immediately after loading matched the original `7cd985db2518a09c143ffe93b4718e33`.
- A plain `features.transform(unlabeled_text)` changed that whole-object hash to `1550fbc83e89e2c744981892c4acb29f`.
- Both vectorizers' vocabulary mappings and IDF arrays were unchanged. This check did not fit any model or use validation labels.
- The installed scikit-learn `feature_extraction/text.py::_check_stop_words_consistency` stores `id(self.stop_words)` in `_stop_words_id`. The first word-analyzer use in another process refreshes this process-local cache even when transformation parameters and learned features stay identical.

The original guard was too broad: it treated an implementation cache as learned representation. The corrected source compares vectorizer parameters, vocabulary-to-column mappings, IDF bytes and union weights, and tests that real vocabulary/IDF changes are detected. Fresh measurements from the corrected protocol belong in `../person_b/`; do not mix run manifests. Input data, split, model parameters, sample selection and pseudo-label thresholds were not changed in response to the failure or validation performance. Earlier commits preserve the initial generated SVG; its harmless trailing whitespace was subsequently normalized.
