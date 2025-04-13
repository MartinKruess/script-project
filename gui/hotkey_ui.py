import customtkinter as ctk
from libs.hotkey_manager import hotkeys

def render_hotkeys(frame_hotkeys_preview):

    for i, key in enumerate(hotkeys):
        ctk.CTkLabel(
            master=frame_hotkeys_preview,
            text=f"{key["hotkey"]} - {key["type"]}",
            font=("Teko", 22),
        ).place(x=50, y=30 * i+ 20)


def render_hotkeys_table(frame):
    headers = ["Hotkey", "Typ", "Ziel", "Aktion"]
    for col, title in enumerate(headers):
        label = ctk.CTkLabel(frame, text=title.upper(), font=("Arial", 12, "bold"))
        label.grid(row=0, column=col, padx=8, pady=(0, 8))

    for i, hk in enumerate(hotkeys, start=1):
        ctk.CTkLabel(frame, text=hk["hotkey"]).grid(row=i, column=0, padx=5, pady=2)
        ctk.CTkLabel(frame, text=hk["type"]).grid(row=i, column=1, padx=5, pady=2)

        # Ziel: Pfad oder URL
        if hk["type"] == "execute":
            target = hk.get("path", "-")
        elif hk["type"] == "link":
            target = hk.get("url", "-")
        else:
            target = f'Modus {hk.get("mode_index", "→")}'
        ctk.CTkLabel(frame, text=target).grid(row=i, column=2, padx=5, pady=2)

        # Optional Button
        ctk.CTkButton(frame, text="✏️").grid(row=i, column=3, padx=5)