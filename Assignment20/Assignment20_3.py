'''
Design a python application that creates two separate therads named EvenList and OddList.
    - Both therads should accept one list integer as input.
    - The EvenList therad Should:
        - Extract all even elements from the list.
        - Calculate and dislplay their sum.
    - The OddList therad Should:
        - Extract all odd elements from the list.
        - Calculate and dislplay their sum .
    - Threads should run concurrently.
'''
import threading
import time

def EvenList(Num_list):
    sum = 0
    for i in Num_list:
        if i % 2 == 0:
            sum = sum + i
    print("Even sum from list is : ",sum)

def OddList(Num_list):
    sum = 0
    for i in Num_list:
        if i % 2 != 0:
            sum = sum + i
    print("Odd sum from list is : ",sum)

def main():
    Num_list = []
    No = int(input("Enter how many elements you want in list : "))
    for i in range(No):
        No = int(input(f"Enter element {i+1} : "))
        Num_list.append(No)

    start_time = time.time()

    t1 = threading.Thread(target = EvenList, args=(Num_list,))
    t2 = threading.Thread(target = OddList, args=(Num_list,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    end_time = time.time()
    print(f"Time taken for thread execution: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()