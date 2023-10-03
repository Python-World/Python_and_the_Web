import os
from os import listdir
from os.path import isfile, join

import numpy as np
import PIL
from PIL import Image


def merge_pics_vertically(images_list, name):
    # Opens all files and stores them in a list
    imgs = [Image.open(i) for i in images_list]
    min_img_width = min(i.width for i in imgs)

    # Sums up the total height
    total_height = 0
    for i, img in enumerate(imgs):
        if img.width > min_img_width:
            imgs[i] = img.resize(
                (min_img_width, int(img.height / img.width * min_img_width)),
                Image.ANTIALIAS,
            )
        total_height += imgs[i].height

    # Pastes all of them together
    img_merge = Image.new(imgs[0].mode, (min_img_width, total_height))
    y = 0
    for img in imgs:
        img_merge.paste(img, (0, y))
        y += img.height

    # Then saves the final image
    img_merge.save(name + ".jpg")


def get_files(directory, ext=None):
    if ext is None:
        ext = [".jpg"]
    files = []
    # Scans the folder and gets all files with the extension
    for f in os.scandir(directory):
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)
    return files


name = input("Sub-folder with images to be merged: ")
path = os.getcwd() + "/" + name
pictures = get_files(path)
merge_pics_vertically(pictures, path)
