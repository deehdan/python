import random
import string

print("\n PASSWORD GENERATOR")
print("=" * 35, "\n")

#Characters loading
characters = string.ascii_letters + string.digits + string.punctuation

#Get password length
length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your password is: \n", password, "\n \n")
