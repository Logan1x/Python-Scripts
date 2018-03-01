import urllib.request
import sys
from lxml import html

if len(sys.argv) < 2:
    print('Usage example: python fetch_html.py https://github.com')
    sys.exit(1)

url = sys.argv[1]
response = urllib.request.urlopen(url)
html_text = response.read().decode('UTF-8')
text = html.fromstring(html_text).text_content()

print(text)
