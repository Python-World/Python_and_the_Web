import time

from dhooks import Embed, Webhook
from inshorts import getNews

"""
Steps to Get Discord Channel WebHook
1. Go to your server
2. Select A channel
3. Right Click then Edit Channel
4. Select integration
5. and Create a new Webhook
6. Copy the webhook url and paste it below to url
7. IMPORTANT STEP: don't forget to change the url from 'https://discordapp.com/api/webhooks/76182371...' to 'https://discord.com/api/webhooks/76182371'
remove the app part from discord webhook url
"""

url = "YOUR WEB HOOK URL"


hook = Webhook(url)

newz = getNews("")

hook.send("**News Briefing**")

for bits in newz["data"]:
    newsTitle = bits["title"]
    newsContent = bits["content"]
    imageUrl = bits["imageUrl"]
    newsAuthor = bits["author"]
    newsReadmore = bits["readMoreUrl"]

    embed = Embed(
        title=newsTitle,
        url=newsReadmore,
        description=newsContent,
        color=0x5CDBF0,
        timestamp="now",
    )
    image1 = imageUrl
    embed.set_image(image1)
    embed.set_footer(text=newsAuthor)

    hook.send(embed=embed)
    time.sleep(2)

hook.send("**News Briefing Completed**")
