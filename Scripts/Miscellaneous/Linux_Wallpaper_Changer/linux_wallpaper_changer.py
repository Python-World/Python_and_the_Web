from tkinter import Tk, Label, Button  # from Tkinter import Tk for Python 2.x
from tkinter.filedialog import askopenfilename
import subprocess
from sys import platform
from pathlib import Path

# Permitted Extensions
ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png"]

# Terminal command to change the background image (this may be different for different Linux distributions)
LINUX_TERMINAL_COMMAND = [
    "gsettings",
    "set",
    "org.gnome.desktop.background",
    "picture-uri",
]
filename = None


def get_file():
    global filename
    filename = askopenfilename(
        title="Choose an image",
        filetypes=[("Image files", ("*.jpg", "*.jpeg", "*.png"))],
    )

    # Check for extension and if it is not allowed set the file to None
    if not filename.split(".")[-1] in ALLOWED_EXTENSIONS:
        print("Please select a JPEG/PNG file")
        filename = None

    print("Selected Image: ", filename)


def set_wallpaper():
    # Return if an image file is not selected
    if filename is None:
        return
    # Identify the user's platform (Windows, Linux or Mac OS)
    user_os = platform.lower()

    if user_os in ["linux", "linux2"]:
        # Convert the image path into a file uri
        file_uri = Path(filename).as_uri()

        # Execute the terminal command to change the wallpaper using the image's file uri
        process = subprocess.Popen(
            LINUX_TERMINAL_COMMAND + [file_uri], stdout=subprocess.PIPE
        )
        stdout = process.communicate()
        process.terminate()

        # Check for any errors and print them
        if stdout[1]:
            print(stdout)
        else:
            print("Wallpaper Set Successfully!")
    else:
        print("Your operating system is currently not supported")


# Tkinter GUI
window = Tk()
window.title("Python World")
title = Label(text="Linux Wallpaper Changer", height=2, width=40).pack()

# Buttons to get file path and set the wallpaper
file_chooser = Button(
    text="Choose an image (JPEG or PNG)", height=1, width=30, command=get_file
).pack(pady=5)
submit_button = Button(
    text="Set as wallpaper", height=2, width=30, command=set_wallpaper
).pack(pady=5)
window.mainloop()
