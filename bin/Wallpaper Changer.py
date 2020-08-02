# wallpaper changer to fetch images from reddit with bloom filter to avoid repitition 
# Find the full Repo at https://github.com/ApoorvTyagi/praw
import praw, requests, re
import os, config, ctypes
import random
import schedule, time
import logging
import mmh3
from bitarray import bitarray


#Setting Up Logs
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

#initializing bloom filter and hash
filter=bitarray(128) 
filter.setall(0)
no_of_hash=3

def resetFilter():
    logger.info("Reseting Filter...")
    filter.setall(0)

def add(item):
    for i in range(no_of_hash):
        index=mmh3.hash(item,i)%64
        filter[index]=1

def find(item):
    for i in range(no_of_hash):
        index=mmh3.hash(item,i)%64
        if filter[index]==0:
            return False
    return True

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    username="",
    password="",
    user_agent="",
)

def set_wallpaper_from_file(filename):
    logger.info("Setting wallpaper to your desktop")
    use = os.getcwd() + "/" + filename
    ctypes.windll.user32.SystemParametersInfoW(20, 0, use, 0)
    time.sleep(2)
    os.remove(use)
    return "Success"


def get_random_subreddit():
    logger.info("Selceting random subreddit...")
    #subreddits = ["Wallpaper"]
    subreddits = [
        "Wallpaper",
        "Wallpapers",
        "BackgroundArt",
        "naturepics",
        "natureporn",
        "EarthPorn"
    ]

    random_subreddit = random.choice(subreddits)
    print(random_subreddit)
    return random_subreddit


def change_wallpaper():
    tryCount=1
    logger.info("Getting subreddit...")
    subreddit = reddit.subreddit(get_random_subreddit())
    logger.info("Getting hot post...")
    topPost = subreddit.hot(limit=5)

    for post in topPost:
        url = post.url
        print('url is :',url)
        print("Post_id is " , post.id)
        
        if tryCount>3:
            return "Failure, Try-Count Limit Exceeded"

        
        print("Try Count : {}".format(tryCount))
        tryCount+=1
        if(reddit.submission(post.id).domain != 'i.redd.it'):
            logger.info("Post does not have any media")
            continue
        if find(post.id):
            logger.info("Post already added in last 7 days...")
            continue
        else:
            logger.info("Found New Image Post")
            add(post.id)


        file_name = url.split("/")

        if len(file_name) == 0:
            file_name = re.findall("/(.*?)", url)

        file_name = file_name[-1]
        if "." not in file_name:
            file_name += ".jpg"

        break

    print(file_name)
    r = requests.get(url)
    with open(file_name, "wb") as f:
        f.write(r.content)

    return set_wallpaper_from_file(file_name)


#print(change_wallpaper())
#schedule.every(1).minutes.do(change_wallpaper)
schedule.every().sunday.at("07:00").do(resetFilter)
schedule.every().day.at("07:00").do(change_wallpaper)
while True:
    schedule.run_pending() 
    time.sleep(3600)

