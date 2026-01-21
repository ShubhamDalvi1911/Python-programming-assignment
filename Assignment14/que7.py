# Write a lambda function which accepts one number and returns True if divisible by 5
DivFive = lambda No : True if (No % 5) == 0 else False

def main():
    No = int(input("Enter a number : "))

    result = DivFive(No)
    
    print(result)

if __name__ == "__main__":
    main()
