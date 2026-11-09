# Person B report: Q2 and Q3

Yuchen Feng (yf467), Group Number 3. Local report text prepared for team integration on November 9, 2026. This file does not claim the full team report, final model selection or course submission is complete.

## Q2.1: fixed-model experiment and observed results

We used the team's word (1-2 grams) and char_wb (3-5 grams) TF-IDF logistic regression. The classifier uses C=4 and at most 2,000 iterations. Seed 42 defines nested, balanced subsets of the shared 8,000-row training pool. Each TF-IDF transform is fitted only on its current subset. All sizes use the same 2,000 validation rows. The full-pool point reuses the baseline fit.

| Training rows | Training AUROC | Validation AUROC |
|---:|---:|---:|
| 500 | 1.000000 | 0.872922 |
| 1,000 | 1.000000 | 0.906055 |
| 2,000 | 1.000000 | 0.922570 |
| 5,000 | 1.000000 | 0.944931 |
| 8,000 | 1.000000 | 0.950644 |

Scores are rounded to six decimals. The unrounded 8,000-row training AUROC is 0.999999875. AUROC evaluates ranking and does not imply perfect classification at a fixed threshold. The 2,000-row learning subset is sampled from the shared training pool; it is not a substitute use of train_starter_2000.csv.

## Q2.2: learning curves

![Training and validation AUROC versus labeled training-set size](person_b_learning_curve.png)

Figure: the same configuration and validation IDs are used throughout. The training curve remains near 1, while validation AUROC improves with diminishing gains at larger sample sizes.

## Q2.3: discussion (119 words)

Training AUROC stays essentially 1.0000 at every training size, whereas validation AUROC rises from 0.8729 with 500 examples to 0.9506 with 8,000. This gap suggests overfitting, especially with limited labels, rather than an inability to fit the training data. Increasing the labeled sample size reduces the gap from about 0.1271 to 0.0494 and improves generalization on the fixed validation set. Returns diminish: the first 500 additional examples improve validation AUROC by 0.0331, while increasing from 5,000 to 8,000 adds only 0.0057. More labels may still help, but the curve does not establish performance beyond 8,000 examples. These findings concern one sampling seed and one validation split; further repetitions would be needed to assess variability and performance under distribution shift.

## Q3.1: method and validation-label isolation (100 words)

We performed one round of confidence-filtered self-training using the fixed random split. First, the unchanged TF-IDF plus logistic regression baseline was trained on 8,000 labeled examples. It predicted AI probabilities for all 3,000 official unlabeled texts. Before evaluating self-training, we fixed acceptance thresholds at 0.05 and 0.95. We retained 247 pseudo-human and 381 pseudo-AI examples, froze the baseline vocabulary and IDF weights, and refitted only logistic regression on the combined 8,628 rows with equal sample weights. The same 2,000 validation examples were used only for scoring. Their texts never entered fitting, and their labels never determined pseudo-labels or threshold choices.

## Q3.2: supervised comparison

| Method | True labeled rows | Pseudo-labeled rows | Validation AUROC |
|---|---:|---:|---:|
| Supervised only | 8,000 | 0 | 0.950644 |
| With unlabeled data | 8,000 | 628 | 0.950170 |

Change: -0.000474. Selection retained 247 pseudo-human and 381 pseudo-AI rows; the other 2,372 unlabeled rows were excluded. The fixed TF-IDF representation passed the before/after semantic fingerprint check. No validation labels determined pseudo-labels, thresholds or training weights.

## Q3.3: discussion (101 words)

Adding pseudo-labeled data changed validation AUROC from 0.950644 to 0.950170, a decrease of 0.000474. Thus, this fixed self-training configuration did not improve the supervised baseline on the shared validation set. Confidence filtering retained only 628 of 3,000 unlabeled examples, so most extra texts contributed no training signal. Incorrect confident predictions could reinforce existing mistakes, while selecting easy examples may provide little new information. We cannot measure pseudo-label accuracy because their true labels are unavailable. The small decrease on one split does not establish a reliable harmful effect or rule out other semi-supervised methods. We retain the supervised baseline as the reference.

## Reproducibility and evidence

The original data came from the teacher-linked [official competition](https://www.kaggle.com/competitions/cornell-tech-cs-5785-combined-2026-ai-vs-human-text/data). Original CSV and shared split hashes, full parameters, dependencies, source hashes and validation-ID fingerprints are in `../results/person_b/run_manifest.json` and the data audit. Primary experiment source: bb8eaf5f8811755b3cc3f3c19b8eaaf6944c10de. Original model baseline: c7be9f30ac94e34573a9057d429c77f91d52ad6d.

A clean-checkout reproduction and a separate integration run with team update 0e09450 both reproduced the saved probabilities exactly. Each comparison passed 51 checks. This validates this Mac and the installed environment; a fresh dependency installation and other platforms were not tested. Commands and the comparison tool are documented in `../PERSON_B_RUNBOOK.md`.

## Integration with Aarushi's November 9 update

Aarushi's `results/learning_curve.csv` adds two models, three seeds and 250/4,000-row points. It does not contain the required 5,000-row point or training AUROC. The five-row table and training-versus-validation figure above supply those required Q2 items; her multi-seed curves can be supplementary evidence. Values at smaller sizes differ because the sampling seeds and subset construction differ.

Her `results/pseudo_label.csv` includes self-training and a style-GBM teacher, each at three thresholds. Her student refits TF-IDF on augmented texts; the controlled study above freezes the labeled-only representation. Her 0.95 self-training result is therefore a separate experiment from our 0.950170 result. Her best teacher-student value is 0.9537 versus a rounded 0.9506 control, an exploratory result selected among several settings. Attribute that extension to Aarushi and disclose selection on the shared validation set. It is not a new independent confirmation of improvement and is not evidence that the fixed-feature study improved.

The fixed model used for Q2/Q3 need not be the final Kaggle model. The team should state that distinction and agree on the final selection. See `TEAM_UPDATE_REVIEW_ZH.md` for the reviewed scope and remaining group decisions.
