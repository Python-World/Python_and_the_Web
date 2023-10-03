from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_sentiment(tweets):
    # define the analyser object
    analyser = SentimentIntensityAnalyzer()
    sentiment = []

    for t in tweets:
        # get polairty score for each tweet.
        # sentiment_dict will have various scores for pos, neg, neu, and a compound score(-1 to 1)
        sentiment_dict = analyser.polarity_scores(t)

        # Considering compound score for determining tweet sentiment
        if sentiment_dict["compound"] >= 0.05:
            sentiment.append("Positive")

        elif sentiment_dict["compound"] <= -0.05:
            sentiment.append("Negative")

        else:
            sentiment.append("Neutral")

    return sentiment
