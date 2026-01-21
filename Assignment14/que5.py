# Write a lambda function which accepts one number and returns True if number is even otherwise False.
EvenTF = lambda No : True if (No % 2) == 0 else False

def main():
    No = int(input("Enter a number : "))

    result = EvenTF(No)
    
    print(result)

if __name__ == "__main__":
    main()
