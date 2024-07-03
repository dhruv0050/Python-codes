import random

computer = random.choice([-1, 0, 1])
yours = input("Enter your choice: ")
refDict = {"p": 1, "r": -1, "s": 0}
reverseDict = {1: "Paper", -1: "Rock", 0: "Scissor"}

you = refDict[yours]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw ._.")

else:
    if(computer ==-1 and you == 1): 
        print("Let's Go, You Win :)")

    elif(computer ==-1 and you == 0):
        print("Better Luck Next Time :(")

    elif(computer == 1 and you == -1):
        print("Better Luck Next Time :(")

    elif(computer ==1 and you == 0):
        print("Let's Go, You Win :)")

    elif(computer ==0 and you == -1):
        print("Let's Go, You Win :)")

    elif(computer == 0 and you == 1):
        print("Better Luck Next Time :(")

    else:
        print("Something went wrong!")