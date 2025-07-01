dict={}
name=input("Welcome to the secret auction program\nWhat is your name? ")
bid=int(input("What is your bid? $"))
isBidders=input("Are there any other bidders? yes or no: ")
dict[bid]=name
while isBidders=="yes":
    name=input("Welcome to the secret auction program\nWhat is your name? ")
    bid=int(input("What is your bid? $"))
    isBidders=input("Are there any other bidders? yes or no: ")
    dict[bid]=name
m=0
for key in dict:
    m=max(m,key)
print("the winner is "+dict[m])