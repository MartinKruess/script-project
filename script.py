from rich.pretty import pprint
from tkinter import *
import customtkinter as ctk
import pygetwindow as getWindow

# Libs (Config)
from libs.rules import not_allowed_titles, window_shorts

# Modules (refactoring)
from modules.modi_controller import modis, delete_mode, render_modis, delete_mode, add_mode
from modules.set_label import label_window
from modules.generate_ui import generate_ui
from modules.simplify_title import simplify_title
from modules.generate_modi_btn import generate_modi_btn

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
ctk.set_default_color_theme("blue")

# Main Window Properties
root = ctk.CTk()
root.title("Controll Center - Dashboard")
root.geometry("600x800")
root.configure(bg="#242639")
root.resizable(False, False)

# GUI-Struktur
frame_modis = ctk.CTkFrame(
    master=root,
    width= 280,
    height=110
)
frame_modis.place(x=20, y=40)
frame_add_del = ctk.CTkFrame(
    master=root,
    width= 265,
    height=110
)
frame_add_del.place(x=310, y=40)

render_modis(modis, frame_modis, change_mode)

status_var = ctk.StringVar(value=modis[current_mode_index]["title"].upper())

# ACTIVE MODE
Label_active_mode = ctk.CTkLabel(
    master=root,
    textvariable=status_var,
    font=("Impact", 14),
    text_color="#009dff",
    height=25,
    width=75,
    corner_radius=0,
    bg_color="#1c1c1c",
    fg_color="#1c1c1c",
)
Label_active_mode.place(x=530, y=0)


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


# button = ctk.CTkButton(root, text="Modus wechseln", command=change_mode)
# button.grid(row=1, column=0, columnspan=2, pady=(0, 16))

# 4. Fensterliste anzeigen
# generate_ui(windows, root)

# GUI starten
root.mainloop()