import win32process
import psutil

def get_process_info(hwnd):
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        proc = psutil.Process(pid)
        path = proc.exe()
        name = proc.name()
        return name, path
    except Exception as e:
        print(f"Fehler beim Lesen des Prozesses für hwnd {hwnd}: {e}")
        return None, None
