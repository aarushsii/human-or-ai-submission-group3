"""Effect of training-set size: train on stratified subsets of the 8,000-row
training fold and always score on the same fixed 2,000-row validation set.

    python src/learning_curve.py

Writes results/learning_curve.csv and results/learning_curve.png.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

from data import ROOT, get_split, load_splits, load_train
from models import MODELS

MODEL_NAMES = ["tfidf_logreg", "style_gbm"]
SIZES = [250, 500, 1000, 2000, 4000, 8000]
SEEDS = [0, 1, 2]


def subsample(df, n, seed):
    if n >= len(df):
        return df
    sub, _ = train_test_split(df, train_size=n, stratify=df["label"], random_state=seed)
    return sub


def main():
    train, splits = load_train(), load_splits()
    tr, va = get_split(train, splits, "random_fold")

    rows = []
    for name in MODEL_NAMES:
        for n in SIZES:
            seeds = SEEDS if n < len(tr) else [0]  # full set: subsets are identical
            for seed in seeds:
                sub = subsample(tr, n, seed)
                model = MODELS[name]()
                model.fit(sub["text"], sub["label"])
                auc = roc_auc_score(va["label"], model.predict_proba(va["text"])[:, 1])
                rows.append({"model": name, "n_train": n, "seed": seed, "val_auroc": auc})
                print(f"{name:<14} n={n:<5} seed={seed}  val AUROC={auc:.4f}")

    df = pd.DataFrame(rows)
    out_csv = ROOT / "results" / "learning_curve.csv"
    df.to_csv(out_csv, index=False)

    summary = df.groupby(["model", "n_train"])["val_auroc"].agg(["mean", "std"]).fillna(0)
    print("\n", summary.round(4))

    fig, ax = plt.subplots(figsize=(6, 4))
    for name in MODEL_NAMES:
        s = summary.loc[name]
        ax.errorbar(s.index, s["mean"], yerr=s["std"], marker="o", capsize=3, label=name)
    ax.set_xscale("log")
    ax.set_xticks(SIZES)
    ax.set_xticklabels([str(n) for n in SIZES])
    ax.set_xlabel("Number of training examples (log scale)")
    ax.set_ylabel("Validation AUROC (fixed 2,000 rows)")
    ax.set_title("Effect of training-set size")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    out_png = ROOT / "results" / "learning_curve.png"
    fig.savefig(out_png, dpi=200)
    print(f"Saved {out_csv.relative_to(ROOT)} and {out_png.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
