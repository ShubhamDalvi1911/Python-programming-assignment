# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.
from functools import reduce
Max = lambda No1, No2 : No1 if (No1 > No2) else No2

def main():
    nums = list()
    no = int(input("Enter how many numbers you want to store : "))
    for i in range(no):
        print("Enter", i+1 ," number : ", end='')
        nums.append(int(input()))

    result = reduce(Max,nums)

    print("Maximum element is ",result)


if __name__ == "__main__":
    main()