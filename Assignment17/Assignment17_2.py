# Write a program which accept one number and display below patter
def Patter(No):
    for i in range(No):
        print("   *   "*No)

def main():
    No = int(input("Enter a number : "))
    Patter(No)

if __name__ == "__main__":
    main()