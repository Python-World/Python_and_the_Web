from requests_futures.sessions import FuturesSession
from pprint import pprint
from HTMLParser import HTMLParser
import re
import json
import sys


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def get_quotes(num=10):
    futures = []
    url = "http://www.quotedb.com/quote/quote.php?action=random_quote"
    session = FuturesSession()
    for i in range(1, num+1):
        futures.append(session.get(url))
    results = []
    for f in futures:
        res = f.result()
        results.append(res.content)
    return results


def extract_quote(text):
    matches = re.findall(r'document.write\(\'(.*)\'\)', text)
    if not matches or len(matches) != 2:
        print "Error: matches = ", matches
        return None
    quote = strip_tags(matches[0])
    author = re.search(r'More quotes from (.*)', strip_tags(matches[1]))
    if author:
        author = author.group(1)
    return (quote, author)


def write_to_json_file(tups, filename="quotes.json"):
    data = []
    for quote, author in tups:
        data.append({'quote': quote, 'author': author})
    json_str = json.dumps(data)
    with open(filename, 'w') as f:
        f.write(json_str)
    return filename


def main():
    if len(sys.argv) == 2:
        num = sys.argv[1]
    else:
        num = 10
    print "Getting {} quotes...".format(num)
    print "This may take a while..."
    results = get_quotes(num=num)
    tups = []
    print "...Done"
    print "Extracting quotes and authors..."
    for r in results:
        tup = extract_quote(r)
        if tup is not None:
            try:
                q = unicode(tup[0], 'utf8')
                a = unicode(tup[1], 'utf8')
                tups.append(tup)
            except Exception as e:
                print "Failed to extract data: {}".format(str(e))
                print "Skipping to next..."
                pass
    print "...Done"
    print "Writing to file..."
    filename = write_to_json_file(tups)
    print "Saved to", filename


if __name__ == '__main__':
    main()