import customtkinter as ctk
from PIL import Image
from tkinter import filedialog
from functools import partial
from libs.brows_and_store import browse_and_store
from libs.handle_config import load_from_config, save_in_config

config = load_from_config()
hotkeys = config["hotkeys"]

def render_hotkeys(hotkeys_frame):

    for i, key in enumerate(hotkeys):
        ctk.CTkLabel(
            master=hotkeys_frame,
            text=f"{key["hotkey"]} - {key["type"]}",
            font=("Teko", 22),
        ).place(x=50, y=30 * i+ 20)

img_x = ctk.CTkImage(
    light_image=Image.open("images/reset.png"),
    dark_image=Image.open("images/reset.png"),
    size=(16, 16),
)

def render_hotkeys_table(frame, modis, root):
    # Erstelle Tabel-Head
    headers = ["Hotkey", "Typ", "Aktion", "Lock", "Reset"]
    for col, title in enumerate(headers):
        label = ctk.CTkLabel(frame, text=title.upper(), font=("Teko", 24, "bold"))
        label.grid(row=0, column=col, padx=8, pady=(10, 8))

    # Filter active Hotkeys
    active_hotkeys = [hk for hk in hotkeys if hk.get("hotkey")]
    for i, hk in enumerate(active_hotkeys, start=1):
        # Col 0 - show Hotkey
        ctk.CTkLabel(frame, text=hk["hotkey"], font=("Teko", 20)).grid(row=i, column=0, padx=3, pady=2)

        # Col 1 - show Types
        ctk.CTkLabel(frame, text=hk["type"], font=("Teko", 20)).grid(row=i, column=1, padx=5, pady=0)

        # Col 2 - show Action
        if hk["type"] == "mode":
            index = hk.get("mode_index")
            if index is not None and index < len(modis):
                title = modis[index]["title"]
                ctk.CTkLabel(frame, text=f"Modus: {title}", font=("Teko", 20)).grid(row=i, column=2, padx=5, pady=2)

        # Col 3: Lock/Unlock Checkbox (execute only)
        if hk["type"] == "execute":
            is_locked = ctk.BooleanVar(value=hk.get("is_locked", True))

            # Entry für Pfad/Namen
            display_text = hk.get("name") or hk.get("path") or "Ziel wählen..."
            entry = ctk.CTkEntry(frame, width=120, font=("Teko", 20))
            entry.insert(0, display_text)
            entry.grid(row=i, column=2, padx=5, pady=1)
            entry.configure(state="disabled" if is_locked.get() else "normal")

            if is_locked.get():
                entry.unbind("<Button-1>")
            else:
                entry.bind("<Button-1>", partial(browse_and_store, entry, hk, root, hotkeys, is_locked))

            # Reset-Button
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

            # Reset-Funktion (muss VOR der Verwendung existieren!)
            def reset_hotkey(entry, hk):
                entry.delete(0, 'end')
                hk["path"] = ""
                hk["name"] = ""
                entry.insert(0, "Ziel wählen...")
                reset_button.configure(state="disabled")
                entry.configure(state="disabled")
                save_in_config(config)

            # Checkbox
            checkbox = ctk.CTkCheckBox(
                master=frame,
                text="",
                width=0,
                variable=is_locked
            )
            checkbox.grid(row=i, column=3, padx=5, pady=3)

            # Callback: Lock/Unlock
            def toggle_lock(hk=hk, var=is_locked, button=reset_button, entry=entry):
                locked = var.get()
                hk["is_locked"] = locked
                button.configure(state="disabled" if locked else "normal")
                entry.configure(state="disabled" if locked else "normal")

                # 🔁 Binding aktualisieren
                if locked:
                    entry.unbind("<Button-1>")
                else:
                    entry.bind("<Button-1>", partial(browse_and_store, entry, hk, root, hotkeys))

                save_in_config(config)

            checkbox.configure(command=toggle_lock)
