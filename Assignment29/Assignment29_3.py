'''
Copy File Contents into a New File(Command Line)
Problem Statement:
    Write a program which accepts a existing file name through command line arguments, 
    creates a new file named Demo.txt and copies all contents from the given file into Demo.txt
'''
import os
import sys 

def ChkFile(OldFileName , NewFileName):
    if (os.path.exists(OldFileName)):
        # Open existing file
        fobj = open(OldFileName,"r")
        print(f"File {OldFileName} Gets Opend Successfully: ")
        Data = fobj.read()
        fobj.close()

        fobj2 = open(NewFileName,"w")
        fobj2.write(Data)
        fobj2.close()
        print(f"Copied all contents from {OldFileName} into {NewFileName} Successfully.")

    else:
        print(f"File {OldFileName} is NOT exists in current directory.")


def main():
    NewFileName = input("Enter new file name which you want to create : ")
    ChkFile(sys.argv[1],NewFileName)

if __name__ == "__main__":
    main()