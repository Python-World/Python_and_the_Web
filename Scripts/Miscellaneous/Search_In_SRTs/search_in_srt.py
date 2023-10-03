class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


import argparse
import glob

import srt

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--dir", help="path to directory containing srt files")
group.add_argument("--file", help="path to srt file")

args = parser.parse_args()

if args.dir is None:  # if its a single file
    files = [
        args.file,
    ]
else:  # list of files in the directory
    files = glob.glob(args.dir + "/*.srt")


def search():
    """
    Takes a input from the user and searches for that text accross multiple SRT files in the specified folder.
    Returns a list of srt file contents that matched with the given text.
    """
    search_string = input("search for ? : ")
    search_string = search_string.lower()
    full_subtitles_list = []
    counter = 0
    id_iterator = 0
    for filename in files:
        print("Reading file ", filename, "...")

        with open(filename, "r") as f:
            srt_content = f.read()

            subtitles = list(srt.parse(srt_content))
            full_subtitles_list += subtitles

            for sub in subtitles:
                content = sub.content
                if search_string in content.lower():
                    counter += 1
                    print(bcolors.BOLD, bcolors.FAIL, "ID : ", id_iterator)
                    print(
                        bcolors.BOLD,
                        bcolors.OKGREEN,
                        "CONTENT : ",
                        bcolors.ENDC,
                        content,
                    )
                    print(
                        bcolors.BOLD,
                        bcolors.OKBLUE,
                        "START TIME : ",
                        bcolors.ENDC,
                        sub.start,
                    )
                    print(
                        bcolors.BOLD,
                        bcolors.HEADER,
                        "FILE : ",
                        bcolors.ENDC,
                        filename,
                        end="\n\n",
                    )

                id_iterator += 1

    print(bcolors.BOLD, "Total records found : ", counter, bcolors.ENDC)
    return full_subtitles_list


def expand_subtitle(full_subtitles_list, threshold=5):
    """
    Expands the content of a srt file.
    full_subtitles_list : full list of srt contents
    threshold : specifies how many srt contents to show before and after the currently detected content.

    """
    response = input("\n Enter ID of subtitle : ")
    if response == "q":
        return

    if not response.isnumeric():
        print("ID should be an integer")
        return

    id = int(response)

    threshold = 5
    if id - threshold < 0:
        start = 0
    else:
        start = id - threshold

    if id + threshold > len(full_subtitles_list):
        end = len(full_subtitles_list)
    else:
        end = id + threshold

    result = ""
    for i in range(start, end):
        sub = full_subtitles_list[i]
        if i == id:
            result += (
                " "
                + bcolors.WARNING
                + sub.content.strip()
                + bcolors.ENDC
                + " "
            )
        else:
            result += " " + sub.content.strip() + " "

    print("\n\n", result)


full_subtitles_list = []

while True:
    print("\n< press s to search a phrase >")
    print("< press e to expand a subtitle >")
    print("< press q to quit program >")
    print("\n")

    resp = input("input ? : ")
    if resp == "s":
        full_subtitles_list = search()
    elif resp == "e":
        expand_subtitle(full_subtitles_list)
    elif resp == "q":
        print("Bye bye!")
        break
    else:
        print("Invalid choice ")
