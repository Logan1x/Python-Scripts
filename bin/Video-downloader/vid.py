from __future__ import unicode_literals
import youtube_dl
import sys
import requests
# Master dictionary--will be expanding in future iterations of the project
# version 1 of vid.py
master = {
    'Audio': {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    },
    'Video': {
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
            # 'preferredquality': '137',
        }]
    },
    'list': {
        'listsubtitles': True
    },
    'listformat': {
        'lisformats': True
    }
}


def net(url):
    """
    check if the user has connected to the internet.
    """
    try:
        requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Please check your network connection.")
        return False
    except requests.exceptions.Timeout:
        print("Site is taking too long to load, TimeOut.")
        return False
    except requests.exceptions.TooManyRedirects:
        print("Too many Redirects.")
        return False
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(e)
        sys.exit(1)
    return True


def check(link):
    """
    checking the validity of the link.
    """
    try:
        requests.get(link)
        return True
    except requests.exceptions.ConnectionError:
        print("disconnected from network.")
        return False
    except requests.exceptions.HTTPError as err:
        print(err)
        return False


def download(link, data):
    try:
        with youtube_dl.YoutubeDL(data) as ydl:
            ydl.download([link])
    except youtube_dl.utils.DownloadError as err:
        print(err)


def main():
    ch = 'Y'
    if net(r"https://www.youtube.com/"):
        if ch == 'Y':
            link = str(input("Enter the link: "))
            if check(link):
                print("1.Download an Audio playlist")
                print("2.Download a Video playlist")
                print("3.Download a Single Audio")
                print("4.Download a single video file")
                ch = int(input("Enter your choice: "))
                if ch in [1, 2, 3, 4]:
                    if ch == 1:
                        master['Audio']['noplaylist'] = False
                        download(link, master['Audio'])
                    elif ch == 2:
                        master['Video']['noplaylist'] = False
                        download(link, master['Video'])
                    elif ch == 4:
                        download(link, master['Video'])
                    else:
                        download(link, master['Audio'])
                else:
                    print("Bad choice")
                ch = str(input("do you want to continue?(Y/n)"))


if __name__ == "__main__":
    main()
