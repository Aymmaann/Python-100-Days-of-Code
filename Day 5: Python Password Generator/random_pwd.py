import random
import string

print("Welcome to PyPassword Generator")

letters = int(input(f"How many letters would you like in your password? \n"))
symbols = int(input("How many symbols would you like? \n"))
numbers = int(input("How many numbers would you like? \n"))

passlet = ""
passsym = ""
passnum = ""

for i in range(0,letters):
    passlet = passlet + random.choice(string.ascii_letters)

for i in range(0,symbols):
    passsym = passsym + random.choice(string.punctuation)

for i in range(0,numbers):
    passnum = passnum + random.choice(string.digits)

def combine_strings_randomly(str1, str2, str3):
    combined = list(str1 + str2 + str3)
    random.shuffle(combined)
    pwd = ""
    pwd = pwd.join(combined)
    return pwd

password = combine_strings_randomly(passlet, passsym, passnum)
print(f"Generated password: {password}")

