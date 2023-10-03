import os

import requests


def download(fileName):
    with open(fileName, "wb") as f:
        f.write(
            requests.get(
                "https://thispersondoesnotexist.com/image",
                headers={"User-Agent": "Incognito"},
            ).content
        )
        f.close()


n = int(input("Enter no. of images to download: "))
print("1.Specify path to a directory to store the images")
print("2.Create a directory to store the images")
ch = int(input("Enter option:"))
if ch == 1:
    dir = input("Enter path to directory: ")
    for i in range(n):
        download(dir + "/" + "person" + str(i + 1) + ".jpg")
        print("person" + str(i + 1) + ".jpg downloaded")
else:
    parent = input("Enter parent directory: ")
    new = input("Enter directory name to be created: ")
    path = os.path.join(parent, new)
    os.mkdir(path)
    print("Directory '% s' created" % new)
    print(path)
    for i in range(n):
        download(path + "/" + "person" + str(i + 1) + ".jpg")
        print("person" + str(i + 1) + ".jpg downloaded")
