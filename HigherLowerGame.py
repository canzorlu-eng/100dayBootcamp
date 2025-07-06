import random
data=[
    {
        "name":"ronaldo",
        "desc":"footballer",
        "followers": 90
    },
    {
        "name":"messi",
        "desc":"footballer",
        "followers": 110
    },
    {
        "name":"neymar",
        "desc":"footballer",
        "followers": 40
    },
    {
        "name":"Rafa Silva",
        "desc":"footballer",
        "followers": 290
    },
    {
        "name":"Solskjaer",
        "desc":"Techincal Director",
        "followers": 100
    },
    {
        "name":"salah",
        "desc":"footballer",
        "followers": 50
    },
    {
        "name":"Zidane",
        "desc":"footballer",
        "followers": 124
    }
]
score=0
while True:
    who=random.choice(data)
    whom=random.choice(data)
    while whom==who:whom=random.choice(data)
    print(f"A: {who["name"]}, {who["desc"]}")
    print("Compare VS")
    print(f"B: {whom["name"]}, {whom["desc"]}")
    inp=input("Higher or Lower: ").lower()
    if inp=="higher" and who["followers"]>whom["followers"]:
        score+=1
        print("Correct")
    elif inp=="lower" and who["followers"]<whom["followers"]:
        score+=1
        print("Correct")
    else:
        print(f"Your final score is {score}")
        break