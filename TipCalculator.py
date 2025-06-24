bill=float(input("welcome to the tip calculator\nwhat was the total bill? "))
percent=float(input("how much tip you wanna give %x: "))
people=float(input("how many people split the bill: "))
print(f"Each of you will pay: {round((bill+bill*percent/100)/people,2)}"+"$")

