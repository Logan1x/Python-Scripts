import urllib2
from urllib2 import urlopen
import json
import re
import requests
# Get Public IP


def getPublicIP():
    data = requests.get('http://checkip.dyndns.com/').content
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)

IP = str(getPublicIP())

# Get Location
url = 'http://ipinfo.io/' + IP + '/json'
response = urlopen(url)
data = json.load(response)
city = data['city']
region = data['region']
country = data['country']
location = data['loc']
org = data['org']

# Print Extracted Details
print "Your City : " + city
print "Your Region : " + region
print "Your Country : " + country
print "Your Location : " + location
print "Your ISP : " + org
