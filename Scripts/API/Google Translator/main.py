from sys import exit

from googletrans import LANGUAGES, Translator

lang = LANGUAGES
translator = Translator()


def greeting():
    # the initail one time greeting message
    welcome = """
************************************************************
*                                                          *
*                Welcome to G-Py translator                *
*                                                          *
************************************************************
"""
    print(welcome, "\n")

    input("Press Enter to continue...")
    print("\nList of Available Languages : \n\n", lang)


def custom(src, dst):
    sent = input("\nEnter your sentence : ")

    if src == 0:
        print("Output -> ", translator.translate(sent, dest=dst).text)
    else:
        print("Output -> ", translator.translate(sent, src=src, dest=dst).text)


def from_file(src, dst):
    name = input("\nEnter absolute path for file : ")

    try:
        with open(name, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("This file doesn't exist!\nExiting...")
        exit()

    print("\n", "-" * 100)
    print("\nOriginal text -> \n\n{}\n".format(content))
    print("-" * 100)

    if src == 0:
        output = translator.translate(content, dest=dst).text
    else:
        output = translator.translate(content, src=src, dest=dst).text

    print("\nTranslated text -> \n\n{}\n\n".format(output))
    print("-" * 100)

    x = input("\nSave output to a file? y/n : ").lower()

    if x == "y":
        x = input("Enter file name : ")
        try:
            with open(x, "w") as f:
                f.write(output)
        except FileExistsError:
            print("This file already exist!\nExiting...")
            exit()
    else:
        print("Bye")
        exit()


def main():
    prompt = """
Available options :
1. Custom text translation
2. Text from a file
3. 'q' to Quit
Choose (1-3)

"""

    choice = input(prompt).lower()

    if choice == "q":
        print("Bye")
        exit()
    elif choice not in ["1", "2"]:
        print("Invalid choice, exiting...")
        exit()

    num = input("\nAuto detect source language? y/n : ")

    if num.lower() not in ["y", "n"]:
        print("Invalid choice, exiting...")
        exit()

    src = 0
    if num == "n":
        src = input("Enter source language : (can be abbr/full form) : ")

        if src not in lang.values() and src not in lang:
            print("Invalid source langauge, exiting...")
            exit()

    dst = input("Enter destination language : (can be abbr/full form) : ")
    if dst not in lang.values() and dst not in lang:
        print("Invalid destination langauge, exiting...")
        exit()

    if choice == "1":
        custom(src, dst)
    else:
        from_file(src, dst)


if __name__ == "__main__":
    greeting()
    main()
