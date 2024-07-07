#Write a class "Calculator" capable of finding square, cube and square root of a number

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square is {self.num * self.num}")

    def cube(self):
        print(f"The cube is {self.num * self.num * self.num}")

    def root(self):
        print(f"The square root is {self.num ** 0.5}")

a = Calculator(int(input("Enter Number: ")))
a.square()
a.cube()
a.root()
