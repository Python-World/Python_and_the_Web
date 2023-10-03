import time

import pyautogui


def main():
    time.sleep(5)
    file = open("Text.txt", "r")
    for word in file:
        pyautogui.typewrite(word)
        pyautogui.press("Enter")


if __name__ == "__main__":
    main()
