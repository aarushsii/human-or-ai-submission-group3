# Person B report integration package

- `PERSON_B_REPORT_EN.md`: full Q2.1–Q2.3 and Q3.1–Q3.3 text, tables, method and integration notes.
- `person_b_q2_q3.tex`: section block to replace the existing Q2/Q3 placeholder sections in the actual team template.
- `person_b_learning_curve.png`: compact, readable report rendering of the checked primary CSV. Rebuild from repository root with `.venv/bin/python submissions/group-number-3/report/build_person_b_figure.py`.
- `PERSON_B_Q2_Q3_REPORT.tex`: standalone wrapper used to compile and visually check these sections locally. It is not the full team report.
- `PERSON_B_CONTRIBUTION_AND_AI.md`: contribution, AI-use and development-history material; human-specific verification remains for the author to state accurately.
- `PERSON_B_NOTES_ZH.md`: plain Chinese explanation of the experiments and their limits.
- `TEAM_UPDATE_REVIEW_ZH.md`: review of Aarushi's nine new commits, overlap, numerical checks and remaining group decisions.
- `PERSON_B_MEETING_NOTES.tex`: English speaking-note source. The user also has a longer bilingual Markdown manuscript in their local workspace.

The local PDF previews are in the user's workspace `output/pdf/`. They were compiled with Tectonic and checked after rendering. They have not been uploaded to Overleaf. During step 12, add `\usepackage{graphicx}` to the actual main preamble once and upload `person_b_learning_curve.png`, then replace only the existing Q2 and Q3 sections. Preserve other people's report work and recompile the actual shared document.

Q2.3 has 119 English words; Q3.1 has 100 and Q3.3 has 101. Values are generated from the real run records. Do not substitute Aarushi's refitted-feature Q3 result into the frozen-feature method text. Her teacher-student extension must retain its own method, selection caveat and attribution.
