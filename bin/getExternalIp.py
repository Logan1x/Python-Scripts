import requests
import re

try:
    res = requests.get("http://whatismyip.org")
    myIp = re.compile('(\d{1,3}\.){3}\d{1,3}').search(res.text).group()
    if myIp != "":
        print(myIp)
except:
    print('N/A')
    pass
