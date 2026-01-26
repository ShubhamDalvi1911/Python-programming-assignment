# Write a program which contains one function that accept one number from user and return true if number is divisible by 5 otherwise return false.
def DivBy(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():
    No = int(input("Enter a number to check whether divisible by 5 or Not : "))
    result = DivBy(No)
    print(result)

if __name__ == "__main__":
    main()