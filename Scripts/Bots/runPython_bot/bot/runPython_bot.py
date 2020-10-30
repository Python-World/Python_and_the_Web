'''
I'm the *Python Runner* bot 😀 

I have been created by Aahnik Daw and you may see my [source code](http://bit.ly/runPython) on GitHub.

I am currently *alive and kicking* on a free tier server of Python Anywhere.

😁 Sometimes I behave quite differently from a regular python interactive shell. 
Certain things are not allowed to prevent horrible consequences.

_Start using me to figure out more about me_.

Every message is executed freshly. Suppose you define a variable in one message, you wont be able to access it in the next message.

But you can write _multiline code in one message_
->Tab is 4 spaces
-> Newline is a newline in the same message body

If I am being used by too many people, there may be delay in response as I am deployed on a free tier server.
'''

# the module docstring will be sent to the user if the bot is alive

from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from .execute_code import run

with open('token.txt') as f:
    tok = f.readline().strip()


def bot():
    updater = Updater(token=tok)

    dispatcher = updater.dispatcher

    def start(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f'{__doc__}\n', parse_mode='Markdown')

    def reply(update, context):
        returned_val = run(update)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=returned_val)

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(Filters.text & (~Filters.command), reply)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
