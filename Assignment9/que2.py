#Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number
def ChkGreater(No1, No2):
    if No1 > No2:
        print(No1," Is Grater")
    else:
        print(No2, " Is Greater")

def main():
    print("Enter first number : ")
    No1 = int(input())
    print("Enter second number : ")
    No2 = int(input())

    ChkGreater(No1,No2)

if __name__ == "__main__":
    main()