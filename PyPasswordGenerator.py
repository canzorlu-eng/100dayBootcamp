import random
letters=int(input("Welcome to the PyPasswordGenerator\nHow many letters would you like in your password? "))
symbols=int(input("How many symbols would you like in your password? "))
numbers=int(input("How many numbers would you like in your password? "))
letterslist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","w","x"]
symbolslist=["!","#","$","%","&","(",")","*","+"]
nums=["0","1","2","3","4","5","6","7","8","9"]

password=[]
for char in range(0,letters):
    password.append(random.choice(letterslist))

for char in range(0,symbols):
    password.append(random.choice(symbolslist))

for char in range(0,numbers):
    password.append(random.choice(nums))

random.shuffle(password)
p=""
for char in password:
    p+=char
print("Your password: "+p)