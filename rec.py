#Write a program to print the sum of first n natural no.s using recursion

def sum(n):
    if (n==0):
        return 0
    return n+sum(n-1)

a=int(input("Enter no."))
print(f"Sum of {(a)} no.s is {sum(a)}")
