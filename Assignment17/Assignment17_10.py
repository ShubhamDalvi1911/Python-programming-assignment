# Write a program which accept one number and return additon of digit in that number
def DigitOf(No):
    Num = 0
    Sum = 0
    while No > 0:
        Num = No % 10
        No = No // 10
        Sum = Sum + Num
    return Sum

def main():
    No = int(input("Enter a number : "))
    result = DigitOf(No)
    print(result)
    

if __name__ == "__main__":
    main()