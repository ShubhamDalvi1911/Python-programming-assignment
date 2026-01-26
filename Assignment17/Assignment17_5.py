# Write a program which accept one number and checks whether number is prime or not
def ChkPrime(No):
    if No == 1:
        return "1 is nither prime nor composit"
    else:
        for i in range(2,No//2):
            if No % i == 0:
                return "Not Prime"
            else:
                return "Prime"

def main():
    No = int(input("Enter a number : "))
    result = ChkPrime(No)
    print("It is ", result," Number")

if __name__ == "__main__":
    main()