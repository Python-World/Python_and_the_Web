import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=Instagram Bot',
    '-F',
    '--icon=IG_bot_logo.ico',
    'Instagram_bot.py',
])
