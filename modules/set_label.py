def label_window(windows):
    for i, win in enumerate(windows):
        print(f"[{i}] {win['title']}  →  Aktuell: {win['label']}")

    try:
        label = input("Label: ")
        id = int(input("Fenster ID: "))

        if len(label) >= 1:
            windows[id]["label"] = label
            print(f'✅ Label gesetzt: "{windows[id]["title"]}" → "{label}"')
        else:
            print("❌ Kein Label eingegeben – abgebrochen.")
    except:
        print("❌ Ungültige Eingabe – bitte nochmal versuchen.")