import customtkinter as ctk
import json

LABEL_OPTIONS = ["FREE", "WORK", "STREAM", "Video", "Audio", "Image", "Streamer"]

def create_window_label_entry(frame, window, row):
    """Erzeugt Label und Dropdown für ein Fenster."""
    # Titelanzeige
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

    # Dropdown zur Label-Zuweisung
    current_label = ctk.StringVar(value=window["label"] or "Kein Label")

    def set_label(selected_label=None, target_window=window, label_var=current_label):
        target_window["label"] = label_var.get()
        print(f'Label gesetzt: {target_window["title"]} → {target_window["label"]}')

    label_dropdown = ctk.CTkOptionMenu(
        master=frame,
        variable=current_label,
        values=LABEL_OPTIONS,
        command=lambda _: set_label()
    )
    label_dropdown.grid(row=row, column=1, padx=5, pady=2, sticky="e")

def generate_ui(windows, root):
    """Erzeugt die gesamte Fenster-UI dynamisch."""
    for i, window in enumerate(windows):
        create_window_label_entry(root, window, row=i + 2)
