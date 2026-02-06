"""
Design automation script which accept directory name and write names of duplicate files
from that directory into log file named as Log.txt  Log.txt file should be created into 
current directory

Usage : DirectoryDusplicate.py "Demo"

Demo is name of directory
"""
import os
import sys
import hashlib

def DirectoryCheckSum(fname):
    fobj = open(fname, "rb")
    Buffer = fobj.read(1024)

    hobj = hashlib.md5()

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def DirectoryTravesal(DirectoryName):
    Border = "-"*50
    Duplicate = {}

    if os.path.exists(DirectoryName):
        for FoldarName , SubFoldarName , FileName in os.walk(DirectoryName):
            for fname in FileName:
                fname = os.path.join(FoldarName, fname)
                ChkSum = DirectoryCheckSum(fname)
                
                if ChkSum in Duplicate:
                    Duplicate[ChkSum].append(fname)
                else:
                    Duplicate[ChkSum] = [fname]

        # MyDict = Duplicate

        Result = list(filter(lambda x : len(x) > 1 , Duplicate.values()))

        fobj = open("Log.txt","w")
        fobj.write(Border + "\n")
        fobj.write("This is a log file created by duplicate file Log Automation.\n")
        fobj.write("This log file contains the list of duplicate files.\n")
        fobj.write(Border + "\n")

        for Value in Result:
            for SubValue in Value:
                fobj.write(SubValue+"\n")

        fobj.write(Border + "\n")
        fobj.close()
    
    else:
        print("Directory not found.")

def main():
    Border = "-" * 50
    print(Border)
    print("-------Welcome to Duplicate Log Automation--------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Usage : <DirectoryCheckSum.py> <Demo>")
            print("<Demo> is name of directory")
        elif sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("Help : This is automation to create log file of Duplicate")
            print("You need to provide one argument as Directory name.")

        else:
            DirectoryTravesal(sys.argv[1])
    else:
        print("Invalid number of command line arguments.") 
        print("Please specify the name of directory.")
        print("Use the give flags as : ")
        print("--u : Use to display the Usage")
        print("--h : Use to display the Help")


    print(Border)
    print("-----------Thanku For Using Automation-----------")
    print(Border)


if __name__ == "__main__":
    main()
