from bs4 import BeautifulSoup
import requests, string, re, sys
from unidecode import unidecode


base_url='https://guide.michelin.com/en/restaurant/'

# remove puntuations and special charecters (é->e)
def normalize_input(resturant_name):
    resturant_name = resturant_name.lower().strip()
    resturant_name = resturant_name.translate(str.maketrans("", "", string.punctuation))
    return unidecode(resturant_name.replace(" ", "-"))

def get_resturent_details(resturant_name):
    url = base_url+resturant_name
    print(url)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    data = {}
    
    data['name'] = soup.h2.text

    data['address'] = soup.find(class_='restaurant-details__heading--list').li.text

    data['description'] = soup.find('p').text

    data['tags'] = [re.sub(r'[^a-zA-Z0-9]','',tag.text) for tag in soup.select('.restaurant-details__classification--list li')]

    # lift, car-parking etc...
    data['facilities'] = [re.sub(r'[^a-zA-Z0-9]', '', facility.text) for facility in soup.select('.restaurant-details__services--list li')]

    data['gmaps_link'] = soup.select('.google-map__static iframe')[0]['src']

    price_and_type_string = soup.find(class_='restaurant-details__heading-price').text.split('•')

    data['price'] = re.sub(r'[^a-zA-Z0-9-]', '', price_and_type_string[0])

    #some resturents so not have the type listed
    if len(price_and_type_string) == 2:
        data['type'] = re.sub(r'[^a-zA-Z0-9-]', '', price_and_type_string[1])
    
    return data

def main():
    resturent = normalize_input(str(sys.argv[1]))
    print(get_resturent_details(resturent))


main()




    