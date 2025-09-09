# Git-Automation-Script
A Python script designed to automate and simplify the Git workflow with an interactive menu system.

📋 Description

This Python script provides an interactive command-line interface to automate common Git operations, eliminating the need to remember complex commands and streamlining the version control process.
⚙️ Prerequisites

    Git must be installed and configured on your machine

    Python 3.x installed on your system

    PyInstaller (for creating executable)

📦 Installation

    Install PyInstaller:

bash

pip install pyinstaller

    Create executable:

bash

pyinstaller --onefile --console --name="GitMenu" your_script_name.py

✨ Features

    Interactive Menu System: User-friendly interface for Git operations

    Automated Commit Process: Handles git add . and git commit with a custom message

    One-Click Push/Pull: Simplified synchronization with remote repositories

    Cross-Platform Compatibility: Works on both Windows and Unix-based systems

    Error Handling: Robust error checking and user feedback

    Clean Interface: Automatic terminal clearing for better user experience

🚀 Usage

Run the executable:
bash

./GitMenu

Or run the script directly:
bash

python git_automation.py

Then choose from the following options:

    Commit: Stage all changes and commit with a custom message

    Push: Push committed changes to the remote repository

    Pull: Fetch and merge changes from the remote repository

    Exit: Close the application

🔧 Functions

    gc(message): Git add and commit with a custom message

    gps(): Git push to remote repository

    gpl(): Git pull from remote repository

    clearSystem(): Cross-platform terminal clearing

    menu(): Display interactive options

    main(): Main program loop

💡 Benefits

    Saves time on repetitive Git commands

    Reduces human error in the commit process

    Provides consistent commit practices

    Ideal for both beginners and experienced developers

    Easily extendable for additional Git functionality

📝 Example Workflow

    Run the script/executable

    Select option 1 (Commit)

    Enter your commit message

    Select option 2 (Push) to sync with remote

    Enjoy your automated Git workflow!

⚠️ Important Notes

    Ensure Git is properly installed and configured with your user credentials

    The script must be run in a directory that is a Git repository

    Your remote repository must be properly set up for push/pull operations

This script is particularly useful for developers who frequently work with Git and want to streamline their daily version control tasks.
