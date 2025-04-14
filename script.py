from rich.pretty import pprint
from tkinter import *
import customtkinter as ctk
import pygetwindow as getWindow

# Libs (Config)
from libs.rules import not_allowed_titles, window_shorts

# GUI (Optik)
from gui.generate_modi_btn import generate_modi_btn
from gui.generate_ui import generate_ui
from libs.hotkey_manager import generate_hotkeys
from gui.hotkey_ui import render_hotkeys, render_hotkeys_table

# GUI (Frames)
from gui.structures.modi_frame import create_frame_modis
from gui.structures.add_del_frame import create_frame_add_del
from gui.structures.hotkey_frame import create_frame_hotkeys

# Modules (refactoring)
from modules.modi_controller import modis, delete_mode, render_modis, delete_mode, add_mode
from modules.set_label import label_window
from modules.simplify_title import simplify_title

# Debug-Ausgabe (ich)
def log(obj):
    pprint(obj, expand_all=True)


current_mode_index = 0

# 1. Fenster erfassen und eigene Struktur bauen
activeWindows = getWindow.getWindowsWithTitle("")
windows = []

for window in activeWindows:
    if not window.title.strip():
        continue

    if not window.title in not_allowed_titles:
        first_part = window.title.split("-")
        short_title = simplify_title(window.title, window_shorts)

        state = {
            "id": window._hWnd,
            "title": short_title,
            "label": None,
            "screen": 1,
            "border": None,
            "is_active": window == getWindow.getActiveWindow(),
            "is_minimized": (window.left == -32000 and window.top == -32000),
            "handle": window,
        }
        windows.append(state)

# 2. GUI-Funktion: Modus wechseln
def change_mode(i):
    print("change_mode", i,)
    global current_mode_index
    current_mode_index = i
    status_var.set(modis[current_mode_index]["title"].upper())

# 3. GUI-Fenster erstellen
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Main Window Properties
root = ctk.CTk()
root.title("Controll Center - Dashboard")
root.geometry("600x800")
root.configure(bg="#242629")
root.resizable(False, False)

# GUI-Struktur

# Modis
frame_modis = create_frame_modis(root)
frame_modis.place(x=15, y=40)
frame_add_del = create_frame_add_del(root)
frame_add_del.place(x=310, y=40)

# Hotkeys
frame_hotkeys = create_frame_hotkeys(root)
frame_hotkeys["container"].place(x=20, y=170)

# load Modi_btns in frame
render_modis(modis, frame_modis, change_mode)
generate_hotkeys(change_mode)
# render_hotkeys(frame_hotkeys["preview"])
render_hotkeys_table(frame_hotkeys["preview"], modis, root)

status_var = ctk.StringVar(value=modis[current_mode_index]["title"].upper())

# ACTIVE MODE
Label_active_mode = ctk.CTkLabel(
    master=root,
    textvariable=status_var,
    font=("Impact", 20),
    text_color="#009dff",
    height=35,
    width=110,
    corner_radius=0,
    bg_color="#1c1c1c",
    fg_color="#1c1c1c",
)
Label_active_mode.place(x=490, y=0)


# ADD LABEL
Entry_add_mode = ctk.CTkEntry(
    master=frame_add_del,
    placeholder_text="add Label",
    placeholder_text_color="#999999",
    font=("Arial", 14),
    text_color="#ffffff",
    height=30,
    width=120,
    border_width=1,
    corner_radius=10,
    border_color="#000000",
    bg_color="#1c1c1c",
    fg_color="#242424",
    )
Entry_add_mode.place(x=20, y=20)
Entry_add_mode.bind("<Return>", lambda event: add_mode(modis, Entry_add_mode, frame_modis, change_mode))

# Delete LABEL
Entry_delete_mode = ctk.CTkEntry(
    master=frame_add_del,
    placeholder_text="delete Label",
    placeholder_text_color="#999999",
    font=("Arial", 14),
    text_color="#ffffff",
    height=30,
    width=120,
    border_width=1,
    corner_radius=10,
    border_color="#000000",
    bg_color="#1c1c1c",
    fg_color="#242424",
    )
Entry_delete_mode.place(x=20, y=60)
Entry_delete_mode.bind("<Return>", lambda event: delete_mode(modis, Entry_delete_mode, frame_modis, change_mode))


# 4. Fensterliste anzeigen
# generate_ui(windows, root)

# GUI starten
root.mainloop()