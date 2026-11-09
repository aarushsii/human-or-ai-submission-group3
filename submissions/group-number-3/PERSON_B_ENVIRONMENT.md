# Person B Python environment

Verified locally on November 9, 2026. This is environment setup for Q2/Q3, not an experiment result or a reproduction of the historical AUROC.

## Verified configuration

- CPython 3.14.8, macOS 26.6.2, arm64.
- Repository-root `.venv`, isolated from global Python packages and ignored by Git.
- Team source at `c7be9f30ac94e34573a9057d429c77f91d52ad6d`; branch `yuchen/person-b`.
- NumPy 2.5.4; pandas 3.1.1; SciPy 1.18.1; scikit-learn 1.9.1; Matplotlib 3.11.2.
- Jupyter 1.1.1; JupyterLab 4.6.6; Notebook 7.6.5; ipykernel 7.4.0.
- The original team `requirements.txt` remains unchanged. `requirements-person-b.lock.txt` records the exact 112 installed dependency versions. pip itself is 26.2.1.

The team did not record the versions used for its historical baseline. This environment has not yet reproduced that baseline. Exact pins have been verified on this Mac; installation on other operating systems and architectures has not been verified.

## Use the existing environment

Run these commands from the repository root, `Kaggle_Group3_Competition`:

```bash
source .venv/bin/activate
python --version
PIP_CACHE_DIR="$PWD/.venv/pip-cache" python -m pip check
```

The version should be Python 3.14.8. The dependency check should report `No broken requirements found.` Use `deactivate` to leave the virtual environment.

VS Code can use the interpreter at `.venv/bin/python` after opening the correct repository and selecting **Python: Select Interpreter**. The repository and interpreter have not yet been selected in VS Code as part of this setup; command-line verification is complete.

## Recreate the verified environment

From a fresh checkout of this repository, first use a Python 3.14.8 installation. Run from the repository root:

```bash
python3.14 -m venv .venv
PIP_CACHE_DIR="$PWD/.venv/pip-cache" .venv/bin/python -m pip install \
  --only-binary=:all: --index-url https://pypi.org/simple \
  -r submissions/group-number-3/requirements-person-b.lock.txt
PIP_CACHE_DIR="$PWD/.venv/pip-cache" .venv/bin/python -m pip check
```

The `.venv` directory contains local executable paths and should be recreated, not copied between computers or uploaded to GitHub. If the checkout moves or the base Homebrew Python installation changes, recreate the environment as needed.

## What was verified

`person_b_environment.json` records versions, hashes and verification results:

- The Python executable uses the project virtual environment.
- NumPy and pandas perform basic numeric/table operations.
- SciPy performs a small sparse-matrix operation without densifying a text matrix.
- The existing `tfidf_logreg(C=4.0)` pipeline constructs successfully; it was **not fitted**.
- Matplotlib writes a PNG using the noninteractive Agg backend. The example image is an environment check, not a learning curve, and stays inside `.venv`.
- Jupyter, Notebook, JupyterLab and ipykernel import successfully; `python -m jupyter --version` works. No notebook server or kernel was started.
- `pip check` finds no broken dependency requirements.
- All 17 previously tracked files retain their original hashes. The `splits` directory remains absent.

The full resolved install plan, wheel installation report and installation log are local files inside `.venv`. All selected distributions were prebuilt wheels.

In a filesystem-restricted shell, use project-local caches when running plotting tools:

```bash
MPLCONFIGDIR="$PWD/.venv/matplotlib-cache" \
XDG_CACHE_HOME="$PWD/.venv/cache" \
  .venv/bin/python your_script.py
```

During the initial check Fontconfig could not write to global cache directories. Matplotlib still built its local cache and produced the PNG successfully. No elevated font-cache writes were performed.

## Current boundary

No competition CSV was loaded or copied. No split was generated or modified. No model was trained, no AUROC was produced, and no code was pushed. The original shared split is still needed before producing results comparable with the team baseline.

## References

- [Official scikit-learn installation guide](https://scikit-learn.org/stable/install.html)
- [scikit-learn package metadata and wheels](https://pypi.org/project/scikit-learn/)
- [SciPy package metadata and Python support](https://pypi.org/project/scipy/)

## 中文说明

第三步已完成：项目已有独立的 Python 工具箱，依赖已安装并通过基本验证。版本锁定文件用于记录这次实际装了什么；它不表示已经复现队友成绩。当前没有读取比赛数据、训练模型或动切分文件，VS Code 的项目打开和解释器选择也还未进行。
