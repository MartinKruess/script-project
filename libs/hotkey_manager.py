import keyboard
import subprocess
import webbrowser
from libs.handle_config import load_from_config

config = load_from_config()
hotkeys = config["hotkeys"]

def generate_hotkeys(change_mode):
    for hk in hotkeys:
        if hk["type"] == "mode":
            keyboard.add_hotkey(hk["hotkey"], lambda i=hk["mode_index"]: change_mode(i))
        elif hk["type"] == "execute" and hk.get("path"):
            keyboard.add_hotkey(hk["hotkey"], lambda path=hk["path"]: subprocess.Popen(path, shell=True))
        elif hk["type"] == "link" and hk.get("url"):
            keyboard.add_hotkey(hk["hotkey"], lambda url=hk["url"]: webbrowser.open(url))