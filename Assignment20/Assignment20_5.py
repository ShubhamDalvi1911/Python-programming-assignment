'''
Design a python application that creates two threads named THread1 and THread2.
    - Thread 1 should display numbers from 1 to 50.
    - Thread 2 should display numbers from 50 to 1.
    - Ensusre that:
        - THread2 starts execution only after the completion of Thread1.
    - Usse appropriate thread syncronization.
'''
import threading
import time

lobj = threading.Lock()
def Thread1():
    print("Starting of Thread1")
    for i in range(1,51):
        with lobj:
            print(i)
    print("-----------")

def Thread2():
    print("Starting of Thread2")
    for i in range(50,0,-1):
        with lobj:
            print(i)
    print("-----------")

def main():
    start_time = time.time()

    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)

    t1.start()
    t1.join()

    t2.start()
    t2.join()
    
    end_time = time.time()
    print(f"Time taken for thread execution: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()