import keyboard
import subprocess
import webbrowser

hotkeys = [
    {
        "hotkey": "alt+^",
        "increment": 1,
        "type": "mode_next"
    },
    {
        "hotkey": "ctrl+F1",
        "mode_index": 0,
        "type": "mode"
    },
    {
        "hotkey": "ctrl+F2",
        "mode_index": 1,
        "type": "mode"
    },
    {
        "hotkey": "ctrl+F3",
        "mode_index": 2,
        "type": "mode"
    },
    {
        "hotkey": "ctrl+F4",
        "mode_index": 3,
        "type": "mode"
    },
    {
        "hotkey": "ctrl+F5",
        "mode_index": 4,
        "type": "mode"
    },
    {
        "hotkey": "ctrl+F6",
        "mode_index": 5,
        "type": "mode"
    },
    {
        "hotkey": "ctrl+F7",
        "path": "test",
        "type": "execute"
    },
    {
        "hotkey": "ctrl+F8",
        "path": "",
        "type": "execute"
    },
    {
        "hotkey": "ctrl+F9",
        "path": "",
        "type": "execute"
    },
    {
        "hotkey": "ctrl+F10",
        "path": "",
        "type": "execute"
    },
]

def generate_hotkeys(change_mode):
    for hk in hotkeys:
        if hk["type"] == "mode":
            keyboard.add_hotkey(hk["hotkey"], lambda i=hk["mode_index"]: change_mode(i))
        elif hk["type"] == "execute" and hk.get("path"):
            keyboard.add_hotkey(hk["hotkey"], lambda path=hk["path"]: subprocess.Popen(path, shell=True))
        elif hk["type"] == "link" and hk.get("url"):
            keyboard.add_hotkey(hk["hotkey"], lambda url=hk["url"]: webbrowser.open(url))