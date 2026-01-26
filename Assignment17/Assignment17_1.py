"""
Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for Substraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. write on python program which call all the 
functions from arithmetic module by accepting the parameters from user.
"""
import Arithmetic

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
    result = Arithmetic.Add(No1,No2)
    print(result)
    result = Arithmetic.Sub(No1,No2)
    print(result)
    result = Arithmetic.Mult(No1,No2)
    print(result)
    result = Arithmetic.Div(No1,No2)
    print(result)

if __name__ == "__main__":
    main()