import base64
import getpass
import random
import string
import subprocess
import sys
from time import sleep


# the initail greeting message
def greeting():
    welcome = """
************************************************************
*                                                          *
*            Welcome to the Mass Mail Spammer              *
*                                                          *
************************************************************
"""
    print(welcome)


# error handling for user inputs
def check_err(email, target, spam, choice):
    if "@" not in email or "@" not in target:
        print("Error in email/target\nPlease try again\nExiting...\n")
        sys.exit()

    try:
        int(spam)
        int(choice)
    except ValueError:
        print(
            "Number of spam messages/choice should be a positive integer\nExiting...\n"
        )
        sys.exit()


# generate random spam messages
def rand_msg(spam):
    msg = []
    sub = []
    N = int(input("Enter the length of random messages : "))

    for i in range(int(spam)):
        print("Message number #{}/{}".format(i + 1, spam))
        msg.append(
            "".join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(N)
            )
        )
        sub.append(input("Enter subject : "))

    print("Generated spam messages!")
    return msg, sub


# generate user defined messages
def custom_msg(spam):
    msg = []
    sub = []

    for i in range(int(spam)):
        print("Message number #{}/{}".format(i + 1, spam))
        sub.append(input("Enter subject : "))
        msg.append(input("Enter your message : "))

    return msg, sub


# read files into messages
def from_file(spam):
    msg = []
    sub = []

    for i in range(int(spam)):
        print("Reading file number #{}/{}".format(i + 1, spam))
        x = input("Enter absolute path for the file : ")

        try:
            with open(x, "r") as file:
                msg.append(file.read().replace("\n", ""))
            sub.append(input("Enter subject : "))
        except FileNotFoundError:
            print("This file does not exist\nExiting...\n")
            sys.exit()

    return msg, sub


def main():
    greeting()

    email = input("Enter your email : ")
    passwd = getpass.getpass(
        "Enter your passwd : "
    )  # take passwd into as hidden

    target = input("Recipient's email : ")
    spam = input("Number of spam messages : ")

    prompt = """
Choose one of the method below to generate spam messages :
1. Random strings
2. Custom message
3. Message from a file
Choose (1-3)
"""
    choice = input(prompt)

    print("Validating all inputs...")
    check_err(email, target, spam, choice)
    print("Done!")

    if choice == "1":
        msg, sub = rand_msg(spam)
    elif choice == "2":
        msg, sub = custom_msg(spam)
    elif choice == "3":
        msg, sub = from_file(spam)
    else:
        print("The choice can only 1,2 or 3\nExiting...")
        sys.exit()

    print("Encoding credentials in base64...")

    creds = "\00" + email + "\00" + passwd
    encoded_creds = base64.b64encode(creds.encode("ascii")).decode("ascii")

    for i in range(int(spam)):
        subprocess.check_call(
            ["./expect_mail.sh", msg[i], sub[i], encoded_creds, target, email]
        )
        sleep(1)


if __name__ == "__main__":
    main()
