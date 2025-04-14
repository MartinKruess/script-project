from tkinter import filedialog
import customtkinter as ctk
from pathlib import Path

def browse_and_store(entry_ref, hk_ref, root):
    path = filedialog.askopenfilename(title="Datei auswählen")
    if path:
        hk_ref["path"] = path

        # Pop-up zur Namensvergabe
        name_popup = ctk.CTkToplevel()
        name_popup.title("Name vergeben")
        name_popup.geometry("300x140")

        # Always on top
        name_popup.attributes("-topmost", True)

        # Im Vordergrund UND zentrieren relativ zu root:
        root_x = root.winfo_x()
        root_y = root.winfo_y()
        root_width = root.winfo_width()
        root_height = root.winfo_height()

        popup_width = 300
        popup_height = 120

        pos_x = root_x + (root_width - popup_width) // 2
        pos_y = root_y + (root_height - popup_height) // 2

        name_popup.geometry(f"{popup_width}x{popup_height}+{pos_x}+{pos_y}")

        label = ctk.CTkLabel(name_popup, text="Wie soll der Hotkey heißen?")
        label.pack(pady=10)

        name_var = ctk.StringVar()
        entry_name = ctk.CTkEntry(name_popup, textvariable=name_var)
        entry_name.pack(pady=5)

        def save_name():
            name = name_var.get().strip()
            # Wenn leer → Dateiname ohne Erweiterung
            if not name:
                name = Path(path).stem
            hk_ref["name"] = name

            # Update des Entry-Felds
            entry_ref.delete(0, "end")
            entry_ref.insert(0, name)

            name_popup.destroy()

        ctk.CTkButton(name_popup, text="Speichern", command=save_name).pack(pady=5)