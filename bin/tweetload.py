import twitter
import json
import re

# replace 'default' with twitter user
user = 'default'
# path to json file with your twitter credentials (see https://python-twitter.readthedocs.io/en/latest/)
creds = 'creds.json'
file_name = 'tweets.txt'


def init_twitter():
    # load twitter API tokens
    with open(creds) as data_file:
        data = json.load(data_file)

    api = twitter.Api(consumer_key=data["consumer_key"],
                      consumer_secret=data["consumer_secret"],
                      access_token_key=data["access_token_key"],
                      access_token_secret=data["access_token_secret"])

    return api


def main():
    if user == 'default':
        print("Please define the twitter user's screenname to download content from in source code.")
        return

    api = init_twitter()

    # get up to 4000 latest tweets
    tweets = api.GetUserTimeline(screen_name=user, count=200)
    curr_id = tweets[-1].id
    for i in range(19):
        tweets = tweets + \
            api.GetUserTimeline(screen_name=user, count=200, max_id=curr_id)
        curr_id = tweets[-1].id

    print("Tweets: " + str(len(tweets)))

    # write tweets to file
    with open(file_name, 'w') as file_o:
        for tweet in tweets:
            tweet_cont = tweet.text
            # strip links
            tweet_cont = re.sub(r'http\S+', '', tweet_cont)
            # strip mentions
            tweet_cont = re.sub(r'@\S+', '', tweet_cont)
            # strip hashtags
            tweet_cont = re.sub(r'#\S+', '', tweet_cont)
            tweet_cont = tweet_cont.replace('RT: ', '')
            tweet_cont = tweet_cont.replace('RT', '')
            file_o.write(tweet_cont + '\n')


if __name__ == "__main__":
    main()
