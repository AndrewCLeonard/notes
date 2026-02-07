# Virtual Environments (venv) & pip

## Create

```powershell
py -m venv .venv
```

## Activate

```powershell
.\.venv\Scripts\Activate.ps1
```

Prompt should show:

```text
(.venv)
```

Prompt typically shows (venv) when active.

Deactivate:

```powershell
deactivate
```

## Prove it worked

```powershell
python -c "import sys; print(sys.executable)"
```

Must point inside `.venv`.

---

## venv-pip

### Goal

Keep each project’s Python packages isolated and reproducible.

---

### Create a venv (repo root)

````powershell
py -m venv venv

Activate venv (PowerShell)
.\venv\Scripts\Activate.ps1


Prompt typically shows (venv) when active.

Deactivate:

deactivate

The safest pip habit (works with/without activation)

Always run pip via the interpreter you intend to use:

py -m pip install <package>
py -m pip install --upgrade <package>
py -m pip list
py -m pip freeze


If you want to force use of the repo venv without activation:

.\venv\Scripts\python.exe -m pip install <package>
.\venv\Scripts\python.exe your_script.py

Diagnose “wrong environment” in 10 seconds

Which Python am I running?

python -c "import sys; print(sys.executable)"


Which pip is tied to that python?

python -m pip --version


Good: both paths point into ...\<repo>\venv\....

Common pitfalls

Installing with global pip then running venv python (or vice versa).

Confusing PowerShell vs Python REPL:

>>> means you’re inside Python; use exit() to return to shell.

Shadowing modules with filenames (e.g., a local dotenv.py breaking import dotenv).

Minimal workflow

Activate venv (optional but convenient)

Install packages with python -m pip ...

Run scripts with python ...

Snapshot with pip freeze when you want reproducibility


```md
# py-vs-python.md

## On Windows: `py` and `python` are not the same thing

### `py`
- The **Python Launcher for Windows**
- Often the most reliable way to select Python versions
- Good default for “do I have Python installed and which one?”

Examples:
```powershell
py --version
py -c "import sys; print(sys.executable)"
py -m pip --version

python

Runs the first python.exe found on your PATH

Might be:

your venv python

a system install python

the Windows Store shim (WindowsApps\python.exe)

Examples:

python --version
python -c "import sys; print(sys.executable)"
python -m pip --version

The core rule

Always tie pip to the interpreter you intend to run:

Safe:

py -m pip install <package>


Also safe (when venv is active / python points where you expect):

python -m pip install <package>

Fast checks (no guessing)
python -c "import sys; print(sys.executable)"
python -m pip --version


If those paths don’t match the environment you expect, you’re using the wrong interpreter.

Practical habit

Use py when setting up environments and installing packages.

Use python once you’ve activated your venv and confirmed sys.executable points into it.

If you want zero ambiguity

Call the venv interpreter directly:

.\venv\Scripts\python.exe -m pip install <package>
.\venv\Scripts\python.exe your_script.py


```md
# requirements-freeze.md

## Two different files people call “requirements”
You need to know which one you’re making.

### A) Snapshot / lock (exact environment)
Produced by:
```powershell
py -m pip freeze > requirements.txt
```

Captures everything installed, including transitive dependencies.

Good for: “recreate my current environment exactly.”

Noisy, but simple and effective for a personal repo.

Install from it:

py -m pip install -r requirements.txt

B) Top-level intent (minimal)

A hand-written list of the packages you chose, e.g.:

pandas
python-dotenv
requests


Good for: sharing a project without pinning every transitive package.

Not an exact lock unless you pin versions.

Beginner-friendly default

For now: treat requirements.txt as A) snapshot.

Workflow:

Install/upgrade packages

Run your code

Freeze:

py -m pip freeze > requirements.txt

Upgrading packages (choose deliberately)

Preferred: upgrade one package at a time:

py -m pip install --upgrade pandas


If you “upgrade everything,” expect churn. Afterward, run your code and freeze again.

Sanity checks
py -m pip list
py -m pip freeze
py -m pip show pandas

One hard rule

Run pip through the interpreter:

py -m pip ...


This prevents “installed it but import fails” due to mismatched environments.
````
