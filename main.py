import json, os

try:
    import webview, pythonnet
except Exception as e:
    print("This script has dependencies:")
    print("Python packages: pywebview pythonnet")
    print("Other dependencies: Microsoft.DotNet.SDK.7")
    print("You can install them yourself using `pip install pywebview pythonnet` and `winget install Microsoft.DotNet.SDK.7`")
    print("or they can be installed automatically")
    ans = input("Would you like them to be installed automatically? (y/n): ").lower()
    if ans == "yes" or ans == "y":
        os.system("winget install Microsoft.DotNet.SDK.7")
        os.system("pip install pywebview pythonnet")
        import webview, pythonnet
    else:
        print("Ok, exiting")
        exit(0)


def get_settings_path():
    basepath = f"C:/Users/{os.getlogin()}/AppData/Local/Packages/"
    settings_folder = next((f for f in os.listdir(basepath) if f.startswith("Microsoft.WindowsTerminal")), "")

    return f"{basepath}{settings_folder}/LocalState/settings.json"


setting_file = get_settings_path()


def get_config():
    config = json.load(open(setting_file))
    return config


def get_profiles():
    profiles = get_config()["profiles"]["list"]
    return profiles


def set_profiles(profiles_name_order):
    old_profiles = get_profiles()
    new_profiles = []
    for p in profiles_name_order:
        for o in old_profiles:
            if o["name"] == p:
                new_profiles.append(o)
    print(profiles_name_order)
    print(new_profiles)

    conf = get_config()
    conf["profiles"]["list"] = new_profiles
    json.dump(conf, open(setting_file, "w"), indent=4)


def main():
    w = webview.create_window(
        'Terminal Profile Manager',
        'index.html',
        background_color='#000000',
        width=360,
        height=640,
        # draggable=True,
        # easy_drag=False,
    )
    w.expose(get_profiles, set_profiles)

    webview.start(
        debug=False,
        http_server=True,
        # gui="cef",
    )


if __name__ == "__main__":
    main()
