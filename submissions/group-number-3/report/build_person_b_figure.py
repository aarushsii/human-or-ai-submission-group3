"""Copy the canonical checked multi-seed Q2 figure into the report package."""
from pathlib import Path
import shutil
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
t=pd.read_csv(ROOT/'results/learning_curve_required.csv')
assert t.n_train.tolist()==[500,1000,2000,5000,8000]
shutil.copyfile(ROOT/'results/learning_curve_train_val.png',Path(__file__).parent/'person_b_learning_curve.png')
