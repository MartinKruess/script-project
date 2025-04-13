# Workspace Controll Center – Fenster- und Workflow-Management mit Python

## 🔍 Projektübersicht

**WorkspaceCC** ist ein Python-Tool zur Verwaltung von Fenstern, Hotkeys und Programm-Workflows unter Windows.  
Es ermöglicht das schnelle Umschalten zwischen individuell definierten Arbeitsmodi, die Fenster, Programme und Layouts automatisch anpassen – effizient, flexibel und visuell klar strukturiert.

Das Besondere: Dieses Projekt entsteht **komplett im Rahmen meines Python-Lernprozesses**. Ziel ist es, die Sprache nicht nur zu verstehen, sondern durch ein praktisches, alltagsnahes Tool zu meistern.

---

## 💡 Was kann das Tool aktuell?

- 🔍 **Fenster-Erkennung & -Analyse** über `pygetwindow`
- 🪟 Eigene Datenstruktur für Fenster mit Titel, Label, Status & Position
- 🎯 **Fenster-Labeling** mit Dropdown-Auswahl (z. B. Arbeit, Freizeit, Multimedia)
- 🧠 **Modusverwaltung** über GUI (Free, Work, Stream etc.)
- 🔁 **Moduswechsel per Hotkey** (`alt+^`, `ctrl+F1` bis `ctrl+F6`)
- 🧩 Modulare Architektur mit `modules`, `libs` und `GUI`-Verzeichnissen
- 🎛️ Live aktualisierbare Modus-Buttons mit visuellem Status
- Benutzerdefinierte Hotkeys für Programmstart oder URL-Öffnung
- 📋 **Tabellenartige Hotkey-Übersicht** mit Labeln und editierbarem System
- 🧼 Projektstruktur, .gitignore und Konfigurationslogik sind sauber isoliert

---

## 🚀 In Planung

- 💾 Speicherung und Laden aller Konfigurationen (Fenster + Hotkeys)
- 🧠 Automatisches Positionieren & Öffnen von Fenstern je nach Modus
- ⚙️ Automatisches Starten von Programmen pro Modus
- 🔑 Benutzerdefinierte Hotkeys für alles Mögliche (Links, Scripts, Tools)
- 👁️ Dashboard-Overlay für schnelle Übersicht (inkl. Modus, Fensterstatus etc.)
- 🔄 Scrollbare Tabellen und interaktive UI-Elemente
- 🧪 Optionale Event-Erkennung für intelligente Aktionen (z. B. Tab-Wechsel durch Mausbewegung/position)
- 🧼 Trennung von GUI & Logik, um das Projekt später leicht erweitern zu können

---

## 📈 Warum das Projekt besonders ist

Ich lernte letzte Woche die Python Basics und wollt nun ein Projekt umsetzen, dass die Basics und einen Schritt mehr verwendet. Zugegeben, der Schritt, war doch etwas größer, als gedacht, aber Ziel ist es, keine Tutorials blind nachzubauen, sondern **echte Probleme** zu lösen, dabei zu lernen, zu scheitern und die Sprache von Grund auf zu verstehen.

Dabei achte ich besonders auf:

- sauberen Code & Struktur
- sinnvolle Modularisierung
- langfristige Wartbarkeit
- Fokus auf **praktische Anwendung & Usability**
- Der Aufbau einer Software, die mir persönlich im Codingalltag helfen kann, aber auch für andere eine Untertsützung sein kann.

---

## 📦 Projektstruktur (Auszug)

```
script-project/
├── script.py                  # Einstiegspunkt
├── modules/                   # Funktionsmodule (UI, Logik)
│   ├── simplify_title.py
│   ├── generate_modi_btn.py
│   └── modi_controller.py
├── libs/                      # Hilfsklassen & Kontrollsysteme
│   └── hotkey_manager.py
│   └── rules.py
├── gui/                       # GUI-Layout & Frames
│   └── structures/            # GUI-Frames
│       ├── hotkeys_frame.py
│       └── modi_frame.py
│       └── add_del_frame.py
│   └── generate_mod_btn.py
│   └── generate_dropdown_ui.py
│   └── hotkey_ui.py
├── .gitignore
├── .venv
└── README.md (du liest ihn gerade 😉)
```

---

## 🔧 Verwendete Technologien

- 💻 Python 3.13
- 🧰 [`pygetwindow`](https://pypi.org/project/PyGetWindow/)
- 🔢 [`keyboard`](https://pypi.org/project/keyboard/)
- 🎨 [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter)
- 📦 VENV & Paketverwaltung mit `pip`
- 🔧 Manuelles Event- & State-Management

## 🛠️ Dev Tools

- [Pygments](https://pygments.org/)
- [Rich](https://github.com/Textualize/rich)

---

## 🤝 Noch viel zu lernen...

...aber ich bin mittendrin.  
Und das hier ist kein Spielzeug, sondern ein echtes Tool – gebaut mit Leidenschaft fürs Lernen und dem Wunsch, Python **wirklich** zu verstehen.

---

**Stay tuned!**

> ✉️ Bei Fragen oder Interesse gern melden – Feedback immer willkommen.
