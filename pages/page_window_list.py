# GUI (Frames)
from gui.structures.window_list_frame import create_window_frame

# generate main data (not stuctured!)
from gui.generate_ui import generate_ui

def render_window_list_page(windows, parent):
    frame_window_list = create_window_frame(parent)
    frame_window_list.place(x=15, y=10)

    generate_ui(windows, frame_window_list  )