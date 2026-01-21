# Write a lambda function which accepts one number and returns True if number is odd otherwise False.
OddTF = lambda No : True if (No % 2) != 0 else False

def main():
    No = int(input("Enter a number : "))

    result = OddTF(No)
    
    print(result)

if __name__ == "__main__":
    main()
