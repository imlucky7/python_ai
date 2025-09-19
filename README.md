# python_ai
Explore python in AI domain

## Type Checking
Type checking refers to the process of verifying that the values used in your program are of the correct data type (e.g., int, str, list, etc.) for the operations being performed.

1. **Install mypy**

In your terminal (not inside Python), run:
```
pip install mypy
```
2. **Usage**
```
mypy {python file name}
```
## Code Formatter
1. **Installation**
```
pip install black
```
2. **Usage**
```
black {python file name}
```

## Configuring multiple GitHub account in laptop
### Prerequisite
You already have your work GitHub profile configured globally (via git config --global) and now you want to add a personal GitHub profile — but only for repos in a specific folder (so that it doesn’t disturb your work setup).
### Create a Folder for Personal Projects
Let’s say you want all personal repos inside:

`~/github/personal/`

### Auto-apply Config to the Whole Folder (Recommended)

Use Git’s conditional includes to switch configs based on directory:

Edit `~/.gitconfig and add:`
```
[includeIf "gitdir:~/github/personal/"]
    path = ~/.gitconfig-personal
```
Then create a new file `~/.gitconfig-personal:`
```
[user]
    name = Your Personal Name
    email = your_personal_email@example.com
```
Now, any repo inside **~/github/personal/** will automatically use your personal identity.
Your work identity (--global) stays default everywhere else.
### Verify Setup
For a work repo:
```
git config user.name   # Should show Work Name
git config user.email  # Should show work email
```

For a personal repo (inside **~/github/personal/**):
```
git config user.name   # Should show Personal Name
git config user.email  # Should show personal email
```
### Authentication Configuration (separate credential file)

1. Edit `~/.gitconfig-personal`:
```
[user]
    name = Your Personal Name
    email = your_personal_email@example.com

[credential]
    helper = store
    useHttpPath = true
```

2. In `~/github/personal/python_ai/.git/config`, make sure the remote URL is:
```
https://github.com/imlucky7/python_ai.git
```

3. Then store credentials (one-time):
```
git credential-store --file ~/.git-credentials-personal store
```

And inside `~/.git-credentials-personal`:
```
https://imlucky7:YOUR_PERSONAL_PAT@github.com/imlucky7/python_ai.git
```