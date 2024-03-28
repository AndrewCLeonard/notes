# Git Workflow Lessons

## Tagging Commits

Tagging the last commit of a branch before deleting it is a great way to preserve a reference to that point in the project's history without keeping the branch itself. Tags in Git are pointers to specific commits and can serve as milestones or markers for significant versions or states of the code. They are particularly useful for marking releases, but you can also use them to mark the final state of a branch.

Here's how you can tag the last commit of a branch before deleting the branch:

### Tagging the Last Commit

1. First, ensure you're on the branch you intend to delete (or know the commit hash you want to tag):

   ```sh
   git checkout branch-name
   ```

2. Tag the last commit. You can create a lightweight tag or an annotated tag. Annotated tags are recommended because they can contain metadata such as the tagger name, email, date, and tagging message:

   ```sh
   git tag -a tag-name -m "Tagging the last commit of branch-name before deletion"
   ```

   Replace `tag-name` with a meaningful name for the tag and `branch-name` with the name of your branch. The `-m` flag allows you to add a message describing the purpose of the tag.

3. Push the tag to the remote repository. Unlike branches, tags are not automatically synchronized between local and remote repositories. To share the tag with your team or preserve it on the remote server, you need to push it:

   ```sh
   git push origin tag-name
   ```

### Deleting the Branch

After tagging, you can safely delete the branch:

- **Locally**:

  ```sh
  git branch -d branch-name
  ```

  Use `-D` instead of `-d` if Git warns you about the branch not being fully merged (if you're sure it's safe to delete).

- **Remotely**:

  ```sh
  git push origin --delete branch-name
  ```

### Benefits of Tagging Before Deletion

- **Historical Reference**: Tags provide a fixed point in the project's history that's easy to find and refer back to, even after the branch is gone.
- **Clean Repository**: By deleting branches that have served their purpose, you keep the repository's branch list manageable and focused on current work.

- **Release and Milestone Tracking**: Tags are commonly used to mark release points, but they're also useful for marking any significant point in history, such as the end of a feature branch.

Remember, tags are global to the repository and not tied to a specific branch, so even after the branch is deleted, the tag remains accessible as a reference to that snapshot of the code.

## `checkout` vs. `switch`

[good article](https://phoenixnap.com/kb/git-switch-vs-checkout).
"Although both commands can switch branches, git switch is more straightforward and explicit in its purpose. The git switch command was specifically designed to switch branches and doesn't handle other operations like working with individual files.

In contrast, git checkout has a broader range of functionalities, which can confuse new Git users. The command allows you to switch branches and copy files from any branch to the current one. Additionally, it lets you restore changes from a particular commit.

The Git team now advises users to use git switch for branch operations and git restore for file restorations. However, both operations can be done using git checkout."

## Git `--amend` and Divergence Issue

### Key Points

- **`--amend` Use**: Rewrites the last commit. If already pushed, causes divergence.
- **Why Divergence Happens**: Remote sees amended (local) commit history as different because commit hashes change.
- **Conflict Prevention**: Git stops fast-forward merges to prevent data loss.

### Resolving Divergence

1. **Backup Work**: Always backup before making changes that could lose data.
2. **Fetch Latest**: `git fetch origin` to get the latest remote changes.
3. **Rebase (Option 1)**:
   - `git rebase origin/develop`
   - Move local changes on top of remote changes.
   - Resolve conflicts if any.
4. **Merge (Option 2)**:
   - `git merge origin/develop`
   - Combines remote and local changes.
   - May result in a merge commit.
5. **Force Push**:
   - `git push origin develop --force`
   - Overwrites remote with local.
   - Use with caution and communicate with the team.

### Best Practices

- **Amend Unpushed Commits Only**: Safe for local, not for pushed commits.
- **Communicate**: Notify team when rewriting shared branch history.
- **Feature Branches**: Work on features separately, merge after review.
