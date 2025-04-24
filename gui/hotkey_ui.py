# 🔧 Datei: gui/hotkey_ui.py

import customtkinter as ctk
from PIL import Image
from functools import partial
from libs.brows_and_store import browse_and_store
from libs.handle_config import load_from_config, save_in_config
from libs.hotkey_lock import toggle_lock

config = load_from_config()
hotkeys = config["hotkeys"]

def render_hotkeys(hotkeys_frame):
    for i, key in enumerate(hotkeys):
        ctk.CTkLabel(
            master=hotkeys_frame,
            text=f"{key['hotkey']} - {key['type']}",
            font=("Teko", 22),
        ).place(x=50, y=30 * i + 20)

img_x = ctk.CTkImage(
    light_image=Image.open("images/reset.png"),
    dark_image=Image.open("images/reset.png"),
    size=(16, 16),
)

def render_hotkeys_table(frame, modis, root):
    headers = ["Hotkey", "Typ", "Aktion", "Lock", "Reset"]
    for col, title in enumerate(headers):
        label = ctk.CTkLabel(frame, text=title.upper(), font=("Teko", 24, "bold"))
        label.grid(row=0, column=col, padx=8, pady=(10, 8))

    active_hotkeys = [hk for hk in hotkeys if hk.get("hotkey")]
    for i, hk in enumerate(active_hotkeys, start=1):
        ctk.CTkLabel(frame, text=hk["hotkey"], font=("Teko", 20)).grid(row=i, column=0, padx=3, pady=2)
        ctk.CTkLabel(frame, text=hk["type"], font=("Teko", 20)).grid(row=i, column=1, padx=5, pady=0)

        if hk["type"] == "mode":
            index = hk.get("mode_index")
            if index is not None and index < len(modis):
                title = modis[index]["title"]
                ctk.CTkLabel(frame, text=f"Modus: {title}", font=("Teko", 20)).grid(row=i, column=2, padx=5, pady=2)

        if hk["type"] == "execute":
            is_locked = ctk.BooleanVar(value=hk.get("is_locked", True))
            display_text = hk.get("name") or hk.get("path") or "Ziel wählen..."

            entry = ctk.CTkEntry(frame, width=120, font=("Teko", 20))
            entry.insert(0, display_text)
            entry.grid(row=i, column=2, padx=5, pady=1)
            entry.configure(state="disabled" if is_locked.get() else "normal")

            state = "disabled" if is_locked.get() else "normal"
            reset_button = ctk.CTkButton(
                master=frame,
                width=16,
                height=16,
                fg_color="transparent",
                image=img_x,
                text="",
                state=state,
                command=lambda e=entry, h=hk: reset_hotkey(e, h)
            )
            reset_button.grid(row=i, column=4, padx=3, pady=2)

            def reset_hotkey(entry, hk):
                entry.delete(0, 'end')
                hk["path"] = ""
                hk["name"] = ""
                entry.insert(0, "Ziel wählen...")
                reset_button.configure(state="disabled")
                entry.configure(state="disabled")
                save_in_config(config)

            checkbox = ctk.CTkCheckBox(
                master=frame,
                text="",
                width=0,
                variable=is_locked
            )
            checkbox.grid(row=i, column=3, padx=5, pady=3)

            # 🔁 Eventbindung initial setzen
            if not is_locked.get():
                entry.bind("<Button-1>", partial(
                    browse_and_store, entry, hk, root, hotkeys, is_locked, toggle_lock, reset_button
                ))

            checkbox.configure(
                command=lambda hk=hk, var=is_locked, button=reset_button, entry=entry:
                    toggle_lock(hk, var, button, entry, root, hotkeys, reset_button)
            )
