import subprocess
import time
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command)

    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            print(f"🔁 Änderung erkannt: {event.src_path}")
            self.process.kill()
            self.process = subprocess.Popen(self.command)

if __name__ == "__main__":
    path = os.path.abspath(".")
    command = [sys.executable, "script.py"]
    event_handler = ReloadHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print("👀 Beobachte Änderungen in .py-Dateien. Zum Beenden: Strg + C")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
