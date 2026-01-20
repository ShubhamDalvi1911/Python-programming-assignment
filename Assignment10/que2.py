#Write a program which accepts one number and prints sum of first N natural numbers.
def SumOfNatural(NO):
    sum = 0
    for i in range(1,NO+1):
        sum = sum + i
    return sum

def main():
    result = 0
    No = int(input("Enter a number : "))
    result = SumOfNatural(No)
    print(result)

if __name__ == "__main__":
    main()
