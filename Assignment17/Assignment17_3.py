# Write a program which accept one number and return its factorial
def Fact(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact

def main():
    No = int(input("Enter a number : "))
    result = Fact(No)
    print("Factorial is : ", result)

if __name__ == "__main__":
    main()