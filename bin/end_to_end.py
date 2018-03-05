import time
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(msg):
    off = 3
    enc = ""
    for i in msg:
        try:
            enc = enc + a[int((a.index(i)+off)) % 26]
        except ValueError:
            enc += i
    return enc


def decrypt(msg):
    off = 3
    dec = ""
    for i in msg:
        try:
            dec = dec + a[int((a.index(i)-off)) % 26]
        except ValueError:
            dec += i
    return dec


# Client Side(Sender)
print("***** END-TO-END ENCRYPTION *****")
msg = input("Enter message to send : ")
print()
print("Encrypting...")
enc = encrypt(msg.lower())
print("Message sent is       : %s " % enc)

# Server Side
time.sleep(2)
f = open('server.txt', 'w+')
f.write(enc)
f.close()

# Client Side(Receiver)
print()
print("Receiving message...")
time.sleep(2)
f = open('server.txt', 'r+')
msg = f.read()
print("Message received is   : %s " % msg)
print()
print("Decrypting...")
time.sleep(2)
dec = decrypt(msg)
print("Decrypted message     : %s " % dec)
