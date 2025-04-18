import customtkinter as ctk

def create_window_frame(content_frame):
    # Hotkey Container
    window_list_frame = ctk.CTkFrame(
        master=content_frame,
        width=550,
        height=810,
        fg_color="#1c1c1c",
        border_color="#990000",
        border_width=1
    )
    window_list_frame.grid_propagate(False)
    window_list_frame.grid_columnconfigure(0, minsize=400)
    window_list_frame.grid_columnconfigure(1, minsize=100)
    
    return window_list_frame