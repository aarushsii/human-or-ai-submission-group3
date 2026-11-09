# Fixed shared validation split

`splits.csv` is the unchanged file supplied by teammate Aarushi Singh, received and verified on November 9, 2026. It was copied into this directory after verification; it was not regenerated.

- SHA256: `ced00ff13b0e58fee0b332e74e8726aea90110bcc45e1cf08796bc265645f95d`
- Rows: 10,000, one per official training ID, with matching labels.
- Columns: `id`, `label`, `random_fold`, `cluster`, `ood_fold`.
- `random_fold`: 8,000 training / 2,000 validation, stratified with 4,000/4,000 training labels and 1,000/1,000 validation labels. Assignments match the existing SEED=42 split logic.
- `ood_fold`: 7,541 training / 2,459 validation. Whole clusters 5, 6 and 0 are held out according to the existing rule.

The installed file's hash, counts, official training-data hash and loader checks are recorded in `shared_split_manifest.json`. Existing `load_splits()` and `get_split()` read this file successfully. No baseline or Person B experiment has been run yet.

Use this fixed file for comparisons. Do not run the split-generation entrypoint as part of routine experiment setup. If the team adopts a different file later, record its new hash and re-evaluate the common baseline.

The sender indicated that the original file had been retained. No earlier file hash independently links it to the historical baseline AUROC; reproduction of that result remains a separate step.

Only this shared split is exempted from the repository's blanket CSV ignore rule. Raw competition files under `data/` remain ignored.
