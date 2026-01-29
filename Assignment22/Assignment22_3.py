'''Write a python program to implement a class named Arithmetic with the following characteristics:
    - The class should contain two instance variables: Value1 and Value2.
    - Define a constructor (__init__) that initializes all instance variables to 0.
    - Implement the following instance methods:
        - Accept() - Accepts values for Value1 and Value2 from the user.
        - Addition() - return the additon of Value1 and Value2.
        - Subtraction() - return the subtraction of Value1 and Value2.
        - Multiplication() - return the multiplication of Value1 and Value2.
        - Division() - return the division of Value1 and Value2 (Handle divison by zero properly).
    - Create multiple object of the Arithmetic class and invoke all the instance methods.
'''

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        No1 = int(input("Enter first number : "))
        No2 = int(input("Enter second number : "))
        self.Value1 = No1
        self.Value2 = No2

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not allowed"
        else:
            return self.Value1 / self.Value2

Obj1 = Arithmetic()
Obj1.Accept()
print("Addition is :", Obj1.Addition())
print("Subtraction is :", Obj1.Subtraction())
print("Multiplication is :", Obj1.Multiplication())
print("Division is :", Obj1.Division())