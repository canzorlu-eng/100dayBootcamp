alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]
def encode(char,shift):
    charId=shift+alphabet.index(char)
    return alphabet[charId]

def decode(char,shift):
    charId=-1*shift+alphabet.index(char)
    return alphabet[charId]


inp=input("decode or encode? ")
if inp=="encode":
    text=input("enter your text: ")
    shift=int(input("enter shift amount: "))
    res=""
    for c in text:
        res+=encode(c,shift)
    print(res)
elif inp=="decode":
    text=input("enter your text: ")
    shift=int(input("enter shift amount: "))
    res=""
    for c in text:
        res+=decode(c,shift)
    print(res)
else:
    print("wrong entry!")