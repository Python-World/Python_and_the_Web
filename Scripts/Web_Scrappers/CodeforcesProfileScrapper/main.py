import tkinter as tk
from datetime import datetime
from tkinter import Label, ttk
from urllib.request import urlopen

import constants as c
from PIL import Image, ImageTk
from scrapper import UserNotFoundError, user_info


class Bunch(dict):
    def __init__(self, adict):
        dict.__init__(self)
        self.update(adict)
        self.__dict__.update(adict)


class Profile:
    def __init__(self, master, handle):
        self.master = master
        self.master.title(f"Codeforces Profiler - {handle}")

        try:
            self.user = Bunch(
                user_info(handle)[0]
            )  # bcz Namespace syntax is easy
            self.init()
        except UserNotFoundError:
            w = ttk.Label(self.master, text=f"User {handle} does not exists!")
            w.grid()
            b = ttk.Button(self.master, text="OK", command=self.master.destroy)
            b.grid()

    def init(self):
        PROFILE_PIC = ImageTk.PhotoImage(
            Image.open(urlopen(f"https:{self.user.titlePhoto}"))
        )
        RATING_COLOR = c.rating.get(self.user.rank)
        MAX_RATING_COLOR = c.rating.get(self.user.maxRank)
        CONTRIBUTION = "+" * (self.user.contribution > 0) + str(
            self.user.contribution
        )
        CONTRIBUTION_COLOR = c.GREEN if self.user.contribution > 0 else c.GRAY
        # image
        img1 = Label(self.master, image=PROFILE_PIC)
        img1.image = PROFILE_PIC
        img1.grid(row=0, column=2, rowspan=10)
        # rank
        label1 = Label(
            self.master,
            fg=RATING_COLOR,
            font="Verdana 14 bold",
            text=self.user.rank.title(),
        )
        label1.grid(row=0, column=0, sticky="w", columnspan=2)
        # handle
        label2 = Label(
            self.master,
            fg=RATING_COLOR,
            font="Helvetica 23 bold",
            text=self.user.handle,
        )
        label2.grid(row=1, column=0, sticky="w", columnspan=2)
        # name, city, country
        label3 = Label(
            self.master,
            fg="#777777",
            text=f"{self.user.get('firstName', '')} {self.user.get('lastName', '')}, {self.user.get('city', '')}, {self.user.get('country', '')}".strip(
                ", "
            ),
        )
        label3.grid(row=2, column=0, sticky="w", columnspan=2)
        # From
        label4 = Label(
            self.master,
            fg="#777777",
            text=f"From {self.user.get('organization', '')}",
        )
        label4.grid(row=3, column=0, sticky="w", columnspan=2)
        # Contest Rating:
        label5 = Label(
            self.master, font="Arial 14", text="Contest Rating:         "
        )
        label5.grid(row=4, column=0, sticky="w")
        label6 = Label(
            self.master,
            fg=RATING_COLOR,
            font="Arial 14",
            text=self.user.rating,
        )
        label6.grid(row=4, column=1, sticky="w")
        # Max Rating:
        label7 = Label(self.master, font="Arial 14", text="Max Rating:")
        label7.grid(row=5, column=0, sticky="w")
        label8 = Label(
            self.master,
            fg=MAX_RATING_COLOR,
            font="Arial 14",
            text=f"{self.user.maxRank.title()}, {self.user.maxRating}",
        )
        label8.grid(row=5, column=1, sticky="w")
        # Contribution:
        label9 = Label(self.master, font="Arial 14", text="Contribution:")
        label9.grid(row=6, column=0, sticky="w")
        label10 = Label(
            self.master,
            fg=CONTRIBUTION_COLOR,
            font="Arial 14",
            text=CONTRIBUTION,
        )
        label10.grid(row=6, column=1, sticky="w")
        # Friend of:
        label11 = Label(self.master, font="Arial 14", text="Friend of:")
        label11.grid(row=7, column=0, sticky="w")
        label12 = Label(
            self.master,
            font="Arial 14",
            text=f"{self.user.friendOfCount} users",
        )
        label12.grid(row=7, column=1, sticky="w")
        # Last visit:
        label13 = Label(self.master, font="Arial 14", text="Last visit:")
        label13.grid(row=8, column=0, sticky="w")
        label14 = Label(
            self.master,
            font="Arial 14",
            text=datetime.utcfromtimestamp(
                int(self.user.lastOnlineTimeSeconds)
            ),
        )
        label14.grid(row=8, column=1, sticky="w")
        # Registered
        label15 = Label(self.master, font="Arial 14", text="Registered:")
        label15.grid(row=9, column=0, sticky="w")
        label16 = Label(
            self.master,
            font="Arial 14",
            text=datetime.utcfromtimestamp(
                int(self.user.registrationTimeSeconds)
            ),
        )
        label16.grid(row=9, column=1, sticky="w")


class App:
    def __init__(self, master):
        self.master = master
        master.title("Codeforces Scrapper")
        master.bind("<Return>", self.display_profile)

        label1 = ttk.Label(master, text="Handle:")
        label1.grid(row=0, column=0, padx=5, pady=5)
        self.entry1 = ttk.Entry(master)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)
        self.entry1.focus_set()
        button1 = ttk.Button(
            master, text="Fetch Data", command=self.display_profile
        )
        button1.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def display_profile(self, event=None):
        handle = self.entry1.get()
        top = tk.Toplevel()
        Profile(top, handle)
        self.entry1.delete(0, 999)


def main(handle=None):
    root = tk.Tk()
    if handle:
        Profile(root, handle)
    else:
        App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
