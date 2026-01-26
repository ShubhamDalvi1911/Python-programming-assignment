'''
Design a python application that creates two separate therads named EvenFactor and OddFactor.
    - Both therads should accept one integer number as a parameter.
    - The EvenFactor therad Should:
        - Identify all even factors of the given number.
        - Calculate and dislplay the sum of all even factors.
    - The OddFactor therad Should:
        - Identify all odd factors of the given number.
        - Calculate and dislplay the sum of all odd factors.
    - After both theradss complete execution, the main thread should display the message:
        "Exit from main"
'''
import threading
import time

def EvenFactorSum(No):
    sum = 0
    for i in range(1,No+1):
        if No % i == 0 and i % 2 == 0:
            sum = sum + i
    print("Even factor sum is : ",sum)

def OddFactorSum(No):
    sum = 0
    for i in range(1, No+1):
        if No % i == 0 and i % 2 != 0:
            sum = sum + i
    print("Odd factor sum is : ",sum)

def main():
    No = int(input("Enter a number: "))

    start_time = time.time()

    t1 = threading.Thread(target = EvenFactorSum, args=(No,))
    t2 = threading.Thread(target = OddFactorSum, args=(No,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    end_time = time.time()
    print(f"Time taken for thread execution: {end_time - start_time} seconds")
    print("Exit from main")

if __name__ == "__main__":
    main()