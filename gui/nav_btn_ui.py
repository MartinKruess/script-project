import customtkinter as ctk
from gui.generate_modi_btn import generate_modi_btn
from gui.hotkey_ui import render_hotkeys


def generate_nav_elements(nav_frame, switch_page):
    nav_elements = [
        {
            "title": "HOME",
            "bg_color":"#142214",
            "color":"#999",
            "active_color": "#4fffda",
            "isActive": True,
            "target": "home"
        },
        {
            "title": "HOTKEYS",
            "bg_color":"#142214",
            "color":"#999",
            "active_color": "#4fffda",
            "isActive": False,
            "target": "hotkeys"
        },
                {
            "title": "Screen Manager",
            "bg_color":"#142214",
            "color":"#999",
            "active_color": "#4fffda",
            "isActive": False,
            "target": "screenmanager"
        }
    ]

    color = ""
    for i, elem in enumerate(nav_elements):
        if elem["isActive"]:
            color = elem["active_color"]
        else:
            color = elem["color"]

        nav_label = ctk.CTkLabel(
            master=nav_frame,
            width=110 + (38*i),
            height=20,
            text=f""".
{elem["title"]}""",
            text_color=color,
            fg_color=elem["bg_color"],
            font=("Teko", 22, "bold"),
            anchor="s",
        )
    
        nav_label.pack(padx=4, pady=4, side="left")
        nav_label.bind("<Button-1>", lambda event, name=elem["target"]: switch_page(name))
    nav_frame.pack_propagate(False)
    