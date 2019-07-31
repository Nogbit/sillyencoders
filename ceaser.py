# Original Source https://www.thecrazyprogrammer.com/2018/05/caesar-cipher-in-python.html

def encrypt(string, shift):

  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

  return cipher

text = input("enter plain text: ")
key = int(input("enter shift number: "))

print("original text: ", text)
print("encrypted text: ", encrypt(text, key))