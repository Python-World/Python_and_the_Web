import os
import sys
import tkinter.messagebox
from tkinter import *

tk = Tk()
tk.title("Tic Tac Toe")
tk.resizable(False, False)

bclick = True
count = 0


# This function prevents the user from clicking the same button again.
def button(buttons):
    global bclick, count
    if buttons["text"] == "" and bclick is True:
        buttons["text"] = "X"
        bclick = False
        winner()
        count += 1

    elif buttons["text"] == "" and bclick is False:
        buttons["text"] = "O"
        bclick = True
        winner()
        count += 1
    else:
        tkinter.messagebox.showinfo("Tic Tac Toe", "Button already Clicked!")


def playagain():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def winner():
    if (
        button1["text"] == "X"
        and button2["text"] == "X"
        and button3["text"] == "X"
        or button4["text"] == "X"
        and button5["text"] == "X"
        and button6["text"] == "X"
        or button7["text"] == "X"
        and button8["text"] == "X"
        and button9["text"] == "X"
        or button1["text"] == "X"
        and button5["text"] == "X"
        and button9["text"] == "X"
        or button3["text"] == "X"
        and button5["text"] == "X"
        and button7["text"] == "X"
        or button1["text"] == "X"
        and button4["text"] == "X"
        and button7["text"] == "X"
        or button2["text"] == "X"
        and button5["text"] == "X"
        and button8["text"] == "X"
        or button3["text"] == "X"
        and button6["text"] == "X"
        and button9["text"] == "X"
    ):
        msgbox = tkinter.messagebox.askquestion(
            "Tic Tac Toe", "X wins! \n\nDo you want to play again?"
        )
        if msgbox == "yes":
            playagain()
        else:
            tk.destroy()

    elif (
        button1["text"] == "O"
        and button2["text"] == "O"
        and button3["text"] == "O"
        or button4["text"] == "O"
        and button5["text"] == "O"
        and button6["text"] == "O"
        or button7["text"] == "O"
        and button8["text"] == "O"
        and button9["text"] == "O"
        or button1["text"] == "O"
        and button5["text"] == "O"
        and button9["text"] == "O"
        or button3["text"] == "O"
        and button5["text"] == "O"
        and button7["text"] == "O"
        or button1["text"] == "O"
        and button4["text"] == "O"
        and button7["text"] == "O"
        or button2["text"] == "O"
        and button5["text"] == "O"
        and button8["text"] == "O"
        or button3["text"] == "O"
        and button6["text"] == "O"
        and button9["text"] == "O"
    ):
        msgbox = tkinter.messagebox.askquestion(
            "Tic Tac Toe", "O wins! \n\nDo you want to play again?"
        )
        if msgbox == "yes":
            playagain()
        else:
            tk.destroy()

    elif count == 8:
        msgbox = tkinter.messagebox.askquestion(
            "Tic Tac Toe", "It's a tie! \n\nDo you want to play again?"
        )
        if msgbox == "yes":
            playagain()
        else:
            tk.destroy()


# Game Board

restart = Button(
    tk,
    text="RESTART",
    font="Arial",
    bg="white",
    fg="black",
    height=3,
    width=8,
    command=playagain,
)
restart.grid(row=2, column=0)

quit = Button(
    tk,
    text="EXIT",
    font="Arial",
    bg="white",
    fg="black",
    height=3,
    width=8,
    command=tk.destroy,
)
quit.grid(row=2, column=2)

button1 = Button(
    tk,
    text="",
    font="Arial",
    bg="Black",
    fg="white",
    height=4,
    width=8,
    command=lambda: button(button1),
)
button1.grid(row=3, column=0)

button2 = Button(
    tk,
    text="",
    font="Arial",
    bg="Black",
    fg="white",
    height=4,
    width=8,
    command=lambda: button(button2),
)
button2.grid(row=3, column=1)

button3 = Button(
    tk,
    text="",
    font="Arial",
    bg="Black",
    fg="white",
    height=4,
    width=8,
    command=lambda: button(button3),
)
button3.grid(row=3, column=2)

button4 = Button(
    tk,
    text="",
    font="Arial",
    bg="Black",
    fg="white",
    height=4,
    width=8,
    command=lambda: button(button4),
)
button4.grid(row=4, column=0)

button5 = Button(
    tk,
    text="",
    font="Arial",
    bg="Black",
    fg="white",
    height=4,
    width=8,
    command=lambda: button(button5),
)
button5.grid(row=4, column=1)

button6 = Button(
    tk,
    text="",
    font="Arial",
    bg="Black",
    fg="white",
    height=4,
    width=8,
    command=lambda: button(button6),
)
button6.grid(row=4, column=2)

button7 = Button(
    tk,
    text="",
    font="Arial",
    bg="Black",
    fg="white",
    height=4,
    width=8,
    command=lambda: button(button7),
)
button7.grid(row=5, column=0)

button8 = Button(
    tk,
    text="",
    font="Arial",
    bg="Black",
    fg="white",
    height=4,
    width=8,
    command=lambda: button(button8),
)
button8.grid(row=5, column=1)

button9 = Button(
    tk,
    text="",
    font="Arial",
    bg="Black",
    fg="white",
    height=4,
    width=8,
    command=lambda: button(button9),
)
button9.grid(row=5, column=2)

tk.mainloop()
