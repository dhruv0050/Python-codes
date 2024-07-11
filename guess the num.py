import random
x=random.randint(1,100)
y=0
guess=0
while(y!=x):
    guess+=1
    y=int(input("Enter a number : "))
    if(y>x):
        print("No! Enter a Lower number")
    else:
        print("No! Enter a Higher Number")

print(f"You got the number {x} right after {guess} attempts")