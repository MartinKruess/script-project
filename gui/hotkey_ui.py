import customtkinter as ctk
from PIL import Image
from tkinter import filedialog
from functools import partial
from libs.hotkey_manager import hotkeys
from libs.brows_and_store import browse_and_store

def render_hotkeys(frame_hotkeys_preview):

    for i, key in enumerate(hotkeys):
        ctk.CTkLabel(
            master=frame_hotkeys_preview,
            text=f"{key["hotkey"]} - {key["type"]}",
            font=("Teko", 22),
        ).place(x=50, y=30 * i+ 20)

img_lock = ctk.CTkImage(
    light_image=Image.open("images/lock.png"),
    dark_image=Image.open("images/lock.png"),
    size=(16, 16),
)

def render_hotkeys_table(frame, modis, root):
    headers = ["Hotkey", "Typ", "Aktion", "Lock", "Reset"]
    for col, title in enumerate(headers):
        label = ctk.CTkLabel(frame, text=title.upper(), font=("Teko", 24, "bold"))
        label.grid(row=0, column=col, padx=8, pady=(10, 8))

    for i, hk in enumerate(hotkeys, start=1):
        # Hotkey anzeigen
        ctk.CTkLabel(frame, text=hk["hotkey"], font=("Teko", 20)).grid(row=i, column=0, padx=3, pady=2)

        # Typ anzeigen
        ctk.CTkLabel(frame, text=hk["type"], font=("Teko", 20)).grid(row=i, column=1, padx=5, pady=0)

        # Interaktives Ziel-Feld (nur bei execute/link)
        if hk["type"] in ["execute", "link"]:
            # Zeige Namen wenn vorhanden, sonst Pfad
            display_text = hk.get("name") or hk.get("path") or "Ziel wählen..."

            # Eingabefeld mit Button zum Pfad auswählen
            entry = ctk.CTkEntry(frame, width=120, font=("Teko", 20))
            entry.insert(0, display_text)
            entry.grid(row=i, column=2, padx=5, pady=1)

            entry.bind("<Button-1>", partial(browse_and_store, entry, hk, root, hotkeys))

            ctk.CTkCheckBox(frame, text="", width=0).grid(row=i, column=3, padx=5, pady=3)

            img_x = ctk.CTkImage(
                light_image=Image.open("images/reset.png"),
                dark_image=Image.open("images/reset.png"),
                size=(16, 16),
            )

            ctk.CTkButton(
                master=frame,
                width=16,
                height=16,
                fg_color="transparent",
                image=img_x,
                text=""
            ).grid(row=i, column=4, padx=3, pady=2)

        elif hk["type"] == "mode":
            index = hk.get("mode_index")
            if index is not None and index < len(modis):
                title = modis[index]["title"]
                ctk.CTkLabel(frame, text=f"Modus: {title}").grid(row=i, column=2, padx=5, pady=2)
