import pygetwindow as getWindow
from libs.rules import not_allowed_titles, window_shorts
from libs.simplify_title import simplify_title

def get_windows(label):
    activeWindows = getWindow.getWindowsWithTitle("")
    windows = []

    for window in activeWindows:
        if not window.title.strip():
            continue
        
        if not window.title in not_allowed_titles:
            short_title = simplify_title(window.title, window_shorts)

            state = {
                "id": window._hWnd,
                "title": short_title,
                "label": None or label,
                "screen": 1,
                "border": None,
                "is_active": window == getWindow.getActiveWindow(),
                "is_minimized": (window.left == -32000 and window.top == -32000),
                "pos_x": window.left,
                "pos_y": window.top,
                "width": window.width,
                "height": window.height,
            }
            windows.append(state)
    
    return windows