# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.
square = lambda No : No*No

def main():
    nums = list()
    no = int(input("Enter how many numbers you want to store : "))
    for i in range(no):
        print("Enter", i+1 ," number : ", end='')
        nums.append(int(input()))

    result = list(map(square,nums))

    print("list of squares of each numbers are ",result)


if __name__ == "__main__":
    main()