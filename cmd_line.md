# Command Line

## Command Line Basics

| command                      | example                                                | explanation                                                                                    |
| ---------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| `tree`                       | `tree`                                                 | graphical representation of the current directory                                              |
| `tree /f`                    | `tree /f`                                              | include names of files in each folder                                                          |
| `tree /a`                    | `tree /a`                                              | use ASCII characters, useful for recreating by typing or when special characters won't display |
| `cd path\to\folder`          | `cd "G:\My Drive\Obsidian\WorkVault"`                  | change directory (navigate into a folder)                                                      |
| `cd ..`                      | `cd ..`                                                | move up one folder level                                                                       |
| `pwd`                        | `pwd`                                                  | print the current working directory                                                            |
| `dir`                        | `dir`                                                  | list files and folders in the current directory                                                |
| `mkdir FolderName`           | `mkdir "G:\My Drive\Obsidian\WorkVault\NewFolder"`     | create a new folder                                                                            |
| `mkdir "Folder With Spaces"` | `mkdir "G:\My Drive\Obsidian\WorkVault\Meeting Notes"` | create a folder when the name includes spaces                                                  |
| quoting paths                | `"G:\My Drive\Obsidian\WorkVault"`                     | always use quotes when the folder name includes spaces                                         |

---

## Globbing (Wildcards & Patterns)

Globbing lets you match multiple files/folders using wildcards. Useful for searching, listing, or batch operations.

| pattern   | example                                            | explanation                                                         |
| --------- | -------------------------------------------------- | ------------------------------------------------------------------- |
| `*`       | `dir "G:\My Drive\Obsidian\WorkVault\*.md"`        | matches zero or more characters (all Markdown files in this folder) |
| `?`       | `dir "G:\My Drive\Obsidian\WorkVault\Project?.md"` | matches a single character (`Project1.md`, `ProjectA.md`)           |
| `prefix*` | `dir "G:\My Drive\Obsidian\WorkVault\Project*"`    | matches everything starting with "Project"                          |
| `*2025*`  | `dir "G:\My Drive\Obsidian\WorkVault\*2025*"`      | matches everything containing "2025"                                |
| `[abc]*`  | `dir "G:\My Drive\Obsidian\WorkVault\[abc]*"`      | matches anything starting with `a`, `b`, or `c`                     |
| `[0-9]*`  | `dir "G:\My Drive\Obsidian\WorkVault\[0-9]*"`      | matches anything starting with a digit                              |

---

⚠️ Note:

- PowerShell supports `*`, `?`, and `[...]` globbing patterns.
- Unlike Linux shells, PowerShell does **not** support `{a,b}` brace expansion. Use loops instead for creating multiple folders.

## Globbing in PowerShell

PowerShell supports wildcards (`*`, `?`, `[...]`) when listing or selecting files/folders, but **does not support `{a,b}` brace expansion** natively.

| pattern  | example                                            | explanation                                                         |
| -------- | -------------------------------------------------- | ------------------------------------------------------------------- |
| `*`      | `dir "G:\My Drive\Obsidian\WorkVault\*.md"`        | matches zero or more characters (all Markdown files in this folder) |
| `?`      | `dir "G:\My Drive\Obsidian\WorkVault\Project?.md"` | matches a single character (`Project1.md`, `ProjectA.md`)           |
| `[abc]*` | `dir "G:\My Drive\Obsidian\WorkVault\[abc]*"`      | matches anything starting with `a`, `b`, or `c`                     |
| `[0-9]*` | `dir "G:\My Drive\Obsidian\WorkVault\[0-9]*"`      | matches anything starting with a digit                              |

---

## Brace Expansion (Two Approaches)

### 🔹 1. Native in Linux/macOS (Bash/Zsh)

Brace expansion works out of the box:

```bash
mkdir -p Campaigns/CampaignA/Projects/ProjectA/{Logs,Meetings}
```

This creates:

```shell
Campaigns/
|   CampaignA/
|   |-- Projects/
|       |-- ProjectA/
|           |-- Logs/
|           \-- Meetings/
```

### 🔹 2. Simulating Brace Expansion in PowerShell

Since PowerShell doesn’t support {Logs,Meetings}, you use loops or arrays:

#### Option A: foreach loop

```shell
foreach ($folder in "Logs","Meetings") {
mkdir "G:\My Drive\Obsidian\WorkVault\Campaigns\CampaignA\Projects\ProjectA\$folder"
}
```

#### Option B: ForEach-Object with pipeline

```shell
"Logs","Meetings" | ForEach-Object {
mkdir "G:\My Drive\Obsidian\WorkVault\Campaigns\CampaignA\Projects\ProjectA\$_"
}
```

Both create the same structure:

```shell
ProjectA/
|-- Logs/
\-- Meetings/
```

#### Key Takeaway

- Linux/macOS → use {} for quick one-liners.
- PowerShell → use arrays + loops to simulate brace expansion.

## Combining Globbing with Folder Creation

You can combine globbing (wildcards) with `mkdir` to create subfolders inside multiple matching folders at once.

### Example: Create a `Logs` folder in every project ending with "2025"

```shell
mkdir "G:\My Drive\Obsidian\WorkVault\Campaigns\*\Projects\*2025*\Logs"
```

What happens:

- `*` matches all campaigns
- _2025_ matches all projects with 2025 in the name
- Logs is created inside each one

Result:

```shell
Campaigns
|-- CampaignA
|   \-- Projects
|       \-- WorkerList2025
|           \-- Logs
|-- CampaignB
|   \-- Projects
|       \-- Outreach-2025-Q3
|           \-- Logs
```

### Example: Create Logs and Meetings in all projects

PowerShell doesn’t support `{Logs,Meetings}`, so use a loop with globbing:

```shell
foreach ($folder in "Logs","Meetings") {
    mkdir "G:\My Drive\Obsidian\WorkVault\Campaigns\*\Projects\*\$folder"
}
```

Result:

```shell
ProjectA
|-- Logs
\-- Meetings

ProjectB
|-- Logs
\-- Meetings
```

### Example: Verify with tree

After running the commands, check the structure:

```shell
tree "G:\My Drive\Obsidian\WorkVault\Campaigns" /a /f
```

This will show you exactly which folders were created where.
