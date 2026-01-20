# Write a program which accepts one number and print sum of digits
def SumOfDigit(No):
    digit = 0
    sum = 0
    for i in range(len(str(abs(No)))):
        digit = No % 10
        sum = sum + digit
        No = No //10
    return sum


def main():
    No = int(input("Enter a number : "))
    result = SumOfDigit(No)
    print(result)

if __name__ == "__main__":
    main()