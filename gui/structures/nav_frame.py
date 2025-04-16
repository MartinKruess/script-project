import customtkinter as ctk

def create_frame_nav(root):
    frame_nav = ctk.CTkFrame(
        master=root,
        width= 450,
        height=40,
        fg_color="#282c2c"
    )
    return frame_nav