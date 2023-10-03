import sys
import urllib

import requests
from bs4 import BeautifulSoup
from whaaaaat import prompt


class ScrapeLyrics:
    """Class to scrape lyrics"""

    def __init__(self, url, parse_type):
        """ """
        self.url = url
        self.parse_type = parse_type
        self.soup = None
        self.out = None

    def parse(self):
        """ """
        res = requests.get(self.url)
        self.soup = BeautifulSoup(res.text, "html.parser")

    def parse_songlist(self):
        """parsing the list of matched songs"""
        self.out = []
        for tds in self.soup.find_all("td"):
            data = tds.attrs.get("onclick", None)
            if data:
                self.out.append((tds.text, data.split("=")[-1]))
        self.out = dict(self.out)

    def parse_lyrics(self):
        """parsing the lyrics"""
        for tds in self.soup.find_all("div"):
            if not tds.attrs:
                self.out = tds.text

    def driver(self):
        """method for all methods"""
        self.parse()
        if self.parse_type == "song_list":
            self.parse_songlist()
        else:
            self.parse_lyrics()


class LyricsConsole(ScrapeLyrics):
    """Class for search and display"""

    def __init__(self, song_name):
        """ """
        self.song_name = song_name
        super().__init__(url=None, parse_type=None)

    def search_song(self):
        """framing url and parsing list"""
        form_url = (
            "https://search.azlyrics.com/search.php?q={song_name}".format(
                song_name="+".join(self.song_name.split())
            )
        )
        super().__init__(url=form_url, parse_type="song_list")
        self.driver()

    def display_prompt(self):
        """displaying the result on console"""
        choices = list(self.out.keys())
        if not choices:
            return
        questions = [
            {
                "type": "list",
                "name": "link",
                "message": "Select the closet match",
                "choices": choices,
            }
        ]
        answers = prompt(questions)
        self.url = self.out[answers["link"]].replace("'", "")
        self.parse_type = "song"
        self.driver()
        return self.out


if __name__ == "__main__":
    song_name = sys.argv[1]
    obj = LyricsConsole(song_name)
    obj.search_song()
    print(obj.display_prompt())
