class Student:
    lang = "Python" #Default Language

    def __init__(self, name, age, branch, language=None):
        self.name = name
        self.age = age
        self.branch = branch
        self.language = language if language else Student.lang  

S1 = Student("Dhruv", "19", "CSE", "Javascript")
S2 = Student("Rohan", "19", "CSE", "C++")
S3 = Student("Druv", "19", "CSE")  # This will use the default language

print(S1.name, S1.age, S1.branch, S1.language)
print(S2.name, S2.age, S2.branch, S2.language)
print(S3.name, S3.age, S3.branch, S3.language)
