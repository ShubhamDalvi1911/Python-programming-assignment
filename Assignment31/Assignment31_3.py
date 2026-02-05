"""
Design automation script which accept two directory names. Copy all file from first directory into
second directory. Second directory should be created at run time.

Usage : DirectoryCopy.py  "Demo" "Temp"

Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and Copy all files from Demo to Temp
"""

import os
import sys
import shutil

def DirectoryCopy(DirectoryNameOld , DirectoryNameNew):

    if not os.path.exists(DirectoryNameOld):
        print(f"Source directory {DirectoryNameOld} not found")

    elif os.path.exists(DirectoryNameNew):
        print(f"Destination directory {DirectoryNameNew} already exists")

    else:
        shutil.copytree(DirectoryNameOld, DirectoryNameNew)
        print(f"{DirectoryNameOld} successfully copied to {DirectoryNameNew}.")


def main():
    Border = "-" * 80
    print(Border)
    print("------------------Welcome to Directory File Copy Application--------------------")
    print(Border)
    
    if len(sys.argv) != 3:
        print("Invalid number of arguments. Please provide directory name from you want to copy and new directory name")
        print("Usage: python Assignment31_2.py <DirectoryNameOld> <DirectoryNameNew>")
    
    else:
        DirectoryCopy(sys.argv[1], sys.argv[2])

    print(Border)
    print("---------------Thank you for using Directory File Copy Application--------------")
    print(Border)

if __name__ == "__main__":
    main()