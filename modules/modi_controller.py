import tkinter.font as tkfont
import customtkinter as ctk
import json
from gui.generate_modi_btn import generate_modi_btn
from libs.save_in_config import save_in_config

with open("data/config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

modis = config["modes"]

# GUI-Modi-BTN´s

def render_modis(modis, parent_frame, change_mode):

    for widget in parent_frame.winfo_children():
        widget.destroy()

    for i, mode in enumerate(modis):
        mode_title = f"Btn_{mode["title"]}"
        mode_title = ctk.CTkButton(**generate_modi_btn(mode["title"], mode["bg_color"], mode["color"], i, parent_frame, change_mode))
        if i != 0 and i < 3:
            mode_title.place(x=20 + 10 * i + i * 75, y=15)
        elif i == 3:
            mode_title.place(x=20, y=60)
        elif i >= 3:
            mode_title.place(x=20 + 10 * (i - 3) + (i -3) * 75, y=60)
        else:
            mode_title.place(x=20, y=15)

# ADD Mode
def add_mode(modis, Entry_add_mode, frame_modis, change_mode):
    user_input = Entry_add_mode.get()

    for mode in modis:
        if mode["title"] == "":
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