import PyInstaller.__main__

PyInstaller.__main__.run(
    [
        "--name=Instagram Bot",
        "-F",
        "--icon=favicon.ico",
        "Instagram_bot.py",
    ]
)
