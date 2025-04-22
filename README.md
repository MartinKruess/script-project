<!-- # Workspace Controll Center – Fenster- und Workflow-Management mit Python

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

> ✉️ Bei Fragen oder Interesse gern melden – Feedback immer willkommen. -->

# 🧠 WorkspaceCC – Dein smarter Fenster-Organizer für den Alltag

Das **Workspace Control Center** ist mein persönliches Tool für mehr Übersicht, Fokus und Effizienz.  
Ob "Work", "Stream", "Chill" oder "Urlaub" – mit nur einem Klick bringe ich meine Fenster genau dorthin, wo ich sie brauche.

Ziel der App ist es, ein cleveres und gleichzeitig stylisches Dashboard zu bauen, mit dem man seine tägliche Fenster-Arbeitsumgebung organisieren und Hotkeys zentral verwalten kann – ohne sich täglich alles neu zusammensuchen zu müssen.

## 💬 Warum das Ganze?

Angefangen als kleines Python Script zu Übungszwecken, um ein wenig die Sprache zu lernen wurde aus dem kleinen Script nun ein komplexes Tool, dass mehr als meine ursprünglich geplanten Funktionen beinhaltet.

WorkspaceCC ist ein übersichtliches Tool, dass mir hilft meine Projekte einfacher zu handhaben.

## Vorläufiger Programmstart (zum Testen)

```python
.venv/Scripts/active

python script.py
```

---

## Was kann WorkspaceCC bisher?

### ✅ Organisation

- Willkommens Fenster mit Kurzeinleitung
- Übersichtliches Tutorial - Help Button (unten rechts)
- Feedback und Bugreport (Mach alles besser Knopp!)

### ✅ Benutzeroberfläche

- Übersichtliches UI mit Tabs (HOME / HOTKEYS / SCREEN MANAGER)
- Live-Statusanzeige des aktiven Modus
- Icons und ein schlichtes CustomTkinter-Design (Funktional)

### ✅ Modusverwaltung

- 4 Eigene Modis erstellen, benennen und löschen
- speichern von bis 10 Fenstern pro Modus (Save Monitor Config)
- Fenster können einem oder mehreren Modis zugeordnet sein
- Modus wechsel via Button oder Hotkey

### ✅ Fenster-Handling

- Aktive Fenster werden automatisch erkannt und im Screen Manager aufgelistet
- Position und Größe werden gespeichert
- solide automatische Wiedererkennung von Fenstern sowie Zuordnung zu entsprechender Konfiguration
- ScreenManager zeigt aktive Fenster an
- Monitor Daten update via Button bei Wechsel oder drehen eines Monitors

### ✅ Hotkeys

- 7 Mode Hotkeys (Moduswechsel)
- 4 Programm und Datei Hotkeys (`execute`)
- 🔒 Single-Lock-Funktion
- 🔄 Single-Reset-Funktion

---

## ✨ Geplante Features (next steps)

### 🔧 Verhalten & Automatisierung

- Fenster automatisch positionieren bei Moduswechsel
- Programme oder Dateien automatisch starten, wenn ein Modus aktiviert wird
- Zuweisung von Fenstern zu Modus über den ScreenManager (Dropdowns)
- 9 Frei konfigurierbare Hotkeys mit Typ-Auswahl: `execute` oder `link`
- Autostart

### 🎨 UI/UX

- Tooltips für Buttons und Icons
- Ausbau des Tutorials
- Redesign mit weiteren Tools
- Anzeige der im Modus verwalteten Fenster und Programme (HOME)

---

## 🛠 Aktueller Status

WorkspaceCC ist ein Projekt in aktiver Entwicklung – viele Kernfeatures laufen bereits stabil.  
Der Fokus liegt aktuell auf dem Ausbau der Hotkey-Verwaltung, dem automatisierten Fensterverhalten und allgemeinen UI-Verbesserungen.

---

## 🧰 Tech-Stack

### 🐍 Programmiersprache

- **Python 3**

### 🖼️ GUI

- TKinter (basic)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) – modernes UI mit Dark-Mode-Unterstützung

### 🪟 Fenstererkennung & Systemsteuerung

- `pygetwindow` – Fenster erkennen, verschieben, maximieren, minimieren
- `screeninfo` – Monitorposition und -größe abfragen
- `subprocess` – Programme/Dateien starten
- `os`, `platform` – Systemfunktionen & Autostart-Pfade
- `pywin32` oder `ctypes` – Low-Level-Zugriff auf Fenster (z. B. für Handles)

---

## Bekannte Bugs

- Screen Manager - Label Error (erwartet Str erält List)
- Hotkeys - Event fehler beim Anlegen und Locken von Hotkeys
- Navbar - Active Tab funktioniert nicht
