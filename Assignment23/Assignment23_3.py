'''Write a Python program to implement a class named Numbers with the following specifications:
   - The class should contain one instance variables:
     - Value
   - Define a constructor (__init__) that a number from the user and initializes Value.
   - Implement the following instance method:
     - ChkPrime() - return True if the number is prime, otherwise return False.
     - ChkPerfect() - return True if the number is perfect, otherwise return False.
     - Factors() - displays all factors of the number
     - SumFactors() - return the sum of all factors
  - Create multiple objects and call all methods.'''

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value == 1:
            return False
        else:
            for i in range(2, (self.Value//2)+1):
                if (self.Value % i) == 0:
                    return False
            return True
        
    def ChkPerfect(self):
        sum = 0
        for i in range(1, (self.Value//2)+1):
            if (self.Value % i) == 0:
                sum = sum + i

        if sum == self.Value:
            return True
        else:
            return False
        
    def Factors(self):
        print("Factors of",self.Value,"are: ", end="")
        for i in range(1, (self.Value//2)+1):
            if (self.Value % i) == 0:
                print(i, end=" ")
        print(self.Value)

    def SumFactors(self):
        sum = 0
        for i in range(1, (self.Value//2)+1):
            if (self.Value % i) == 0:
                sum = sum + i
        sum = sum + self.Value
        return sum
    
Obj1 = Numbers()
print("Is number prime ",Obj1.ChkPrime())
print("Is number perfect ",Obj1.ChkPerfect())
Obj1.Factors()
print("Sum of factors is: ",Obj1.SumFactors())