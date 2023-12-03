import tkinter as tk
import json
import os

basepath = "C:/Users/User/AppData/Local/Packages/"
settings_folder = ""
for folder in os.listdir(basepath):
    if folder.startswith("Microsoft.WindowsTerminal"):
        settings_folder = folder
        break
# Your JSON configuration data
setting_file = f"{basepath}{settings_folder}/LocalState/settings.json"


# Parse the JSON data
config = json.load(open(setting_file))
profiles = config["profiles"]["list"]


# Function to handle profile reordering
def move_up():
    pass  # Add logic to move the selected profile up


def move_down():
    pass  # Add logic to move the selected profile down


# Function to update the displayed profiles
def update_profiles(view):
    view.delete(0, tk.END)
    # for profile in profiles if profile["hidden"] == False :
    for profile in filter(lambda x: not x["hidden"], profiles):
        profiles_listbox.insert(tk.END, profile["name"])


(root := tk.Tk()).configure(bg="#333")
root.title("Powershell Profile Manager")

(frame := tk.Frame(root)).pack(padx=10, pady=10)
frame.configure(bg="#333")
(profiles_listbox := tk.Listbox(frame, width=50, height=15)).pack(side=tk.LEFT, padx=10)
(up_button := tk.Button(frame, text="👆", command=move_up)).pack(pady=5)
(down_button := tk.Button(frame, text="👇", command=move_down)).pack(pady=5)

update_profiles(profiles_listbox)


root.mainloop()
