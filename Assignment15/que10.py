# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.
Even = lambda No : (No % 2 == 0)

def main():
    nums = list()
    no = int(input("Enter how many numbers you want to store : "))
    for i in range(no):
        print("Enter", i+1 ," number : ", end='')
        nums.append(int(input()))

    result = list(filter(Even,nums))

    print("Count of even numbers are ", len(result))


if __name__ == "__main__":
    main()