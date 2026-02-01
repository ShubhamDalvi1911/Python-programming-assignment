'''
Frequency of s String in File
Problem Statement:
    Write a program which accepts two file name and one string from the user and return frequency
    (Count of occurances) of that string in the file.
'''
import os
import sys 

def ChkFile(FileName , String):
    if (os.path.exists(FileName)):
        # Open First file
        fobj = open(FileName,"r")
        Data = fobj.read()
        fobj.close()

        # Check Count of occurance
        count = Data.count(String)
        print(f"Occurance of {String} in {FileName} is : ",count)

    else:
        print(f"Files are NOT exists in current directory.")


def main():
    ChkFile(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()