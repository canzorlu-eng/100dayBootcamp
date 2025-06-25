direction=input("welcome to the treasure island\n\tleft or right(L or R): ").upper()
if direction=="R":print("Game Over")
else:
    way=input("swim or wait: ").lower()
    if way=="swim":
        print("Game Over")
    else:
        door=input("Which door(R,B,Y): ").upper()
        if door=="Y":
            print("You Win")
        else:
            print("Game Over")
