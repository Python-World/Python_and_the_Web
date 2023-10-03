#! /usr/bin/env python

import time
import tweepy
import sys

# Replace the foo bar with your twitter API keys from dev.twitter.com
auth = tweepy.auth.OAuthHandler(consumer_key="foo", consumer_secret="bar")
auth.set_access_token("foo", "bar")

# the following dictionaries etc aren't strictly needed for this
# but useful for your own more in-depth apps.

api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True)

print("Loading followers..")
followers = []
for follower in tweepy.Cursor(api.followers).items():
    followers.append(follower)

print("Found %s followers, finding friends.." % len(followers))
friends = []
for friend in tweepy.Cursor(api.friends).items():
    friends.append(friend)

# creating dictionaries based on id's is handy too

friend_dict = {}
for friend in friends:
    friend_dict[friend.id] = friend

follower_dict = {}
for follower in followers:
    follower_dict[follower.id] = follower

# now we find all your "non_friends" - people who don't follow you
# even though you follow them.

non_friends = [friend for friend in friends if friend.id not in follower_dict]

# double check, since this could be a rather traumatic operation.

print("Unfollowing %s non-following users.." % len(non_friends))
print("This will take approximately %s minutes." % (len(non_friends) / 60.0))
answer = input("Are you sure? [Y/n]").lower()
if answer and answer[0] != "y":
    sys.exit(1)

for nf in non_friends:
    print("Unfollowing " + str(nf.id).rjust(10))
    try:
        nf.unfollow()
    except Exception:
        print("  .. failed, sleeping for 5 seconds and then trying again.")
        time.sleep(5)
        nf.unfollow()
    print(" .. completed, sleeping for 1 second.")
    time.sleep(1)
