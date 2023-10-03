import logging

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

logging.basicConfig(level=logging.WARNING)
import telegram
from piratebay import pirate


def get_quote(search):
    data = pirate(search)
    name = data[0]["name"]
    if name == "No results returned":
        return "Sorry I Couldn't Find It...😔\n Try Searching Something Else 🙂 "

    size = data[0]["size"]
    seeders = data[0]["seeders"]
    leechers = data[0]["leechers"]
    magnetlink = data[0]["magnetlink"]

    message = f"{name} \n**Size:** {size} \n**Seeders:** {seeders} \n**Leechers:** {leechers} \nMagnet Link:\n```{magnetlink}```"

    return message


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command.😔",
    )


def quote(update, context):
    update.message.chat_id
    if update.message:
        query = update.message.text
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            parse_mode=telegram.ParseMode.MARKDOWN,
            text=str(get_quote(query)),
        )


def start(update, context):
    inf = context.bot.get_chat_member(
        chat_id="-g370152138", user_id=update.message.chat_id
    )
    user = inf["user"]
    first_name = user["first_name"]
    last_name = user["last_name"]
    if last_name is None:
        last_name = " "
    name = f"Hi! {first_name} {last_name} "
    context.bot.send_message(chat_id=update.effective_chat.id, text=name)

    welcome = """
Hi I'm Torrent Search Bot

Send /help for Help 

Made With ❤️ In India By @Apex-code

"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome)
    user = context.bot.get_chat_member(
        chat_id="-g370152138", user_id=update.message.chat_id
    )


def help(update, context):
    helpmessage = """
Send Me Any Movie, Game, Song Name 

I'll Send You A Magnet Link based On Your Query

For Example : "Infinity War" , "Avatar" , "Joker" 😁 

Type

/help to Get this Message 

/donate To Donate Me (Not Added)

If Any Issues Contact : @Apex-code

"""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=helpmessage
    )


def donate(update, context):
    donate = """
Donate Feature Haven't Added Yet 

If You Want to Donate 
Contact Me :
    Telegram : @Apex-code
"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=donate)


def main():
    updater = Updater("BOT_TOKEN", use_context=True)
    dp = updater.dispatcher
    start_handler = CommandHandler("start", start)
    dp.add_handler(start_handler)

    help_handler = CommandHandler("help", help)
    dp.add_handler(help_handler)

    donate_handler = CommandHandler("donate", donate)
    dp.add_handler(donate_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dp.add_handler(unknown_handler)

    quote_msg = MessageHandler(Filters.text, quote)
    dp.add_handler(quote_msg)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
