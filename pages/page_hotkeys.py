# GUI (Optik)
from libs.hotkey_manager import generate_hotkeys
from gui.hotkey_ui import render_hotkeys, render_hotkeys_table

#GUI (Frames)
from gui.structures.hotkey_frame import create_frame_hotkeys

def render_hotkeys_page(modis, parent, root):
    frame_hotkeys_preview = create_frame_hotkeys(parent)
    frame_hotkeys_preview.place(x=15, y=10)

    # Render Hotkeys
    render_hotkeys_table(frame_hotkeys_preview, modis, root)