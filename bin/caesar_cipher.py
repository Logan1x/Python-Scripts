key = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()


def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result


print("Encrypt or decrypt?")
ans = input()
ans = ans.lower()
print("Enter message")
k = input()
print("Enter rotation number")
nn = int(input())
if ans == 'encrypt':
    ret = encrypt(nn, k)
    print('Encrytped: %s' % ret)
else:
    ret = decrypt(nn, k)
    print('Decrytped: %s' % ret)
