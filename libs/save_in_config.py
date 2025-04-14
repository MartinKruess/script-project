import json

def save_in_config(data):
    with open("data/config.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)