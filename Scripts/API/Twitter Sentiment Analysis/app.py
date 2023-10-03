import btm_model
import requests
import sentiment
import text_cleaning
from flask import Flask, redirect, render_template, url_for
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter

app = Flask(__name__)
app.config["SECRET_KEY"] = "youareawesomethiscanbeanything"

twitter_blueprint = make_twitter_blueprint(api_key="", api_secret="")

app.register_blueprint(twitter_blueprint, url_prefix="/login")


@app.route("/")
def index():
    # Home page
    # If the user is not authorized, redirect to the twitter login page
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    return redirect("http://127.0.0.1:5000/twitter")


@app.route("/twitter")
def twitter_login():
    # If the user is not authorized, redirect to the twitter login page
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    # If user is authorized retrieve his/her account details
    account_info = twitter.get("account/settings.json")
    # If user is authorized retrieve his/her tweets
    user_tweets = twitter.get("statuses/user_timeline.json")

    # If account information is successfully retrieved, proceed to analyse and display it
    if account_info.ok:
        # Convert retrieved info to json format
        user_tweets_json = user_tweets.json()
        account_info_json = account_info.json()

        # Get tweet text from the objects returned
        all_tweets = []
        print(account_info_json)
        for tweet in user_tweets_json:
            all_tweets.append(tweet["text"])

        # Text Cleaning for tweets
        all_tweets_cleaned = text_cleaning.clean_tweets(all_tweets)

        # BTM model for topic modeling results
        classified_tweets, topics = btm_model.categorize(all_tweets_cleaned)

        # Sentiment analysis
        tweet_sentiment = sentiment.get_sentiment(all_tweets_cleaned)

        # Prepare data to be sent and rendered on the template for user dashboard
        data = {
            "all_tweets": all_tweets,
            "account_info_json": account_info_json,
            "classified_tweets": classified_tweets,
            "topics": topics,
            "sentiment": tweet_sentiment,
        }

        # Render template with user data
        return render_template("user_dash.html", data=data)

    # If account info is not retrieved successfully return an error message.
    return "<h2>Error</h2>"


if __name__ == "__main__":
    app.run(debug=True)
