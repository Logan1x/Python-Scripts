# Python Scripts

> This Repo is a collection of Various python scripts.

In this repo there are different kinds of python scripts for their respective uses. These all are open sourced and you can use them in any form for free.


## Installation

Make sure you've already git installed. Then you can run the following commands to get the scripts on your computer:

OS X, Linux and Windows:

```bash
git clone https://github.com/Logan1x/Python-Scripts.git
cd Python-Scripts
```

### Meme Density
This script tells you the amount of memes in your facebook feed


```bash
pip install memedensity 

memedensity
```


## Usage
### Facebook Auto Post
This is python script that log in into facebook and post the status.  

You can see live execution of this script [here](https://www.youtube.com/watch?v=YES16mVB0lQ).


```bash
pip install -r facebook-auto-post.requirements.txt
python facebook-auto-post.py
```

### Locate Me
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

### Mi Community Bot
This python script uses selenium module in python to automate the thread posting.  

You can see live execution of this script [here.](https://www.youtube.com/watch?v=gWRF7-_xhx0)

If you want to understand this code you can visit [here.](https://l0gan1x.quora.com/1-Python-Thread-Posting-Bot-Using-selenium-module?srid=Ic2Y)

```bash
pip install -r mi-community-bot.requirements.txt
python mi-community-bot.py
```

### Password Strength Checker
This code checks for your password strength. For the right password, password must contain mixture of an upper case letters, an digit (including 0-9), and a special characters with lower case letters.


```bash
python password-strength-checker.py
```

### YouTube Bot
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

## Meta

Khushal Sharma – [@Khushal](https://twitter.com/herkuch) – sharmakhushal78@gmail.com

Distributed under the MIT LICENSE license. See ``LICENSE`` for more information.

[Logan1x](https://github.com/Logan1x/)

## Contributing

1. Fork it (<https://github.com/Logan1x/Python-Scripts/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
6. Add your name with a link to your profile in the contributors list.

## Contributors

The following people helped in creating the above content.

* <a href="https://github.com/Logan1x" target="_blank">Khushal Sharma</a>
* <a href="https://github.com/KayvanMazaheri" target="_blank">Kayvan Mazaheri</a>
* <a href="https://github.com/kalbhor" target="_blank">Lakshay Kalbhor</a>
