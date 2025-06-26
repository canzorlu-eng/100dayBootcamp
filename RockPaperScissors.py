import random
choice=int(input("0 for rock,1 for paper,2 for scissors: "))
list=["R","P","S"]
compid=random.randint(0,2)
comp=list[compid]
if(choice==compid):print("Draw")
elif(choice==0 and compid==1):print(f"you lost, computer chosed {comp}")
elif(choice==1 and compid==2):print(f"you lost, computer chosed {comp}")
elif(choice==2 and compid==0):print(f"you lost, computer chosed {comp}")
else:print(f"you win, computer chosed {comp}")


