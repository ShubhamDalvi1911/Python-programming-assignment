# Write a program which contains filter(), map() and reduce() in it. Python application which 
# contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which greater than or equal to 70 and less that or 
# equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

from functools import reduce

def main():
    No = int(input("Enter number of elements you want in list: "))
    Num_List = []
    for i in range(No):
        no = int(input(f"Enter element {i+1}: "))
        Num_List.append(no)

    print("Original List:", Num_List)
    # Filter numbers between 70 and 90
    Filter_list = list(filter(lambda x : x >= 70 and x <= 90, Num_List))
    print("Filtered List (70 to 90):", Filter_list)

    # Map to increase each number by 10
    Map_list = list(map(lambda x : x + 10, Filter_list))
    print("Mapped List (each element increased by 10):", Map_list)

    # Reduce to get product of all numbers
    result = reduce(lambda a, b : a * b, Map_list)
    print("Product of all elements in Mapped List:", result)


if __name__ == "__main__":
    main()