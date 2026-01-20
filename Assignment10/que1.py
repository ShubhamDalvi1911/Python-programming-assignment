# Write a program which accepts one number and prints multiplication table of that number.
def Mtable(No):
    for i in range(1,11):
        print(i*No)

def main():
    No = int(input("Enter a number : "))
    Mtable(No)

if __name__ == "__main__":
    main()