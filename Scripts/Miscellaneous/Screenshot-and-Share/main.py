import os
import platform
import time

import pyautogui
import pyperclip
import requests
from pynput import keyboard

if not os.path.exists("captures"):
    os.makedirs("captures")
path = os.getcwd()

url = "https://api.anonfiles.com/upload"


if "Windows" in platform.system():
    COMBINATIONS = [{keyboard.Key.print_screen}]
else:
    COMBINATIONS = [
        {keyboard.Key.print_screen, keyboard.Key.ctrl_l},
        {keyboard.Key.print_screen, keyboard.Key.ctrl_r},
    ]

current = set()


def execute():
    fname = time.strftime(
        os.path.join(path, "captures", "%Y%m%d%H%M%S") + ".png"
    )
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(fname)
    print("Uploading..")
    pyperclip.copy("Uploading..")
    with open(os.path.join(path, "captures", fname), "rb") as f:
        resp = requests.post(url, files={"file": f})
    if resp.status_code == 200:
        if resp.json()["status"] is True:
            print(resp.json()["data"]["file"]["url"]["short"])
            pyperclip.copy(resp.json()["data"]["file"]["url"]["short"])
        else:
            print("Upload failed.")
            pyperclip.copy("Upload failed.")
    else:
        print("Upload failed.Maybe no internet conncetion")
        pyperclip.copy("Upload failed.Maybe no internet conncetion")


def on_press(key):
    if any((key in COMBO for COMBO in COMBINATIONS)):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()


def on_release(key):
    if any((key in COMBO for COMBO in COMBINATIONS)):
        current.remove(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


# chaha0s
