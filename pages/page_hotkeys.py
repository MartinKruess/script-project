# GUI (Optik)
from libs.hotkey_manager import generate_hotkeys
from gui.hotkey_ui import render_hotkeys, render_hotkeys_table

#GUI (Frames)
from gui.structures.hotkey_frame import create_hotkey_frame

def render_hotkeys_page(modis, parent, root):
    hotkeys_frame = create_hotkey_frame(parent)
    hotkeys_frame.place(x=15, y=10)

    # Render Hotkeys
    render_hotkeys_table(hotkeys_frame, modis, root)