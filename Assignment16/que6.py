# Write a program which accept number from user and check whether that number is positive or negative or zero.

def Chk(No):
    if No < 0:
        return "Negative"
    elif No > 0:
        return "Positive"
    else:
        return "Zero"

def main():
    No = int(input("Enter a number to check whther it is positive or negative or zero : "))
    result = Chk(No)
    print(result)

if __name__ == "__main__":
    main()