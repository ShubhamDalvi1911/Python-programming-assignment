# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.
from functools import reduce
Product = lambda No1 , No2 : No1 * No2

def main():
    nums = list()
    no = int(input("Enter how many numbers you want to store : "))
    for i in range(no):
        print("Enter", i+1 ," number : ", end='')
        nums.append(int(input()))

    result = reduce(Product,nums)

    print("Product of elemnts are ",result)


if __name__ == "__main__":
    main()