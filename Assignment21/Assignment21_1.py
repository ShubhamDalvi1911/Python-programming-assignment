'''
Design a python application that creates two threads named Prime and NonPrime.
   - Both threads should accept a list of integers.
   - The prime thread should display all prime numbers from the list.
   - The non-prime thread should display all non-prime numbers from the list.
'''

import threading

def is_prime(num):
    prime = []
    for i in num:
        if i == 1:
            continue
        else:
            for j in range(2, (i // 2) + 1):
                if (i % j) == 0:
                    break
            else:
                prime.append(i)
    print("Prime numbers:", prime)

def is_non_prime(num):
    non_prime = []
    for i in num:
        if i == 1:
            continue
        else:
            for j in range(2, (i // 2) + 1):
                if (i % j) == 0:
                    non_prime.append(i)
                    break
    print("Non-Prime numbers:", non_prime)

def main():
    No = int(input("Enter number of elements: "))
    numbers = []
    for i in range(No):
        no = int(input(f"Enter element {i + 1}: "))
        numbers.append(no)

    t1 = threading.Thread(target=is_prime, args=(numbers,))
    t2 = threading.Thread(target=is_non_prime, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()