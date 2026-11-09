"""Learning from unlabeled data via pseudo-labeling.

The student is always the word+char TF-IDF LogReg (its learning curve was still
rising at 8k rows, so more data should help it). We try two teachers:

  self:      the student itself labels unlabeled.csv (classic self-training)
  style_gbm: the stylometric GBM labels unlabeled.csv (teacher-student)

For each teacher and confidence threshold t, unlabeled passages with
p >= t (-> AI) or p <= 1 - t (-> human) are added to the 8,000 training rows.
Everything is scored on the same fixed 2,000-row validation set and compared
with a control trained on the 8,000 labeled rows only.

    python src/pseudo_label.py
"""
import pandas as pd
from sklearn.metrics import roc_auc_score

from data import ROOT, get_split, load_splits, load_train, load_unlabeled
from models import style_gbm, tfidf_logreg

THRESHOLDS = [0.99, 0.95, 0.90]


def val_auc(model, va):
    return roc_auc_score(va["label"], model.predict_proba(va["text"])[:, 1])


def main():
    train, splits, unl = load_train(), load_splits(), load_unlabeled()
    tr, va = get_split(train, splits, "random_fold")

    rows = []

    control = tfidf_logreg().fit(tr["text"], tr["label"])
    control_auc = val_auc(control, va)
    rows.append({"teacher": "none (control)", "threshold": None, "n_added": 0,
                 "frac_ai_added": None, "val_auroc": control_auc})
    print(f"Control (8,000 labeled rows only): val AUROC = {control_auc:.4f}\n")

    teachers = {
        "self": control,
        "style_gbm": style_gbm().fit(tr["text"], tr["label"]),
    }

    for name, teacher in teachers.items():
        p = teacher.predict_proba(unl["text"])[:, 1]
        for t in THRESHOLDS:
            mask = (p >= t) | (p <= 1 - t)
            pseudo = pd.DataFrame({"text": unl.loc[mask, "text"],
                                   "label": (p[mask] >= 0.5).astype(int)})
            aug = pd.concat([tr[["text", "label"]], pseudo], ignore_index=True)
            student = tfidf_logreg().fit(aug["text"], aug["label"])
            auc = val_auc(student, va)
            rows.append({"teacher": name, "threshold": t, "n_added": int(mask.sum()),
                         "frac_ai_added": round(pseudo["label"].mean(), 3),
                         "val_auroc": auc})
            print(f"teacher={name:<10} t={t:<5} added={mask.sum():>4} "
                  f"({pseudo['label'].mean() * 100:4.1f}% AI)  val AUROC = {auc:.4f}  "
                  f"({auc - control_auc:+.4f} vs control)")

    df = pd.DataFrame(rows)
    df["val_auroc"] = df["val_auroc"].round(4)
    out = ROOT / "results" / "pseudo_label.csv"
    df.to_csv(out, index=False)
    print(f"\nSaved {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
