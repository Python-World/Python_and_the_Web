import requests
import json
from scrapmagnet import scrapmag


def pirate(search):
    array = []
    base_link = "https://beaindia.org"
    url = base_link + "/apibay/q.php?q=" + search
    cookies = {
        "__cfduid": "dfa53d7227d2614eca69ee49261e0958e1596182467",
        "_ga": "GA1.2.1067275401.1596182469",
        "_gid": "GA1.2.2013677734.1596182469",
        "ppu_main_b1f57639c83dbef948eefa8b64183e1e": "1",
        "sb_main_740b003479a7eba76fd37c6ed9b4e91a": "1",
        "dom3ic8zudi28v8lr6fgphwffqoz0j6c": "5b26a583-ce6b-49fb-b679-fdf4d45980a9%3A1%3A2",
        "494668b4c0ef4d25bda4e75c27de2817": "5b26a583-ce6b-49fb-b679-fdf4d45980a9:1:2",
        "sb_count_740b003479a7eba76fd37c6ed9b4e91a": "2",
        "ppu_sub_b1f57639c83dbef948eefa8b64183e1e": "4",
    }
    headers = {
        "Connection": "close",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "Accept": "/",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": base_link + "/search.php?q=saf",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
    }
    result = json.loads(
        requests.get(url, headers=headers, cookies=cookies).text
    )
    for index, value in enumerate(result):
        if index > 25:
            break
        data = {}
        data["name"] = value["name"]
        data["hash"] = value["info_hash"]
        data["leechers"] = value["leechers"]
        data["seeders"] = value["seeders"]
        data["totalfiles"] = value["num_files"]
        data["uploaded-by"] = value["username"]
        data["magnetlink"] = scrapmag(data["hash"], data["name"])
        data["size"] = (
            str(float("{:.2f}".format(float(value["size"]) / 1000000000)))
            + " GB"
        )
        array.append(data)
    return array
