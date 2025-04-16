import customtkinter as ctk

# GUI (Frames)
from gui.structures.modi_frame import create_frame_modis
from gui.structures.add_del_frame import create_frame_add_del

# Modules (refactoring)
from modules.modi_controller import modis, delete_mode, render_modis, delete_mode, add_mode

def render_home_page(modis, parent, change_mode):
    frame_modis = create_frame_modis(parent)
    frame_modis.place(x=15, y=10)

    frame_add_del = create_frame_add_del(parent)
    frame_add_del.place(x=310, y=10)

    # load Modi_btns in frame
    render_modis(modis, frame_modis, change_mode)

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