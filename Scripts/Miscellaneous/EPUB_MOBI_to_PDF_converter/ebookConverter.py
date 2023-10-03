import os
import webbrowser
from tkinter import *
from tkinter import filedialog

import convertapi


# function to open the convertAPI webiste in browser
def openWebsite():
    webbrowser.open("https://www.convertapi.com/a", new=3)


# function to clear all widgets in the main frame to render new ones
def clearFrame():
    for w in main_frame.winfo_children():
        w.destroy()


# function to choose file to be converted
def chooseFile():
    global CHOSEN_FILE_LOC
    CHOSEN_FILE_LOC = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select file to convert",
        filetypes=(("epub files", "*.epub"), ("mobi files", "*.mobi")),
    )

    global CHOSEN_FILE_NAME
    CHOSEN_FILE_NAME = CHOSEN_FILE_LOC.split("/")[-1]

    clearFrame()

    label4 = Label(
        main_frame, text="Chosen file: " + CHOSEN_FILE_LOC.split("/")[-1]
    )
    button_next = Button(
        main_frame,
        text="CONVERT>> (takes 2-3 minutes)",
        padx=5,
        pady=5,
        bg="#F48024",
        fg="#FFFFFF",
        command=convertToPDF,
    )

    label4.grid(row=2, column=0, padx=10, pady=10)
    button_next.grid(row=4, column=0, padx=10, pady=10)


# function that contacts convertAPI with the file & carries out the conversion
def convertToPDF():
    global CHOSEN_FILE_LOC
    global CHOSEN_FILE_NAME

    target_folder = os.getcwd()

    print("filename is: " + CHOSEN_FILE_NAME)
    file_ext = CHOSEN_FILE_NAME[-4:]
    file_name_trimmed = CHOSEN_FILE_NAME[:-4]

    print("format is:  " + file_ext)
    print("trimmed name is:  " + file_name_trimmed)

    result = convertapi.convert(
        "pdf", {"File": CHOSEN_FILE_LOC}, from_format=file_ext
    )

    result.file.save(target_folder + "\\" + file_name_trimmed + ".pdf")

    clearFrame()
    label = Label(main_frame, text="File Converted to PDF, Happy Reading!")
    button_exit = Button(
        main_frame,
        text="Exit",
        padx=5,
        pady=5,
        bg="#F48024",
        fg="#FFFFFF",
        command=root.quit,
    )

    label.grid(row=0, column=0, padx=10, pady=10)
    button_exit.grid(row=1, column=0, padx=10, pady=10)


# first tkinter window of the code
def window1():
    # define the labels, input box and buttons
    label = Label(
        main_frame, text="Step 1: Sign up at ConvertApi to get your secret key"
    )
    button_capi = Button(
        main_frame,
        text="OPEN WEBSITE",
        padx=5,
        pady=5,
        bg="#0095FF",
        fg="#FFFFFF",
        command=openWebsite,
    )
    label2 = Label(main_frame, text="Step 2: Enter the secret key below:")
    button_next = Button(
        main_frame,
        text="NEXT>",
        padx=5,
        pady=5,
        bg="#F48024",
        fg="#FFFFFF",
        command=window2,
    )

    # arrange in grid
    label.grid(row=0, column=0, padx=10, pady=10)
    button_capi.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=5, pady=5)
    key_text_box.grid(row=3, column=0, padx=5, pady=5)
    button_next.grid(row=4, column=0, padx=10, pady=10)


def window2():
    secret_key = key_text_box.get()
    convertapi.api_secret = secret_key

    clearFrame()

    label3 = Label(
        main_frame,
        text="Step 3: Choose the file to be converted(epub or mobi):",
    )
    button_file_choose = Button(
        main_frame,
        text="CHOOSE FILE",
        padx=5,
        pady=5,
        bg="#0095FF",
        fg="#FFFFFF",
        command=chooseFile,
    )

    label3.grid(row=0, column=0, padx=10, pady=10)
    button_file_choose.grid(row=1, column=0, padx=10, pady=10)


# driver code
if __name__ == "__main__":
    root = Tk()
    root.title("Ebook to PDF converter")
    root.iconbitmap("pdfIcon.ico")

    # the main frame which will be re-rendered for new window
    main_frame = LabelFrame(root, padx=25, pady=25)
    key_text_box = Entry(main_frame, borderwidth=5)
    main_frame.pack()
    window1()


# global variables & statements
CHOSEN_FILE_NAME = ""
CHOSEN_FILE_LOC = ""
root.mainloop()
