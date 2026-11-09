# 11 月 9 日团队更新核对

本记录核对 Aarushi 15:08 在项目群中提到的 GitHub 和共享文档更新。远端核对版本为 `0e09450db2be0281ad8ebf47f104a33da5308cdc`，相对旧起点新增 9 个提交、23 个文件；结束前再次 fetch 后仍为该版本。共享文档首次读取的修改时间为 15:06:52，结束前发现更新为 2026-11-09 15:11:49 America/New_York，并重新读取了新增内容。群消息只读取，没有代用户回复。

## 已核实的更新

| 内容 | 仓库或页面证据 | 核对结果与边界 |
|---|---|---|
| 模型比较 | `src/models.py`、`src/features.py`、`results/val_results.jsonl` | 已加入 word/char LR、NB、校准线性 SVM、style GBM；style 随机 AUROC 0.9945、OOD 约 0.9900。我们从保存的验证概率重算 style 随机 AUROC 为 0.994542；没有宣称从头重跑了她所有模型。 |
| 原基线兼容 | 新旧模型参数与 `results/val_predictions.csv` | TF-IDF 基线所有参数相同；她保存的验证 ID/标签与我们同一 2000 条相符。LR AUROC 重算为 0.950644，预测与我们只有保存精度量级的差别。 |
| C 调参 | `results/tune_C.csv` | C=8 为 0.9512，C=4 为 0.9506，其余较大 C 接近。文档说保留 C=4，但这不是“C=4 的验证分数严格最高”。我们的固定 C=4 是原先就采用的基线。 |
| Q2 学习曲线 | `src/learning_curve.py`、`results/learning_curve.csv/png` | 两模型、seed 0/1/2、规模 250/500/1000/2000/4000/8000；完整 8000 只跑一次。CSV 只有验证 AUROC，没有训练 AUROC，也没有指定的 5000 点。我们的五行训练/验证表和双曲线补足必做项；小规模数值不同有抽样设置依据。 |
| Q3 伪标签 | `src/pseudo_label.py`、`results/pseudo_label.csv` | 监督控制 0.9506；self 在 0.99/0.95/0.90 阈值加 81/628/1114 条，AUROC 为 0.9506/0.9501/0.9501。style teacher 加 2095/2612/2727 条，为 0.9517/0.9537/0.9534。所有分数在 CSV 中仅保留四位小数。 |
| Q3 与我们的差异 | 两份源代码 | 她把 TF-IDF 在增加伪标签的文本上重新 fit；我们冻结原有词表和 IDF，只重新训练分类器。我们的 0.950170 与她的 0.9501 不应直接混写；同为 628 条并不使两种方法完全相同。最高 teacher 结果在多个设置中选出，只能作为探索性结果，不能当独立确认。 |
| 格式特征 | `newline_check.csv`、`style_importance.csv`、原始 CSV 汇总 | newline_ratio 置换重要性最高，AUROC drop 约 0.2706。去掉此特征，style 验证从 0.9945 到 0.9418。原始 train 中，5000 条 human 的双换行文本为 0，5000 条 AI 为 3301（66.02%）；unlabeled 为 34%，test 为约 31.87%。有双换行与有任意换行是不同统计。 |
| 鲁棒性 | `results/robustness.csv/png` | 去换行后 style 为 0.8118，TF-IDF 仍约 0.9506；15% 单词受 typo 扰动时 TF-IDF 为 0.9424。说明格式敏感性与错字敏感性不同，不等于已证明最终隐藏测试表现。 |
| 长度和错误分析 | `auroc_by_length.csv`、`top_features.txt`、`misclassified.txt`、`val_predictions.csv` | 四个长度组共 2000 条；TF-IDF 最短组约 0.9257、最长组 0.9712。共 20 个导出的错误例子，其 ID、真标签、概率和 0.5 决策阈值一致；组员仍需写各例的简短失败假设。 |
| 错误重叠 | 从保存的两模型预测重算 | 在 0.5 阈值，TF-IDF 错 224 条，style 错 62 条，其中重合 19 条。互补性值得测试，但“组合一定提高”仍是待检验假设。 |
| 近重复 | 从 `max_sim_to_train >= 0.8` 重算 | 标记 10/2000 条。排除后 TF-IDF AUROC 为 0.950146，原为 0.950644，约下降 0.000498。可称影响较小，不能写严格为零；这也不等于排除了所有类型的数据泄漏。 |
| Kaggle | 登录状态下的比赛 Submissions 页面 | 看到 Aarushi 的 `submission.csv` 成功记录，public score 0.86401，与文档约 0.864 一致。它是公开榜成绩，不是本地验证分数或 private score。助手没有上传预测、选择最终提交或消耗次数。 |
| 最新提交计划 | 共享文档新增 Models for submissions 表 | 新表列 style_gbm、char_logreg、word_logreg、Keep as a spare，以及已提交 baseline。表内是计划，不是五项都已提交。它和文档较早待办中的 style/no-newline/combined 表述不同，meeting 上应确认最终计划及 Q5 集成使用哪个名额。课程参考值约 0.868 是 private AUROC，不能与 public 分数当作同一数据集的直接对照。 |
| Overleaf | 项目 `6ae79007c0377f3c27b046b4` 的只读源码下载 | Q2/Q3 仍是空表和占位内容，并未因代码更新自动写入。现封面只有 Aarushi、Yuchen；不能据此推断 Vivian 退出。源模板缺少 graphicx，插入图时需在导言区补一次。NetID 拼写应由成员确认。 |
| split 和依赖 | 远端文件树与已有本地记录 | 新远端版本仍没有 `splits/splits.csv`；我们本地已保留并跟踪原样附件，交付时会补齐。她的新功能使用现有依赖；本次没有看到她单独记录完整版本。我们的锁定环境成功运行了临时整合后的 Person B 实验。 |

## 本次实际做了哪些复核

在干净 worktree 上，从头执行了原 Person B 的 baseline、Q2、Q3；又在该临时副本中合入新远端版本，再从头执行同样三个入口。每组都通过 6 项单元测试及 51 项结果比较，保存的验证预测与原结果完全相同。临时合并无冲突，自己的正式工作分支未自动 merge/push。详细 JSON 位于 `../results/person_b_qa/`。

所有新增源文件均已读取，提交表格、图、验证预测和报告状态已核对。此次没有完整重跑她的六模型比较、所有调参、所有 teacher 和所有扰动组合；这些项目应表述为“已审代码/核对已提交结果”，不能称为全部独立复现。没有把她的结果算作 Yuchen 独立产生。

## 与 meeting 和交付的关系

1. 建议 Q2 主文采用我们齐全的五个规模、训练/验证表和双曲线；她的多模型、多 seed 曲线用于补充稳定性，保持各自来源。
2. Q3 可采用我们的固定特征实验作为清楚的受控比较，再单独说明她的 teacher-student 扩展；最终主文取舍由组内一致决定。
3. 文档还列出的待办是 Q5 集成测试、最终 Kaggle 模型/提交、README 与课程 PR、报告。不要把她消息中的“steps 1–4 done”误读为我们原 13 步流程的第 1–4 步或整份报告完成。
4. Q1 仍需在报告中补全各模型训练 AUROC、训练时间和最终选择；Q4 仍需按最终选定模型写训练/验证差距和各错误假设。代码与结果存在不等于每个评分字段已经写完。
5. 我们接下来做第 11 步个人分支/内部 PR、第 12 步 Overleaf、第 13 步组内交接。最终课程 PR 和全组最终预测由团队统一完成。

来源：[共享文档](https://docs.google.com/document/d/1kBn3ITDP76Fbby966O9YKoYWWbYrh2qdT0YQ_SLVfKU/edit)、[核对的团队 commit](https://github.com/aarushsii/Kaggle_Group3_Competition/commit/0e09450db2be0281ad8ebf47f104a33da5308cdc)、[Kaggle submissions](https://www.kaggle.com/competitions/cornell-tech-cs-5785-combined-2026-ai-vs-human-text/submissions)、[团队 Overleaf](https://www.overleaf.com/project/6ae79007c0377f3c27b046b4)。完整私人文档快照和下载证据仅留在用户工作区 output/，没有加进团队仓库。
