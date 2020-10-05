## Screenshot-and-Share

## What does the script do?
1. Takes screenshot with your custom defined shortcut
2. Uploads the capture to anonfiles
3. Copies the link to the clipboard


    Uses pyAutoGUI to capture screen, requests to upload on anonfiles and pyperclip to copy the link to clipboard.
    pynput to detect triggers, which on Windows is PrtSc and on Linux is Ctrl + PrtSc

## Installation

    pip install -r requirements.txt
    python main.py
