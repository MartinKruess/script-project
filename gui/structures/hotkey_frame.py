import customtkinter as ctk

def create_frame_hotkeys(content_frame):
    # Hotkey Container
    frame_hotkeys_preview = ctk.CTkFrame(
        master=content_frame,
        width=550,
        height=810,
        fg_color="#1c1c1c",
        border_color="#990000",
        border_width=1
    )
    frame_hotkeys_preview.grid_propagate(False)
    frame_hotkeys_preview.grid_columnconfigure(0, minsize=130)
    frame_hotkeys_preview.grid_columnconfigure(1, minsize=100)
    frame_hotkeys_preview.grid_columnconfigure(2, minsize=120)
    frame_hotkeys_preview.grid_columnconfigure(3, minsize=60)
    frame_hotkeys_preview.grid_columnconfigure(4, minsize=60)
    
    return frame_hotkeys_preview