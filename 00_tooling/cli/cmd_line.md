# Command Line (PowerShell + Python)

This file is a **working reference**, not a tutorial.  
The goal is operational fluency: knowing where you are, what you’re touching, and which environment you’re modifying.

---

## Core Mental Model (Anchor This First)

Every shell command answers one of four questions:

1. **Where am I?**
2. **What files are here?**
3. **What program am I running?**
4. **What environment is it running in?**

If you can answer those four, you are not lost.

---

## Command Line Basics

### Navigation & Inspection

| command             | example                               | explanation                                            |
| ------------------- | ------------------------------------- | ------------------------------------------------------ |
| `pwd`               | `pwd`                                 | print the current working directory                    |
| `cd path\to\folder` | `cd "G:\My Drive\Obsidian\WorkVault"` | change directory                                       |
| `cd ..`             | `cd ..`                               | move up one directory                                  |
| `dir`               | `dir`                                 | list files and folders (PowerShell equivalent of `ls`) |
| `tree`              | `tree`                                | show directory structure                               |
| `tree /f`           | `tree /f`                             | include files                                          |
| `tree /a`           | `tree /a`                             | ASCII output (portable / copyable)                     |

### Creating Folders

| command                      | example                            | explanation                       |
| ---------------------------- | ---------------------------------- | --------------------------------- |
| `mkdir FolderName`           | `mkdir Notes`                      | create a folder                   |
| `mkdir "Folder With Spaces"` | `mkdir "Meeting Notes"`            | quotes required when spaces exist |
| quoting paths                | `"G:\My Drive\Obsidian\WorkVault"` | always quote paths with spaces    |

---

## Globbing (Wildcards & Patterns)

Globbing matches **multiple files or folders** using patterns. PowerShell supports `*`, `?`, and `[...]`.

| pattern   | example           | explanation             |
| --------- | ----------------- | ----------------------- |
| `*`       | `dir *.md`        | zero or more characters |
| `?`       | `dir Project?.md` | exactly one character   |
| `prefix*` | `dir Project*`    | starts with prefix      |
| `*2025*`  | `dir *2025*`      | contains substring      |
| `[abc]*`  | `dir [abc]*`      | starts with a, b, or c  |
| `[0-9]*`  | `dir [0-9]*`      | starts with a digit     |

### Notes

- PowerShell supports `*`, `?`, and `[...]`
- PowerShell does **not** support `{a,b}` brace expansion

---

## Brace Expansion (Linux vs PowerShell)

### Linux / macOS (Bash, Zsh)

```bash
mkdir -p Campaigns/CampaignA/Projects/ProjectA/{Logs,Meetings}
```

Creates:

```text
ProjectA/
├─ Logs/
└─ Meetings/
```

### PowerShell (Simulated Brace Expansion)

#### Option A: foreach loop

```powershell
foreach ($folder in "Logs","Meetings") {
    mkdir "G:\My Drive\Obsidian\WorkVault\Campaigns\CampaignA\Projects\ProjectA\$folder"
}
```

#### Option B: pipeline

```powershell
"Logs","Meetings" | ForEach-Object {
    mkdir "G:\My Drive\Obsidian\WorkVault\Campaigns\CampaignA\Projects\ProjectA\$_"
}
```

##### Key takeaway

- Linux/macOS → `{}`
- PowerShell → arrays + loops

---

## Combining Globbing + Folder Creation

### Create `Logs` in every 2025 project

```powershell
mkdir "G:\My Drive\Obsidian\WorkVault\Campaigns\*\Projects\*2025*\Logs"
```

What happens:

- `*` matches all campaigns
- `*2025*` matches all 2025 projects
- `Logs` is created inside each

### Create `Logs` and `Meetings` everywhere

```powershell
foreach ($folder in "Logs","Meetings") {
    mkdir "G:\My Drive\Obsidian\WorkVault\Campaigns\*\Projects\*\$folder"
}
```

### Verify with tree

```powershell
tree "G:\My Drive\Obsidian\WorkVault\Campaigns" /a /f
```

---

## Processes (When Things Are “Locked”)

| purpose      | command               |
| ------------ | --------------------- |
| list running | `Get-Process python`  |
| kill process | `Stop-Process -Force` |

Used when:

- venv won’t delete
- files are locked
- Python interpreters are stuck running

---

## Python-Specific (Critical for Real Work)

These are **diagnostic commands**, not trivia.

| question                 | command                                         |
| ------------------------ | ----------------------------------------------- |
| which Python is running? | `python -c "import sys; print(sys.executable)"` |
| which pip is active?     | `python -m pip -V`                              |
| what’s installed?        | `python -m pip list`                            |
| inspect a package        | `python -m pip show pandas`                     |

If `sys.executable` is not inside your project’s `.venv`, you are in the wrong environment.

---

## Stop Memorizing Flags — Ask This Instead

After every command, ask:

> **What state did this change?**

Examples:

- `py -m venv .venv` → created an isolated Python runtime
- `Activate.ps1` → modified environment variables
- `pip install X` → installed packages into _that_ interpreter
- `python script.py` → executed code with current cwd + env

---

## Reading Help Like a Professional

```powershell
Get-Help Remove-Item -Examples
```

Use `-Examples` first. Ignore full references unless needed.

---

## The “Explain-It-Back” Drill (Weekly)

After any setup session, answer from memory:

1. What directory was I in?
2. Which Python interpreter did I use?
3. Where were packages installed?
4. How could I recreate this environment from scratch?

If you can answer those, you understand what you just did.

---

## Why Copy/Paste Is Acceptable (For Now)

You are not copying magic words.  
You are applying **known transformations** to system state.

Learning happens when you:

- verify results (`sys.executable`, `pip list`)
- predict outcomes
- debug mismatches

---

## 10-Minute Self-Practice Exercise

Without a tutorial:

1. Create a throwaway folder
2. Create a `.venv`
3. Activate it
4. Install one package
5. Prove which Python is running
6. Delete the venv

If you can do this unaided, you are no longer “copypasta-ing.”
