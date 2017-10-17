# Python Scripts
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

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
* ### Meme Density
This script tells you the amount of memes in your facebook feed


```bash
pip install memedensity

memedensity
```

* ### Facebook Auto Post
This is python script that log in into facebook and post the status.  

You can see live execution of this script [here](https://www.youtube.com/watch?v=YES16mVB0lQ).


```bash
pip install -r facebook-auto-post.requirements.txt
python facebook-auto-post.py
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

* ### Mi Community Bot
This python script uses selenium module in python to automate the thread posting.  

You can see live execution of this script [here.](https://www.youtube.com/watch?v=gWRF7-_xhx0)

If you want to understand this code you can visit [here.](https://l0gan1x.quora.com/1-Python-Thread-Posting-Bot-Using-selenium-module?srid=Ic2Y)

```bash
pip install -r mi-community-bot.requirements.txt
python mi-community-bot.py
```

* ### Password Strength Checker
This code checks for your password strength. For the right password, password must contain mixture of an upper case letters, an digit (including 0-9), and a special characters with lower case letters.


```bash
python password-strength-checker.py
```

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


* ### Blog Reader

Blog Reader is the terminal reader that scrapes the article from [planet dgplug](http://planet.dgplug.org/) and displays it on the terminal.

It seprates the content accrding to the screen size.

```bash
python Blog_reader.py
```

* ### Find Large Files

Searches a file location and subdirectories for files larger than a given size.
Useful for phones which might hide files in FileExplorer, but allow use as flash memory.
Directly prints results if run directly.
May also be imported, yielding results one by one.


* ### Approximating *pi*

This script is useful to show a way to approximate the value of pi using a Monte Carlo method. It is also optimized using the `@jit` (*just-in-time*) decorator from the [numba](https://numba.pydata.org/) library.

To see different approximations you just need to modify the argument passed to the main function.

```bash
python pi.py
```


* ### Plotting a function

This script contains an example of plotting a function using [`matplotlib`](http://matplotlib.org/). Feel free to modify the value of `y` to obtain different functions that depend on `x`.

```bash
python plot_example.py
```

* ### Bulk add users to Twitter list

Simple script helps you mass add users to your twitter list to follow (Ex: Bitcoin/Altcoins official account, news, traders...)

- Prepare list screen names
- Setup your app and get an access token

```bash
pip install twitter
python bulk_add_twitter_list.py
```

* ### Expense Manager
Simple GUI program which helps you calculate your expenses, monitor them just through mouse clicks. All you have to do is run the script and choose an option from the menu which will displayed when you run the script. Enter Your Expenses as eg: "Biscuits Rs 15" <press enter> "<item> rs <amount>" ignore the quotes.

```bash
python expense_manger.py
```
* ### Caesar Cipher
Encrypts or Decrypts any message you want, simply enter the message and the rotation number
```bash
python caesar_cipher.py
```
* ### Image Encoder
It is a simple program to encode and decode images, which helps to reduce and handle images on server, as it is convertedto base64 address.
```bash
python image_encoder.py
```

* ### Missionaires And Cannibals Problem
It is a simple program to mimic Missionaries And Cannibals River Crossing Problem.
```bash
python missionaries_and_cannibals_problem.py
```

* ### End To End Encryption
It is a simple program to implement and understand the basic of end_to_end encryption.
Here i am using caesar cipher to encrpt nbut in reality they Use algotihms lile SHA-1, RSA etc.
```bash
python end_to_end.py
```



* ### Server And Client

It is simple client server communication script, will add more functionality in future.
```bash
cd server_client
python client.py
python server.py
```


### Get_Lyrics
A python script to get lyrics of all the songs in current directory and save them to single 'lyrics.txt' file.
```bash
python Get_Lyrics.py
```


* ### Integrate to find area of a graph
The script takes a given graph along with the range within which the area is to be calculated.
It then calculates the area using two methods, the Simpson method and the Trapezoid method and displays the results on a graph.
```bash
python integrate-graph.py
```

### Convert an image in for of 64*64*3 numpy array data
The script takes an image in a particular directory and resizes it to a 64*64 pixel image and then converts it to a data.
```bash
python ImagetoData.py
```


## Release History

* 0.0.1
    * Work in progress

## Meta

Khushal Sharma – [@Khushal](https://twitter.com/herkuch) – sharmakhushal78@gmail.com

Distributed under the MIT LICENSE license. See [``LICENSE``](https://github.com/Logan1x/Python-Scripts/blob/master/LICENSE) for more information.

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
* <a href="https://github.com/Pradhvan">Pradhvan Bisht</a>
* <a href="https://github.com/toonarmycaptain" target="_blank">David Antonini</a>
* <a href="https://github.com/vigov5" target="_blank">Nguyen Anh Tien</a>
* <a href="https://github.com/akshitgrover" target="_blank">Akshit Grover</a>
* <a href="https://github.com/Sharanpai" target="_blank">Sharan Pai</a>
* <a href="https://github.com/MadhavBahlMD" target="_blank">Madhav Bahl</a>
* <a href="https://github.com/ishank011" target="_blank">Ishank Arora</a>
* <a href="https://github.com/vis2797" target="_blank">Vishal Sharma</a>
* <a href="https://github.com/apuayush" target="_blank">Apurva Nitanjay</a>

### If you like the project give a star  [<img src="Selection_008.png" alt="Star button" align="top">](https://github.com/Logan1x/Python-Scripts)
