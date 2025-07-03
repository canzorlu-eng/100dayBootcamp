import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user=[]
comp=[]
for i in range(2):
    user.append(random.choice(cards))
    comp.append(random.choice(cards))

if sum(comp)==21:print("computer won")
elif sum(user)==21:print("user won")
else:
    keep="y"
    while keep=="y":
        if sum(user)>21 and (11 not in user or sum(user)-10>21):
            print("user lost")
            break
        if sum(user)>21 and 11 in user and sum(user)-10<=21:
            user[user.index(11)]=1
        
        else:
            print("comps 1st card: "+str(comp[0]))
            print(str(user) + " score: "+ str(sum(user)))
            keep=input("wanna continue (y or n): ")
            if keep=="n":
                comp.append(random.choice(cards))
                if sum(comp)>21 and 11 in comp:comp[comp.index(11)]=1
                while sum(comp)<16:
                    comp.append(random.choice(cards))
                    if sum(comp)>21 and 11 in comp:comp[comp.index(11)]=1
                if sum(comp)>21:print("user won")
                else:
                    if sum(comp)>sum(user):print("computer won")
                    elif sum(user)>sum(comp):print("user won")
                    else:print("draw")
                    break
            else:
                user.append(random.choice(cards))    

print("*********************")
print(str(user) + " score: "+ str(sum(user)))
print(str(comp) + " score: "+ str(sum(comp)))