# Minimum Viable Python Tooling (pip / venv / requirements)

## Core idea
- **venv** isolates project dependencies.
- **pip** installs/upgrades packages into a specific Python environment.
- **requirements.txt** lets you recreate that environment.

---

## The 3 concepts (and the one rule)
- **Interpreter**: the `python.exe` you are running.
- **venv**: a folder containing an isolated interpreter + `site-packages`.
- **pip**: installs packages into the interpreter’s `site-packages`.

**Rule:** pip must match the interpreter you run.

---

## The safest habit: run pip via the interpreter
**Windows**
```powershell
py -m pip <command>
```

**Mac/Linux**
```bash
python3 -m pip <command>
```

Why: it guarantees you’re installing into the same Python you’re invoking.

---

## Python flags vs pip flags (don’t mix these up)

### Python flag: `-m` (run a module)
```powershell
py -m pip --version
```
- `-m` belongs to **Python**
- Means: “run the module named `pip` using this interpreter”

This is why `py -m pip ...` is reliable.

### pip flag: `-r` (requirements file)
```powershell
py -m pip install -r requirements.txt
```
- `-r` belongs to **pip**
- Means: “read packages from this file and install them”

Other common pip flags:
- `--upgrade` / `-U`: upgrade package(s)
- `--version`: show pip version

---

## The 4 commands to memorize
1) Install a package
```powershell
py -m pip install python-dotenv
```

2) Upgrade one package (preferred habit)
```powershell
py -m pip install --upgrade pandas
```

3) Snapshot exact environment (lock-style)
```powershell
py -m pip freeze > requirements.txt
```

4) Recreate environment from snapshot
```powershell
py -m pip install -r requirements.txt
```

---

## Create + activate a venv (Windows)
Create (repo root):
```powershell
py -m venv venv
```

Activate (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```

Deactivate:
```powershell
deactivate
```

If you don’t want activation, force the venv interpreter directly:
```powershell
.\venv\Scripts\python.exe -m pip install <package>
.\venv\Scripts\python.exe your_script.py
```

---

## “pip freeze” is a snapshot, not a plan
- `pip freeze` outputs **everything installed**, including transitive deps.
- Good for: **personal reproducibility** (“make my machine match later”).
- Noisy for: “only the top-level packages I chose.”

Beginner default: **use freeze**; keep it simple.

---

## About “upgrade everything” one-liners (PowerShell)
Example:
```powershell
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
```
- This is **PowerShell**, not grep.
- It upgrades **everything** in the environment.
- Useful occasionally, but riskier: can introduce breaking changes.

If you upgrade things:
- run your code/tests
- then freeze again:
```powershell
py -m pip freeze > requirements.txt
```

---

## Fast sanity checks (no guessing)
Which Python am I running?
```powershell
python -c "import sys; print(sys.executable)"
```

Does pip match that Python?
```powershell
python -m pip --version
```

What’s installed?
```powershell
py -m pip list
py -m pip freeze
```

---

## `py` vs `python` on Windows (why it matters)

### What changes
- **`py`** uses the Windows *Python Launcher* (more predictable, can target versions like `py -3.12`).
- **`python`** runs whichever `python.exe` comes first on your **PATH** (could be your venv, system Python, or the Windows Store shim).

### When it makes no difference
- If your venv is activated and `python` points into it, then:
  - `python -m pip ...` installs into the venv (fine).

### When it causes problems
- If your venv is NOT activated, `python` may point to a global/system Python, so:
  - `python -m pip install ...` installs packages somewhere else
  - then your project’s venv Python can’t import them (“installed it but import fails”).

### Verify (no guessing)
Run these in the same terminal session you’re using:

```powershell
python -c "import sys; print(sys.executable)"
python -m pip --version
```

✅ Good: both paths point inside ...\<repo>\.venv\...

Zero-ambiguity option (works even without activation)

Force the repo venv interpreter directly:
```powershell
.\.venv\Scripts\python.exe -m pip install <package>
.\.venv\Scripts\python.exe your_script.py
```

---

## Two classic failure modes
1) Installed into one Python, ran another → “installed it but import fails”
2) Local filename shadows a module (e.g., `dotenv.py` breaks `import dotenv`)