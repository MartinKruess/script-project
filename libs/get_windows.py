import pygetwindow as getWindow
from libs.rules import not_allowed_titles, window_shorts
from libs.simplify_title import simplify_title
from libs.handle_config import load_from_config
from libs.get_process import get_process_info

def calculate_screen_for_window(x, y, w_width, w_height, screens):
    center_x = x + w_width // 2
    center_y = y + w_height // 2

    for screen in screens:
        if (
            screen["x"] <= center_x < screen["x"] + screen["width"] and
            screen["y"] <= center_y < screen["y"] + screen["height"]
        ):
            return screen["index"]
    return 0

def get_windows():
    activeWindows = getWindow.getWindowsWithTitle("")
    windows = []

    config = load_from_config()
    screens = config.get("screens", [])

    for window in activeWindows:
        if not window.title.strip():
            continue

        if not window.title in not_allowed_titles:
            short_title = simplify_title(window.title, window_shorts)

            if "Visual Studio Code" in short_title:
                splitted_title = short_title.split(" - ")
                short_title = splitted_title[1] + " - " + "Visual Studio Code"

            pos_x = window.left
            pos_y = window.top

            screen_index = calculate_screen_for_window(pos_x, pos_y, window.width, window.height, screens)
            process_name, exe_path = get_process_info(window._hWnd)

            state = {
                "id": window._hWnd,
                "title": short_title,
                "screen": screen_index,
                "border": None,
                "is_active": window == getWindow.getActiveWindow(),
                "is_minimized": (pos_x == -32000 and pos_y == -32000),
                "pos_x": pos_x,
                "pos_y": pos_y,
                "width": window.width,
                "height": window.height,
                "labels": [],
                "process": process_name or "",
                "path": exe_path or ""
            }
            windows.append(state)

    return windows
