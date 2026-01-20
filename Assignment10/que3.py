#Write a program which accepts one number and prints factorial of that number.
def factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact

def main():
    result = 0
    No = int(input("Enter a number : "))
    result = factorial(No)
    print(result)

if __name__ == "__main__":
    main()