## Twitter Sentiment Analyis

### This script fetches 500 most recent tweets based on a single hashtag input, classifies the tweets based on sentiment polarity of either 'Positive', 'Negative' or 'Neutral' and writes the output to a .xls script.

### Pre-requisites

This script uses the twitter API called tweepy. For this you will require a set of access token and consumer keys. Following steps show you how to obtain these credentials:
– Login to twitter developer section
– Go to “Create an App”
– Fill the details of the application.
– Click on Create your Twitter Application
– Details of your new app will be shown along with consumer key and consumer secret.
– Click on "Create my access token" to obtain access token.

### How to use this script?

1. Make sure all the requirements for the script are present in your system by running:

    pip install -r requirements.txt
    
2. Enter the following values in 'credentials.yaml' based on access/consumer tokens obtained above:
- consumer_key
- consumer_secret
- access_token
- access_token_secret

3. Run the following command (replace #hashtag with # of your choice):

    python twitter_sentiment_analysis.py #hashtag

3. Open Sentiment_Analysis.xls to see analysed and categorised tweets

### Author

[Schezeen Fazulbhoy](https://github.com/schezfaz)