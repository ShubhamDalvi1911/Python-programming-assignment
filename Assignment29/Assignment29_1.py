'''
Check File Exists in Current Directory 
Problem Statement:
    Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
'''
import os
def ChkFile(FileName):
    if (os.path.exists(FileName)):
        print(f"File {FileName} is exists in current directory.")
    else:
        print(f"File {FileName} is NOT exists in current directory.")


def main():
    FileName = input("Enter File name which you want to check : ")
    ChkFile(FileName)

if __name__ == "__main__":
    main()