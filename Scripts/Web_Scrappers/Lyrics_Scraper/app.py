import requests

from bs4 import BeautifulSoup
from whaaaaat import prompt, print_json, Separator

class ScrapeLyrics:
    """Class to scrape lyrics"""
    
    def __init__(self, url, parse_type):
        """"""
        self.url = url
        self.parse_type = parse_type
        self.soup = None
        self.out = None
        
    def parse(self):
        """"""
        res = requests.get(self.url)
        self.soup = BeautifulSoup(res.text,'html.parser')
        if self.parse_type == 'song_list':
            self.parse_songlist()
        else:
            self.parse_lyrics()
            
    def parse_songlist(self):
        """"""
        self.out = []
        for tds in self.soup.find_all('td'):
            data = tds.attrs.get('onclick',None)
            if data :
                self.out.append((tds.text, data.split('=')[-1]))
        self.out = dict(self.out)
    
    def parse_lyrics(self):
        """"""
        for tds in self.soup.find_all('div'):
            if not tds.attrs:
                self.out = tds.text
    
    def driver(self):
        """"""
        self.parse()
        if self.parse_type == 'song_list':
            self.parse_songlist()
        else:
            self.parse_lyrics()
        return self.out

class LyricsConsole(ScrapeLyrics):
    """Class for search and display"""
    
    def __init__(self, song_name):
        """"""
        self.song_name = song_name
        
    def search_song(self):
        """"""
    
    def display_prompt():
        """"""