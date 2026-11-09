# Person B contribution and AI-use material

Aarushi supplied the original TF-IDF/style models, multi-seed sampling study, full-pipeline self-training and style-teacher pseudo-labeling, and the submitted reference results. These remain the primary basis and retain her attribution.

Yuchen Feng (yf467), with substantial Codex assistance, merged those experiments, added the missing 5,000-row TF-IDF runs and training AUROC, produced the required training/validation plot and five-row report table, prepared all Q2/Q3 responses, restored the unchanged shared split to version control, documented the environment/commands, and checked the official inputs and fresh results. A local full style/pseudo-label replication is retained separately because it does not exactly reproduce the submitted style scores.

Codex assisted with setup, planning, code generation, execution, debugging, output checks, explanations and report drafting. No external LLM labeled or predicted the competition texts. No hidden labels were retrieved. This statement does not claim independent hand-written implementation, manual line-by-line review or that Yuchen has understood every detail. Each author should describe the human checks and modifications actually performed in the final Q6.3 response.

Earlier fixed-feature and seed42 studies are supplementary development history. They are not substituted for Aarushi's primary methods/results. The course final PR, final model/submissions and shared-report compilation remain team tasks.
