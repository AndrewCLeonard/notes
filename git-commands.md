# Git Commands

## Common Commands 

| Category          | Command                                      | Explanation                                               |
|-------------------|----------------------------------------------|-----------------------------------------------------------|
| Branching         | `git branch`                                 | List all local branches.                                  |
| Branching         | `git branch <branch-name>`                   | Create a new branch.                                      |
| Branching         | `git branch -d <branch-name>`                | Delete a local branch safely (only if merged).            |
| Branching         | `git branch -D <branch-name>`                | Force delete a local branch (even if not merged).         |
| Checkout          | `git checkout <branch-name>`                 | Switch to an existing branch.                             |
| Checkout          | `git checkout -b <branch-name>`              | Create and switch to a new branch.                        |
| Cloning           | `git clone <repository-url>`                 | Clone a repository into a new directory.                  |
| Committing        | `git commit -m "<message>"`                  | Commit the staged changes with a message.                 |
| Committing        | `git commit --amend`                         | Amend the most recent commit.                             |
| Diff              | `git diff`                                   | Show changes between commits, commit and working tree, etc.|
| Fetching          | `git fetch`                                  | Fetch changes from the remote repository.                 |
| Initializing      | `git init`                                   | Initialize a new Git repository.                          |
| Logging           | `git log`                                    | Show the commit logs.                                     |
| Merging           | `git merge <branch-name>`                    | Merge the specified branch into the current branch.       |
| Pulling           | `git pull`                                   | Fetch from and integrate with another repository or local branch. |
| Pushing           | `git push`                                   | Update remote refs along with associated objects.         |
| Pushing           | `git push origin --delete <branch-name>`     | Delete a remote branch.                                   |
| Rebasing          | `git rebase <base>`                          | Reapply commits on top of another base tip.               |
| Remote Management | `git remote add <name> <url>`                | Add a remote named <name> for the repository at <url>.    |
| Remote Management | `git remote -v`                              | List all configured remote repositories.                  |
| Staging           | `git add <file>`                             | Add a file to the staging area.                           |
| Staging           | `git add .`                                  | Add all new and changed files to the staging area.        |
| Stashing          | `git stash`                                  | Stash the changes in a dirty working directory away.      |
| Stashing          | `git stash pop`                              | Apply stashed changes back to your working directory.     |
| Status Checking   | `git status`                                 | Show the working tree status.                             |
| Switching         | `git switch <branch-name>`                   | Switch to another branch.                                 |
| Switching         | `git switch -c <branch-name>`                | Create and switch to a new branch.                        |
| Tagging           | `git tag`                                    | List all tags.                                            |
| Tagging           | `git tag <tag-name>`                         | Create a new tag at the current commit.                   |

## Common Flags

| Flag Short | Flag Long              | Description                                          | Common Commands           |
|------------|------------------------|------------------------------------------------------|---------------------------|
| `-a`       | `--all`                | Show all (branches, tags, etc.) or stage all changes | `git branch`, `git add`   |
| `-b`       | `--branch`             | Create and switch to a new branch                    | `git checkout`, `git switch` |
| `-d`       | `--delete`             | Delete the branch                                    | `git branch`, `git push`  |
| `-D`       |                        | Force delete a branch                                | `git branch`              |
| `-f`       | `--force`              | Force the command to execute                         | `git push`, `git fetch`   |
| `-m`       | `--message`            | Use the given message as the commit message          | `git commit`              |
| `-r`       | `--remote`             | Operate on a remote repository                       | `git branch`              |
| `-u`       | `--set-upstream`       | Set upstream for a branch                            | `git push`                |
| `-v`       | `--verbose`            | Be more verbose                                      | `git clone`, `git fetch`  |
| `--amend`  |                        | Amend the previous commit                            | `git commit`              |
| `--cached` |                        | Show cached/staged changes                           | `git rm`, `git diff`      |
| `--ff`     | `--ff-only`            | Allow fast-forward merge only                        | `git merge`               |
| `--no-ff`  |                        | Create a merge commit even if fast-forward is possible | `git merge`            |
| `--rebase` |                        | Reapply commits on top of another base               | `git pull`                |
| `--tags`   |                        | Fetch all tags from remote                           | `git fetch`               |
