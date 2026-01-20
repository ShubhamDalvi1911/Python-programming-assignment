# write a program which accepts one number and checks whether it is palindrome or not.
def palindrome(No):
    str_No = str(No)
    if str(No) == str_No[::-1]:
        return True
    else:
        return False

def main():
    No = int(input("Enter a number : "))
    result = palindrome(No)
    if result == True:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()