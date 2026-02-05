"""
Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extenstion with the second file extension.
Usage : DirectoryRename.py  "Demo" ".txt" ".doc"

Demo is name of directory and .txt is the extension that we want to search and rename 
with .doc
After execution this script each .txt file gets renamed as .doc
"""

import os
import sys

def DirectoryRename(DirectoryName, FileExtensionOld, FileExtensionNew):
    if os.path.exists(DirectoryName):
        for foldername, subfolder, filenames in os.walk(DirectoryName):
            for filename in filenames:
                if filename.endswith(FileExtensionOld):
                    old_path = os.path.join(foldername, filename)
                    
                    new_filename = filename.replace(FileExtensionOld, FileExtensionNew)

                    new_path = os.path.join(foldername, new_filename)

                    os.rename(old_path, new_path)


    else:
        print("Directory does not exist.")

def main():
    Border = "-" * 80
    print(Border)
    print("------------------Welcome to Directory File Rename Application------------------")
    print(Border)
    
    if len(sys.argv) != 4:
        print("Invalid number of arguments. Please provide directory name and file extensions.")
        print("Usage: python Assignment31_2.py <DirectoryName> <FileExtensionOld> <FileExtensionNew>")
    
    else:
        DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

    print(Border)
    print("--------------Thank you for using Directory File Rename Application-------------")
    print(Border)

if __name__ == "__main__":
    main()