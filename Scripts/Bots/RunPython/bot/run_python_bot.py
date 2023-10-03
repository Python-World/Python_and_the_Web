"""
This module makes the bot actually run
"""

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from .execute_code import eval_py, run

# python-telegram-bot is a Pythonic Wrapper to the core Telegram API
# it helps us to be DRY by giving us convinient wrapper functions to deal with Telegram API
# you can install it by pip install python-telegram-bot --upgrade
# learn more about it here https://github.com/python-telegram-bot/python-telegram-bot


# read the token for authenticating our bot
with open("token.txt") as f:
    tok = f.readline().strip()

with open("docs/start.txt") as f:
    start_text = f.read()

with open("docs/help.txt") as f:
    help_text = f.read()

with open("docs/code.txt") as f:
    code_text = f.read()


def handle_long_message(msg):
    """Telegram does not support messages over 4096 characters.
    This handler handles all messages above 2000 characters
    """

    if msg:
        if len(msg) > 2000:
            return (
                msg[:2000]
                + "\n\n 😟 Output was too long, truncated to 2000 characters"
            )
        return msg
    return "handle_long_message recieved an empty message"


def bot():
    """
    Running this function runs the bot
    You may learn more from this tutorial
    https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
    """

    updater = Updater(token=tok)

    dispatcher = updater.dispatcher

    def start(update, context):
        """This fuction replies to the start command"""

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=start_text,
            parse_mode="Markdown",
        )
        # for more info on parse modes
        # see https://python-telegram-bot.readthedocs.io/en/stable/telegram.parsemode.html

    def bot_help(update, context):
        """This function replies to the help command"""
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=help_text,
            parse_mode="Markdown",
        )

    def code_info(update, context):
        """This function replies to the code command."""
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=code_text,
            parse_mode="Markdown",
        )

    def reply_execute(update, context):
        """
        This function replies to any non-command messages.
        """
        input_text = str(update.message.text)
        # allowing usage of /e at the end of expressions

        if input_text == "hi":
            user = update.message.from_user
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f'Hi! {user["username"]} 🥰',
            )

        if input_text.endswith("/e"):
            message = handle_long_message(eval_py(input_text.strip("/e")))
            update.message.reply_text(message, quote=True)
        else:
            returned_val = run(update)
            if not returned_val:
                update.message.reply_text(
                    """*No output. No error.*
                    \n> Try using a `print` statement.
                    \n > To evaluate an expression use the /e command.""",
                    quote=True,
                    parse_mode="Markdown",
                )
            else:
                message = handle_long_message(returned_val)
                update.message.reply_text(message, quote=True)

    def reply_eval(update, context):
        """This function handles the /e command"""
        if context.args:
            input_text = ""
            for string in context.args:
                input_text += string + " "
            out = eval_py(input_text)
            message = handle_long_message(out)
            update.message.reply_text(message, quote=True)
        else:
            update.message.reply_text(
                """*No expression provided to eval*.
                \nUse command /e before or after your expression like
                \n/e `4 >= 5` \n \t or \n`4 >= 5` /e """,
                quote=True,
                parse_mode="Markdown",
            )

    _handlers = {}

    _handlers["start_handler"] = CommandHandler("start", start)
    _handlers["help_handler"] = CommandHandler("help", bot_help)
    _handlers["code_info_handler"] = CommandHandler("code", code_info)
    _handlers["message_handler"] = MessageHandler(
        Filters.text & (~Filters.command), reply_execute
    )
    _handlers["eval_handler"] = CommandHandler("e", reply_eval)

    for name, _handler in _handlers.items():
        print(f"Adding {name}")
        dispatcher.add_handler(_handler)

    updater.start_polling()
    updater.idle()
    # Search google to know what is polling...
    # i came to know while building this project
    # this can be stopped by interrupting the terminal by `Ctrl+C`
