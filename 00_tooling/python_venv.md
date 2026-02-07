# Virtual Environments (venv) & pip (Windows)

## Goal
Keep each project’s Python packages isolated and reproducible.

---

## Create a venv (repo root)
Convention: use `.venv/` as the folder name.

```powershell
py -m venv .venv
```

---

## Activate / Deactivate (PowerShell)

Activate:
```powershell
.\.venv\Scripts\Activate.ps1
```

Your prompt should show something like:
```text
(.venv)
```

Deactivate:
```powershell
deactivate
```

---

## Prove you’re using the venv (no guessing)

Which Python am I running?
```powershell
python -c "import sys; print(sys.executable)"
```
✅ Good: path points inside `...\<repo>\.venv\Scripts\python.exe`

Which pip is tied to that Python?
```powershell
python -m pip --version
```
✅ Good: path points inside `...\<repo>\.venv\Lib\site-packages\...`

---

## The safest pip habit (works with or without activation)

### Always run pip through an interpreter
This avoids “installed it but import fails” due to mismatched environments.

Preferred on Windows:
```powershell
py -m pip install <package>
py -m pip install --upgrade <package>
py -m pip list
py -m pip freeze
```

If your venv is active, these also target the venv:
```powershell
python -m pip install <package>
python -m pip install --upgrade <package>
python -m pip list
python -m pip freeze
```

---

## Force the repo venv without activation (zero ambiguity)
Use the venv’s interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install <package>
.\.venv\Scripts\python.exe your_script.py
```

---

## Python flags vs pip flags (don’t mix these up)

### Python flag: `-m` (run a module)
```powershell
py -m pip --version
```
- `-m` belongs to **Python**
- Means: “run the module named `pip` using this interpreter”

### pip flag: `-r` (read requirements file)
```powershell
py -m pip install -r requirements.txt
```
- `-r` belongs to **pip**
- Means: “install packages listed in this file”

Other common pip flags:
- `--upgrade` / `-U`: upgrade package(s)

---

## Snapshot dependencies (reproducibility)

Write a lock-style snapshot:
```powershell
py -m pip freeze > requirements.txt
```

Recreate from snapshot:
```powershell
py -m pip install -r requirements.txt
```

Note: `pip freeze` includes transitive dependencies; noisy but simple and reliable for personal projects.

---

## Common pitfalls
- Installing with one interpreter’s pip and running another interpreter.
- Confusing PowerShell with Python REPL:
  - `>>>` means you’re inside Python; type `exit()` to return to the shell.
- Shadowing modules with filenames:
  - e.g., a local `dotenv.py` breaks `import dotenv`.

---

## Minimal workflow (day-to-day)
1) Create venv once: `py -m venv .venv`
2) Activate: `.\.venv\Scripts\Activate.ps1`
3) Install packages: `python -m pip install ...`
4) Run code: `python your_script.py`
5) Freeze when you want reproducibility: `py -m pip freeze > requirements.txt`