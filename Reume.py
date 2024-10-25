import subprocess

def clone_repo(repo_url, clone_dir):
    try:
        subprocess.run(['git', 'clone', repo_url, clone_dir], check=True)
        print(f"Cloned repository to {clone_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")

def create_branch(repo_path, branch_name):
    try:
        # Navigate to the repo directory and create the branch
        subprocess.run(['git', '-C', repo_path, 'checkout', '-b', branch_name], check=True)
        print(f"Branch '{branch_name}' created and checked out.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

import subprocess

def stage_changes(repo_path):
    try:
        # Stage all changes
        subprocess.run(['git', '-C', repo_path, 'add', '.'], check=True)
        print("Changes staged successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error staging changes: {e}")

def commit_changes(repo_path, commit_message):
    try:
        # Commit the changes
        subprocess.run(['git', '-C', repo_path, 'commit', '-m', commit_message], check=True)
        print("Changes committed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error committing changes: {e}")

def push_changes(repo_path, branch_name):
    try:
        # Push the changes to the remote repository
        subprocess.run(['git', '-C', repo_path, 'push', 'origin', branch_name], check=True)
        print(f"Changes pushed to branch '{branch_name}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing changes: {e}")


def upload_changes(repo_path, commit_message, branch_name):
    stage_changes(repo_path)
    commit_changes(repo_path, commit_message)
    push_changes(repo_path, branch_name)

# Path to your repository
repo_path = r"D:/MyWork/Resume/MyResume"  # Update this to your repo's path
commit_message = "Added new feature resume file"
branch_name = "bala-25102024"

upload_changes(repo_path, commit_message, branch_name)

#1repo_url = "https://github.com/Bala4426/Resume.git"
#1clone_dir = "D:/MyWork/Resume/MyResume"
#1branch_name = "bala-25102024"
#clone_repo(repo_url, clone_dir)
#1create_branch(clone_dir, branch_name)

