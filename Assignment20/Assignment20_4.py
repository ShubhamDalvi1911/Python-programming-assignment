'''
Design a python application that creates small , capital and digits.
    - All threads should accept one string as input.
    - THe samll thread should count and display the number of lowercase characters.
    - The capital thread should count and display the number of uppercase characters.
    - The digits thread should count and display the number of numeric digits.  
    - Each thrrad must also display:
        - Thread ID
        - Thread Name
'''
import threading
import time

def Small(Strs):

    print("Thread ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)
    count = 0
    for ch in range(len(Strs)):
            for i in range(97,123):
                if ord(Strs[ch]) == i:
                    count = count + 1
    print("Count of Small from string is : ",count) 
    print("-------------------------------------------")

def Capital(Strs):
    print("Thread ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)
    count = 0
    for ch in range(len(Strs)):
            for i in range(65,91):
                if ord(Strs[ch]) == i:
                    count = count + 1
    print("Count of Capital from string is : ",count) 
    print("-------------------------------------------")

def Digits(Strs):
    print("Thread ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)
    count = 0
    for ch in range(len(Strs)):
            for i in range(48,58):
                if ord(Strs[ch]) == i:
                    count = count + 1
    print("Count of digits from string is : ",count) 
    print("------------------------------------------")


def main():
    Strs = input("Enter a string : ")
    start_time = time.time()

    t1 = threading.Thread(target=Small, args=(Strs,))
    t2 = threading.Thread(target=Capital, args=(Strs,))
    t3 = threading.Thread(target=Digits, args=(Strs,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    
    end_time = time.time()
    print(f"Time taken for thread execution: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()