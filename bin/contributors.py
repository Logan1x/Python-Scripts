import sys
import requests
from urllib.parse import urljoin
import PIL
import shutil

from PIL import Image


def generate_markdown(data):
    """
    This functions takes an array of dicts with keys login and avatar
    and generates markdown. For embeding images in markdown it downloads the
    image and resizes it to standard size
        :param data: Array of dicts with key login and avatar
    """
    basewidth = 50
    markdown = ''
    for author in data:
        response = requests.get(author.get('avatar'), stream=True)
        with open('temp.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        img = Image.open("temp.png")
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img.save(author.get('login') + '.png')
        markdown = markdown + '![' + author.get('login', '') + '](' + author.get('login', '')+'.png  "'+author.get('login', '') + '" )'

    with open("contributors.md", "w") as text_file:
        text_file.write(markdown)


def get_data(url):
    """
    Fetches data from the given url and filters author sub dictionary
        :param url: String
    """
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'accept': 'application/json'
    }
    response = requests.get(urljoin(url, 'graphs/contributors-data'), headers=headers)
    if response.status_code == 200:
        data = [author.get('author', '') for author in response.json()]
        return data
    else:
        print('Check if the url is right and if you have network connection')
        sys.exit(0)


repo_url = sys.argv[1]
if repo_url is None or len(repo_url) == 0:
    print('Please enter valid url')
else:
    generate_markdown((get_data(repo_url)))
