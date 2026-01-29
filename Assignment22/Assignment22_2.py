'''Write a python program to implement a class named Circle with the following requirements:
    - The class should contain three instance variables: Radius, Area, and Circumfarance.
    - The class should contain one class variable named PI, initialized to 3.14.
    - Define a constructor (__init__) that accepts two parameters and initializes the instance variables to 0.0
    - Implement following instance methods:
        - Accept() - Accepts the radious of the circle from the user.
        - CalculateArea() - Calculates the area of the circle and store it in the Area varable.
        - CalculateCircumferance() - Calculates the circumference of the circle and stores it in the Circumference variable.
        - Display() - display the value of Radius , Area and Circumferance.
    - Create multiple object of the Circle class and invoke all the instance methods for each object
'''

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumfarance = 0.0

    def Accept(self):
        R = int(input("Enter the radius of circle : "))
        self.Radius = R

    def CalculateArea(self):
        Area = Circle.PI * (self.Radius*self.Radius)
        self.Area = Area

    def CalculateCircumferance(self):
        Circumfarance = 2*Circle.PI * self.Radius
        self.Circumfarance = Circumfarance

    def Display(self):
        print("Radius is : ",self.Radius)
        print("Area is : ",self.Area)
        print("Circumfarance is : ",self.Circumfarance)

Obj1 = Circle()
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumferance()
Obj1.Display()