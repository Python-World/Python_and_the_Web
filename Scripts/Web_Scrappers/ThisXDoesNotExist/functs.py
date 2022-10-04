import random
import typing as ty

import requests
from bs4 import BeautifulSoup


def get_random_number_with_zero(min_num: int, max_num: int) -> str:
    """
    Get a random number in range min_num - max_num of len max_num (padded with 0).

    @param min_num: the lowest number of the range in which the number should be generated
    @param max_num: the highest number of the range in which the number should be generated
    @return: A string like "00183"
    """
    return str(random.randint(min_num, max_num)).zfill(len(str(max_num)))


# These functions all do the same thing: they return a tuple like (type, bytes) where type is a string
# that indicates the type of the image and bytes is the image like in ("png", b'....')


def get_pony() -> ty.Tuple[str, bytes]:
    # It's https://thisponydoesnotexist.net/v1/w2x-redo/jpgs/seed + 5 random digits + .jpg
    base_url = "https://thisponydoesnotexist.net/v1/w2x-redo/jpgs/seed%s.jpg"
    # This is one the images url.
    img_url = base_url % get_random_number_with_zero(0, 99999)
    # Fetch the photo and return it
    return "jpeg", requests.get(img_url).content


def get_politician() -> ty.Tuple[str, bytes]:
    # It's https://vole.wtf/this-mp-does-not-exist/mp/mp00 + 3 random digits + .jpg (three random digits < 649)
    base_url = "https://vole.wtf/this-mp-does-not-exist/mp/mp00%s.jpg"
    img_url = base_url % get_random_number_with_zero(0, 649)
    return "jpeg", requests.get(img_url).content


def get_horse() -> ty.Tuple[str, bytes]:
    return "jpeg", requests.get("https://thishorsedoesnotexist.com/").content


def get_art() -> ty.Tuple[str, bytes]:
    return "jpeg", requests.get("https://thisartworkdoesnotexist.com/").content


def get_snack() -> ty.Tuple[str, bytes]:
    page_html = requests.get("https://thissnackdoesnotexist.com/").text
    soup = BeautifulSoup(page_html, "html.parser")
    # the tag looks like:
    # <meta property="og:image" content="https://images.unsplash.com/photo-....">
    img_url = soup.find(
        "meta", attrs=dict(property="og:image")
    ).get_attribute_list("content")[0]
    return "jpeg", requests.get(img_url).content


def get_cat() -> ty.Tuple[str, bytes]:
    return "jpeg", requests.get("https://thiscatdoesnotexist.com/").content


def get_waifu() -> ty.Tuple[str, bytes]:
    # This time there is no need to add 0, "1", "25" or "34267" are all valid
    base_url = "https://www.thiswaifudoesnotexist.net/example-%d.jpg"
    img_url = base_url % random.randint(0, 100000)
    return "jpeg", requests.get(img_url).content


def get_dog() -> ty.Tuple[str, bytes]:
    img_url = requests.get("https://random.dog/woof").text
    return (
        img_url.split(".")[-1],
        requests.get("https://random.dog/" + img_url).content,
    )
