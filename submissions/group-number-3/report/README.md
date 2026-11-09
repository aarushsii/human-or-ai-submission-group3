# Person B completion package

Current primary report: PERSON_B_REPORT_EN.md and person_b_q2_q3.tex. These build on Aarushi's submitted methods and results, supplemented by Yuchen (yf467) with Codex assistance.

- Q2: results/learning_curve_required.csv (five required sizes, three-seed means), results/learning_curve_train_val.png (training and validation), and the extended results/learning_curve.csv/png. Original style validation records remain unchanged; training values for those historical style fits are unavailable.
- Q3: Aarushi's unchanged results/pseudo_label.csv, extracted results/pseudo_label_report.csv and source/selection notes in results/pseudo_label_reference.json.
- Full local replication: results/person_b_team_recheck/; style scores differ slightly and are kept distinct from the primary submitted table.
- Report text/LaTeX, a report figure, Chinese explanation and contribution/AI-use text are in this folder. Add graphicx and the image when integrating with the actual team Overleaf later.
- Earlier seed42/frozen-feature results and the initial meeting draft are supplementary historical material. Their numbers should not replace the current primary report.

Run python src/complete_person_b.py from the team directory to rebuild Q2 and prepare the preserved Q3 reference. To refit the pseudo-label grid locally, use python src/pseudo_label.py --output-dir results/person_b_new_recheck. These runs do not submit to Kaggle or edit Overleaf. See ../PERSON_B_RUNBOOK.md.
