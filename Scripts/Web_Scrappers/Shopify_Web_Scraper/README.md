# Shopify Web Scraper
Shopify Web Scraper allows you to list collections, download collection information
in csv format and a Standard HTML summarizer. This Scraper supports

* Multiple Images
* HTML Output
* Shopify CSV Format Output
* List Collections

A example have been included in this folder where products.csv is the shopify csv, products.html is html output.

## Examples
To list collections
```commandline
python shopify.py --list-collections <Website_URL>
```

To Obtain CSV for collection
```commandline
python shopify.py --collections <collection_1>,<collection_2>,...,<collection_n> <Webisite_URL>
```

HTML is not emitted by default for that you will have to
```commandline
python shopify.py --collections <collection_1>,<collection_2>,...,<collection_n> --generate-html <Website_URL>
```