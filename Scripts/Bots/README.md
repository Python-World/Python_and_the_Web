## Python script for sending Telegram Messages ; ) 

## Initial Steps:

(1) First of all, create a bot using Telegram BotFather. To create a BotFather follow the below steps –

Open the telegram app and search for @BotFather.
* Click on the start button or send “/start”.
* Then send “/newbot” message to set up a name and a username.
* After setting name and username BotFather will give you an API token which is your bot token.

(2) Then create an app on the telegram. Follow the below steps –
* Log into the telegram core: https://my.telegram.org
* Go to ‘API development tools’ and fill out the form.
* You will get the api_id and api_hash parameters required for user authorization.

## Python modules (must) : 
* telebot: `pip3 install telebot`
* telethon: `pip3 install telethon`

Or, simply run `pip3 install -r requirements.txt`

## Script execution :

`python3 telegram_bot.py`
