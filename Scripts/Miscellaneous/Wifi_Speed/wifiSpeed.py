# Python script that provides the download and upload speed of your Wifi.

# Python module for testing internet bandwidth
from sys import exit

import speedtest

# Creating a instance
try:
    s = speedtest.Speedtest()
except speedtest.ConfigRetrievalError:
    print(
        "Sorry, looks like you are not connected to any network!\nPlease make sure you are connected to the internet."
    )
    exit()

# Menu
print("Select a valid option from below:\n")
print("1. Download")
print("2. Upload")
print("3. Exit\n")

# Run until valid option is selected
while True:
    # Getting options from user
    option = int(input("Enter Option: "))

    if option == 1:
        download = s.download() / 1000
        print("Download Speed : %.2f kb/s\n" % download)
    elif option == 2:
        upload = s.upload() / 1000
        print("Upload Speed : %.2f kb/s\n" % upload)
    elif option == 3:
        print("\nExiting Successfully...")
        break
    else:
        print("INVALID OPTION SELECTED! Re-", end="")
