'''
Design a python application that creates two threads.
    - Thread 1 should compute the sum of elements from a list.
    - Thread 2 should compute the product of elements from the same list.
    - Return the result to the main thread and display them.
'''
import threading


def sum_of_element(Nums):
    sum = 0
    for i in range(len(Nums)):
        sum = sum + Nums[i]
    print("Sum of elements:", sum)

def product_of_element(Nums):
    product = 1
    for i in range(len(Nums)):
        product = product * Nums[i]
    print("Product of elements:", product)

def main():
    no = int(input("Enter how many elements you want in the list: "))
    Nums = []
    for i in range(no):
        value = int(input(f"Enter element {i + 1}: "))
        Nums.append(value)

    t1 = threading.Thread(target=sum_of_element, args=(Nums,))
    t2 = threading.Thread(target=product_of_element, args=(Nums,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
   


if __name__ == "__main__":
    main()