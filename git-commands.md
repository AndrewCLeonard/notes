# Git Commands

## Common Commands

| Category          | Command                                  | Explanation                                                                 |
| ----------------- | ---------------------------------------- | --------------------------------------------------------------------------- |
| Branching         | `git branch`                             | List all local branches.                                                    |
| Branching         | `git branch <branch-name>`               | Create a new branch.                                                        |
| Branching         | `git branch -d <branch-name>`            | Delete a local branch safely (only if merged).                              |
| Branching         | `git branch -D <branch-name>`            | Force delete a local branch (even if not merged).                           |
| Checkout          | `git checkout <branch-name>`             | Switch to an existing branch.                                               |
| Checkout          | `git checkout -b <branch-name>`          | Create and switch to a new branch.                                          |
| Cloning           | `git clone <repository-url>`             | Clone a repository into a new directory.                                    |
| Committing        | `git commit -m "<message>"`              | Commit the staged changes with a message.                                   |
| Committing        | `git commit --amend`                     | Amend the most recent commit.                                               |
| Committing        | `git commit -a`                          | Automatically stage tracked, modified files before committing.              |
| Committing        | `git commit -am "<message>"`             | Stage tracked changes and commit with a message in one step.                |
| Revert            | `git revert <commit-hash>`               | Create a new commit that reverses the changes made by the specified commit. |
| Diff              | `git diff`                               | Show changes between commits, commit and working tree, etc.                 |
| Diff              | `git diff --staged`                      | Show changes staged for the next commit.                                    |
| Fetching          | `git fetch`                              | Fetch changes from the remote repository.                                   |
| Initializing      | `git init`                               | Initialize a new Git repository.                                            |
| Logging           | `git log`                                | Show the commit logs.                                                       |
| Logging           | `git log --all`                          | Show commits from all branches.                                             |
| Logging           | `git log --decorate`                     | Add branch and tag names to commit messages.                                |
| Logging           | `git log --oneline`                      | Condense each commit to a single line for readability.                      |
| Logging           | `git log --graph`                        | Display an ASCII graph of the branch and merge history.                     |
| Merging           | `git merge <branch-name>`                | Merge the specified branch into the current branch.                         |
| Pulling           | `git pull`                               | Fetch from and integrate with another repository or local branch.           |
| Pulling           | `git pull --rebase`                      | Rebase the current branch on top of the upstream branch after fetching.     |
| Pushing           | `git push`                               | Push local commits to the remote repository.                                |
| Pushing           | `git push origin <branch-name>`          | Push a local branch to the remote.                                          |
| Pushing           | `git push -u origin <branch-name>`       | Push a branch and set upstream tracking (link local and remote branch).     |
| Pushing           | `git push origin --delete <branch-name>` | Delete a remote branch.                                                     |
| Rebasing          | `git rebase <base>`                      | Reapply commits on top of another base tip.                                 |
| Rebasing          | `git rebase -i <base>`                   | Interactively rebase commits (edit, squash, reorder).                       |
| Remote Management | `git remote add <name> <url>`            | Add a remote named `<name>` for the repository at `<url>`.                  |
| Remote Management | `git remote -v`                          | List all configured remote repositories.                                    |
| Staging           | `git add <file>`                         | Add a file to the staging area.                                             |
| Staging           | `git add .`                              | Add all new and changed files to the staging area.                          |
| Staging           | `git add -p`                             | Interactively choose changes to stage (patch mode).                         |
| Stashing          | `git stash`                              | Stash the changes in a dirty working directory away.                        |
| Stashing          | `git stash pop`                          | Apply stashed changes back to your working directory.                       |
| Stashing          | `git stash list`                         | List all stashes.                                                           |
| Status Checking   | `git status`                             | Show the working tree status.                                               |
| Switching         | `git switch <branch-name>`               | Switch to another branch.                                                   |
| Switching         | `git switch -c <branch-name>`            | Create and switch to a new branch.                                          |
| Tagging           | `git tag`                                | List all tags.                                                              |
| Tagging           | `git tag <tag-name>`                     | Create a new tag at the current commit.                                     |
| Tagging           | `git tag -d <tag-name>`                  | Delete a local tag.                                                         |
| Tagging           | `git push origin <tag-name>`             | Push a tag to the remote repository.                                        |
| Tagging           | `git push origin --delete <tag-name>`    | Delete a remote tag.                                                        |

## Common Flags

| Flag Short | Flag Long        | Description                                            | Common Commands              |
| ---------- | ---------------- | ------------------------------------------------------ | ---------------------------- |
| `-a`       | `--all`          | Show all (branches, tags, etc.) or stage all changes   | `git branch`, `git add`      |
| `-b`       | `--branch`       | Create and switch to a new branch                      | `git checkout`, `git switch` |
| `-d`       | `--delete`       | Delete the branch                                      | `git branch`, `git push`     |
| `-D`       |                  | Force delete a branch                                  | `git branch`                 |
| `-f`       | `--force`        | Force the command to execute                           | `git push`, `git fetch`      |
| `-m`       | `--message`      | Use the given message as the commit message            | `git commit`                 |
| `-r`       | `--remote`       | Operate on a remote repository                         | `git branch`                 |
| `-u`       | `--set-upstream` | Set upstream for a branch                              | `git push`                   |
| `-v`       | `--verbose`      | Be more verbose                                        | `git clone`, `git fetch`     |
| `--amend`  |                  | Amend the previous commit                              | `git commit`                 |
| `--cached` |                  | Show cached/staged changes                             | `git rm`, `git diff`         |
| `--ff`     | `--ff-only`      | Allow fast-forward merge only                          | `git merge`                  |
| `--no-ff`  |                  | Create a merge commit even if fast-forward is possible | `git merge`                  |
| `--rebase` |                  | Reapply commits on top of another base                 | `git pull`                   |
| `--tags`   |                  | Fetch all tags from remote                             | `git fetch`                  |

## `git checkout` vs. `git switch`

```text
git switch my-branch              # same as git checkout my-branch
git switch -c my-branch           # same as git checkout -b my-branch
git switch -c my-branch HEAD~3    # branch off HEAD~3
git switch --detach HEAD~3        # checkout commit without branching
```

### 🔹 How it combines with other args

- git switch -c my-branch → create my-branch at the current commit (HEAD).
- git switch -c my-branch HEAD~3 → create my-branch starting from 3 commits before HEAD.
- Without -c, git switch my-branch just moves you onto an existing branch.

### 🔹 Why it exists

- git checkout was overloaded (it could mean “check out a commit,” “create branch,” “switch branch,” etc.).
- Newer Git versions encourage:
  - git switch for changing branches
  - git restore for restoring files
- This makes Git’s commands less confusing.

🧠 So the rule of thumb:
git switch my-branch → switch to it (must already exist).
git switch -c my-branch → create then switch to it.
