import tkinter.font as tkfont
import customtkinter as ctk
from gui.generate_modi_btn import generate_modi_btn
from libs.handle_config import load_from_config, save_in_config

config = load_from_config()
modis = config["modes"]

# GUI-Modi-BTN´s

def render_modis(modis, parent_frame, change_mode):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    for i, mode in enumerate(modis):
        title = mode["title"]

        # Nur Buttons mit Titel anzeigen
        if not title:
            continue

        btn = ctk.CTkButton(**generate_modi_btn(
            title,
            mode["bg_color"],
            mode["color"],
            i,
            parent_frame,
            change_mode
        ))

        # Debug (optional)
        print(f"Button {i+1}: {title}")

        # Max. 3 Buttons pro Zeile, danach Umbruch
        if i < 3:
            btn.place(x=20 + i * (75 + 10), y=15)
        else:
            btn.place(x=20 + (i - 3) * (75 + 10), y=60)


# ADD Mode
def add_mode(modis, Entry_add_mode, frame_modis, change_mode):
    user_input = Entry_add_mode.get().strip()

    for mode in modis:
        if mode["title"] == "":
            print(mode["title"])
            mode["title"] = user_input[:9] or user_input
            render_modis(modis, frame_modis, change_mode)
            Entry_add_mode.delete(0, "end")
            save_in_config(config)
            return
        else:
            continue


# delete mode
def delete_mode(modis, Entry_delete_mode, frame_modis, change_mode):
    index = int(Entry_delete_mode.get())
    if index < 2:
        print("Systemmodi dürfen nicht gelöscht werden.")
        return False
    modis[index]["title"] = ""
    render_modis(modis, frame_modis, change_mode)
    Entry_delete_mode.delete(0, "end")
    save_in_config(config)
    return True