import customtkinter as ctk

def render_save_screen_config(content_frame, width, height, text, function):
    save_screen_config_btn = ctk.CTkButton(
        master=content_frame,
        width=width,
        height=height,
        font=("Teko", 20),
        text= text,
        text_color= "#ffffff",
        corner_radius=10,
        fg_color="#3366ff",
        command= lambda:  function()
    )
    return save_screen_config_btn