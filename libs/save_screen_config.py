from screeninfo import get_monitors
from libs.handle_config import load_from_config, save_in_config
from libs.get_windows import get_windows

config = load_from_config()

def get_monitor_data():
    data = []

    for i, m in enumerate(get_monitors()):
        monitor = {
            "index": i,
            "x": m.x,
            "y": m.y,
            "width": m.width,
            "height": m.height,
        }

        # Optional Details
        if hasattr(m, "width_mm"):
            monitor["width_mm"] = m.width_mm
        if hasattr(m, "height_mm"):
            monitor["height_mm"] = m.height_mm
        if hasattr(m, "name"):
            monitor["name"] = m.name
        if hasattr(m, "is_primary"):
            monitor["is_primary"] = m.is_primary

        data.append(monitor)
    
    config["screens"] = data
    save_in_config(config)
    print("New Screen Data are Saved!")

def save_screen_config():
    monitors = get_monitors()
    print(monitors[0])
    print("--------")
    print(monitors[0])

def save_window_data():
    config = load_from_config()
    modis = config["modes"]
    current_mode_id = config["user_settings"]["last_mode"]
    current_label = modis[current_mode_id]["title"]
    config["window_positions"] = get_windows(current_label)
    save_in_config(config)
