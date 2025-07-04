import random
mode=input("Welcome to the number guessing game\nI am thinking a number between 1-100\nSelect a mode 'easy' or 'hard': ")
lives=5
if mode=="hard":lives=3
num=random.randint(1,100)
while lives>0:
    sel=int(input("Guess: "))
    if sel==num:
        print("Correct Guess")
        break
    elif sel<num:
        print("too low")
        lives-=1
    else:
        print("too big")
        lives-=1
if lives==0:print(f"You lost! The number was {num}")