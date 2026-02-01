'''
Compare Two File(Command Line)
Problem Statement:
    Write a program which accepts two file names through command line arguments, 
    and compare the contents of both files.
        - If both files contains the same contens, display Success
        - otherwise display Failure.
'''
import os
import sys 

def ChkFile(FirstFileName , SecondFileName):
    Ret1 = os.path.exists(FirstFileName)
    Ret2 = os.path.exists(SecondFileName)
    if (Ret1 == True and Ret2 == True):
        # Open First file
        fobj = open(FirstFileName,"r")
        FirstData = fobj.read()
        fobj.close()

        # Open Second file
        fobj2 = open(SecondFileName,"r")
        SecondData = fobj2.read()
        fobj2.close()
        
        # Compaire the data
        if (FirstData == SecondData):
            print("Success")
        else:
            print("Failure")

    else:
        print(f"Files are NOT exists in current directory.")


def main():
    ChkFile(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()