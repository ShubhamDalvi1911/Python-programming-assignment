'''
Design a python application that creates two threads.
   - thread 1 should calculate and display the maximum number from a list.
   - thread 2 should calculate and display the minimum number from a list.
   - The list should be accepted from the user.
'''

import threading

def Maximum(num):
    max_num = 0
    for i in num:
        if i > max_num:
            max_num = i
    print("Maximum number:", max_num)

def Minimum(num):
    min_num = num[0]
    for i in num:
        if i < min_num:
            min_num = i
    print("Minimum number:", min_num)

def main():
    No = int(input("Enter number of elements: "))
    numbers = []
    for i in range(No):
        no = int(input(f"Enter element {i + 1}: "))
        numbers.append(no)

    t1 = threading.Thread(target=Maximum, args=(numbers,))
    t2 = threading.Thread(target=Minimum, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()