'''
Design a python application that creates two separate therads named as Even and Odd.
   - The even therad should display the first 10 even numbers.
    - The odd therad should display the first 10 odd numbers.
    - Both therads should execute independently using the threading module.
    - Ensure proper therad creation and execution.
'''
import threading
import time

def Even():
    for i in range(0, 20, 2):
        print(f"Even: {i}")

def Odd():
    for i in range(1, 20, 2):
        print(f"Odd: {i}")

def main():
    t1 = threading.Thread(target = Even)
    t2 = threading.Thread(target = Odd)

    start_time = time.time()
    t1.start()
    t2.start()
    end_time = time.time()
    
    t1.join()
    t2.join()

    print(f"Time taken for thread execution: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()