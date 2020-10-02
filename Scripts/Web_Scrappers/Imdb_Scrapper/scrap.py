import os
import requests
from bs4 import BeautifulSoup
from youtube_search import YoutubeSearch
import json
import time
import random
import argparse


def get_movie_data_credits(url):
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data,'html.parser')
    temp = soup.find('div',{'id': 'fullcredits_content'})
    data = {}
    try:
        for h4 in temp.find_all('h4'):
            data[h4.text.strip()] = []
            for x in h4.find_next('table').find_all('a'):
                data[h4.text.strip()].append(x.text.strip())
    except:
        data = None
    return data
        
def get_movie_data_keywords(url):
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data,'html.parser')
    temp = soup.find('table',{'class': 'dataTable evenWidthTable2Col'})
    keywords = list()
    try:
        for x in soup.find_all('div',{'class':'sodatext'}):
            keywords.add(x.find('a').text)
    except:
        keywords = None
    return keywords

def get_movie_data_review(url):
    try:
        html_data = requests.get(url).text
        soup = BeautifulSoup(html_data,'html.parser')
        temp = soup.find('div',{'class' : 'lister-list'})
        review = {
            'rating' : list(),
            'title' : list(),
            'review' : list()
        }
        for x in  temp.find_all('div',{'class' : 'lister-item-content'}):
            review['rating'].append(x.find('span',{'class':'rating-other-user-rating'}).text.strip())
            review['title'].append(x.find('a').text.strip())
            review['review'].append(x.find('div',{'class':'text show-more__control'}).text.strip())
        return review
    except:
        return None


def get_movie_data_production(url):
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data,'html.parser')
    temp = soup.find('div',{'id':'company_credits_content'}) 
    data = {}
    try:
        for h4 in temp.find_all('h4'):
            data[h4.text.strip()] = []
            for x in h4.find_next('ul').find_all('a'):
                data[h4.text.strip()].append(x.text.strip())
    except:
        data = None
    return data

def get_movie_data(url,imdb_id):
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data,'html.parser')

    try:
        p_title = soup.find('div', {'class' : 'title_wrapper'}).find('h1').text.strip()
        run_time = soup.find('div', {'class' : 'title_wrapper'}).find('div', {'class':'subtext'}).find('time').text.strip()
    except:
        p_title, run_time = None, None
    try:
        temp = soup.find('div', {'class' : 'title_wrapper'}).find('div', {'class':'subtext'}).find_all('a')
        temp.pop()
        genres = list()
        for x in temp:
            genres.append(x.text.strip())
    except:
        genres = None
    try:
        temp = soup.find('div',{'class': 'ratingValue'}).find('strong').get('title').split(' ')
        imdb_rating,imdb_rated_by = temp[0], temp[3]
    except:
        imdb_rating, imdb_rated_by = None, None
    try:
        metascore = soup.find('div',{'class': 'metacriticScore score_mixed titleReviewBarSubItem'}).find('span').text
    except:
        metascore = None
    try:
        imdb_plot_1 = soup.find('div',{'class':'plot_summary'}).find('div',{'class':'summary_text'}).text.strip()
    except:
        imdb_plot_1 = None
    try:
        imdb_plot_2 = soup.find('div',{'class' : 'inline canwrap'}).find('span').text.strip()
    except:
        imdb_plot_2 = None
    try:
        poster = f"{soup.find('div',{'class': 'poster'}).find('img').get('src').split('@@.')[0]}@@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg"
    except:
        poster = None
    try:
        temp = YoutubeSearch(f'{p_title} trailer', max_results=1).to_json()
        trailer = f"https://youtube.com{json.loads(temp)['videos'][0]['url_suffix']}"
    except:
        trailer = None
    country = set()
    language = set()
    release_day = None
    release_month = None
    release_year = None
    movie_color_type = None
    for x in soup.find_all('div',{'class':'txt-block'}):
        try:
            if x.find('h4').text == 'Country:':
                for y in x.find_all('a'):
                    country.add(y.text)
            if x.find('h4').text == "Language:":
                for y in x.find_all('a'):
                    language.add(y.text)
            if x.find('h4').text == "Release Date:":
                release_day = x.text.split(" ")[2]
                release_month = x.text.split(" ")[3]
                release_year = x.text.split(" ")[4]
            if x.find('h4').text == "Color:":
                movie_color_type = x.find('a').text
        except:
            pass
    production = get_movie_data_production(f'{url}/companycredits')
    keywoards = get_movie_data_keywords(f'{url}/keywords')
    cast = get_movie_data_credits(f'{url}/fullcredits')
    review = get_movie_data_review(f'{url}/reviews?sort=totalVotes&dir=desc&ratingFilter=0')
    if len(country) == 0:
        country = None
    if len(language) == 0:
        language = None
    final_data = {
        'imdb_id' : imdb_id,
        'names' : {
            'p_title' : p_title,
            'o_title' : p_title
        },
        'run_time' : run_time,
        'genres' : genres,
        'rating' : {
            'imdb_rating' : imdb_rating,
            'metascore' : metascore
        },
        'description' : {
            'plot' : imdb_plot_1,
            'summary' : imdb_plot_2
        },
        'production' : production,
        'cast' : cast,
        'keywoards' : keywoards,
        'basic_info' : {
            'country' : country,
            'language' : language,
            'release_date' : {
                'day' : release_day,
                'month' : release_month,
                'year' : release_year
            },
            'country' : country
        },
        'media' : {
            'posted' : poster,
            'trailer' : trailer
        },
        'review' : review
    }
    return final_data
  

def main(id):
    data = get_movie_data(f'https://www.imdb.com/title/{id}',id)
    print(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Commands")
    parser.add_argument(
        "id",
        help="id: Enter imdb id",
    )
    args = parser.parse_args()
    main(str(args.id))
