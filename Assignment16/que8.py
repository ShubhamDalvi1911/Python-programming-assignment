# Write a program which accept number from user and print that number of "*" on screen.
def Pattern(No):
    for i in range(No):
        print("*" , end=" ")

def main():
    No = int(input("Enter number : "))
    Pattern(No)


if __name__ == "__main__":
    main()