# Git Workflow Reference

A working reference for solo development, structured so the habits transfer to team work later. Sections marked **▸ Team habit** are things that cost almost nothing solo but are expected the moment someone else reads your repo.

---

## 1. The mental model

Git stores **snapshots**, not changes. Every commit is a complete picture of the project at a moment in time, plus a pointer to the commit before it.

A **branch** is just a movable label pointing at one of those commits. Making a branch costs nothing — it creates a name, not a copy of your files. This is why branching is cheap and why teams do it constantly.

`main` is a branch like any other. It's only special because everyone agrees it is.

```text
A --- B --- C          ← main
             \
              D --- E  ← feature/name-cleaning
```

Commits D and E exist. `main` doesn't know about them until you merge or rebase.

---

## 2. Commits

### What makes a good commit

One logical change. If the commit message needs the word "and," it's probably two commits.

| Bad                                            | Better                                                |
| ---------------------------------------------- | ----------------------------------------------------- |
| `update`                                       | `Extract suffixes before splitting names`             |
| `fixes`                                        | `Fix phone extension corruption from digit-stripping` |
| `wip`                                          | `Add where_to_split correction column`                |
| `changed a bunch of stuff and fixed the thing` | _(split into two commits)_                            |

**Message format:** imperative mood, present tense — "Add X", not "Added X" or "Adds X". Reads as _what applying this commit does_. This is a near universal convention and following it signals familiarity.

### How often to commit

Commit when something works. Not when everything works.

The test: **could I go back to this commit and have a functioning state?** If yes, commit. Half-finished refactors that don't run are exactly what branches are for (§3), not what commits are for.

Practical rhythm for the kind of work you're doing:

- Finished cleaning phone numbers, `isna()` returns 0 → commit
- Extracted a working function to `cleaning.py` → commit
- Added a correction row to `where_to_split.csv` → commit

### Everyday commit cycle

```sh
git status                      # what's changed
git diff                        # what exactly changed
git add cleaning.py             # stage specific files
git add .                       # or stage everything
git diff --staged               # review what you're about to commit
git commit -m "Extract phone cleaning into cleaning.py"
git push
```

`git diff --staged` before every commit is a habit worth building. It catches the accidentally-committed API key, the debug print, the 8,000-line data file.

▸ **Team habit:** on a team, your commits are read by other people during review. Small, well-titled commits make review possible; one giant commit makes it impossible.

---

## 3. Branches

### The honest answer for solo work

You don't need a branch for most of what you do. Linear work on `main` is fine and not a bad habit.

Branch when you hit one of these **three specific signals**:

| Signal                                                                            | Example from real work                                                              |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **You want to change something structural while the current version still works** | Extracting notebook code into `.py` modules while the notebook still runs correctly |
| **You're trying something you might throw away**                                  | Testing whether `rapidfuzz` beats a simple groupby, unsure which wins               |
| **You need to context-switch mid-task**                                           | Half-finished refactor, and something urgent comes in                               |

All three share a shape: _you need a working version to stay working while you break things somewhere else._

### Branch mechanics

```sh
git switch -c feature/extract-modules    # create and switch to it
# ... work, commit, work, commit ...
git switch main                          # go back
git merge feature/extract-modules        # bring the work in
git branch -d feature/extract-modules    # clean up
```

`git switch` is the modern command for changing branches. `git checkout` also works and you'll see it everywhere, but it does too many unrelated things (switching branches, restoring files, checking out commits), which is why the Git team split it into `switch` and `restore`.

### Naming

```text
feature/catalist-normalization
fix/phone-extension-parsing
refactor/extract-cleaning-module
experiment/rapidfuzz-comparison
```

Prefix, slash, kebab-case description. Costs nothing solo, and it's the convention almost every team uses.

▸ **Team habit:** teams often require branch names to reference a ticket — `feature/DATA-142-catalist-matching`. Adopt whatever the team uses.

---

## 4. Merge vs. rebase

This is the section worth understanding properly, because it's the most common Git interview question and the most common source of confusion.

### The situation both commands solve

You branched off `main`. While you worked, `main` moved forward.

```text
A --- B --- C --- F        ← main (someone else's work, or your own)
             \
              D --- E      ← your feature branch
```

Your branch is based on C, but `main` is now at F. You need to reconcile these. Two options.

### Merge

`git merge main` (from your feature branch) creates a **new commit** that has two parents — it ties the two histories together.

```text
A --- B --- C --- F --------- M   ← main after merge
             \               /
              D --- E ------/
```

- **Preserves history exactly as it happened.** D and E keep their original commit hashes and their original parent.
- **Adds a merge commit** (M) that exists only to join the branches.
- **Non-destructive.** Nothing is rewritten.
- History becomes a graph with visible branch-and-join structure.

### Rebase

`git rebase main` (from your feature branch) **replays your commits on top of the new base**, as if you'd started from F all along.

```text
A --- B --- C --- F                    ← main
                   \
                    D' --- E'          ← your branch, rebased
```

- **Rewrites your commits.** D' and E' are _new commits_ with different hashes — same changes, different identity.
- **No merge commit.** History stays linear.
- **Destructive to history**, which is why the rule below exists.

### The one rule that matters

> **Never rebase commits that other people have pulled.**

Because rebase creates new commits with new hashes, anyone who already has the old commits now has a diverged history that Git can't reconcile. This is what causes the "your branch and origin/x have diverged" mess.

Practical version of the rule:

- **Rebase your own unpushed work** — clean, safe, encouraged
- **Merge anything shared** — or coordinate loudly before rewriting

### Which to use

| Situation                                                          | Use                                                  |
| ------------------------------------------------------------------ | ---------------------------------------------------- |
| Updating your feature branch with the latest `main`, work unpushed | **rebase** — keeps history clean                     |
| Bringing a finished feature into `main`                            | **merge** — preserves the fact that it was a feature |
| Anything already pushed and shared                                 | **merge** — never rewrite shared history             |
| You're unsure                                                      | **merge** — it's the non-destructive option          |

Solo, unpushed work: rebase freely, it produces nicer history. Everything else: merge.

### Resolving conflicts

Both commands can produce conflicts when the same lines changed in both places. Git marks them in the file:

```text
<<<<<<< HEAD
df['phone'] = df['phone'].str.strip()
=======
df['phone'] = df['phone'].str.strip().str.replace('+', '')
>>>>>>> feature/phone-cleaning
```

Edit the file to what it should actually be, delete the marker lines, then:

```sh
git add <file>
git commit          # if merging
git rebase --continue   # if rebasing
```

Escape hatch if it goes badly:

```sh
git merge --abort
git rebase --abort
```

Both return you to the state before you started. Use them freely — an aborted merge costs nothing.

---

## 5. Pull requests

### What a PR actually is

A request to merge one branch into another, with a discussion attached. The branch already exists and the commits are already pushed — the PR is a _wrapper_ around that merge that adds:

- A place to describe **why** the change exists
- A diff view others can read and comment on line by line
- A gate — automated tests and reviews run before the merge happens

### Why bother solo

The review conversation is absent, but three things still work:

1. **The diff view is a genuine self-review tool.** Reading your own changes
   in GitHub's interface, away from your editor, catches things you missed. Debug prints, commented-out code, an accidentally staged data file.
2. **The description forces articulation.** Writing "why" in a PR body is
   practice for the thing you'll do constantly on a team.
3. **You build the muscle memory.** In an interview, "walk me through your
   workflow" is much easier to answer when you've actually done it.

### When to open one solo

Not for every commit — that's overhead with no return. Open a PR when the change is **big enough that you'd want a second look**:

- A refactor that touches multiple files
- A new stage of the pipeline
- Anything where you'd struggle to explain the change from memory a month later

### The flow

```sh
git switch -c feature/extract-modules
# ... work, commit ...
git push -u origin feature/extract-modules
```

Then on GitHub: **Compare & pull request** → write a description → **Create pull request** → read your own diff → **Merge**.

`-u` sets the upstream so future pushes on this branch are just `git push`.

### Writing the description

```markdown
## What

Extracts name-splitting and phone-cleaning logic from the notebook into
`cleaning.py`.

## Why

The notebook cell was ~80 lines with three near-identical blocks. Variable
name collisions between blocks caused two bugs.

## Notes

Notebook now imports from `cleaning.py`. Requires `%autoreload 2` to pick up
edits without a kernel restart.
```

▸ **Team habit:** on a team the "why" section is the important one. Reviewers can read what changed; they can't read your reasoning.

---

## 6. Undoing things

Ordered by how destructive they are.

### Undo the last commit, keep changes staged

```sh
git reset --soft HEAD~1
```

Commit disappears, files unchanged and still staged. Use when you committed too early or want to rewrite the message.

### Undo the last commit, unstage changes

```sh
git reset --mixed HEAD~1
```

Commit disappears, changes remain in working directory but unstaged.

### Undo the last commit and discard the work

```sh
git reset --hard HEAD~1
```

**Destructive.** Changes are gone. Only when you're certain.

### Amend the last commit

```sh
git commit --amend -m "Better message"
```

Rewrites the last commit — new hash, same as rebase. **Safe only if unpushed.** If already pushed, you've diverged from remote and need §4's rules.

### Undo a commit that's already pushed

```sh
git revert <commit-hash>
```

Creates a _new_ commit that undoes the old one. Nothing is rewritten, so it's safe on shared history. This is the correct tool for "I pushed something bad."

### Recover from almost anything

```sh
git reflog
```

A log of everywhere `HEAD` has been, including commits you "lost" via reset. Find the hash, `git reset --hard <hash>`, and you're back.

Worth knowing this exists before you need it. Git very rarely loses committed work permanently.

---

## 7. Stashing

Set aside uncommitted work temporarily.

```sh
git stash              # shelve current changes
git switch main
# ... do something else ...
git switch feature/my-work
git stash pop          # bring the changes back
```

`git stash list` shows what's shelved. `git stash pop` applies and removes the most recent; `git stash apply` applies but keeps it.

Useful when you need to switch context mid-task and aren't at a committable point. Don't let stashes accumulate — they're easy to forget and have no descriptions by default.

---

## 8. Inspecting history

```sh
git log --oneline                              # compact list
git log --all --decorate --oneline --graph     # visual branch structure
git show                                       # what the last commit changed
git show <commit-hash>                         # what any commit changed
git diff                                       # unstaged changes
git diff --staged                              # staged changes
git blame <file>                               # who changed each line, when
```

The `--graph` version is the one to run when branches confuse you. It draws the actual structure.

---

## 9. Tags

A tag is a permanent name for a specific commit. Unlike branches, tags don't move.

Mostly used for releases (`v1.0.0`), but also useful for marking any state worth returning to.

```sh
git tag -a v1.0.0 -m "First complete pipeline run"
git push origin v1.0.0
```

`-a` creates an _annotated_ tag with author, date, and message. Prefer it over a lightweight tag (`git tag v1.0.0`) — the metadata is worth having.

Tags aren't pushed automatically. `git push` alone won't send them.

### Tagging before deleting a branch

If a branch has work worth referencing but you don't want to keep the branch:

```sh
git switch branch-name
git tag -a archive/experiment-rapidfuzz -m "Final state before abandoning"
git push origin archive/experiment-rapidfuzz
git branch -d branch-name
```

The tag survives the branch deletion and keeps those commits reachable.

Niche, but worth knowing. Most solo work never needs it.

---

## 10. `.gitignore`

Never commit:

```sh
.venv/
__pycache__/
.ipynb_checkpoints/
*.env
credentials.json
```

**Data files are a judgment call.** Small inputs that the code depends on (a correction table, a lookup CSV) belong in the repo — they're part of the project. Large raw exports don't.

Anything with real names, phone numbers, or addresses should not be in a repo that might become public. Consider a `data/` directory that's gitignored entirely, with a `data/README.md` explaining what belongs there.

---

## 11. Practice track — building the habits now

The goal is that none of this is theoretical when someone asks about it.

**Already doing:**

- [x] Commit regularly to `main`
- [x] Meaningful commit messages

**Next — low cost, real value:**

- [ ] Run `git diff --staged` before every commit
- [ ] Use imperative mood consistently ("Add", not "Added")
- [ ] Create one branch for the next structural change (extracting `.py` modules is the natural candidate)
- [ ] Merge that branch back into `main` and delete it

**Then — the team-readiness pieces:**

- [ ] Open one PR against yourself for a change big enough to be worth reviewing. Read your own diff in GitHub's interface before merging.
- [ ] Deliberately create a merge conflict in a scratch repo and resolve it. Two branches, same line of the same file, changed differently. Doing this once removes most of the fear.
- [ ] Rebase an unpushed feature branch onto an updated `main`, and run `git log --graph` before and after to see what changed.

**Later, once modules exist:**

- [ ] Tag the first complete end-to-end pipeline run

---

## 12. Applied: `catalist-ab-match`

What the above looks like in the current project.

**Now (linear work on `main`):**

```sh
git add cleaning.py
git diff --staged
git commit -m "Add supervisor name extraction from supervisory_organization"
git push
```

**The next branch-worthy change** — extracting notebook code into `.py` modules, since the notebook currently works and the refactor could break it:

```sh
git switch -c refactor/extract-cleaning-module
# move name-splitting and phone-cleaning into cleaning.py
# update notebook to import from it
# confirm the pipeline still runs
git add .
git commit -m "Extract name and phone cleaning into cleaning.py"
git push -u origin refactor/extract-cleaning-module
```

Then open a PR, read the diff, merge, and delete the branch. That single cycle covers branching, PRs, and merging in one pass on a change you were going to make anyway.

**Branch candidates later in this project:**

- `feature/phone-agreement-matching` — Phase 3
- `experiment/confidence-threshold` — trying threshold values, may discard
- `feature/action-builder-upload` — Phase 4

**Tag candidate:** the first successful end-to-end run producing an Action Builder-ready output.
