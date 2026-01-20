#Write a program which accepts one number and prints cube of that number.
def cube(No):
    return No*No*No

def main():
    Result = 0
    No = int(input("Enter a number you want a cube of : "))
    Result = cube(No)
    print(Result)
    
if __name__ == "__main__":
    main()