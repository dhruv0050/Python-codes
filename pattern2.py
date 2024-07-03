# # Write a program to for the below pattern:
# #       *
# #      ***
# #     ***** and so on type pattern

n= int(input("Enter pattern line"))
for i in  range (1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")

