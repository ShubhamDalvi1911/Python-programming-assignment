"""Write a program to display 
   1) Data Type
   2) Memory Address
   3) Size in bytes of Variable entered by user."""
from sys import getsizeof

def displayinfo(var):
    print("Data Type:", type(var))
    print("Memory Address:", id(var))
    print("Size in bytes:", getsizeof(var))

def main():
    No = input("Enter a value: ")
    displayinfo(No)
if __name__ == "__main__":
    main()