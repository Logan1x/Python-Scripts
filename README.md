# [Python Scripts](https://logan1x.github.io/Python-Scripts/)

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/built-by-developers.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/check-it-out.svg)](http://www.logan1x.me/Python-Scripts/)


[![Join the chat at https://gitter.im/Python_Scripts/Lobby](https://badges.gitter.im/Python_Scripts/Lobby.svg)](https://gitter.im/Python_Scripts/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

> This Repo is a collection of Various python scripts.

In this repo there are different kinds of python scripts for their respective uses. These all are open sourced and you can use them in any form for free.


## Installation

Make sure you've already git installed. Then you can run the following commands to get the scripts on your computer:

OS X, Linux and Windows:

```bash
git clone https://github.com/Logan1x/Python-Scripts.git
cd Python-Scripts/bin
```

## Scripts

* ### Air Quality Script
    - This script renders the air quality from the location of the user
    - The location is fetched using the user's IP address

    - This script requires a key from WAQI. 
    - It is free and can be fetched from http://aqicn.org/data-platform/token/#/
    #### Usage Instructions
    ```python
    python air-quality.py token
    ```
* ### Approximating *pi*

This script is useful to show a way to approximate the value of pi using a Monte Carlo method. It is also optimized using the `@jit` (*just-in-time*) decorator from the [numba](https://numba.pydata.org/) library.

* ### Blog Reader

Blog Reader is the terminal reader that scrapes the article from [planet dgplug](http://planet.dgplug.org/) and displays it on the terminal.

It seprates the content accrding to the screen size.

```bash
python Blog_reader.py
```

* ### Bulk add users to Twitter list

Simple script helps you mass add users to your twitter list to follow (Ex: Bitcoin/Altcoins official account, news, traders...)

- Prepare list screen names
- Setup your app and get an access token

```bash
pip install twitter
python bulk_add_twitter_list.py
```


* ### Caesar Cipher
Encrypts or Decrypts any message you want, simply enter the message and the rotation number
```bash
python caesar_cipher.py
```

* ### Contributor list
For a given repo generate contribute.md with images in same size like the one in this README.md

```python
 python .\contributors.py https://github.com/Logan1x/Python-Scripts/
```
where the argument is the url of the repo

you may need to install packages like PIL@1.1.7 and requests if not installed 

* ### End To End Encryption
It is a simple program to implement and understand the basic of end_to_end encryption.
Here i am using caesar cipher to encrpt nbut in reality they Use algotihms lile SHA-1, RSA etc.
```bash
python end_to_end.py
```


* ### Expense Manager
Simple GUI program which helps you calculate your expenses, monitor them just through mouse clicks. All you have to do is run the script and choose an option from the menu which will displayed when you run the script. Enter Your Expenses as eg: "Biscuits Rs 15" <press enter> "<item> rs <amount>" ignore the quotes.

```bash
python expense_manger.py
```



* ### Facebook Auto Post
This is python script that log in into facebook and post the status.  

You can see live execution of this script [here](https://www.youtube.com/watch?v=YES16mVB0lQ).


```bash
pip install -r facebook-auto-post.requirements.txt
python facebook-auto-post.py
```


* ### Find Large Files

Searches a file location and subdirectories for files larger than a given size.
Useful for phones which might hide files in FileExplorer, but allow use as flash memory.
Directly prints results if run directly.
May also be imported, yielding results one by one.

* ### FTP Download File
A simple application to download a file via FTP with the given remote and local path
Parameters:
 * -hh hostname
 * -u  username
 * -p  password
 * -rd remote directory
 * -ld local directory
```bash
python ftp_download_file.py

* ### Fetch HTML
This script fetch html response from the provided url and parse xml tag to get only text content and print out.

```bash
python fetch_html.py https://github.com
``````

* ### Get External IP
Gets the external ip-address from the current machine and prints it to the console
```bash
python getExternalIp.py
```

* ### Group files by type
    - Group files by their extensions
    - Files are moved into folders with extension names

    #### Usage Instructions
    ```python
    python group_file_by_type.py 'C:\\test\\products'
    ```

* ### Handy offline dictionary
A tiny offline dictionary app based on nltk wordnet and pyqt5
```bash
cd dictionary
python app.py
```

* ### Highcharts loader
It is a simple program that can load charts from [highcharts](www.highcharts.com).
After loading chart you can save it to file or embed it into your html page in base64 format.
Don't forget install `requests` library from `highcharts_loader_requirements.txt`
```python
from highcharts_loader import ChartLoader, Options

options = Options(from_file='options.json')
chart = ChartLoader(options)
chart.save_to_file('result.png')
```

options.json example:
```json
{
    "chart": {
        "type": "bar"
    },
    "title": {
        "text": "Which channels are driving engagement?"
    },
    "xAxis": {
        "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    },
    "series": [{
        "data": [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
    }]
}
```

* ### Image Encoder
It is a simple program to encode and decode images, which helps to reduce and handle images on server, as it is convertedto base64 address.
```bash
python image_encoder.py
```


* ### Integrate to find area of a graph
The script takes a given graph along with the range within which the area is to be calculated.
It then calculates the area using two methods, the Simpson method and the Trapezoid method and displays the results on a graph.
```bash
python integrate-graph.py
```

* ### Locate Me
Run this script and it will locate you.

This will tell you your

1. City
2. Region
3. Country
4. Latitude & Longitude.
5. Your Internet Service Provider  


This uses [Checkip](http://checkip.dyndns.com/) and [ipinfo.io](http://ipinfo.io/developers).

```bash
python locate-me.py
```

* ### Meme Density
This script tells you the amount of memes in your facebook feed


```bash
pip install memedensity

memedensity
```

* ### Mi Community Bot
This python script uses selenium module in python to automate the thread posting.  

You can see live execution of this script [here.](https://www.youtube.com/watch?v=gWRF7-_xhx0)

If you want to understand this code you can visit [here.](https://l0gan1x.quora.com/1-Python-Thread-Posting-Bot-Using-selenium-module?srid=Ic2Y)

```bash
pip install -r mi-community-bot.requirements.txt
python mi-community-bot.py
```
* ### Missionaires And Cannibals Problem
It is a simple program to mimic Missionaries And Cannibals River Crossing Problem.
```bash
python missionaries_and_cannibals_problem.py
```
* ### Password Strength Checker
This code checks for your password strength. For the right password, password must contain mixture of an upper case letters, an digit (including 0-9), and a special characters with lower case letters.


```bash
python password-strength-checker.py
```
* ### Plotting a function

This script contains an example of plotting a function using [`matplotlib`](http://matplotlib.org/). Feel free to modify the value of `y` to obtain different functions that depend on `x`.

* ### Server And Client
It is simple client server communication script, will add more functionality in future.
```bash
cd server_client
python client.py
python server.py
```

* ### Tweetload
Download latest tweets (default: up to 4000) from a specific twitter user. The script will create a file with one tweet per line, stripped from mentions, hashtags and links.
<br>
For that to work, create a json file with your twitter credentials (see source) and define the twitter user in source code.  
```bash
python3 tweetload.py
```
* ### Twitter_retweet_bot
It is a simple script that retweets any hashtag provided in it. 
```bash
python twitter_retweet_bot.py
```
* ### Twitter Sentiment Analysis
A python script that goes through the twitter feeds and calculates the sentiment of the users on the topic of Demonetization in India. 
Sentiments are calculated to be positive, negative or neutral.
Various other analyses are represented using graphs. 
 
```bash
pip install -r analyseTweets-requirements.txt
python analyseTweets.py
```


* ### URL Shortener
This is python script that shortens any URL provided to it.

```bash
# Takes multiple inputs and returns shortened URL for both
python shortener.py url1 url2

#Stores shortened URLs in a file
python shortener.py url1 url2 > file.txt
```

* ### Video-downloader v1.1

  #### About


This file allows the user to download videos off of the web.
as of version 1 the user is able to download highquality videos as a playlist or single file as well as audio files from the supported

websites given here http://rg3.github.io/youtube-dl/supportedsites.html are supported.

More features will be added in the future iterations of the project.
a simple video downloader using youtube-dl Library, a starter script for making use
of youtube-dl.

#### Requirements
* You will need to install youtube_dl
  * This can be installed using pip on windows,
  * if you do not know how to use pip please read the installation instructions
* requests library
  * can be downloaded using pip on windows and respective package managers on different operating systems.
* ffmpeg in order to convert the downloaded files to the right format

#### Installation

clone this repo and run `python vid.py` script!
assuming you already have the other requirements.
#### FFmpeg
* ### Bulk add users to Twitter list
Follow this wiki-How tutorial

http://www.wikihow.com/Install-FFmpeg-on-Windows

#### PIP

Extensive information on how to set up virtual env and pip.

https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/

#### Commands

Just run the script and follow the interface! Videos downloaded in same folder as the script.

* ### YouTube Bot
This is a simple python script that increases your video count/ views.
Log out from all google accounts and run this.

```bash
# For Linux Users
python youtube-bot-linux.py

# For Windows Users
python youtube-bot-windows.py
```

#### NOTE:  
In case your browser stoped working delete/comment the following line in the script.  
#### _Linux_
 `os.system(" killall -9 " + brow)`
#### _Windows_
 `os.system("TASKKILL /F /IM " + brow + ".exe")`

## Release History

* 0.0.1
    * Work in progress


### Markdown to presentation
You can convert markdown in a directory into a **.html** file for presentation using reveal.js

``` 
python reveal-md.py -d folder_name -c config

```

### Note
the config is optional. You can specify with keys as here https://github.com/hakimel/reveal.js/#configuration in a json file. Reveal.js cdn link is included in generated html you may need to download them if you want to use the presentation offline

## Meta

Khushal Sharma – [@Khushal](https://twitter.com/herkuch) – sharmakhushal78@gmail.com

Distributed under the MIT LICENSE license. See [``LICENSE``](https://github.com/Logan1x/Python-Scripts/blob/master/LICENSE) for more information.

[Logan1x](https://github.com/Logan1x/)


## Contributing

1. Fork it (<https://github.com/Logan1x/Python-Scripts/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Add your docs in `docs/data.json` file
4. Commit your changes (`git commit -am 'Add some fooBar'`)
5. Push to the branch (`git push origin feature/fooBar`)
6. Create a new Pull Request
7. Add your name with a link to your profile in the contributors list


## Contributors

The following people helped in creating the above content.

![ayrusme](./images/ayrusme.png  "ayrusme" )![lionasp](./images/lionasp.png  "lionasp" )![zinuzoid](./images/zinuzoid.png  "zinuzoid" )![dgupta777](./images/dgupta777.png  "dgupta777" )![chiraag-jain](./images/chiraag-jain.png  "chiraag-jain" )![niharikakrishnan](./images/niharikakrishnan.png  "niharikakrishnan" )![ahadali](./images/ahadali.png  "ahadali" )![khushboopaddiyar](./images/khushboopaddiyar.png  "khushboopaddiyar" )![Harshvardhan58](./images/Harshvardhan58.png  "Harshvardhan58" )![pr0me](./images/pr0me.png  "pr0me" )![abhinavralhan](./images/abhinavralhan.png  "abhinavralhan" )![Souldiv](./images/Souldiv.png  "Souldiv" )![szepnapot](./images/szepnapot.png  "szepnapot" )![SuryaThiru](./images/SuryaThiru.png  "SuryaThiru" )![apuayush](./images/apuayush.png  "apuayush" )![ishank011](./images/ishank011.png  "ishank011" )![ValentinChCloud](./images/ValentinChCloud.png  "ValentinChCloud" )![MadhavBahlMD](./images/MadhavBahlMD.png  "MadhavBahlMD" )![vigov5](./images/vigov5.png  "vigov5" )![RodolfoFerro](./images/RodolfoFerro.png  "RodolfoFerro" )![toonarmycaptain](./images/toonarmycaptain.png  "toonarmycaptain" )![harsha7890](./images/harsha7890.png  "harsha7890" )![Pradhvan](./images/Pradhvan.png  "Pradhvan" )![Rafi993](./images/Rafi993.png  "Rafi993" )![ehnydeel](./images/ehnydeel.png  "ehnydeel" )![shivamp123](./images/shivamp123.png  "shivamp123" )![vis2797](./images/vis2797.png  "vis2797" )![Sharanpai](./images/Sharanpai.png  "Sharanpai" )![kalbhor](./images/kalbhor.png  "kalbhor" )![iyanuashiri](./images/iyanuashiri.png  "iyanuashiri" )![akshitgrover](./images/akshitgrover.png  "akshitgrover" )![KayvanMazaheri](./images/KayvanMazaheri.png  "KayvanMazaheri" )![Logan1x](./images/Logan1x.png  "Logan1x" )

### If you like the project give a star  [<img src="Selection_008.png" alt="Star button" align="top">](https://github.com/Logan1x/Python-Scripts/stargazers)


[`Back to Top`](https://github.com/Logan1x/Python-Scripts#python-scripts)
