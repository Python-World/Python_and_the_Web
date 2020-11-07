# run-py-bot

Run python code from your telegram chat!

[![GitHub license](https://img.shields.io/github/license/aahnik/lovely-telegram)](https://github.com/aahnik/run-py-bot/blob/main/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance Yes](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://gitHub.com/aahnik/REPO/graphs/commit-activity)

![RunPythonBot](https://github.com/aahnik/run-py-bot/blob/main/docs/images/runPython_bot.png?raw=true)

<!-- A simple bot that runs python code. Free and Open Source. For more info visit http://bit.ly/runPython -->

## 🕵️ Find on Telegram

You can find this bot on Telegram as [@runPython_bot](https://telegram.me/runPython_bot).

This bot is deployed on [Python Anywhere](https://www.pythonanywhere.com/) free Beginner Account.
You may check whether the bot is alive or not, by clicking on the start command. If the bot responds, it is alive.

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

- Clone this repository and move into it.

      git clone https://github.com/aahnik/run-py-bot.git && cd run-py-bot

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

## 🤗 The Shameless Plug

Authored by **Aahnik Daw**.

You may connect with me by clicking on any of the icons below !

<a href = "https://medium.com/@aahnikdaw" > <img src = "https://github.com/aahnik/aahnik/blob/master/social_media_logos/medium.png?raw=true" alt = "medium" > </a >
<a href = "https://www.facebook.com/aahnik.daw" > <img src = "https://github.com/aahnik/aahnik/blob/master/social_media_logos/facebook.png?raw=true" alt = "facebook" > </a >
<a href = "https://www.linkedin.com/in/aahnik-daw-067a011b3/" > <img src = "https://github.com/aahnik/aahnik/blob/master/social_media_logos/linkedin.png?raw=true" alt = "linkedin" > </a >
<a href = "https://t.me/AahniKDaw" > <img src = "https://github.com/aahnik/aahnik/blob/master/social_media_logos/telegram.png?raw=true" alt = "telegram" > </a >
<a href = "https://twitter.com/AahnikD" > <img src = "https://github.com/aahnik/aahnik/blob/master/social_media_logos/twitter.png?raw=true" alt = "twitter" > </a >
<a href = "https://www.quora.com/profile/Aahnik-Daw" > <img src = "https://github.com/aahnik/aahnik/blob/master/social_media_logos/quora.png?raw=true" alt = "quora" > </a >
<a href = "https://www.youtube.com/channel/UCcEbN0d8iLTB6ZWBE_IDugg" > <img src = "https://github.com/aahnik/aahnik/blob/master/social_media_logos/youtube.png?raw=true" alt = "youtube" > </a >
<a href = "https://stackoverflow.com/users/13523305/aahnik-daw" > <img src = "https://github.com/aahnik/aahnik/blob/master/social_media_logos/stackOverflow.png?raw=true" alt = "stackOverflow" > </a >
<a href = "https://dev.to/aahnik" > <img src = "https://github.com/aahnik/aahnik/blob/master/social_media_logos/dev.png?raw=true" alt = "dev" > </a >
