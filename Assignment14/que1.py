# Write a lambda function which accepts one number and returns square of that number.
square = lambda No : No*No  

def main():
    No = int(input("Enter a number you want square of : "))
    result = square(No)
    print("Square is ", result)

if __name__ == "__main__":
    main()

