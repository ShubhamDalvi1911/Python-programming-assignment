# Write a program which accept one number and return adition of its factors
def Factors(No):
    fact = 0
    for i in range(1,No):
        if No % i == 0:
            fact = fact + i
    return fact

def main():
    No = int(input("Enter a number : "))
    result = Factors(No)
    print("Adition of factors is : ", result)

if __name__ == "__main__":
    main()