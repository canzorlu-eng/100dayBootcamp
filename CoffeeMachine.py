input=input("Waht would you like(es/lat/cap)? ")
machine={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0
}
coffees={
    "es":20,
    "lat":10,
    "cap":5
}
if input=="report":
    for key in machine:
        print(key + " : "+ str(machine[key]))
elif input=="lat":
    print("insert coins")
    quar=input("How many quarters: ")
    dim=input("How many dimes: ")
    nick=input("How many nickles: ")
    pen=input("How many pennys: ")
    total=(quar*25+dim*10+nick*5+pen)/100
    if total<coffees["lat"]:
        print("insufficient money")
    else:
        machine["money"]+=total

#THİS WAS AN EASY PROJECT AND I DONT WANT TO COMPLETE IT !!