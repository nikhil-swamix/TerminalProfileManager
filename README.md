# Terminal Profile Manager

![Image of profiles being reordered](./images/drag-example.png)

## Introduction

Python script that utilizes the [`pywebview`](https://pywebview.flowrl.com/) library to create a window and display an HTML interface for managing Terminal profiles, a hacky fix for issue
[`#8914`](https://github.com/microsoft/terminal/issues/8914). The script "intelligently" reads the settings file of the Windows Terminal app to retrieve the existing profiles and allows the user to reorder them. The modified profiles are then saved back to the settings file. Since terminal watches this file, it will reload the profiles automagically!

## Features

- Drag and drop profiles to reorder them, and save the new order to the settings file.
- Intelligently read settings from `AppData/Local` folder irrespective of user name.
- Color theme matched to Windows Terminal dark mode.
- Edit/extend logic using simple Python code and change GUI using HTML and CSS.
- If Python is already installed, half the setup is done.
- jQuery, jQuery-UI and Bootstrap 5 used for GUI.
- Hidden profiles explicitly dimmed.
- Keyboard support planned in future.

## Prerequisites

Before running the script, please make sure you have the following prerequisites installed:

- Python 3.10 or higher (may work with lower versions, you can try and report)
- Run `pip install -r requirements.txt` and try running
- `winget` package manager for installing dotnet on the fly. If you don't want to install `winget`, then you can install it [here](https://dotnet.microsoft.com/en-us/download). Requires\* dotnet 5.0 or higher (\*might work with lower versions, untested).

## Usage

To use the PowerShell Manager script, follow these steps:

1. Try running `launcher.pyw`, if it works, you can skip to step 4.
2. Run the script using `python script.py`.
3. The PowerShell Manager window will open, displaying the profiles in the Windows Terminal settings file.
4. Reorder the profiles by dragging and dropping them.
5. Click the "Save" button to save the new profile order to the settings file.
6. Use `install-in-terminal.py` to install it right in terminal! ![Image of Profile Manager in the profile list](./images/profile-list-example.png)

## Configuration

The Profile Manager script includes the following configuration options:

- `width` and `height`: Set the width and height of the window displayed by the `webview` library.
- `debug`: Set to True to enable debug mode for `webview`.
- Styles have been kept similar to Windows Terminal, also you can change the styles in the `assets/styles.css` file.

## Bugs and Limitations

- `pythonnet` has some strange issue, when i tried to rip it to exe file using `py2exe`, it was not working, and using `pyinstaller` had partial success. if you know any fixes, please let me know, or send a PR addressing [this issue.](https://github.com/pythonnet/pythonnet/issues/1728)
- Currently tested for windows only, sorry 😅 you need to change few lines and find the settings.json in linux and macos and the logic should work.

### Urgent Notice!

#### im looking for a job, if you have any openings, please contact! if ur a dev, please give a referral. contacts in resume.

RESUME : https://docs.google.com/document/d/e/2PACX-1vRvk0ZEqt71qmJDJi-rhPt7zd4Aq3l7gN87BJjEKFZmNK4SQZTbSOKmg3T2OGd-D_SYyMYn3YjibVRj/pub
