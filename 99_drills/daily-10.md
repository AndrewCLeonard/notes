# 99_drills/daily-10.md

## Daily 10 (rotate, answer from memory, then verify in terminal)

### Environment / pip / venv (Windows)

1. What does `python -m pip ...` protect you from compared to `pip ...`?
2. Command: show the full path of the Python interpreter currently running.
3. Command: show which pip is associated with that interpreter.
4. What does it mean if your prompt does NOT show `(venv)`?
5. What are two ways to use a venv without activating it?

### Paths / files

1. In `Path("titanic.csv")`, what is that path relative to?
2. Command: print the current working directory from Python.
3. What’s the difference between `Path.cwd()` and `Path(__file__).parent`?

### Type hints

1. What practical effect do type hints have in VS Code?
2. Do type hints enforce types at runtime? If not, what does?

---

## Verification snippets (use after you answer)

```powershell
python -c "import sys; print(sys.executable)"
python -m pip --version
python -c "from pathlib import Path; print(Path.cwd())"
```

## Rule for adding new drills

When you hit friction (error, confusion, repeated lookup):

- add 1 question that would have prevented it
- add 1 command to verify the answer
