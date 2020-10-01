from twython import Twython
from twython import TwythonStreamer
class MyStreamer(TwythonStreamer):
	def on_success(self, data):
		if 'text' in data:
			a=data['text'].lower()
			username=data['user']['screen_name']
			id=data['id']
			st.create_favorite(id=id)
      #change 'nice tweet' too your desired retweet reply
			st.update_status(status='Nice Tweet @'+username, in_reply_to_status_id=id)
#enter your unique keys and tokens
api_k='*'               
api_secret_k='*'
access_t='*'
access_secret_t='*'
api=MyStreamer(api_k,api_secret_k,access_t,access_secret_t)
st=Twython(api_k,api_secret_k,access_t,access_secret_t)

keyword=input("Enter keyword to track: ")
api.statuses.filter(track=keyword)
