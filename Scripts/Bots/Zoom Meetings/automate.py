import subprocess
import time

import pyautogui
from pynput.keyboard import Controller, Key

# In this program all the text-fields, buttons, check-boxes are located using screenshots
# You can change the sleep-time as per the loading time of your pc


# Method to host a new meeting with video off and audio off
def zoom_automate(meeting_id, meeting_passcode):
    # Opens the zoom app
    # Change the path to the one where zoom app is stored
    subprocess.Popen("C:\\Users\\pc\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

    ## Opening time for App
    time.sleep(10)

    # To press the "Join a Meeting" button
    join_a_meeting = pyautogui.locateOnScreen("trainer\\join1.png")
    pyautogui.click(join_a_meeting)

    # Waiting time for next screen to load
    time.sleep(10)

    # To type the meeting_id
    pyautogui.typewrite(meeting_id)

    # To join the meeting with video turned off
    video_off = pyautogui.locateOnScreen("trainer\\videooff.png")
    pyautogui.click(video_off)

    # To press the join button to move to "Meeting Passcode" screen
    join = pyautogui.locateOnScreen("trainer\\join2.png")
    pyautogui.click(join)

    # Waiting time for next screen to load
    time.sleep(10)

    # To type the meeting_passcode
    pyautogui.typewrite(meeting_passcode)

    # Finally to join the meeting
    final_join = pyautogui.locateOnScreen("trainer\\finaljoin.png")
    pyautogui.click(final_join)

    # Waiting time for the host to admit the user in meeting
    time.sleep(30)

    # To join with the computer Audio
    join_audio = pyautogui.locateOnScreen("trainer\\computeraudio.png")
    pyautogui.click(join_audio)

    time.sleep(1)
    # To mute using shortcut key - "Alt+A"
    mute = Controller()
    mute.press(Key.alt_l)
    mute.press("a")
    mute.release("a")
    mute.release(Key.alt_l)


# Automating Zoom Meeting
if __name__ == "__main__":
    meeting_id = input("Meeting Id: ")
    meeting_passcode = input("Meeting Passcode: ")
    print("\nZoom App is starting.......")
    zoom_automate(meeting_id, meeting_passcode)
