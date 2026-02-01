'''
Display File Contents
Problem Statement:
    Write a program which accepts a file name from the user,  opens that file, and display the entire contents on the console.
'''
import os
def ChkFile(FileName):
    if (os.path.exists(FileName)):
        fobj = open(FileName,"r")
        Data = fobj.read()
        fobj.close()

        print(f"Data of {FileName} is: ", Data)

    else:
        print(f"File {FileName} is NOT exists in current directory.")


def main():
    FileName = input("Enter File name to Display the Contents : ")
    ChkFile(FileName)

if __name__ == "__main__":
    main()