
import os
import argparse
import requests
import six
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from getpass import getpass
from argparse import RawTextHelpFormatter

ASCII = """
  __  __                     _____                 _ _
 |  \/  |                   |  __ \               (_) |
 | \  / | ___ _ __ ___   ___| |  | | ___ _ __  ___ _| |_ _   _
 | |\/| |/ _ \ '_ ` _ \ / _ \ |  | |/ _ \ '_ \/ __| | __| | | |
 | |  | |  __/ | | | | |  __/ |__| |  __/ | | \__ \ | |_| |_| |
 |_|  |_|\___|_| |_| |_|\___|_____/ \___|_| |_|___/_|\__|\__, |
                                                          __/ |
                                                         |___/
"""

DESC = """
- Tells you approximately how many memes are currently in your facebook
newsfeed. Provides % memes in newsfeed.
- Provides memes in newsfeed urls
"""

if six.PY2:
    input = raw_input
else:
    pass


def _login_fb():

    email = input('> Email or Phone: ')
    password = getpass('> Password: ')

    return email, password


def _xkcd():

    r = requests.get('http://xkcd.com/info.0.json').json()
    return r['img']


def _execute_script(email, password, count):

    print("\nLoading..\nCheck out today's xkcd comic till then : %s \n\n" % (_xkcd()))

    driver = webdriver.PhantomJS()
    driver.get('https://www.facebook.com')

    email_ID = driver.find_element_by_id('email')
    pass_ID = driver.find_element_by_id('pass')

    email_ID.send_keys(email)
    pass_ID.send_keys(password)
    pass_ID.send_keys(Keys.ENTER)
    sleep(5)

    for i in range(0, count):
        driver.execute_script(
            "window.scrollBy(0, document.body.scrollHeight);")
        sleep(1)

    sleep(5)

    driver_tags = driver.execute_script(
        'return document.getElementsByClassName("scaledImageFitWidth img")')

    driver_img_list = {
        'src': [x.get_attribute('src') for x in driver_tags],
        'alt': [x.get_attribute('alt') for x in driver_tags],
    }

    driver.quit()

    return driver_img_list


def _check_memes(driver_img_list, verbose):

    alt_list = driver_img_list['alt']
    if len(alt_list) == 0:
        print("Error getting newsfeed. Possibly username or password was incorrect")
        return

    output = "\n{} memes in your newsfeed.\n{} total images in your newsfeed.\n{}% memes in newsfeed.\n"
    count = 0

    for key, alt in enumerate(alt_list):
        if "text" in alt or "meme" in alt:
            count += 1
            if verbose:
                print(driver_img_list['src'][key])

    print(output.format(count, len(alt_list), round(count*100/len(alt_list), 2)))


def main():

    print('\n')

    parser = argparse.ArgumentParser(
        description='\n{}\n{}\n'.format(ASCII, DESC), formatter_class=RawTextHelpFormatter)
    parser.add_argument('-C', '--count', action='store', dest='count',
                        help='How many times to scroll newsfeed (default = 5)')
    parser.add_argument('-L', '--login', action='store_true',
                        help='Input login credentials')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Shows meme urls')
    args = parser.parse_args()

    count = int(args.count or '5')
    login_bool = args.login
    verbose_bool = args.verbose

    if login_bool:
        email, password = _login_fb()
    else:
        try:
            email = os.environ['fb_email']
            password = os.environ['fb_pass']
        except KeyError:
            print("Couldn't find fb_email and fb_pass in environment variables")
            email, password = _login_fb()

    driver_img_list = _execute_script(email, password, count)
    _check_memes(driver_img_list, verbose_bool)


if __name__ == '__main__':

    main()
