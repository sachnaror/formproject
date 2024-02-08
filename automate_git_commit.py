
# automate_git_commit.py


import subprocess


def get_git_status():
    """Run `git status` command and return its output."""
    result = subprocess.run(
        ["git", "status", "--porcelain"], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip().split('\n')


def parse_git_status(status_lines):
    """Parse the output of `git status --porcelain` and organize file changes."""
    changes = {'A': [], 'M': [], 'D': []
               }  # A for added, M for modified, D for deleted
    for line in status_lines:
        if line:  # Ignore empty lines
            status = line[0]
            filename = line[3:]
            if status in changes:
                changes[status].append(filename)
            elif status == 'R':  # Handle renamed files
                _, old_file, new_file = line.split(" ")
                changes['D'].append(old_file)
                changes['A'].append(new_file)
    return changes


def generate_commit_message(changes):
    """Generate a commit message based on the file changes."""
    messages = []
    if changes['A']:
        messages.append("Added: " + ", ".join(changes['A']))
    if changes['M']:
        messages.append("Modified: " + ", ".join(changes['M']))
    if changes['D']:
        messages.append("Deleted: " + ", ".join(changes['D']))
    return "; ".join(messages)


def commit_changes(message):
    """Commit changes with the given commit message."""
    subprocess.run(["git", "add", "."])  # Stage all changes
    subprocess.run(["git", "commit", "-m", message])


# Main workflow
status_lines = get_git_status()
if status_lines:
    changes = parse_git_status(status_lines)
    commit_message = generate_commit_message(changes)
    if commit_message:  # Proceed to commit if there are changes
        commit_changes(commit_message)
        print(f"Committed with message: '{commit_message}'")
    else:
        print("No changes to commit.")
else:
    print("No changes detected.")


def get_git_status():
    """Run `git status` command and return its output."""
    result = subprocess.run(
        ["git", "status", "--porcelain"], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip().split('\n')


def parse_git_status(status_lines):
    """Parse the output of `git status --porcelain` and organize file changes."""
    changes = {'A': [], 'M': [], 'D': []
               }  # A for added, M for modified, D for deleted
    for line in status_lines:
        if line:  # Ignore empty lines
            status = line[0]
            filename = line[3:]
            if status in changes:
                changes[status].append(filename)
            elif status == 'R':  # Handle renamed files
                _, old_file, new_file = line.split(" ")
                changes['D'].append(old_file)
                changes['A'].append(new_file)
    return changes


def generate_commit_message(changes):
    """Generate a commit message based on the file changes."""
    messages = []
    if changes['A']:
        messages.append("Added: " + ", ".join(changes['A']))
    if changes['M']:
        messages.append("Modified: " + ", ".join(changes['M']))
    if changes['D']:
        messages.append("Deleted: " + ", ".join(changes['D']))
    return "; ".join(messages)


def commit_changes(message):
    """Commit changes with the given commit message."""
    subprocess.run(["git", "add", "."])  # Stage all changes
    subprocess.run(["git", "commit", "-m", message])


# Main workflow
status_lines = get_git_status()
if status_lines:
    changes = parse_git_status(status_lines)
    commit_message = generate_commit_message(changes)
    if commit_message:  # Proceed to commit if there are changes
        commit_changes(commit_message)
        print(f"Committed with message: '{commit_message}'")
    else:
        print("No changes to commit.")
else:
    print("No changes detected.")
