import customtkinter as ctk
from libs.tooltip import CTkTooltip

# links
from libs.open_webside import open_webside

# GUI (Frames)
from gui.structures.modi_frame import create_frame_modis
from gui.structures.add_del_frame import create_frame_add_del

# Modules (refactoring)
from modules.modi_controller import modis, delete_mode, render_modis, delete_mode, add_mode

# save screen data
from libs.save_screen_config import get_monitor_data, save_window_data
from gui.render_save_screen_config import render_save_screen_config

def render_home_page(modis, parent, change_mode, config):
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


    # update screen data btn
    update_screen_data_btn = render_save_screen_config(parent, 200, 30, "Update Monitor Data", lambda: get_monitor_data(config))
    update_screen_data_btn.place(x=15, y=150)
    CTkTooltip(update_screen_data_btn, "Speichere Änderungen an den Screensettings (neuer Monitor, neue Ausrichtung/Einstellung)")

    # save screen config btn
    save_screen_config_btn = render_save_screen_config(parent, 200, 30, "Save Monitor Config", lambda: save_window_data(""))
    save_screen_config_btn.place(x=15, y=200)
    CTkTooltip(save_screen_config_btn, "Speichert alle aktuell geöffneten Fenster für den aktiven Modus")

    # feedback btn
    feedback_btn = render_save_screen_config(
        parent,
        400,
        30,
        "Der mach alles besser Knopp! / Make everything better button!",
       lambda: open_webside("https://github.com/MartinKruess/script-project/discussions"))
    feedback_btn.place(x=92, y=785)
    CTkTooltip(feedback_btn, "Stoße Diskussionen an und gib Feedback auf GitHub")

    # help btn
    help_btn = render_save_screen_config(
        parent,
        30,
        30,
        "?",
       lambda: open_webside("https://github.com/MartinKruess/script-project/blob/main/tutorial.md"))
    help_btn.place(x=540, y=785)
    CTkTooltip(help_btn, "Öffnet das Tutorial auf GitHub")