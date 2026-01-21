# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.
DivBy = lambda No : (No % 3 == 0 and No % 5 == 0)

def main():
    nums = list()
    no = int(input("Enter how many numbers you want to store : "))
    for i in range(no):
        print("Enter", i+1 ," number : ", end='')
        nums.append(int(input()))

    result = list(filter(DivBy,nums))

    print("Numbers which are divisible by 3 and  5 are ",result)


if __name__ == "__main__":
    main()