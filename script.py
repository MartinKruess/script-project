from tkinter import *
import customtkinter as ctk
import pygetwindow as getWindow

# Pages
from pages.page_home import render_home_page
from pages.page_hotkeys import render_hotkeys_page

# Libs (Config)
from libs.rules import not_allowed_titles, window_shorts
from libs.handle_config import load_from_config, save_in_config

# GUI (Optik)
from gui.nav_btn_ui import generate_nav_elements
from gui.generate_modi_btn import generate_modi_btn
from gui.generate_ui import generate_ui
from libs.hotkey_manager import generate_hotkeys
from gui.hotkey_ui import render_hotkeys, render_hotkeys_table

# GUI (Frames)
from gui.structures.nav_frame import create_frame_nav
# from gui.structures.modi_frame import create_frame_modis
# from gui.structures.add_del_frame import create_frame_add_del
# from gui.structures.hotkey_frame import create_frame_hotkeys

# Modules (refactoring)
from modules.modi_controller import modis, delete_mode, render_modis, delete_mode, add_mode
from modules.set_label import label_window
from modules.simplify_title import simplify_title


config = load_from_config()

# Reset Start-Settings
for i, mode in enumerate(config["modes"]):
    if mode.get("is_default"):
        current_mode_index = i
        config["user_settings"]["last_mode"] = current_mode_index
        break

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
    global current_mode_index
    current_mode_index = i
    status_var.set(modis[current_mode_index]["title"].upper())
    config["user_settings"]["last_mode"] = current_mode_index
    save_in_config(config)

# 3. GUI-Fenster erstellen
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Main Window Properties
root = ctk.CTk()
root.title("Controll Center - Dashboard")
root.geometry("600x900")
root.configure(bg="#242629")
root.resizable(False, False)

# GUI-Struktur

# Navigation
frame_nav = create_frame_nav(root)
frame_nav.place(x=15, y=5)

# Inhalt wechselbar
content_frame = ctk.CTkFrame(root, width=580, height=830)
content_frame.place(x=10, y=60)


# Navigation Logik
def switch_page(target = "home"):
    global render_modis, render_hotkeys, content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    if target == "home":
        render_home_page(modis, content_frame, change_mode)
    elif target == "hotkeys":
        render_hotkeys_page(modis, content_frame, root)

# render_modis( frame_nav, change_mode)
generate_nav_elements(frame_nav, switch_page)

# load Hotkeys
generate_hotkeys(change_mode)

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


# 4. Fensterliste anzeigen
# generate_ui(windows, root)

switch_page("home")

# GUI starten
root.mainloop()