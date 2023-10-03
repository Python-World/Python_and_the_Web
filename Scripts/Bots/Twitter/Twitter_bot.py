import configparser

from twython import Twython, TwythonStreamer


class MyStreamer(TwythonStreamer):
    @staticmethod
    def on_success(data):
        if "text" in data:
            data["text"].lower()
            username = data["user"]["screen_name"]
            id = data["id"]
            st.create_favorite(id=id)
            # change 'nice tweet' too your desired retweet reply
            st.update_status(
                status="Nice Tweet @" + username, in_reply_to_status_id=id
            )
            print("https://twitter.com/" + username + "/status/" + str(id))


# enter your unique keys and tokens in config file
config = configparser.ConfigParser()
config.read("config.ini")

api_key = config["keys"]["api_key"]
api_secret_key = config["keys"]["api_secret_key"]
access_token = config["keys"]["access_token"]
access_secret_token = config["keys"]["access_secret_token"]

api = MyStreamer(api_key, api_secret_key, access_token, access_secret_token)
st = Twython(api_key, api_secret_key, access_token, access_secret_token)

keyword = input("Enter keyword to track: ")
api.statuses.filter(track=keyword)
