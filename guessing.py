import random

number=random.randint(1,10)
guess=None
while True:
    user=input("enter a guess from 1 to 10: ")
    user=int(user)
    if(user<number):
        print("TOO LOW")
    elif(user>number):
        print("TOO HIGH")
    else:
        print("YOU WON")
        val=input("do you wanna play again? y/n: ")
        if(val=="y"):
            number=random.randint(1,10)
            guess==None
        else:
            print("thanks for playing")
            break
