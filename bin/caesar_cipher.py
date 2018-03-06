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


print("***** CAESAR CIPHER *****")
ans = input("Encrypt or Decrypt ? ")
ans = ans.lower()
k = input("Enter message : ")
nn = int(input("Enter number of rotation : "))
if ans == 'encrypt':
    ret = encrypt(nn, k)
    print('Encrytped message: %s' % ret)
else:
    ret = decrypt(nn, k)
    print('Decrytped message: %s' % ret)
