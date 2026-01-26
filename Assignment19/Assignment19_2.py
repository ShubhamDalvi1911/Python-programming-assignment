# Write a program which contains one lambda function which accepts two parameter and return its multiplication

Multiplication = lambda A,B: A * B

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))
    result = Multiplication(No1, No2)
    print(f"The multiplication of {No1} and {No2} is {result}")

if __name__ == "__main__":
    main()