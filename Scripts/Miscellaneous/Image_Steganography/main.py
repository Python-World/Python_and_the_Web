import random

import numpy as np
import PIL.Image as Image


def encode(pic_path, text, name):
    text = " " + text
    text = list(text)
    img = Image.open(pic_path)
    width, height = img.size
    pixels = width * height
    if pixels < len(text):
        print("Encoding not Possible")
    else:
        while True:
            skip = random.randint(3, 209)
            if pixels // skip >= len(text):
                break
        edit_image = np.array(img)
        counter = 0
        info = False
        j = 0
        while j < pixels:
            k = j % width
            i = j // height
            if counter >= len(text):
                break
            elif j == 0 and info is False:
                edit_image[i][k][2] = len(text) - 1
                edit_image[i][k + 1][2] = skip
                info = True
            else:
                edit_image[i][k][2] = ord(text[counter])
                counter += 1
            j += skip
        new_img = Image.fromarray(edit_image)
        new_img.save(name + ".png")
        print("Done")


def decode(pic_path):
    text = ""
    img = Image.open(pic_path)
    img_arrayy = np.array(img)
    length = img_arrayy[0][0][2]
    skip = img_arrayy[0][1][2]
    width, height = img.size
    pixels = width * height
    j = 0
    j += skip
    while j < pixels:
        k = j % width
        i = j // height
        if len(text) > length:
            break
        else:
            text += chr(img_arrayy[i][k][2])
        j += skip
    print("Completed")
    print(text)


def main():
    mode = input("Encode/Decode (e/d) : ")
    if mode.lower() == "e":
        img_path = input("Enter path to Image that you want to Encode : ")
        name = input(
            "Enter the Name of the Output File (without extension) : "
        )
        text = input("Enter the Text to be Hidden : ")
        encode(img_path, text, name)
    if mode.lower() == "d":
        img_path = input("Enter path to Image that you want to Decode : ")
        decode(img_path)


main()
