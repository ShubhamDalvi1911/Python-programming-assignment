# Write a program which accept one number and return number of digit in that number
def DigitOf(No):
    Num = No
    counter = 0
    while Num > 0:
        Num = Num // 10
        counter = counter + 1
    return counter

def main():
    No = int(input("Enter a number : "))
    result = DigitOf(No)
    print(result)
    

if __name__ == "__main__":
    main()