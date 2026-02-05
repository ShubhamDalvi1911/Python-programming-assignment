"""
Design automation script which accept directory name and file extension from user. Display all files with that extension.
"""

import os
import sys

def DirectoryFileSearch(DirectoryName, FileExtension):
    if os.path.exists(DirectoryName):
        for foldername, subfolder, filenames in os.walk(DirectoryName):
            for filename in filenames:
                if filename.endswith(FileExtension):
                    print(filename)

    else:
        print("Directory does not exist.")

def main():
    Border = "-" * 80
    print(Border)
    print("------------------Welcome to Directory File Search Application------------------")
    print(Border)
    
    if len(sys.argv) != 3:
        print("Invalid number of arguments. Please provide directory name and file extension.")
        print("Usage: python Assignment31_1.py <DirectoryName> <FileExtension>")
    
    else:
        DirectoryFileSearch(sys.argv[1], sys.argv[2])

    print(Border)
    print("--------------Thank you for using Directory File Search Application-------------")
    print(Border)
if __name__ == "__main__":
    main()