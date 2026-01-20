# write a program which accepts one number and print reverse of that number
def reverseDigit(No):
    digit = 0
    reverse = 0
    for i in range(len(str(abs(No)))):
        digit = No % 10
        reverse = (reverse*10) + digit
        No = No // 10
    return reverse

def main():
    No = int(input("Enter a number : "))
    result = reverseDigit(No)
    print(result)

if __name__ == "__main__":
    main()