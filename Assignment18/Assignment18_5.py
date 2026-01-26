# Write a program whcih accept N numbers from user and store it into list. 
# Return addition of all prime numbers from that list. Main python file accepts N numbers from user
# and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum
# Name of the function from main python file should be ListPrime().
from MarvellousNum import prime as ChkPrime

def ListPrime(num_list):
    Sum = 0
    for i in num_list:
        if ChkPrime(i) == True:
            Sum = Sum + i
            
    return Sum

def main():
    num = int(input("Enter how many numbers you want to enter: "))
    num_list = []
    for i in range(num):
        No = int(input(f"Enter number {i+1} :"))
        num_list.append(No)

    result = ListPrime(num_list)
    print("Sum of Prime number is ", result)

if __name__ == "__main__":
    main()