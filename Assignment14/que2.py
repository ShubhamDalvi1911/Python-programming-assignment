# Write a lambda function which accepts one number and returns cube of that number.
cube = lambda No : No*No*No

def main():
    No = int(input("Enter a number you want cube of : "))
    result = cube(No)
    print("Cube is ", result)

if __name__ == "__main__":
    main()
