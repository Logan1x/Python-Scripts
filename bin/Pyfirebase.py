import requests.packages.urllib3
import serial
import json
from firebase import firebase

requests.packages.urllib3.disable_warnings()
arduinoData = serial.Serial('com31', 9600)


firebase = firebase.FirebaseApplication(
    'https://___YOUR_PROJECT_NAME____.firebaseio.com/')

while 1:
    myData = (arduinoData.readline().strip())
    myData = (myData.decode('utf-8'))
    myData = float(myData)
    result = firebase.put('MainNode/Leaf', 'temp', myData)
    print 'Data : ', result
