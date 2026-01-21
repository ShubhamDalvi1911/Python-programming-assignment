# Write a lambda function which accepts three numbers and returns largest number.
Largest = lambda No1, No2, No3 : No1 if (No1 > No2)  else (No2 if (No2 > No3) else No3)

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
    No3 = int(input("Enter third number : "))

    result = Largest(No1, No2, No3)
    
    print("Largest number is ",result)

if __name__ == "__main__":
    main()
