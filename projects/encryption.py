import random
import string

chars = " " + string.ascii_letters + string.punctuation + string.digits
chars = list(chars)

key = chars.copy()
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key : {key}")

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

#Encrypt
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Your encrypted message is : {cipher_text}")    

#Decrypt
message = ""
for letter in cipher_text:
    index = key.index(letter)
    message += chars[index]

print(f"Your message was: {message}")