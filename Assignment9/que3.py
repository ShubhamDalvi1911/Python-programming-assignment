# Write a program which accepts one number and prints square of that number
def squre(No):
    return No*No

def main():
    Result = 0
    No = int(input("Enter a number you want a square of : "))
    Result = squre(No)
    print(Result)
    
if __name__ == "__main__":
    main()