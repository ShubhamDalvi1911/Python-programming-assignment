"""
Design automation script which accept two directory names and one file extension. Copy all
files with the specified extension from first directory into second directory. Second directory
should be created at run time.

Usage : DirectoryCopyExt.py  "Demo" "Temp" ".exe"

Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and Copy all files with extension .exe from Demo to Temp
"""

import os
import sys
import shutil

def DirectoryCopy(DirectoryNameOld , DirectoryNameNew , Extension):

    if not os.path.exists(DirectoryNameOld):
        print(f"Source directory {DirectoryNameOld} not found")

    else:
        for FolderName , SubFoldarName , FileName in os.walk(DirectoryNameOld):
            rel_path = os.path.relpath(FolderName, DirectoryNameOld)
            dest_root = os.path.join(DirectoryNameNew,rel_path)
            os.makedirs(dest_root, exist_ok=True)

            for fname in FileName:
                if fname.endswith(Extension):
                    src_path = os.path.join(FolderName , fname)
                    dst_path = os.path.join(dest_root , fname)
                    shutil.copy2(src_path,dst_path)
        print(f"{DirectoryNameOld} successfully copied to {DirectoryNameNew} file with {Extension} extention file only.")

def main():
    Border = "-" * 80
    print(Border)
    print("------------------Welcome to Directory File Copy Application--------------------")
    print(Border)
    
    if len(sys.argv) != 4:
        print("Invalid number of arguments. Please provide directory name from you want to copy\n and new directory name and extension of files")
        print("Usage:python Assignment31_2.py <DirectoryNameOld> <DirectoryNameNew> <Extension>")
    
    else:
        DirectoryCopy(sys.argv[1], sys.argv[2] , sys.argv[3])

    print(Border)
    print("---------------Thank you for using Directory File Copy Application--------------")
    print(Border)

if __name__ == "__main__":
    main()