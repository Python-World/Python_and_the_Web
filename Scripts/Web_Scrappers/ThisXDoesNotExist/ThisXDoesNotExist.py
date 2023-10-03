#!/usr/bin/env python3
import argparse
import io
import logging
from datetime import datetime
from pathlib import Path

# If Pillow isn't installed it won't show the image but just install it
try:
    import PIL.Image

    pillow_available = True
except ImportError:
    logging.getLogger(__name__).warning("Unable to import PIL")
    pillow_available = False

from functs import (
    get_art,
    get_cat,
    get_dog,
    get_horse,
    get_politician,
    get_pony,
    get_snack,
    get_waifu,
)

# the functions to call to get the type of the image and the image itself, since the names are all the same a dict
# isn't really needed, I could've just used getattr or similar tricks.
# If you want to change a name of a type of a photo (Ex: you don't like dog and want to change "--type dog"
# to "--type doggo"), you can do it by changing keys in this dict.
fun_dict = {
    "art": get_art,
    "cat": get_cat,
    "dog": get_dog,
    "pony": get_pony,
    "politician": get_politician,
    "horse": get_horse,
    "snack": get_snack,
    "waifu": get_waifu,
}

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "--type",
    "-t",
    type=str,
    required=True,
    choices=fun_dict.keys(),
    help="Type of image to retrieve.",
)
arg_parser.add_argument(
    "--memory",
    "-m",
    action="store_true",
    help="Pass to not save the image",
)
arg_parser.add_argument(
    "--outfile",
    "-of",
    type=str,
    default="{TYPE}_{DATE}.{EXT}",
    help="The file where the image should be saved. \n"
    "{DATE} will be replaced with the date, {TYPE} with the image type (see --type), {EXT} for the extension. \n"
    "Use {{ and }} to include { and }",
)
arg_parser.add_argument(
    "--outdir",
    "-od",
    type=str,
    default="images",
    help="The directory where the file should be saved. Default set to images",
)
arg_parser.add_argument(
    "--no-pil", "-np", action="store_true", help="Pass to not show the image."
)
args = arg_parser.parse_args()
del arg_parser

img_type, img_bytes = fun_dict[args.type]()

if not args.memory:
    # date format: dd_mm_yyyy_hh_mm
    OutPath = Path(args.outdir) / Path(
        args.outfile.format(
            TYPE=args.type,
            DATE=datetime.now().strftime("%d_%m_%Y_%H_%M"),
            EXT=img_type,
        )
    )
    OutPath.open(mode="wb").write(img_bytes)
    print("[*] Saved file to: %s" % OutPath)

# If --no-pil wasn't passed and Pil is installed, show the image
if not args.no_pil and pillow_available:
    try:
        PIL.Image.open(
            io.BytesIO(img_bytes),
        ).show()
    except PIL.UnidentifiedImageError:
        # Sometimes the dog site will return a .mp4 file. Pillow can't open such files so it'll throw an exception.
        print(
            "[-] Unable to show the photo (probably because it's a video)! Image extension: %s"
            % img_type
        )
