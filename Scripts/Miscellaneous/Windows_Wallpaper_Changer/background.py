from tkinter import Tk  # from Tkinter import Tk for Python 2.x
from tkinter.filedialog import askopenfilename
import ctypes

Tk().withdraw()
filename = askopenfilename()
SPI_SETDESKWALLPAPER = 20

# Permitted Extensions
allowed_extensions = ["jpg", "png"]

# Check for extension
if filename.split(".")[-1] in allowed_extensions:
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, filename, 0
    )
    print("Wallpaper Set Successfully!")
else:
    print("Please select a JPEG/PNG file")
