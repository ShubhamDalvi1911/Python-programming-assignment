# Write a program which contains one function named as ChkNum(). which accept one parameter as number. if number is even then it should display "Even number" otherwise display "Odd number" on console.

def ChkNum(Num):
    if Num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

def main():
    No = int(input("Enter a number you want to check "))
    result = ChkNum(No)
    print(result)

if __name__ == "__main__":
    main()