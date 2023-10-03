import json
from typing import Dict, List

import requests
from bs4 import BeautifulSoup as Soup

HEADERS = {"Content-type": "application/xml"}
LOCATION_XMLRPC = "xmlrpc.php"
METHODS = {
    "validate": "system.listMethods",
    "list_methods": "system.listMethods",
}


def get_template_call_simple() -> str:
    data = None
    with open(
        "method_call_simple_rpc.xml", encoding="utf-8"
    ) as template_simple_xml:
        data = template_simple_xml.read()

    return data


def get_sites_wordpress() -> List[Dict]:
    sites_wordpress = []

    with open("sites.json", encoding="utf-8") as sites_json:
        sites_wordpress = json.load(sites_json)

    return sites_wordpress


def modify_valid_url(url: str) -> str:
    if len(url) - 1 != "/":
        url += "/"

    return url


def get_petition(url_site: str, data_xml: str):
    return requests.post(url_site, data=data_xml, headers=HEADERS)


def accept_xml_rpc_request(url_site: str, data_xml: str) -> bool:
    data_xml = data_xml.replace("{{{method_name}}}", METHODS["validate"])
    result = get_petition(url_site, data_xml)
    if result.status_code == 200:
        return True
    return False


def get_methods_allows(url_site: str, data_xml: str):
    data_xml = data_xml.replace("{{method_name}}", METHODS["list_methods"])
    result = get_petition(url_site, data_xml)
    method_allows = Soup(result.text, features="xml")
    print("Methods allowed are listed below ")
    print("--------------------------------")
    count = 0
    for method in method_allows.find_all("string"):
        print(method.string)
        count += 1
    print(f"{url_site} has {count} methods allowed ")


def main():
    sites_wordpress = get_sites_wordpress()
    data_xml = get_template_call_simple()

    for site in sites_wordpress:
        url_site = modify_valid_url(site["url_site"]) + LOCATION_XMLRPC
        if accept_xml_rpc_request(url_site, data_xml):
            print()
            print(f"The url {url_site} allowed petitions for xml-rpc")
            print("-------------------------------------------------")
            get_methods_allows(url_site, data_xml)


if __name__ == "__main__":
    main()
