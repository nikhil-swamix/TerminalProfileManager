import webview, json, os, pythonnet

# try:
#     from pythonnet import load
#     load("coreclr")

# except Exception as e:
#     print(e)
#     os.system("winget install Microsoft.DotNet.SDK.7")

basepath = f"C:/Users/{os.getlogin()}/AppData/Local/Packages/"
settings_folder = next((f for f in os.listdir(basepath) if f.startswith("Microsoft.WindowsTerminal")), "")
setting_file = f"{basepath}{settings_folder}/LocalState/settings.json"


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


w = webview.create_window(
    'powershell Manager',
    'index.html',
    background_color='#000',
    width=360,
    height=640,
    # draggable=True,
    # easy_drag=False,
)
w.expose(get_profiles, set_profiles)

webview.start(
    debug=True,
    http_server=True,
    gui="cef",
    
)
