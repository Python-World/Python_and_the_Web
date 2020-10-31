# runPython_bot

Run python code from your telegram chat !

[![GitHub license](https://img.shields.io/github/license/aahnik/lovely-telegram)](https://github.com/aahnik/lovely-telegram/blob/main/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance Yes](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://gitHub.com/aahnik/REPO/graphs/commit-activity)

![RunPythonBot](https://user-images.githubusercontent.com/66209958/97750350-9d773d80-1b16-11eb-89a5-7626f5547a10.png)

<!-- A simple bot that runs python code. Free and Open Source. For more info visit http://bit.ly/runPython -->

## Find on Telegram

You can find this bot on Telegram: click on this [link](https://t.me/@runPython_bot) or search `@runPython_bot` on telegram. The spelling is case sensitive.

This bot is deployed on [Python Anywhere](https://www.pythonanywhere.com/) free Beginner Account.
You may check whether the bot is alive or not, by clicking on the start command. If the bot responds, it is alive.

## Example Use

You may use pythonic expressions to easily calculate any complex problem. Or you may test your algorithms on the go.

> If you are viewing from a smartphone, click on the gif to view full screen ...

![runPython_bot](https://user-images.githubusercontent.com/66209958/97753037-1e383880-1b1b-11eb-863e-bcf82006820b.gif)

## Deploy

You can easily *deploy this bot* on [Python Anywhere](https://www.pythonanywhere.com/) or your **local machine** by following the below steps:

> Note: While pasting on your machine terminal you should use `Ctrl+Shift+V` but make sure to use `Ctrl+V` to paste in the Python Anywhere bash console from the browser.

Create a free Python Anywhere account and open a Bash Console, which has everything pre-loaded.

If you are planning to deploy on your **own machine**, make sure to have `Python3+`, `pip`, and `make`.

The following instructions will work smoothly on *Linux* and *Mac*. If you are on Windows, you may have to make slight modifications. Google is your best friend here.

- Create a `projects` directory and move into it

      mkdir projects && cd projects

- Clone this repository containing the collection of bots
  
      git clone https://github.com/aahnik/lovely-telegram.git

- Delete all other folders except the folder containing this bot
  
      find ./lovely-telegram -mindepth 1 ! -regex '^./lovely-telegram/runPython_bot\(/.*\)?' -delete

- Now move into the directory which contains this README file, you are reading now.

      cd lovely-telegram/runPython_bot

- Now add the token in the first line of `token.txt`.Run `cat > token.txt` -> Paste the token -> Press `Ctrl+D`

- To install all dependencies. Simply run `make requirements`

- Activate the bot by running `make start`

- You may now close the Python Anywhere bash console window from your browser, but the bot will continue running.

Your bot is now up and running, Enjoy ! 😊

To stop the bot, Press `Ctrl+C`. To restart the bot run `make start`

## Limitations

Currently, the bot is deployed on a Free Tier account of Python Anywhere.

For security and performance reasons, you **cannot** do the following with the bot:

- import any package
- run the `input()` function
- run the `open()` function
- Execute a piece of code which takes longer than 30 seconds to execute.

You may overcome these limitations by tweaking the code a little bit and running the bot on your own server.

## The Shameless Plug

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
