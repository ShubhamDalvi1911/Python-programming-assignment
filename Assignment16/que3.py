# Write a program which contains one function named as Add(). which accept two numbers from user and return addition of that two numbers

def Add(No1,No2):
    return No1 + No2

def main():
    No1 = int(input("Enter first number "))
    No2 = int(input("Enter second number "))
    result = Add(No1,No2)
    print(result)

if __name__ == "__main__":
    main()