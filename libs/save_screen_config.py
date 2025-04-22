from screeninfo import get_monitors
from libs.handle_config import load_from_config, save_in_config
from libs.get_windows import get_windows
from libs.window_matcher import identify_window, find_matching_window

def get_monitor_data(config):
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




def save_window_data():
    config = load_from_config()
    modis = config["modes"]
    current_mode_id = config["user_settings"]["last_mode"]
    current_label = modis[current_mode_id]["title"]
    
    if current_label == "FREE":
        return

    current_windows = get_windows(label=None)
    stored_windows = config.get("labeled_windows", [])

    for win in current_windows:
        match = find_matching_window(win, stored_windows)

        if match:
            if match["is_minimized"]:
                continue
            # Label ergänzen, falls noch nicht enthalten
            if current_label not in match.get("labels", []):
                match["labels"].append(current_label)
        else:
            if win["is_minimized"] or win["title"] == "WorkspaceCC - Workspace Control Center":
                continue
            # Neues Fensterobjekt mit aktuellem Label anlegen
            win["labels"] = [current_label]
            stored_windows.append(win)

    config["labeled_windows"] = stored_windows
    save_in_config(config)
