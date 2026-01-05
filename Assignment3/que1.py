#Write a function to accept two numbers and return their multiplication.

def Multiplication(Val1, Val2):
    Ans = Val1 * Val2
    return Ans

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))
    Result = Multiplication(No1, No2)
    print("Multiplication is:", Result) 

if __name__=="__main__":
    main()