"""
Design automation script which accept directory name and display checksum of all files.

Usage : DirectoryCheckSum.py "Demo"

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
    if os.path.exists(DirectoryName):
        for FoldarName , SubFoldarName , FileName in os.walk(DirectoryName):
            for fname in FileName:
                fname = os.path.join(FoldarName, fname)
                ChkSum = DirectoryCheckSum(fname)
                print(f"Check sum of {fname} is : {ChkSum}")
    
    else:
        print("Directory not found.")

def main():
    Border = "-" * 50
    print(Border)
    print("----------Welcome to CheckSum Automation----------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Usage : <DirectoryCheckSum.py> <Demo>")
            print("<Demo> is name of directory")
        elif sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("Help : This is automation to display checksum of all files.")
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
