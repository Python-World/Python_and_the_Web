import numpy as np
from biterm.biterm.btm import oBTM
from biterm.biterm.utility import topic_summuary, vec_to_biterms
from sklearn.feature_extraction.text import CountVectorizer


def categorize(tweets_list, number_of_topics=3):
    # vectorize texts
    vec = CountVectorizer(stop_words="english")
    X = vec.fit_transform(tweets_list).toarray()

    # get vocabulary
    vocab = np.array(vec.get_feature_names())

    # get biterms
    biterms = vec_to_biterms(X)

    # create btm
    btm = oBTM(num_topics=number_of_topics, V=vocab)

    # print("\n\n Train Online BTM ..")
    for i in range(0, len(biterms), 100):  # prozess chunk of 200 texts
        biterms_chunk = biterms[i : i + 100]
        btm.fit(biterms_chunk, iterations=50)
    topics = btm.transform(biterms)

    # print("\n\n Topic coherence ..")
    res = topic_summuary(btm.phi_wz.T, X, vocab, 6)

    topics_top_words = res["top_words"]

    topic_classification = []

    # print("\n\n Texts & Topics ..")
    for i in range(len(tweets_list)):
        # print("{} (topic: {})".format(tweets_list[i], topics[i].argmax()))
        topic_classification.append(topics[i].argmax())

    # print(type(topics))

    return topic_classification, topics_top_words
