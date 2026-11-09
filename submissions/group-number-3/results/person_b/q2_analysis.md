# Q2: effect of labeled training-set size

Local experiment draft for later report integration. Source: `learning_curve_results.csv`, `q2_run_details.json`, `q2_subset_ids.json` and `run_manifest.json`. The model constructor and hyperparameters are unchanged across sizes; seed 42 defines nested balanced subsets. All rows use the same 2000 validation examples. TF-IDF is fitted only on each training subset. The 8000-example row is the exact random-fold baseline fit, reused without an additional training run.

## Q2.1: observed scores

| Labeled training examples | Training AUROC | Validation AUROC |
|---:|---:|---:|
| 500 | 1.000000 | 0.872922 |
| 1000 | 1.000000 | 0.906055 |
| 2000 | 1.000000 | 0.922570 |
| 5000 | 1.000000 | 0.944931 |
| 8000 | 1.000000 | 0.950644 |

Training values are rounded to six decimals; the unrounded 8000-example training AUROC is 0.999999875. AUROC measures ranking, so an AUROC near 1 does not assert perfect classification at a fixed probability threshold. All fits converged without recorded warnings.

## Q2.2: learning curves

Use `learning_curve.png` or the vector version `learning_curve.svg`. Both show training and validation AUROC against actual training-set size on a linear x-axis. The PNG has been visually inspected for labels, legend, clipping and agreement with the score table.

## Q2.3: English discussion

Training AUROC stays essentially 1.0000 at every training size, whereas validation AUROC rises from 0.8729 with 500 examples to 0.9506 with 8,000. This gap suggests overfitting, especially with limited labels, rather than an inability to fit the training data. Increasing the labeled sample size reduces the gap from about 0.1271 to 0.0494 and improves generalization on the fixed validation set. Returns diminish: the first 500 additional examples improve validation AUROC by 0.0331, while increasing from 5,000 to 8,000 adds only 0.0057. More labels may still help, but the curve does not establish performance beyond 8,000 examples. These findings concern one sampling seed and one validation split; further repetitions would be needed to assess variability and performance under distribution shift.
