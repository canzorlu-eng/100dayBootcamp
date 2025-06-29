import random
list=["computer","science","engineer"]
selected=random.choice(list)
blank="_ "*len(selected)
print(blank+"\n")
lives=5
correct_letters=[]
while lives>0 and blank.find("_")!=-1:
    print(f"*********Lives {lives}/5 *********")
    guess=input("guess a letter: ")
    display=""
    if selected.find(guess)!=-1:
        print("correct guess\n")
        
        for i in range(len(selected)):
            if selected[i]==guess:
                display+=guess
                correct_letters.append(guess)
            elif selected[i] in correct_letters:display+=selected[i]
            else:display+="_"
        print(display+"\n")
        blank=display
        
    else:
        print("Wrong\n")
        lives-=1
        
if lives==0:
    print("You lost!")
else:
    print("You win!")