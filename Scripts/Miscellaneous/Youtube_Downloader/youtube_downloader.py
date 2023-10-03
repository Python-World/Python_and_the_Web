import sys

import youtube_dl

opts = {
    "outtmpl": "./videos/%(title)s.%(ext)s",
}


def banner():
    print(
        '\t"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'
    )
    print(
        "\t                            Youtube Downloader                         "
    )
    print(
        '\t"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'
    )


def ytdl(x):
    with youtube_dl.YoutubeDL(opts) as service:
        service.download([x])


def main():
    banner()
    if len(sys.argv) < 2:
        print(
            "Error: Invalid arguments \n Usage: python youtube_downloader url_of_video"
        )
    else:
        ytdl(sys.argv[1])


if __name__ == "__main__":
    main()
