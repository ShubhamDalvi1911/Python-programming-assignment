# Write a program whcih accepts one number and prints that many numbers in reverse
def PrintNum(No):
    for i in range(No,0,-1):
        print(i, end=' ')

def main():
    No = int(input("Enter number : "))
    result = PrintNum(No)

if __name__ == "__main__":
    main()