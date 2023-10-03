import re
import sys

import tweepy
import xlwt
import yaml
from textblob import TextBlob
from tweepy import OAuthHandler


class TwitterClient:
    def __init__(self):
        """
        Class constructor: Authentication via twitter API keys
        """
        with open(r"credentials.yaml") as file:
            cred = yaml.load(file, Loader=yaml.FullLoader)

        consumer_key = cred["consumer_key"]
        consumer_secret = cred["consumer_secret"]
        access_token = cred["access_token"]
        access_token_secret = cred["access_token_secret"]

        # attempting authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    @staticmethod
    def clean_tweet(tweet):
        """
        Removing links/special characters to clean up tweet
        """
        return " ".join(
            re.sub(
                "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\ / \ / \S+)  ",
                " ",
                tweet,
            ).split()
        )

    def get_tweet_sentiment(self, tweet):
        """
        Classifying tweet as Positive/Negative/Neutral using textblob's sentiment function
        """
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return "positive"
        if analysis.sentiment.polarity == 0:
            return "neutral"
        return "negative"

    def get_tweets(self, hashtag):
        """
        Fetching & parsing 500 tweets based on hashtag
        """
        all_tweets = []
        search_words = hashtag

        try:
            tweets = tweepy.Cursor(
                self.api.search, q=search_words, lang="en", result="recent"
            ).items(500)
            for tweet in tweets:
                all_tweets.append(tweet.text)

            return all_tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))


def main():
    api = TwitterClient()
    hashtag = sys.argv[1]
    all_tweets = api.get_tweets(hashtag)

    # creating dictionary of tweet + sentiment
    wb = xlwt.Workbook(encoding="utf-8")
    style_head = xlwt.easyxf(
        "pattern: fore_colour green; font: colour black, bold True;align: wrap yes; align: horiz center"
    )
    style_rows = xlwt.easyxf("align: wrap yes; align: horiz center")
    sheet = wb.add_sheet("Analysed Tweets")
    sheet.col(0).width = 256 * 50
    sheet.col(1).width = 256 * 20
    sheet.write(0, 0, "TWEET", style_head)
    sheet.write(0, 1, "CLASSIFICATION", style_head)

    for i in range(0, len(all_tweets)):
        sheet.write((i + 1), 0, all_tweets[i], style_rows)
        sheet.write(
            (i + 1), 1, api.get_tweet_sentiment(all_tweets[i]), style_rows
        )

    wb.save("Sentiment_Analysis.xls")


if __name__ == "__main__":
    main()
