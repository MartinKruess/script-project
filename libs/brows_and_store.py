# from tkinter import filedialog
# import customtkinter as ctk
# from pathlib import Path

# def browse_and_store(entry_ref, hk_ref, root):
#     path = filedialog.askopenfilename(title="Datei auswählen")
#     if path:
#         hk_ref["path"] = path

#         # Pop-up zur Namensvergabe
#         name_popup = ctk.CTkToplevel()
#         name_popup.title("Name vergeben")
#         name_popup.geometry("300x140")

#         # Always on top
#         name_popup.attributes("-topmost", True)

#         # Im Vordergrund UND zentrieren relativ zu root:
#         root_x = root.winfo_x()
#         root_y = root.winfo_y()
#         root_width = root.winfo_width()
#         root_height = root.winfo_height()

#         popup_width = 300
#         popup_height = 120

#         pos_x = root_x + (root_width - popup_width) // 2
#         pos_y = root_y + (root_height - popup_height) // 2

#         name_popup.geometry(f"{popup_width}x{popup_height}+{pos_x}+{pos_y}")

#         label = ctk.CTkLabel(name_popup, text="Wie soll der Hotkey heißen?")
#         label.pack(pady=10)

#         name_var = ctk.StringVar()
#         entry_name = ctk.CTkEntry(name_popup, textvariable=name_var)
#         entry_name.pack(pady=5)

#         def save_name():
#             name = name_var.get().strip()
#             # Wenn leer → Dateiname ohne Erweiterung
#             if not name:
#                 name = Path(path).stem
#             hk_ref["name"] = name


#             # Update des Entry-Felds
#             entry_ref.delete(0, "end")
#             entry_ref.insert(0, name)

#             name_popup.destroy()

#         ctk.CTkButton(name_popup, text="Speichern", command=save_name).pack(pady=5)

from tkinter import filedialog
import customtkinter as ctk
from pathlib import Path
from libs.handle_config import load_from_config, save_in_config

def browse_and_store(entry_ref, hk_ref, root, hotkey_list, is_locked, event):
    path = filedialog.askopenfilename(title="Datei auswählen")
    if path:
        old_path = hk_ref.get("path")
        old_name = hk_ref.get("name")

        # Temporär Pfad aktualisieren, wird nur gespeichert wenn sich etwas ändert
        hk_ref["path"] = path

        # Pop-up zur Namensvergabe
        name_popup = ctk.CTkToplevel()
        name_popup.title("Name vergeben")
        name_popup.geometry("300x140")
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
            if not name:
                name = Path(path).stem

            # Vergleich vor dem Speichern
            if path != old_path or name != old_name:
                hk_ref["path"] = path
                hk_ref["name"] = name
                hk_ref["is_locked"] = True
                is_locked.set(True)
               

                # 🔁 Speichern: ganzen Config laden, Hotkeys ersetzen, speichern
                config = load_from_config()
                config["hotkeys"] = hotkey_list
                save_in_config(config)

                print("✔️ Änderungen gespeichert:", path, name)
            else:
                print("ℹ️ Keine Änderungen – nichts gespeichert.")

            entry_ref.delete(0, "end")
            entry_ref.insert(0, name)
            name_popup.destroy()

        ctk.CTkButton(name_popup, text="Speichern", command=save_name).pack(pady=5)
