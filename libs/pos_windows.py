import pygetwindow as gw

def positionate_windows(windows):
    for window in windows:
        try:
            real_window = gw.getWindowsWithTitle(window["title"])[0]
            real_window.moveTo(window["pos_x"], window["pos_y"])
            real_window.resizeTo(window["width"], window["height"])
        except IndexError:
            print(f"⚠️ Fenster nicht gefunden: {window['title']}")

def find_window(win, mode):
    if mode in win["labels"]:
        return win