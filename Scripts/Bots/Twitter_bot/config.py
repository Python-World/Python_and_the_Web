from twython import Twython
from twython import TwythonStreamer
class MyStreamer(TwythonStreamer):
	def on_success(self, data):
		if 'text' in data:
			a=data['text'].lower()
			username=data['user']['screen_name']
			id=data['id']
			st.create_favorite(id=id)
			st.update_status(status='Nice Tweet @'+username, in_reply_to_status_id=id)
			print("https://twitter.com/"+ username +"/status/" + str(id))

api_k='LpkBnMbu7KQ85UybUdbiWbpG7'
api_secret_k='l5CdR5l1SCm4H0Ga6PmYRTeyjNF1RlsUZHbkv3UefnkgAlockL'
access_t='1271406017889185793-BEoLPylWQ1h0yYhfwhaV5qDsJVvY0P'
access_secret_t='cd7Q902F40qbGlB17YB55GAuJJ4otFHFrFM0cFyo9tpi6'
api=MyStreamer(api_k,api_secret_k,access_t,access_secret_t)
st=Twython(api_k,api_secret_k,access_t,access_secret_t)
keyword=input("Enter keyword to track: ")
api.statuses.filter(track=keyword)
