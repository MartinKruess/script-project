

import customtkinter as ctk

LABEL_OPTIONS = ["Freizeit", "Arbeit", "Hobby", "Video", "Audio", "Image", "Streamer"]

def create_window_label_entry(root, window, row):
    """Erzeugt Label und Dropdown für ein Fenster."""
    # Titelanzeige
    title_var = ctk.StringVar(value=window["title"])
    title_label = ctk.CTkLabel(
        master=root,
        textvariable=title_var,
        font=("Arial", 10),
        width=330,
        wraplength=330,
        anchor="w",
        justify="left"
    )
    title_label.grid(row=row, column=0, padx=5, pady=2, sticky="w")

    # Dropdown zur Label-Zuweisung
    current_label = ctk.StringVar(value=window["label"] or "Kein Label")

    def set_label(selected_label=None, target_window=window, label_var=current_label):
        target_window["label"] = label_var.get()
        print(f'Label gesetzt: {target_window["title"]} → {target_window["label"]}')

    label_dropdown = ctk.CTkOptionMenu(
        master=root,
        variable=current_label,
        values=LABEL_OPTIONS,
        command=lambda _: set_label()
    )
    label_dropdown.grid(row=row, column=1, padx=5, pady=2, sticky="e")

def generate_ui(windows, root):
    """Erzeugt die gesamte Fenster-UI dynamisch."""
    for i, window in enumerate(windows):
        create_window_label_entry(root, window, row=i + 2)
