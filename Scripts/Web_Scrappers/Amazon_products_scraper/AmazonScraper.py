#!/usr/bin/env python

from selectorlib import Extractor
import requests 
import json


# CSS selectors of the product we will scrape.
e = Extractor.from_yaml_file('selectors.yml')

def scrape(url):  

    # The headers our scraper will use.
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download page using requests lib.
    print("Downloading %s"%url)
    req = requests.get(url, headers=headers)
    # This is just to check if Amazon blocked our scraper.
    if req.status_code > 500:
        if "Contact for access to amazon data." in req.text:
            print("Amazon Page: %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Amazon Page: %s was blocked, status code is: %d"%(url,req.status_code))
        return None
    # Return scraped values as text.
    return e.extract(req.text)

with open("search_products.txt",'r') as urllist, open('product_search_output.jsonl','w') as outfile:
    for url in urllist.read().splitlines():
        out_data = scrape(url) 
        if out_data:
            for product in out_data['products']:    
                print(product)
                product['search_url'] = url
                print("Saving Product: %s"%product['title'])
                json.dump(product,outfile)
                outfile.write("\n")