import time
import webbrowser
import os

url = str(input("Enter your video url in ->\"url here \"<-  : "))
n = input("Enter refresh rate(seconds) : ")
brow = input("Enter your default browser in ->\"browser here \"<-  : ")
while (1):
    os.system(" killall -9 " + brow)
    time.sleep(int(n))
    webbrowser.open(url)
    print('Successfully Viewd')
