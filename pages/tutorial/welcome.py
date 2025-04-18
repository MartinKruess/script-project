import customtkinter as ctk
import webbrowser
import json
import os

CONFIG_PATH = "config.json"

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

def show_welcome_window(root):
    config = load_config()
    if config.get("show_welcome", True) is False:
        return  # nicht anzeigen

    win = ctk.CTkToplevel(root)
    win.title("Welcome to WorkspaceCC")
    win.geometry("550x300")
    win.resizable(False, False)

    ctk.CTkLabel(
        win, text="Willkommen bei WorkspaceCC!",
        font=("Teko", 28, "bold")
    ).pack(pady=(20, 5))

    ctk.CTkLabel(
        win,
        text="Diese App hilft dir, Fenster zu organisieren, Hotkeys\n"
            "festzulegen und Arbeitsmodi mit Labels zu speichern.\n\n"
             "Du kannst jederzeit auf das Hilfemenü oben rechts klicken.",
        justify="center",
        font=("Arial", 18)
    ).pack(padx=20, pady=(5, 15))

    def open_docs():
        webbrowser.open("https://github.com/dein-repo/WorkspaceCC")  # <- Link anpassen!

    ctk.CTkButton(win, text="📖 Zum GitHub-Tutorial", font=("Arial", 16, "bold"), command=open_docs).pack(pady=(5, 15))

    show_next_time = ctk.CTkCheckBox(
        win, text="Beim nächsten Start erneut anzeigen", onvalue=True, offvalue=False,
        font=("Arial", 16),
        text_color="#ffff00"
    )
    show_next_time.select()
    show_next_time.pack(pady=(0, 10))

    def close_and_save():
        config["show_welcome"] = show_next_time.get()
        save_config(config)
        win.destroy()

    ctk.CTkButton(win, text="Fertig", font=("Arial", 16, "bold"), command=close_and_save).pack(pady=(0, 20))

# ----------------------- WELCOME END -----------------------

