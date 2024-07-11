try:
    a=int(input("enter a number : "))
    b=int(input("enter a number : "))
    print(f"Sum is {a+b}")
except Exception as e:  
    print(e)

print("THE END")
# If we haven't used this and the user inputs anything other than an integer, then program crashes and thus the last line i.e. "THE END" never gets executed

#Raising Error
x=int(input("enter a number : "))
c=int(input("enter a number : "))
 
if(c==0):
    raise ZeroDivisionError("You cannont divide a number by zero")

print(f"Division of {x}/{c} is {x/c}")
