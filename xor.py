# Based on code from https://stackoverflow.com/a/29408364

from itertools import cycle

def crypt(var, key):
    return [ chr(ord(a) ^ ord(b)) for (a,b) in zip(var, cycle(key)) ]

text = input("enter plain text: ")
key  = input("enter a key: ")
print("original plain text: ", text)

encrypted = crypt(text, key)
decrypted = crypt(encrypted, key)

print("encrypted text: ", encrypted)
print("decrypted text: ", decrypted)