import json

def load_from_config(key = ""):
    with open("data/config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    if key != "":
        return config[key]
    else:
        return config

def save_in_config(data):
    with open("data/config.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)