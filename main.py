import os
import shutil
from tkinter import filedialog

import git


def choice():
    print("This program only allow you to create & manage local git repositories.")
    print()
    print("What would you like to do?")
    print("1. Create a new git repository")
    print("2. Push your repo to github")
    print("3. Exit")
    user_choice = input("Enter your choice: ")
    if user_choice == '1':
        create_repo()
    elif user_choice == '2':
        push_repo()
    elif user_choice == '3':
        print("Goodbye!")
    else:
        print("Not a option")


def create_repo():
    repo_name = input("Enter the name of the repository: ")
    new_repo = git.Repo.init(repo_name)
    print("Select a directory to save the repo...")
    directory_chooser(repo_name)


def push_repo():
    print("1. Create a new git repository")
    print("2. Select an existing git repository")
    print("3. Exit")
    user_choice = input("Enter your choice: ")
    if user_choice == '1':
        create_repo()
    elif user_choice == '2':
        selected_directory = filedialog.askdirectory()
        path = selected_directory
        name = os.path.basename(path)
        print(f'Your git repo {str(name)} was selected successfully at {selected_directory}')
        selected_repo = git.Repo(path)
        # update = selected_repo.git.pull()
        remote_repo = input("Enter the link of the remote repository: ")
        remote_repo = selected_repo.remotes.origin.push()


def directory_chooser(repo_name):
    selected_directory = filedialog.askdirectory()
    print(f'The git repo {repo_name} was create successfully &'
          f' save at {selected_directory}')
    src_path = os.getcwd() + '/' + repo_name
    dst_path = selected_directory
    shutil.move(src_path, dst_path)  # move the repo to the selected directory


def main():
    # choice()
    push_repo()


if __name__ == '__main__':
    main()
