from main import get_config, os, get_settings_path, json


appProfile = {
    "colorScheme": "Campbell",
    "commandline": "pythonw main.py",
    "guid": "{d2f58b89-0841-4866-864b-ca055e3772ee}",
    "hidden": False,
    "icon": "https://cdn-icons-png.flaticon.com/512/4394/4394574.png",
    "name": "Profile Manager",
    "startingDirectory": f"{os.getcwd()}",
    "suppressApplicationTitle": True,
    "tabTitle": "Profile Manager Host",
}

c = get_config()

duplicate = False
for p in c["profiles"]["list"]:
    if p["name"] == "Profile Manager":
        duplicate = True
        break

if not duplicate:
    c["profiles"]["list"].append(appProfile)

json.dump(c, open(get_settings_path(), "w"), indent=4)
