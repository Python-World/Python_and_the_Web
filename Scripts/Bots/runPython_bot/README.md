# run-py-bot

Run python code from your telegram chat!

[![GitHub license](https://img.shields.io/github/license/aahnik/run-py-bot)](https://github.com/aahnik/run-py-bot/blob/main/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance Yes](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://gitHub.com/aahnik/REPO/graphs/commit-activity)

![RunPythonBot](https://github.com/aahnik/run-py-bot/blob/main/docs/images/runPython_bot.png?raw=true)

<!-- A simple bot that runs python code. Free and Open Source. For more info visit http://bit.ly/runPython -->

## 🕵️ Find on Telegram

You can find this bot on Telegram as [@runPython_bot](https://telegram.me/runPython_bot). 
Note: I am constantly learning new concepts and I may update the source code running behind the bot. 

Here is the [link to the repo](https://github.com/aahnik/run-py-bot) which has the latest source for this bot. ![GitHub forks](https://img.shields.io/github/forks/aahnik/run-py-bot?style=social) ![GitHub Repo stars](https://img.shields.io/github/stars/aahnik/run-py-bot?style=social)


## 😍 Featured in 

1. Tweet by [Dev Community](https://twitter.com/ThePracticalDev/status/1325386583537803264)
2. Tweet by [The Python Dev](https://twitter.com/The_Python_DEV/status/1325237102058016768)
3. Dor Moshe's [Newsletter](https://dormoshe.io/newsletters/ag/python/7?utm_source=twitter&utm_campaign=twitter)
4. My YouTube [Video](https://youtu.be/nCuQ-7Rw0gM) [![YouTube Video Views](https://img.shields.io/youtube/views/nCuQ-7Rw0gM?style=social)](https://youtu.be/nCuQ-7Rw0gM)

## 💬 Example Use

You may use pythonic expressions to easily calculate any complex problem. Or you may test your algorithms on the go.

> If you are viewing from a smartphone, click on the gif to view full screen ...

![runPython_bot](https://github.com/aahnik/run-py-bot/blob/main/docs/images/runPython_bot_gif.gif?raw=true)

## ⚡ Deploy

You can easily *deploy this bot* on [Python Anywhere](https://www.pythonanywhere.com/) or your **local machine** by following the below steps:

> Note: While pasting on your machine terminal you should use `Ctrl+Shift+V` but make sure to use `Ctrl+V` to paste in the Python Anywhere bash console from the browser.

Create a free Python Anywhere account and open a Bash Console, which has everything pre-loaded.

If you are planning to deploy on your **own machine**, make sure to have `Python3+`, `pip`.

The following instructions will work smoothly on *Linux* and *Mac*. If you are on Windows, you may have to make slight modifications. Google is your best friend here.

- Clone this repository and move into this directory which has this README you are reading.
```
git clone https://github.com/Python-World/Python_and_the_Web.git && cd Scripts/Bots/runPython_bot
```

- Now add the token in the first line of `token.txt`.Run `cat > token.txt` -> Paste the token -> Press `Ctrl+D`

- Create a virtual environment and install dependencies.

      python3.8 -m venv venv && source venv/bin/activate
      python3.8 -m pip install -r requirements.txt

- Activate the bot by running `python3.8 start.py`

- You may now close the Python Anywhere bash console window from your browser, but the bot will continue running.

Your bot is now up and running, Enjoy ! 😊

All the logs will have the timestamp in the time-zone specified in the `start.py` file.

To stop the bot, press `Ctrl+C`. You may update the code running in your server by `git fetch && git pull`.

## 😑 Limitations

Currently, the bot is deployed on a Free Tier account of Python Anywhere.

For security and performance reasons, you **cannot** do the following with the bot:

- import any package
- run the `input()` function
- run the `open()` function
- Execute a piece of code which takes longer than *6 seconds* to execute.

You may overcome these limitations by changing the `config.py` file in the `bot` subdirectory and running the bot on your own server.

As I am constantly learning new concepts, the [latest version](https://github.com/aahnik/run-py-bot) of this bot will not have these limitations.

## 🤗 The Shameless Plug

Authored by **Aahnik Daw**.

You may click on any of the icons below to connect with me.

<a href = "https://twitter.com/AahnikD" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/twitter.svg?raw=true" alt = "twitter" width=35> </a>
<a href = "https://medium.com/@aahnik" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/medium.svg?raw=true" alt = "medium" width=35> </a>
<a href = "https://www.facebook.com/aahnik.daw" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/facebook.svg?raw=true" alt = "facebook" width=35> </a>
<a href = "https://www.linkedin.com/in/aahnik-daw-067a011b3/" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/linkedin.svg?raw=true" alt = "linkedin" width=35> </a>
<a href = "https://dev.to/aahnik" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/dev_to.svg?raw=true" alt = "dev_to" width=35> </a>
<a href = "https://stackoverflow.com/users/13523305/aahnik-daw" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/stackoverflow.svg?raw=true" alt = "stackoverflow" width=35> </a>
<a href = "https://telegram.me/AahnikD" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/telegram.svg?raw=true" alt = "telegram" width=35> </a>
<a href = "https://www.youtube.com/channel/UCcEbN0d8iLTB6ZWBE_IDugg" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/youtube.svg?raw=true" alt = "youtube" width=35> </a>
