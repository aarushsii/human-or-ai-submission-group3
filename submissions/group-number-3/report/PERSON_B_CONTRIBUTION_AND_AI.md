# Person B contribution and AI-use material

Prepared for the team's Q6/author-contribution integration. This covers the Person B work that is supported by the current branch and run records. The full team's final model, course PR and other members' disclosures are still separate integration tasks.

## Suggested contribution statement

**Yuchen Feng (yf467), Person B, with Codex assistance:** prepared the reproducible local environment and verified the teacher-linked original competition data; recovered, checked and installed the unchanged teammate-supplied split; reproduced the existing TF-IDF logistic regression baseline; completed the five required Q2 training sizes with both training and validation AUROC; evaluated a predeclared, fixed-feature Q3 self-training method; preserved a failed check and its correction; performed clean-checkout and latest-team-code reproductions; and prepared the Q2/Q3 tables, figure, explanations and report text.

The owner designation describes responsibility for this work. Implementation, execution, debugging and drafting were substantially assisted by Codex; it should not be represented as independently hand-written code. Aarushi's separate multi-model/multi-seed curves, style features, teacher-student pseudo-labeling and error-analysis additions belong to her contribution. Vivian's full contribution should be supplied by Vivian; it cannot be inferred from this branch review.

## Suggested AI-use disclosure for the Person B portion

We used OpenAI Codex for experiment planning, environment setup, code generation, debugging, local execution, result checks, concept explanations, and report drafting/editing. The experiments ran locally on the supplied competition files and the shared split. Automated checks recomputed AUROC from saved validation probabilities, verified data and split hashes and training/validation separation, and reproduced the results from fresh fits, including integration with the updated team model code. Yuchen coordinated the project scope and data/split access and reviewed the experiment plan in discussion. No external LLM was used to create competition labels or predictions, and no hidden test labels were obtained.

This text does not assert that Yuchen has manually reviewed every line or independently verified every number. For the final answer to Q6.3, Yuchen should add the specific checks, explanations or modifications he personally performs after reviewing these materials. The team should combine this with each other member's own disclosure. Do not replace that human-specific part with a claim that AI-generated checks were manual checks.

## Q6.2 development-history examples

| Local commit | Concrete change | Lesson or evidence |
|---|---|---|
| `ebc62fe` | Added environment/protocol records, fixed shared split, runner and initial checks | Comparable experiments require the same inputs and validation IDs. |
| `bb8eaf5` | Replaced an overly broad estimator-object hash with a learned-representation fingerprint; added regression coverage | A process-local analyzer cache can change without vocabulary or IDF changing. Preserve failures and test the actual invariant. |
| `75133a0` | Saved completed controlled Q2/Q3 runs and result checks | More labels helped; this fixed self-training setting did not. Both findings should be reported honestly. |

These commits are local at preparation time. Add verified GitHub commit links after the branch is pushed in step 11. The isolated QA merge is `38aef5e595d96e24e4fc578fee08f7ea54c9665b` (parents: this branch's `75133a0` and Aarushi's `0e09450`); it has not been applied to the user's working branch or pushed.

## Q6.1 scope

Person B evaluation commands and pinned dependencies are in `../PERSON_B_RUNBOOK.md`. The runner does not generate the final Kaggle `submission.csv`. The team must record its actual final-model command and course PR URL after choosing and delivering that model; the internal Person B PR is not the course submission PR.
