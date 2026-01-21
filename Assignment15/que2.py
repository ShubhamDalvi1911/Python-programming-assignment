# Write a lambda function using filter() which accepts a list of numbers and returns a list of even of numbers.
Even = lambda No : (No % 2) == 0 

def main():
    nums = list()
    no = int(input("Enter how many numbers you want to store : "))
    for i in range(no):
        print("Enter", i+1 ," number : ", end='')
        nums.append(int(input()))

    result = list(filter(Even,nums))

    print("list of even numbers are ",result)


if __name__ == "__main__":
    main()