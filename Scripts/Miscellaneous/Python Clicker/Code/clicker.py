import time

import pyautogui


def main():
    # Set a Sleep Time
    time.sleep(5)
    # Set a for Loop
    for _ in range(200):
        pyautogui.leftClick(467, 517)


if __name__ == "__main__":
    main()
