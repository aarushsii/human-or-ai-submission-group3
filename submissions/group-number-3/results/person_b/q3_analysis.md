# Q3: using the official unlabeled data

Local experiment draft for later report integration. Sources: `q3_run_details.json`, `pseudo_label_results.csv`, `q3_selected_pseudo_labels.csv` and `run_manifest.json`. This is the completed corrected run. The initial feature-check failure is retained separately in `../person_b_attempt1/`.

## Q3.1: method and leakage prevention

We performed one round of confidence-filtered self-training using the fixed random split. First, the unchanged TF-IDF plus logistic regression baseline was trained on 8,000 labeled examples. It predicted AI probabilities for all 3,000 official unlabeled texts. Before evaluating self-training, we fixed acceptance thresholds at 0.05 and 0.95. We retained 247 pseudo-human and 381 pseudo-AI examples, froze the baseline vocabulary and IDF weights, and refitted only logistic regression on the combined 8,628 rows with equal sample weights. The same 2,000 validation examples were used only for scoring. Their texts never entered fitting, and their labels never determined pseudo-labels or threshold choices.

## Q3.2: observed comparison

| Method | True labeled rows | Added pseudo-labeled rows | Validation AUROC | Change from supervised |
|---|---:|---:|---:|---:|
| Supervised only | 8000 | 0 | 0.950644 | 0.000000 |
| With unlabeled data | 8000 | 628 | 0.950170 | -0.000474 |

Selection: p(AI) <= 0.05 gives pseudo-label 0, p(AI) >= 0.95 gives pseudo-label 1. The 2372 middle-confidence texts are excluded. Pseudo-labels are model predictions, not verified ground truth. All 2000 validation IDs match the supervised comparison. The semantic fingerprint of vocabulary mappings, IDF values, vectorizer parameters and union weights is identical before and after Q3. The classifier converged in 47 iterations without recorded warnings. Neither experiment reads `test.csv` or makes a Kaggle submission.

## Q3.3: English discussion

Adding pseudo-labeled data changed validation AUROC from 0.950644 to 0.950170, a decrease of 0.000474. Thus, this fixed self-training configuration did not improve the supervised baseline on the shared validation set. Confidence filtering retained only 628 of 3,000 unlabeled examples, so most extra texts contributed no training signal. Incorrect confident predictions could reinforce existing mistakes, while selecting easy examples may provide little new information. We cannot measure pseudo-label accuracy because their true labels are unavailable. The small decrease on one split does not establish a reliable harmful effect or rule out other semi-supervised methods. We retain the supervised baseline as the reference.
