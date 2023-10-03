import urllib.request

import praw

# An app will need to be registered with reddit under https://www.reddit.com/prefs/apps
reddit = praw.Reddit(
    client_id="clientid",
    client_secret="secret",  # recommended user agent format: platform:id:version
    user_agent="useragent",
    username="username",
    password="password",
)


# Define subreddit
subreddit = reddit.subreddit("wallpapers")

# Loop through the first 5 posts sorted by 'hot'
for submission in subreddit.hot(limit=5):
    # Get the url of the post
    url = submission.url
    # Define the filename
    filename = submission.title + ".jpg"
    # Save the image
    urllib.request.urlretrieve(url, filename)
