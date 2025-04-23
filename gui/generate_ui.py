import customtkinter as ctk
from libs.save_screen_config import save_window_data
from libs.handle_config import load_from_config

def get_label_options():
    config = load_from_config()
    return [mode["title"] for mode in config["modes"] if mode["title"].strip() != ""]

def create_window_label_entry(frame, window, row):
    """Erzeugt Label und Dropdown für ein Fenster."""
    title_var = ctk.StringVar(value=window["title"][0:63])
    title_label = ctk.CTkLabel(
        master=frame,
        textvariable=title_var,
        font=("Teko", 20),
        width=395,
        anchor="w",
        bg_color="#131619"
    )
    title_label.grid(row=row, column=0, padx=2, pady=2, sticky="w")

    # Aktuelle Label-Logik
    labels = window.get("labels", [])
    first_label = labels[0] if labels else "Kein Label"
    current_label = ctk.StringVar(value=first_label)

    def set_label(selected_label=None, target_window=window, label_var=current_label):
       selected = label_var.get()
       if selected not in target_window.get("labels", []):
            target_window.setdefault("labels", []).append(selected)
       save_window_data(
            call="screenmanagement",
            dropdown_label=selected,
            modified_window=target_window
        )

    label_dropdown = ctk.CTkOptionMenu(
        master=frame,
        variable=current_label, 
   values=get_label_options(),  # ← immer aktuell!
        command=lambda _: set_label()
    )
    label_dropdown.grid(row=row, column=1, padx=5, pady=2, sticky="e")

def generate_ui(windows, root):
    """Erzeugt die gesamte Fenster-UI dynamisch."""
    for i, window in enumerate(windows):
        create_window_label_entry(root, window, row=i + 2)
