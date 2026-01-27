'''
Design a python application where multiple threads update a shared variable.
    - Use a lock to avoid race conditions
    - Each thread should increment the shared counter multiple times.
    - Display the final value of the counter after all threads complete execution.
'''
import threading

counter = 0
lobj = threading.Lock()

def increment_counter(times):
    global counter
    for _ in range(times):
        with lobj:
            counter += 1
    print(f"Thread {threading.current_thread().name} finished incrementing.")
    print(counter)

def main():
    no = int(input("Enter number of increments per thread: "))

    t1 = threading.Thread(target=increment_counter, args=(no,))
    t2 = threading.Thread(target=increment_counter, args=(no,))
    t3 = threading.Thread(target=increment_counter, args=(no,))
    t4 = threading.Thread(target=increment_counter, args=(no,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Final counter value:", counter)

if __name__ == "__main__":
    main()