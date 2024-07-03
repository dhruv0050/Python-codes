#Write a program to input 10 numbers from the user and display all the unique number

s=set()
for i in range(10):
    a=int(input(f"Enter number {i+1} :"))
    s.add(a)
print(s)