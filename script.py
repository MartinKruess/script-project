from tkinter import *
import customtkinter as ctk

# Pages
from pages.tutorial.welcome import show_welcome_window
from pages.page_home import render_home_page
from pages.page_hotkeys import render_hotkeys_page
from pages.page_window_list import render_window_list_page

# Libs (Config)
from libs.handle_config import load_from_config, save_in_config
from libs.get_windows import get_windows

# GUI (Optik)
from gui.nav_btn_ui import generate_nav_elements
from libs.hotkey_manager import generate_hotkeys
from gui.hotkey_ui import render_hotkeys

# GUI (Frames)
from gui.structures.nav_frame import create_frame_nav

# Modules (refactoring)
from modules.modi_controller import modis, render_modis

# Screen
from libs.save_screen_config import get_monitor_data
from libs.pos_windows import positionate_windows, find_window

config = load_from_config()

# Reset Start-Settings
config["user_settings"]["last_mode"] = 0
current_mode_index = 0
save_in_config(config)

# 1. Get Screen Info
get_monitor_data(config)

# 2. Fenster erfassen und eigene Struktur bauen
windows = get_windows()

# 3. GUI-Funktion: Modus wechseln
def change_mode(i):
    global current_mode_index
    current_mode_index = i
    config = load_from_config()
    status_var.set(modis[current_mode_index]["title"].upper())
    config["user_settings"]["last_mode"] = current_mode_index


    windows = config["labeled_windows"]
    mode_windows = list(filter(lambda win: find_window(win, modis[current_mode_index]["title"]), windows))
    print("Windows of mode",  mode_windows)

    positionate_windows(mode_windows)
    save_in_config(config)

# 4. GUI-Fenster erstellen
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# 5. Main Window Properties
root = ctk.CTk()
root.title("WorkspaceCC - Workspace Control Center")
root.geometry("600x900")
root.configure(bg="#242629")
root.resizable(False, False)

# 6. Welcome popup
show_welcome_window(root)

# 7. GUI-Struktur

# Navigation
frame_nav = create_frame_nav(root)
frame_nav.place(x=15, y=5)

# Inhalt wechselbar
content_frame = ctk.CTkFrame(root, width=580, height=830)
content_frame.place(x=10, y=60)

# Navigation Logik
def switch_page(target): #, nav_label={}
    global render_modis, render_hotkeys, content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    if target == "home":
        # nav_label["isActive"].set(True)
        render_home_page(modis, content_frame, change_mode, config)
        # render_screen_details (kommt noch)
        # render_save_screen_config (kommt noch)
    elif target == "hotkeys":
        render_hotkeys_page(modis, content_frame, root)
    elif target == "screenmanager":
        render_window_list_page(windows, content_frame)

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

switch_page("home")

# GUI starten
root.mainloop()