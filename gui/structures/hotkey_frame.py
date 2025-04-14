import customtkinter as ctk

def create_frame_hotkeys(root):
# Container
    frame_hotkeys = ctk.CTkFrame(
        master=root,
        width= 555,
        height=600
    )

    # Left -> show hotkey
    frame_hotkeys_preview = ctk.CTkFrame(
        master=frame_hotkeys,
        # width= 300,
        width=520,
        height=560,
        fg_color="#1c1c1c"
    )
    frame_hotkeys_preview.place(x=16, y=20)
    frame_hotkeys_preview.grid_propagate(False)
    frame_hotkeys_preview.grid_columnconfigure(0, minsize=160)
    frame_hotkeys_preview.grid_columnconfigure(1, minsize=140)
    frame_hotkeys_preview.grid_columnconfigure(2, minsize=80)

    # right -> set hotkey command
    # frame_hotkeys_setter = ctk.CTkFrame(
    #     master=frame_hotkeys,
    #     width= 200,
    #     height=500,
    #     fg_color="#1c1c1c"
    # )
    # frame_hotkeys_setter.place(x=337, y=20)
    
    return {
        "container": frame_hotkeys,
        "preview": frame_hotkeys_preview,
        # "setter": frame_hotkeys_setter
    }