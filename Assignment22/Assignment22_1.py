'''Write a python program to implement a class named Demo with the following specifications:
    - The class should contain two instance variables: no1 and no2.
    - The class should contain one class variable named Value.
    - Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
    - Implement two instance methods:
        - Fun() - display the value of instance variables no1 and no2
        - Gun() - display the value of instance variables no1 and no2.
        
Create two objects of the Demo class as follow:
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Call the instance methods in the given sequance:
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()'''

class Demo:

    Value = 0

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def Fun(self):
        print("Value of No1 and No2 from Fun : ",self.no1, self.no2)
    
    def Gun(self):
        print("Value of No1 and No2 from Gun : ",self.no1, self.no2)

Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
