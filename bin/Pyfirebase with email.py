import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import smtplib
import serial
import json

arduinoData = serial.Serial('com31',9600)

from firebase import firebase

gmail_user = "YourEmail@gmail.com"
gmail_pwd  = "*****"
TO = 'ToEmail@gmail.com'
SUBJECT = "FIRE STATION NOTIFICATION"
TEXT = "The temperature is above critical level"
flag=0

firebase = firebase.FirebaseApplication('https://ProjectName.firebaseio.com/')

while 1:
    myData = (arduinoData.readline().strip())
    myData = (myData.decode('utf-8'))
    myData = float(myData)
    result = firebase.put('MainNode/ChildNode','temp',myData)
    print 'Temperature : ',result,' C'
    if flag==0:
        if myData>50:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_user,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])
            server.sendmail(gmail_user, [TO], BODY)
            print ('email sent')
            flag=1

