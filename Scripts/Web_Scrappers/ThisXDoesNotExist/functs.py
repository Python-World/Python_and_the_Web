import random
import typing as ty

import requests
from bs4 import BeautifulSoup


def get_random_number_with_zero(min: int, max: int) -> str:
    return str(random.randint(min, max)).zfill(len(str(max)))


def get_pony() -> ty.Tuple[str, bytes]:
    """
    Returns a photo of a pony that does not exist as bytes.

    @rtype: bytes
    """
    # It's https://thisponydoesnotexist.net/v1/w2x-redo/jpgs/seed + 5 random digits + .jpg
    base_url = "https://thisponydoesnotexist.net/v1/w2x-redo/jpgs/seed%s.jpg"
    img_url = base_url % get_random_number_with_zero(0, 99999)
    return "jpeg", requests.get(img_url).content


def get_politician() -> ty.Tuple[str, bytes]:
    """
    Returns a photo of a politician that does not exist as bytes.

    @rtype: bytes
    """
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
    img_url = soup.find("meta", attrs=dict(property="og:image")).get_attribute_list(
        "content"
    )[0]
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
    return img_url.split(".")[-1], requests.get("https://random.dog/" + img_url).content
