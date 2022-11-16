import random


capital_alpha   =   "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alpha     =   "abcdefghijklmnopqrstovwxyz"
symbols         =   "!@#$%&*"
numbers         =   "1234567890"

def Generate_Pass():
    length = int(input("Enter your password length: "))
    characters  = []
    password    = []

    for x in range(1, length+1):
        characters.append(random.choice(capital_alpha))
        characters.append(random.choice(small_alpha))
        characters.append(random.choice(symbols))
        characters.append(random.choice(numbers))
        password.append(random.choice(characters))
    return password
        

for i in Generate_Pass():
    print(i , end="")
