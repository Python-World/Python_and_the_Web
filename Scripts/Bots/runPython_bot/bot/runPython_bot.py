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
# python-telegram-bot is a Pythonic Wrapper to the core Telegram API
# it helps us to be DRY by giving us convinient wrapper functions to deal with Telegram API
# you can install it by pip install python-telegram-bot --upgrade
# learn more about it here https://github.com/python-telegram-bot/python-telegram-bot


from .execute_code import run

# read the token for authenticating our bot
with open('token.txt') as f:
    tok = f.readline().strip()


def bot():
    '''
    Running this function runs the bot
    You may learn more from this tutorial 
    https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
    '''

    updater = Updater(token=tok)

    dispatcher = updater.dispatcher

    def start(update, context):
        '''
        This fuction replies to the start command
        '''

        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f'{__doc__}\n', parse_mode='Markdown')
        # for more info on parse modes see https://python-telegram-bot.readthedocs.io/en/stable/telegram.parsemode.html

    def reply(update, context):
        '''
        This function replies to any non-command messages
        '''
        returned_val = run(update)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=returned_val)

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(Filters.text & (~Filters.command), reply)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    # Search google to know what is polling... 
    # i came to know while building this project
    # this can be stopped by interrupting the terminal by `Ctrl+C`
