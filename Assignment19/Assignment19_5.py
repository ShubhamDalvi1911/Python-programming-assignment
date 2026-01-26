# Write a program which contains filter(), map() and reduce() in it. Python application which 
# contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out prime numbers
# Map function will multiplay each number by 2. Reduce will return maximum number from that numbers.

from functools import reduce

def prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, (num // 2) + 1):
            if (num % i) == 0:
                return False
        return True 

def main():
    No = int(input("Enter number of elements you want in list: "))
    Num_List = []
    for i in range(No):
        no = int(input(f"Enter element {i+1}: "))
        Num_List.append(no)

    print("Original List:", Num_List)
    # Filter prime numbers
    Filter_list = list(filter(prime, Num_List))
    print("Filtered List:", Filter_list)

    # Map to multiply each number by 2
    Map_list = list(map(lambda x : x * 2, Filter_list))
    print("Mapped List:", Map_list)

    # Reduce to get maximum of all numbers
    result = reduce(lambda a, b : a if a>b else b, Map_list)
    print("Addition of all elements in Mapped List:", result)


if __name__ == "__main__":
    main()