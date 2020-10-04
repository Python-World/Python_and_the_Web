import pyautogui
import time

time.sleep(5)
file = open("Text.txt", "r")
for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("Enter")
