from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
import sys
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname('localhost')

mySocket = socket(SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))
mySocket.listen(1)
while True:
        client, addr = mySocket.accept()
        data = client.send("Connection Established: ")
sys.exit()
