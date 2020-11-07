'''
Configs for the bot
'''

# expressions which are banned
banned = ['quit', 'input', 'open', 'import', 'exit']

# timeout in seconds
TIMEOUT = 6

timeout_message = f'''😢 Timeout of {TIMEOUT} reached.
I have limited resources. 
You may increase the timeout and run this bot on your own server if required.'''

restricted_message = f'☹️ SECURITY ISSUE:\nYou have used a restricted word \n{banned}'
