Some useful commands to get you started with Git. For more information about a given command, enter `git [command name] --help` in the Terminal. 

# clone

Use this command to clone a remote repo to your local machine. This will put the repo wherever your Terminal or Command Line is currently running in your file system. 

`git clone [repo URL]`

Note: The URL to your repo will be different depending on whether you use SSH or a personal access token (HTTPS).

# status

`git status`

This command is **extremely** useful. Run it whenever you're unsure where you left off with Git, or even to see whether the last command you ran had the intended effect. It will tell you the branch you're on, which files have changed in your staging, which changes you've already committed, and whether you're up to date with the remote.

# Creating a new branch

To create a new local branch: 

`git checkout -b [new branch name]`

To push the branch to the remote repo (so other people can see it and use it):

`git push origin [new-branch-name]`

To checkout an existing remote branch (NOTE: you might need to fetch in order to see newly created remote branches): 

`git checkout [branch name]`.

# fetch

Use this command to make sure you're keeping up to date with changes in the remote repo. This will also allow you to see (and later pull) newly created remote branches. NOTE: `fetch` is not sufficient to get these changes to your local repo. To do so, you will need to `pull`.

`git fetch`

# pull

Use this command to pull changes from the remote repo to your local machine.

`git pull`

# add

Use this command to add files that you've changed locally to the staging.

`git add [filename]`

To add all files that have changed, use `git add -A`. WARNING: this could add sensitive files that you don't want to be tracked in Git. To prevent these files from accidentally being added, specify them in the `.gitignore` file.

# commit

`git commit -m [commit message]`

After you've added the files you want to push, you need to commit them. Specify a message so you and collaborators know what the commit is meant to do.

# push

`git push`

This command will push the changes you've committed to the remote repo.

# restore

`git restore [filename]`

This command will remove a file from the staging area. NOTE: This will not work if you've already committed the file.

# revert

This command will "undo" a commit by adding a new commit that reverts all its changes.

`git revert [commit hash]`