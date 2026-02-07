# Minimum Viable Python Tooling (pip / venv / requirements)

## Core idea

- **venv** isolates project dependencies.
- **pip** installs/upgrades packages into the active environment.
- **requirements.txt** captures what to install so the environment can be recreated.

## The 3 concepts

- **Interpreter**: the `python.exe` you are running.
- **venv**: a folder containing an isolated interpreter + site-packages.
- **pip**: installs packages into _the interpreter’s_ site-packages.

Rule: **pip must match the interpreter** you run.

---

## Always use pip through the interpreter (avoids “wrong pip / wrong venv”)

### Windows

```powershell
py -m pip <command>
```

### Mac/Linux

```bash
python3 -m pip <command>
```

---

## The 4 commands to memorize

### 1) Install a package

```powershell
py -m pip install python-dotenv
```

### 2) Upgrade a single package (preferred habit)

```powershell
py -m pip install --upgrade pandas
```

### 3) Snapshot the _exact_ environment (lock-style)

```powershell
py -m pip freeze > requirements.txt
```

### 4) Recreate environment from snapshot

```powershell
py -m pip install -r requirements.txt
```

---

## “pip freeze” is a snapshot, not a plan

- `pip freeze` outputs **everything installed**, including transitive deps.
- Good for **personal reproducibility** (“make my machine match later”).
- Noisy for “just the top-level deps I chose.”

---

## About “upgrade everything” one-liners

Example PowerShell pipeline:

```powershell
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
```

- This is **PowerShell**, not grep.
- It upgrades **everything** in the environment.
- Useful occasionally, but **riskier**: can introduce breaking changes.

**If you do upgrade things**, then yes:

- run your code/tests
- and **freeze again** to update `requirements.txt`

---

## Quick sanity checks

```powershell
py -m pip list          # what’s installed
py -m pip freeze        # exact versions snapshot
python -c "import sys; print(sys.executable)"  # which Python you’re using
```
