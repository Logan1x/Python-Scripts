"""Script to get the air quality based on the user's current location"""

import sys

import requests as req

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = "https://api.waqi.info/feed/here/?token=" + sys.argv[1]
        response = req.get(url, verify=False)
        if response.json()['status'] == "ok":
            print("The air quality is " + str(response.json()['data']['aqi']))
            print("The data was fetched from " +
                  response.json()['data']['city']['name'])
            print("The pollutant measured was " +
                  str(response.json()['data']['dominentpol']))
        elif response.json()['status'] == "error":
            print("The server returned an error. The message is " +
                  response.json()['data'])
    else:
        print("Cannot fetch AQI without token")
