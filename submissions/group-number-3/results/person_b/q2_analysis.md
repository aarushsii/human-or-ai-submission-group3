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

## 中文解释

可以把训练集理解为练习题，把验证集理解为固定的一套模拟考试题。模型在练习题上的排序成绩始终接近满分，但在新题上的成绩较低，提示有过拟合。增加训练材料后，模拟考试成绩从 0.872922 升到 0.950644，说明更多有标签数据在这次实验中有帮助。

提升的速度逐渐放缓：500 增到 1000 条提高约 0.0331，而 5000 增到 8000 条只再提高约 0.0057。这不能证明继续加数据完全没用，也不能预测超过 8000 条后的确切表现。我们目前只有一个固定抽样种子和一套固定验证题，还没有测量不同抽样的波动，也不能把这些分数当作 Kaggle 隐藏测试集的成绩。
