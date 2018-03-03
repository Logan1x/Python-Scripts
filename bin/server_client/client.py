import sys
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR

SERVER_IP = '127.0.0.1'
PORT_NUMBER = 5000
SIZE = 1024
print("Test client sending packets to IP {0}, via port {1}\n".format(
    SERVER_IP, PORT_NUMBER))

mySocket = socket(SOCK_DGRAM)
mySocket.connect((SERVER_IP, PORT_NUMBER))

while True:
    data = mySocket.recv(SIZE)
    print(data)
sys.exit()
mySocket.close()
