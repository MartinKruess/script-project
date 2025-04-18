import customtkinter as ctk

def create_hotkey_frame(content_frame):
    # Hotkey Container
    hotkeys_frame = ctk.CTkFrame(
        master=content_frame,
        width=550,
        height=810,
        fg_color="#1c1c1c",
        border_color="#990000",
        border_width=1
    )
    hotkeys_frame.grid_propagate(False)
    hotkeys_frame.grid_columnconfigure(0, minsize=130)
    hotkeys_frame.grid_columnconfigure(1, minsize=100)
    hotkeys_frame.grid_columnconfigure(2, minsize=120)
    hotkeys_frame.grid_columnconfigure(3, minsize=60)
    hotkeys_frame.grid_columnconfigure(4, minsize=60)
    
    return hotkeys_frame