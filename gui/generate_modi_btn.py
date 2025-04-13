def generate_modi_btn(mode_title, mode_bg, mode_txt, i, root, change_mode):
    new_btn = {
        "master": root,
        "text": mode_title,
        "font":("Teko", 22),
        "text_color": mode_txt or "#ffffff",
        "height": 25,
        "width": 75,
        "corner_radius" :10,
        "bg_color": "#242639",
        "fg_color": mode_bg,
        "command": lambda:  change_mode(i),
    }
    return new_btn