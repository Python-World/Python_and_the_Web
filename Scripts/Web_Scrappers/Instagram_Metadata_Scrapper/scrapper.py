import json
import pprint
import requests

from bs4 import BeautifulSoup
from faker import Faker

def get_metadata(username):
    """"""
    try:
        url = 'https://www.instagram.com/{username}/'.format(username=username)
        res=requests.get(url,
                         headers={'User-Agent':Faker().user_agent() },
                         allow_redirects=True)

        if res.status_code == 404 :
            return {"error" : "user not found"}

        soup = BeautifulSoup(res.text, 'html.parser')
        ret_data = json.loads([sc.text for sc in soup.find_all('script')\
                               if 'csrf_token' in str(sc)][0].replace\
                                   ("window._sharedData = ","").replace(";",""))\
                                    ['entry_data']['ProfilePage'][0]['graphql']

        if 'user' in ret_data.keys():
            return {
                "username" : ret_data['user'].get('username', None),
                "profile_picture_url": ret_data['user'].get('profile_pic_url_hd', None),
                "follower_count": ret_data['user'].get('edge_followed_by', {}).get('count',None),
                "media_count": ret_data['user'].get('edge_owner_to_timeline_media', {}).get('count',0),
                "follows_count": ret_data['user'].get('edge_follow',{}).get('count',None)
            }
        return {"error" : "problem getting the data , please try again"}

    except :
        return {"error": "internal error"}
pprint.pprint(get_metadata("tomhardy"))
