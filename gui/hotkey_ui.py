import customtkinter as ctk
from tkinter import filedialog
from libs.hotkey_manager import hotkeys
from libs.brows_and_store import browse_and_store

def select_path(entry_field):
    path = filedialog.askopenfilename(title="Wähle eine Datei aus")
    if path:
        entry_field.delete(0, "end")
        entry_field.insert(0, path)


def render_hotkeys(frame_hotkeys_preview):

    for i, key in enumerate(hotkeys):
        ctk.CTkLabel(
            master=frame_hotkeys_preview,
            text=f"{key["hotkey"]} - {key["type"]}",
            font=("Teko", 22),
        ).place(x=50, y=30 * i+ 20)


def render_hotkeys_table(frame, modis, root):
    headers = ["Hotkey", "Typ", "Aktion / Ziel"]
    for col, title in enumerate(headers):
        label = ctk.CTkLabel(frame, text=title.upper(), font=("Teko", 24, "bold"))
        label.grid(row=0, column=col, padx=8, pady=(12, 12))

    for i, hk in enumerate(hotkeys, start=1):
        # Hotkey anzeigen
        ctk.CTkLabel(frame, text=hk["hotkey"], font=("Teko", 22)).grid(row=i, column=0, padx=3, pady=2)

        # Typ anzeigen
        ctk.CTkLabel(frame, text=hk["type"], font=("Teko", 22)).grid(row=i, column=1, padx=5, pady=2)

        # Interaktives Ziel-Feld (nur bei execute/link)
        if hk["type"] in ["execute", "link"]:
            # Zeige Namen wenn vorhanden, sonst Pfad
            display_text = hk.get("name") or hk.get("path") or "Ziel wählen..."

            # Eingabefeld mit Button zum Pfad auswählen
            entry = ctk.CTkEntry(frame, width=160, font=("Teko", 22))
            entry.insert(0, display_text)
            entry.grid(row=i, column=2, padx=5, pady=2)

            entry.bind("<Button-1>", lambda event, e=entry: browse_and_store(e, hk, root))

        elif hk["type"] == "mode":
            index = hk.get("mode_index")
            if index is not None and index < len(modis):
                title = modis[index]["title"]
                ctk.CTkLabel(frame, text=f"Modus: {title}").grid(row=i, column=2, padx=5, pady=2)
