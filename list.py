#Write a program to accept marks of 6 students and store them in a sorted manner

marks_list=[]
for i in range(6):
    a=int(input(f"Enter marks of student{i+1}:"))
    marks_list.append(a)

print("Unsorted marks list: ", marks_list) #INPUTTED LIST
marks_list.sort()
print("Sorted markslist: ",marks_list) #SORTED LIST
