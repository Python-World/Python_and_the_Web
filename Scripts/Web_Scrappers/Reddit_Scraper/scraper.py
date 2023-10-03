import sys

import config
import pandas as pd
import praw

# Too many arguments
if len(sys.argv) > 3:
    print(
        "Too many arguments. EXAMPLE: % python3 scraper.py {NAME OF SUBREDDIT} {WAY TO SORT}"
    )

elif len(sys.argv) > 2:
    # Create reddit object
    reddit = praw.Reddit(
        client_id=config.client_id,
        client_secret=config.client_secret,
        user_agent=config.user_agent,
        username=config.username,
        password=config.password,
    )

    # Create subreddit object
    sub = reddit.subreddit(sys.argv[1])
    posts = []

    # Ways to sort
    if sys.argv[2] == "hot":
        posts = sub.hot(limit=10)
    elif sys.argv[2] == "new":
        posts = sub.new(limit=10)
    elif sys.argv[2] == "top":
        posts = sub.top(limit=10)
    elif sys.argv[2] == "controversial":
        posts = sub.controversial(limit=10)
    elif sys.argv[2] == "rising":
        posts = sub.rising(limit=10)
    else:
        sys.exit(
            "This way to sort does not exist! Please input hot, new, top, controversial, or rising."
        )

    # Dictionary of results
    results = {"Title": [], "URL": [], "Score": []}

    # Append to dictionary
    for result in posts:
        results["Title"].append(result.title)
        results["URL"].append(result.url)
        results["Score"].append(result.score)

    # Create data frame
    results_data = pd.DataFrame(results)

    # Export results to a csv file
    results_data.to_csv(f"{sub}_{sys.argv[2]}_results.csv", index=True)

    print(results_data)

# No way to sort
elif len(sys.argv) > 1:
    print("Input a way to sort!")

# No subreddit
elif len(sys.argv) > 0:
    print("Input a subreddit!")
