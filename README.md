# 🧠 WorkspaceCC – Dein smarter Fenster-Organizer für den Alltag

**Workspace Control Center** ist ein Python-Tool zur Verwaltung von Fenstern, Hotkeys und Programm-Workflows unter Windows.
Es ermöglicht das schnelle Umschalten zwischen individuell definierten Arbeitsmodi, die Fenster, Programme und Layouts automatisch anpassen – effizient, flexibel und visuell klar strukturiert.

## 💬 Warum das Ganze?

Angefangen als kleines Python Script zu Übungszwecken, um ein wenig die Sprache zu lernen wurde aus dem kleinen Script nun ein komplexes Tool, dass mehr als meine ursprünglich geplanten Funktionen beinhaltet.

Ziel ist es, die Sprache nicht nur zu verstehen, sondern durch ein praktisches, alltagsnahes Tool zu meistern.

WorkspaceCC ist ein übersichtliches Tool, dass mir hilft meine Projekte einfacher zu handhaben.

## Vorläufiger Programmstart (zum Testen)

```python
# init virtual area
python -m venv .venv

# start virtual area
.venv/Scripts/active

# Install Dependencies
pip install -r requirements.txt

# app start
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
- 🎨[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) – modernes UI mit Dark-Mode-Unterstützung

### 🪟 Fenstererkennung & Systemsteuerung

- 📦 VENV & Paketverwaltung mit `pip`
- 🔧 Manuelles Event- & State-Management
- 🧰 [`pygetwindow`](https://pypi.org/project/PyGetWindow/) – Fenster erkennen, verschieben, maximieren, minimieren
- 🔢 [`keyboard`](https://pypi.org/project/keyboard/)
- `screeninfo` – Monitorposition und -größe abfragen
- `subprocess` – Programme/Dateien starten
- `os`, `platform` – Systemfunktionen & Autostart-Pfade
- `pywin32` oder `ctypes` – Low-Level-Zugriff auf Fenster (z. B. für Handles)

## 🛠️ Dev Tools

- [Pygments](https://pygments.org/)
- [Rich](https://github.com/Textualize/rich)

---

## Bekannte Bugs

- Screen Manager - Label Error (erwartet Str erält List)
- Hotkeys - Event fehler beim Anlegen und Locken von Hotkeys
- Navbar - Active Tab funktioniert nicht
