"""Render the checked Q2 CSV for the report; no fitting or data changes."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR', str(ROOT / '.person_b_cache/matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

frame = pd.read_csv(ROOT / 'results/person_b/learning_curve_results.csv')
assert frame.training_rows.tolist() == [500, 1000, 2000, 5000, 8000]
with plt.rc_context({'font.size': 11, 'axes.labelsize': 11, 'legend.fontsize': 10}):
    fig, ax = plt.subplots(figsize=(7.2, 3.2), layout='constrained')
    ax.plot(frame.training_rows, frame.training_auroc, 'o-', color='#2563eb',
            linewidth=2, markersize=5, label='Training AUROC')
    ax.plot(frame.training_rows, frame.validation_auroc, 's-', color='#d97706',
            linewidth=2, markersize=5, label='Validation AUROC')
    ax.set(xlabel='Labeled training examples', ylabel='AUROC', ylim=(.85, 1.006))
    ax.set_xticks(frame.training_rows, [f'{int(n):,}' for n in frame.training_rows], fontsize=10)
    ax.grid(alpha=.2)
    ax.legend(loc='lower right', framealpha=.95)
    fig.savefig(Path(__file__).parent / 'person_b_learning_curve.png', dpi=240)
    plt.close(fig)
