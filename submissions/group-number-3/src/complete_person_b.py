"""Complete Person B using Aarushi's shared learning-curve/pseudo-label methods.

Run from the team directory: python src/complete_person_b.py
Use --output-dir results/person_b_rerun for a fresh comparison.
"""
import argparse
from datetime import datetime
from importlib import metadata
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits

from data import ROOT, get_split, load_splits, load_train
from person_b import sha256, validate_split_data

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".person_b_cache/matplotlib"))
from learning_curve import main as learning_curves
from pseudo_label import main as pseudo_labels


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "results")
    parser.add_argument("--rerun-pseudo", action="store_true", help="Rerun Aarushi's full pseudo-label grid into a separate directory.")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    if args.rerun_pseudo and output == (ROOT / "results").resolve():
        parser.error("Use a separate --output-dir for pseudo-label replication; preserve Aarushi's submitted reference table.")
    config = json.loads((ROOT / "config/person_b.json").read_text())
    hashes = {name: sha256(ROOT / name) for name in config["expected_sha256"]}
    if hashes != config["expected_sha256"]:
        raise ValueError("Official input/shared split hash mismatch. Do not regenerate or replace inputs.")
    train, splits = load_train(), load_splits()
    validate_split_data(train, splits)
    tr, va = get_split(train, splits, "random_fold")
    assert (len(tr), len(va)) == (8000, 2000)
    old_curves_path = ROOT / "results/learning_curve.csv"
    old_pseudo_path = ROOT / "results/pseudo_label.csv"
    old_curves = pd.read_csv(old_curves_path) if old_curves_path.exists() else None
    old_pseudo = pd.read_csv(old_pseudo_path) if old_pseudo_path.exists() else None
    record = {
        "started_at": datetime.now(ZoneInfo("America/New_York")).isoformat(),
        "code_commit": subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip(),
        "based_on_team_commit": "0e09450db2be0281ad8ebf47f104a33da5308cdc",
        "python": platform.python_version(),
        "packages": {name: metadata.version(name) for name in ["numpy", "pandas", "scipy", "scikit-learn", "matplotlib"]},
        "input_sha256": hashes,
        "code_sha256": {"src/" + name: sha256(ROOT / "src" / name) for name in [
            "complete_person_b.py", "learning_curve.py", "pseudo_label.py", "models.py", "features.py", "data.py"]},
        "scope": "Complete existing Person B methods; original teacher-linked data and shared split unchanged.",
        "test_data_used_for_training_or_predictions": False, "split_generated": False,
        "model_parameters_changed": False, "threads": 2, "status": "running"}
    destination = output / "person_b_completion_manifest.json"
    destination.write_text(json.dumps(record, indent=2) + "\n")
    with threadpool_limits(limits=2):
        curves = learning_curves(output)
        if args.rerun_pseudo:
            pseudo = pseudo_labels(output)
        else:
            if old_pseudo is None:
                raise ValueError("Aarushi's shared pseudo_label.csv is required as the primary reference.")
            pseudo = old_pseudo.copy()
            if output != (ROOT / "results").resolve():
                shutil.copyfile(old_pseudo_path, output / "pseudo_label.csv")
            pseudo.loc[(pseudo.teacher == "none (control)") |
                       ((pseudo.teacher == "style_gbm") & pseudo.threshold.eq(.95))].to_csv(
                           output / "pseudo_label_report.csv", index=False)
            (output / "pseudo_label_reference.json").write_text(json.dumps({
                "source": "Aarushi's committed pseudo_label.csv at 0e09450, preserved without changing scores",
                "rounding": "Original scores are available at four decimal places only",
                "local_recheck": "results/person_b_team_recheck/ contains the separately measured local replication; style results differ slightly.",
                "feature_policy": "Refit the full student TF-IDF pipeline on original labeled plus pseudo-labeled texts",
                "selection_caveat": "Three thresholds and two teachers were explored on the same validation set; the reported best setting is exploratory."
            }, indent=2) + "\n")
    checks = {"all_inputs_unchanged": all(sha256(ROOT / name) == value for name, value in hashes.items()),
              "required_tfidf_5000_rows_present": len(curves.loc[curves.n_train.eq(5000) & curves.model.eq("tfidf_logreg")]) == 3,
              "tfidf_training_and_validation_scores_present": curves.loc[curves.model.eq("tfidf_logreg"), ["train_auroc", "val_auroc"]].notna().all().all(),
              "completed_curve_records_present": len(curves) == 35,
              "all_seven_existing_pseudo_settings_present": len(pseudo) == 7}
    if old_curves is not None:
        joined = old_curves.merge(curves, on=["model", "n_train", "seed"], suffixes=("_old", "_new"))
        checks["existing_learning_curve_points_preserved"] = len(joined) == len(old_curves) and np.allclose(
            joined.val_auroc_old, joined.val_auroc_new, atol=1e-10, rtol=0)
    if old_pseudo is not None:
        checks["existing_rounded_pseudo_results_reproduced"] = (
            old_pseudo.teacher.tolist() == pseudo.teacher.tolist() and
            old_pseudo.n_added.tolist() == pseudo.n_added.tolist() and
            np.allclose(old_pseudo.val_auroc, pseudo.val_auroc.round(4), atol=1e-12, rtol=0))
    record.update(status="completed" if all(checks.values()) else "needs_review",
                  primary_q3_source="Aarushi's unchanged submitted table" if not args.rerun_pseudo else "Explicit local replication",
                  completed_at=datetime.now(ZoneInfo("America/New_York")).isoformat(),
                  checks={k: bool(v) for k, v in checks.items()}, all_checks_passed=all(checks.values()))
    destination.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"checks": record["checks"], "all_passed": record["all_checks_passed"]}, indent=2), flush=True)
    if not record["all_checks_passed"]:
        raise SystemExit("Inspect the preserved results before publication.")


if __name__ == "__main__":
    main()
