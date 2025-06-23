import random
import string

#password generator

length = int(input("Enter password length: "))

include_symbols = input("Use symbols? (y/n): ")

chars = string.ascii_letters + string.digits

if include_symbols.lower() == "y":
    chars += "!@#$%^&*"

password = ""
for i in range(length):
    password += random.choice(chars)

print("Generated password:", password)
