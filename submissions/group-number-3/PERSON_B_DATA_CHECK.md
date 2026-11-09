# Person B data readiness

Checked on November 9, 2026, America/New_York. This is a local input-data audit, not a model result.

## Official source verified

The teacher's Canvas announcement was read live and its exact Kaggle invitation was followed again after sign-in. It resolves to **CornellTech CS5785 (combined) 2026 - AI vs Human text**, hosted by Ayush Sekhari. The official Data page lists the expected five CSVs. All five files were freshly downloaded using **Download all files -> Download as zip**, safely extracted and compared by SHA256. Every official file is byte-identical to the pre-existing project copy, material copy and desktop original. Active project data was then copied directly from this verified official extraction. No CSV content was edited.

- Teacher announcement: https://canvas.cornell.edu/courses/88330/discussion_topics/1107787
- Teacher invitation: https://www.kaggle.com/t/0cd67c59ef5245a89853abcbaef80c08
- Official data: https://www.kaggle.com/competitions/cornell-tech-cs-5785-combined-2026-ai-vs-human-text/data

The audit JSON contains the archive hash and each file's hash. Data provenance is now verified; formal experiments still require the agreed shared split.

## Data connected

The five competition CSVs are now available under this team directory's `data/` folder, as required by the existing loaders in `src/data.py`.

| File | Rows | Labels / role |
|---|---:|---|
| `train.csv` | 10,000 | 0: 5000, 1: 5000 |
| `train_starter_2000.csv` | 2,000 | 0: 1000, 1: 1000 |
| `unlabeled.csv` | 3,000 | No label column |
| `test.csv` | 3,000 | No label column |
| `sample_submission.csv` | 3,000 | 0.5 placeholders; not ground-truth labels |

## Verified checks

All 31 local data-quality checks passed; official-source verification also passed using the freshly downloaded official files. Full counts, hashes and results are in `person_b_data_audit.json`.

- Each CSV's SHA256 matches the saved source inventory, the source material copy and the desktop original. Original files were not edited.
- Column names and row counts match the inventory. Every file has nonempty, unique IDs.
- Every text field is present and nonempty. The labeled datasets contain only labels 0 and 1, with the expected balanced class counts.
- The starter dataset's IDs, texts and labels match a subset of `train.csv`; its 2,000 rows are not additional labeled examples.
- Train, unlabeled and test ID sets are pairwise disjoint.
- No duplicate texts were found within each text dataset or between train/unlabeled/test. Checks covered exact text and audit-only keys formed by collapsing whitespace and case-folding. Stored texts were not transformed.
- No conflicting training labels were found for the normalized text keys.
- The test IDs and sample-submission IDs match in exactly the same order. Sample-submission values are format placeholders, not hidden test labels or model predictions.
- The existing `load_train()`, `load_unlabeled()` and `load_test()` functions return 10,000, 3,000 and 3,000 rows respectively. `make_splits()` and `load_splits()` were not called.
- All five data files are ignored by Git. The previous code and environment records retain their original SHA256 hashes.

## Current state

- Branch: `yuchen/person-b`; source commit: `c7be9f30ac94e34573a9057d429c77f91d52ad6d`.
- The user-authorized shared split is now installed at `splits/splits.csv`, unchanged from the verified attachment. No split was generated or edited. See `splits/shared_split_manifest.json` for installation checks.
- No model was fitted and no AUROC was calculated.
- The raw data and the new audit records have not been uploaded to GitHub. This audit report contains counts and hashes, with no raw passages or ID lists.
- The next preparation step can be writing Person B experiment entrypoints that require an explicit validated shared split. Comparable baseline/Q2/Q3 results still require the shared split to be settled.

## 中文说明

第四步已完成：五份数据已经放到真正的团队项目里，原有读取函数能找到它们，检查全部通过。原始 CSV 保留原样且被 Git 忽略，不会因为普通代码提交自动进入仓库。`starter` 是训练集子集，提交示例的 0.5 也只是格式占位值。切分文件仍未生成，模型还没有训练。

## Latest checkpoint

Official source verification completed 2026-11-09T14:26:07.565949-05:00. The account and team were also read: current Kaggle username `yuchenfeng030907`, team `Group Number 3`. Two members were visible: Aarushi Singh and Yuchen Feng; Vivian was not visible in this check. No account or team settings were changed. The Kaggle countdown displayed a closing time of November 11, 2026, 23:59 America/New_York.

The user subsequently authorized using the verified attachment to complete the input setup. It is now installed unchanged at `splits/splits.csv` (SHA256 `ced00ff13b0e58fee0b332e74e8726aea90110bcc45e1cf08796bc265645f95d`). The existing `load_splits()` and `get_split()` return the verified 8,000/2,000 random and 7,541/2,459 OOD partitions. A scoped Git-ignore exception allows only this shared CSV to be tracked; raw competition CSVs and `.venv` remain ignored. The original attachment remains preserved separately. No model has been fitted and nothing has been pushed. Input prerequisites are now complete; next is Step 5, implementation of reproducible experiment entrypoints, followed by Step 6 baseline reproduction.
