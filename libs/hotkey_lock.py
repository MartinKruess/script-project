# 🔧 Datei: libs/hotkey_lock.py

from functools import partial
from libs.brows_and_store import browse_and_store
from libs.handle_config import save_in_config

def toggle_lock(hk, var, button, entry, root, hotkeys, reset_btn):
    locked = var.get()
    hk["is_locked"] = locked
    button.configure(state="disabled" if locked else "normal")
    entry.configure(state="disabled" if locked else "normal")

    if locked:
        entry.unbind("<Button-1>")
    else:
        entry.bind("<Button-1>", partial(
            browse_and_store, entry, hk, root, hotkeys, var, toggle_lock, reset_btn
        ))

    config = {"hotkeys": hotkeys}
    save_in_config(config)