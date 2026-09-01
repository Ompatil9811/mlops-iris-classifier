# Version Control Workflow

## Git initialization
Initialize a repository with `git init` inside the project folder. This creates the `.git` metadata that tracks file changes and history.

## Branches
Use branches to isolate work. Common examples include `main`, `develop`, and feature branches such as `feature/add-classification-report` and conflict demo branches. Branches let teams work independently without overwriting each other’s changes.

## Commits
A commit records a snapshot of the project with a descriptive message. Use conventional commit prefixes such as `feat:`, `docs:`, and `merge:` to communicate the intention of the change.

## Pushing to GitHub
After committing locally, push the branch to the remote repository with `git push origin <branch-name>`. This makes the branch available on GitHub for review or collaboration.

## Pull and merge workflow
Keep `main` current with `git pull origin main` before starting new work. When a feature is ready, merge or rebase it into the target branch and then push the updated branch.

## Merge conflicts
Merge conflicts happen when two branches change the same file in different ways. Git stops the merge and marks the conflicting area so you can choose the final result.

## Conflict markers
Conflict markers appear as:

```text
<<<<<<< HEAD
... current branch content ...
=======
... incoming branch content ...
>>>>>>> branch-name
```

These markers must be removed once the final content is chosen.

## Resolving conflicts
Inspect the conflict markers, decide the correct combined content, remove the markers, and save the file. Then stage the file with `git add <file>` and create a merge commit.

## Staging and committing the resolution
After resolving all conflicts, run `git add <resolved-file>` and commit the merge with a message such as `merge: resolve README conflict between demo branches`.

## Verifying the final history
Check the repository status and log with `git status`, `git branch -a`, and `git log --oneline --graph --all` to confirm the branch structure, clean state, and final commit history.
