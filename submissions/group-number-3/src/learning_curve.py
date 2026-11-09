"""Effect of training-set size (report Q2.1-Q2.2).

Train on stratified subsets of the 8,000-row training fold (500, 1k, 2k, 5k, 8k)
with fixed hyperparameters, and record TRAINING AUROC (on the subset itself)
and VALIDATION AUROC (always the same fixed 2,000 rows). Smaller sizes are
repeated with 3 seeds.

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
SIZES = [500, 1000, 2000, 5000, 8000]
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
                tr_auc = roc_auc_score(sub["label"], model.predict_proba(sub["text"])[:, 1])
                va_auc = roc_auc_score(va["label"], model.predict_proba(va["text"])[:, 1])
                rows.append({"model": name, "n_train": n, "seed": seed,
                             "train_auroc": tr_auc, "val_auroc": va_auc})
                print(f"{name:<14} n={n:<5} seed={seed}  train={tr_auc:.4f}  val={va_auc:.4f}")

    df = pd.DataFrame(rows)
    df.to_csv(ROOT / "results" / "learning_curve.csv", index=False)

    summary = (df.groupby(["model", "n_train"])[["train_auroc", "val_auroc"]]
                 .agg(["mean", "std"]).fillna(0))
    print("\n", summary.round(4))
    summary.round(4).to_csv(ROOT / "results" / "learning_curve_summary.csv")

    fig, axes = plt.subplots(1, len(MODEL_NAMES), figsize=(11, 4), sharey=True)
    for ax, name in zip(axes, MODEL_NAMES):
        s = summary.loc[name]
        ax.errorbar(s.index, s[("train_auroc", "mean")], yerr=s[("train_auroc", "std")],
                    marker="o", capsize=3, linestyle="--", label="Training AUROC")
        ax.errorbar(s.index, s[("val_auroc", "mean")], yerr=s[("val_auroc", "std")],
                    marker="o", capsize=3, label="Validation AUROC")
        ax.set_xscale("log")
        ax.set_xticks(SIZES)
        ax.set_xticklabels([f"{n:,}" for n in SIZES])
        ax.set_xlabel("Training examples (log scale)")
        ax.set_title(name)
        ax.grid(alpha=0.3)
        ax.legend(loc="lower right")
    axes[0].set_ylabel("AUROC")
    fig.suptitle("Effect of training-set size (validation = fixed 2,000 rows)")
    fig.tight_layout()
    out_png = ROOT / "results" / "learning_curve.png"
    fig.savefig(out_png, dpi=200)
    print("Saved results/learning_curve.csv, learning_curve_summary.csv, learning_curve.png")


if __name__ == "__main__":
    main()
