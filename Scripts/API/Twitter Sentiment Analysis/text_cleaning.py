import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def remove_stop_words(sentence):
    # Define stop words
    stop_words = set(stopwords.words("english"))

    # Tokenize sentences
    word_tokens = word_tokenize(sentence)

    # remove stop words from the tokens
    filtered_sentence = [w for w in word_tokens if w not in stop_words]

    sentence = " ".join(filtered_sentence)
    return sentence


def clean_tweets(tweets):
    # remove url
    no_url_tweets = [re.sub(r"http\S+", "", t) for t in tweets]

    # remove stop words
    clean_tweets = [remove_stop_words(t) for t in no_url_tweets]

    # remove punctuation signs
    clean_tweets = [re.sub(r"[^\w\s]", "", t) for t in clean_tweets]

    return clean_tweets
