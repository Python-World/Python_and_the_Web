import pyautogui, time
time.sleep(5)
f = open("Text.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("Enter")
