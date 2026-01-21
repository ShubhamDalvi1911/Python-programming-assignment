# Write a lambda function which accepts two numbers and returns maximum number.
# MaxNum = lambda No1 , No2 : max(No1,No2)
MaxNum = lambda No1 , No2 : No1 if (No1 > No2) else No2

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    result = MaxNum(No1, No2)
    
    print("Maximum number is ", result)

if __name__ == "__main__":
    main()
