import requests
from bs4 import BeautifulSoup


# function to get top 10 articles from quantopian
def get_quantopian_articles():
    res = requests.get("https://www.quantopian.com/posts")
    soup = BeautifulSoup(res.text, "html.parser")
    posts = soup.select("#search-results")[0]
    top10 = posts.findAll("div", {"class": "post-title"})[:10]

    lines = []
    for i in top10:
        lines.append(i.text.strip())

    hrefs = []
    for i in top10:
        for a in i.find_all("a", href=True):
            hrefs.append(a["href"].strip())

    links = []
    for href in hrefs:
        link = "https://www.quantopian.com" + href
        links.append(link)

    top10 = "Here's the top 10 articles from Quantopian:\n"
    for i in range(0, 10):
        top10 += lines[i] + "\n" + links[i] + "\n"
    return top10


# function to get top 10 articles from quantocracy
def get_quantocracy_articles():
    # using user agent to bypass the site block for bots
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    res = requests.get("https://quantocracy.com/", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    posts = soup.select("#qo-mashup")[0]
    top10 = posts.findAll("a", {"class": "qo-title"})[:10]

    lines = []
    for i in top10:
        lines.append(i.text.strip())

    links = []
    for i in top10:
        links.append(i["href"])

    top10 = "Here's the top 10 articles from Quantocracy:\n"
    for i in range(0, 10):
        top10 += lines[i] + "\n" + links[i] + "\n"
    return top10


# function to get top 10 articles from quantstart systematic trading
def get_quantstart_articles():
    res = requests.get(
        "https://www.quantstart.com/articles/topic/systematic-trading/"
    )
    soup = BeautifulSoup(res.text, "html.parser")
    posts = soup.select("body > div > section.mb-2 > div")[0]

    lines = []
    for post in posts.findAll("p")[:10]:
        lines.append(post.text)

    hrefs = []
    for href in posts.findAll("a")[:10]:
        hrefs.append(href["href"])

    links = []
    for href in hrefs:
        link = "https://www.quantstart.com" + href
        links.append(link)

    top10 = "Here's the top 10 articles from Quantstart Systematic Trading:\n"
    for i in range(0, 10):
        top10 += lines[i] + "\n" + links[i] + "\n"
    return top10


def main():
    quantopian = get_quantopian_articles()
    quantocracy = get_quantocracy_articles()
    quantstart = get_quantstart_articles()
    with open("output.txt", "w") as f:
        f.write(f"{quantopian}\n\n{quantocracy}\n\n{quantstart}")
    print("Article Links saved in the output file")


if __name__ == "__main__":
    main()
