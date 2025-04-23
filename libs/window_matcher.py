MATCH_RULES = [
    ["title", "path", "pos_x", "pos_y"],
    ["path", "process", "screen"],
    ["title", "process"]
]

def identify_window(stored, new_win):
    """
    Vergleicht ein gespeichertes Fenster mit einem neuen Fenster basierend auf konfigurierten Matching-Regeln.
    Gibt True zurück, wenn ein Match gefunden wurde, sonst False.
    """
    for rule in MATCH_RULES:
        if all(
            stored.get(key) == new_win.get(key)
            for key in rule
        ):
            return True
    return False

def find_matching_window(new_win, stored_windows):
    """
    Sucht in einer Liste gespeicherter Fenster nach einem passenden Fenster zum übergebenen neuen Fenster.
    Gibt das erste passende Fenster zurück, sonst None.
    """
    for stored in stored_windows:
        if identify_window(stored, new_win):
            return stored
    return None