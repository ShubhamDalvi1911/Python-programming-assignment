# Write a program which contains filter(), map() and reduce() in it. Python application which 
# contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which are even
# Map function will calculate its square. Reduce will return addition of all that numbers.

from functools import reduce

def main():
    No = int(input("Enter number of elements you want in list: "))
    Num_List = []
    for i in range(No):
        no = int(input(f"Enter element {i+1}: "))
        Num_List.append(no)

    print("Original List:", Num_List)
    # Filter even numbers
    Filter_list = list(filter(lambda x : x % 2 == 0, Num_List))
    print("Filtered List:", Filter_list)

    # Map to calculate square of each number
    Map_list = list(map(lambda x : x * x, Filter_list))
    print("Mapped List:", Map_list)

    # Reduce to get addtion of all numbers
    result = reduce(lambda a, b : a + b, Map_list)
    print("Addition of all elements in Mapped List:", result)


if __name__ == "__main__":
    main()