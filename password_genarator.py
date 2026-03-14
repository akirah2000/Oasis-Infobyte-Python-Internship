import random
import string

print("Random Password Generator")

# User input
length = int(input("Enter password length: "))

# Characters used in password
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_characters)

print("Generated Password:", password)
