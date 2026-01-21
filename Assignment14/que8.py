# Write a lambda function which accepts two numbers and returns addition
Add = lambda No1, No2 : No1 + No2

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    result = Add(No1, No2)
    
    print("Addition is ",result)

if __name__ == "__main__":
    main()
