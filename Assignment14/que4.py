# Write a lambda function which accepts two numbers and returns minimum number.
# MaxNum = lambda No1 , No2 : min(No1,No2)
MinNum = lambda No1 , No2 : No1 if (No1 < No2) else No2

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    result = MinNum(No1, No2)
    
    print("Minimum number is ", result)

if __name__ == "__main__":
    main()
