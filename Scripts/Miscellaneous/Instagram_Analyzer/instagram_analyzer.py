import sys

import matplotlib.pyplot as plt
import numpy as np
from instagramy import InstagramUser

try:
    filename = sys.argv[1]
    print("Extracting...")
except (IndexError, KeyError):
    print("List of username as textfile in argvment")
    sys.exit()

usernames = []
file = open(filename, "r")
for line in file:
    if line != "\n":
        usernames.append(str(line).strip())
followers = []
following = []
posts = []

for username in usernames:
    user = InstagramUser(username)
    followers.append(user.number_of_followers)
    following.append(user.number_of_followings)
    posts.append(user.number_of_posts)

x = np.arange(len(usernames))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x + 0.2, followers, width, label="Followers")
rects2 = ax.bar(x, following, width, label="Following")
rects3 = ax.bar(x - 0.2, posts, width, label="Posts")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Popularity")
ax.yaxis.set_visible(True)
ax.set_title("Username")
ax.set_xticks(x)
ax.set_xticklabels(usernames)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
fig.tight_layout()
plt.show()
